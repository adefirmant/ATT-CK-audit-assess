import sys
import os
from utils.attck_client import get_attack_data
from utils.audit_generator import generate_audit_items, load_control_templates
from utils.writer import write_to_excel
from utils.attck_client import get_attack_data, get_local_attack_version

def print_banner():
    banner = r"""
   ░███                      ░██ ░██░██████████░██████████ ░██████     ░██████  ░██     ░██ 
  ░██░██                     ░██        ░██        ░██    ░██   ░██   ░██   ░██ ░██    ░██  
 ░██  ░██  ░██    ░██  ░████████ ░██    ░██        ░██    ░██        ░██        ░██   ░██   
░█████████ ░██    ░██ ░██    ░██ ░██    ░██        ░██     ░█████████░██        ░███████    
░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██        ░██    ░██   ░██  ░██        ░██   ░██   
░██    ░██ ░██   ░███ ░██   ░███ ░██    ░██        ░██    ░██   ░██   ░██   ░██ ░██    ░██  
░██    ░██  ░█████░██  ░█████░██ ░██    ░██        ░██     ░█████░███  ░██████  ░██     ░██  

          🔐 Threat-Intelligence Based Audit Checklist Generator
               👤 Author: adeftriangga      🛠️ Version: 1.0
    """
    print(banner)

def get_user_input():
    print("Select ATT&CK Domain:")
    print("1. Enterprise")
    print("2. Mobile")
    print("3. Ics")
    choice = input("Enter choice [1-3]: ").strip()

    domain_map = {"1": "enterprise", "2": "mobile", "3": "ics"}
    domain = domain_map.get(choice)
    if not domain:
        print("❌ Invalid choice. Exiting.")
        sys.exit(1)

    # Get local STIX bundle version
    version, modified = get_local_attack_version(domain)
    print(f"\n📦 Local ATT&CK version: {version} | Last modified: {modified}")

    update_input = input("🔁 Do you want to update the MITRE ATT&CK data? (y/n): ").strip().lower()
    update_flag = update_input == 'y'

    groups = input("🎯 Enter threat actor group(s), comma-separated (e.g. APT29, FIN7): ").strip()
    filename = input("📄 Enter output filename (without .xlsx): ").strip()
    output_file = os.path.join("output", f"{filename}.xlsx")

    return domain, groups, output_file, update_flag

def main():
    print_banner()

    domain, groups, output_file, update_flag = get_user_input()

    print("\n🔍 Loading ATT&CK data...")
    techniques, relationships, mitigations, group_objs = get_attack_data(domain, update=update_flag)

    print("✅ Parsing STIX objects...")
    templates = load_control_templates()
    audit_items = generate_audit_items(techniques, relationships, mitigations, group_objs, groups, templates)

    if not audit_items:
        print("⚠️  No audit items generated. The selected group may not be associated with techniques in the chosen domain.")
        sys.exit(0)

    if not os.path.exists("output"):
        os.makedirs("output")

    write_to_excel(audit_items, output_file)

if __name__ == "__main__":
    main()