import os
import json
import requests
from datetime import datetime
from stix2 import MemoryStore, Filter

STIX_URLS = {
    "enterprise": "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json",
    "mobile": "https://raw.githubusercontent.com/mitre/cti/master/mobile-attack/mobile-attack.json",
    "ics": "https://raw.githubusercontent.com/mitre/cti/master/ics-attack/ics-attack.json"
}

STIX_LOCAL_PATHS = {
    "enterprise": "data/enterprise_attack.json",
    "mobile": "data/mobile_attack.json",
    "ics": "data/ics_attack.json"
}


def download_attack_data(domain: str):
    """Download latest ATT&CK STIX JSON and save to local."""
    url = STIX_URLS.get(domain)
    if not url:
        raise ValueError(f"❌ Unknown domain: {domain}")
    
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"❌ Failed to download STIX data for {domain}")

    stix_data = response.json()
    local_path = STIX_LOCAL_PATHS[domain]
    with open(local_path, "w", encoding="utf-8") as f:
        json.dump(stix_data, f, indent=2)
    
    print(f"✅ Downloaded and saved latest {domain} data to {local_path}")
    return stix_data


def load_local_bundle(domain: str):
    """Load STIX bundle from local file."""
    local_path = STIX_LOCAL_PATHS.get(domain)
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"❌ Local STIX file not found for domain '{domain}': {local_path}")
    
    with open(local_path, "r", encoding="utf-8") as f:
        bundle = json.load(f)
    
    return bundle


def get_local_attack_version(domain: str):
    """Get ATT&CK spec version and last modified from local STIX identity object."""
    try:
        bundle = load_local_bundle(domain)
    except FileNotFoundError:
        return None, None

    objects = bundle.get("objects", [])
    identity_objs = [obj for obj in objects if obj.get("type") == "identity"]

    # Try to find MITRE ATT&CK identity object
    for obj in identity_objs:
        name = obj.get("name", "").lower()
        if "mitre" in name and "attack" in name:
            version = obj.get("x_mitre_attack_spec_version", "N/A")
            modified = obj.get("modified", "N/A")
            try:
                mod_date = datetime.strptime(modified, "%Y-%m-%dT%H:%M:%S.%fZ")
                modified_str = mod_date.strftime("%Y-%m-%d")
            except Exception:
                modified_str = modified
            return version, modified_str

    # Fallback: return info from first identity object if available
    if identity_objs:
        fallback = identity_objs[0]
        version = fallback.get("x_mitre_attack_spec_version", "N/A")
        modified = fallback.get("modified", "N/A")
        try:
            mod_date = datetime.strptime(modified, "%Y-%m-%dT%H:%M:%S.%fZ")
            modified_str = mod_date.strftime("%Y-%m-%d")
        except Exception:
            modified_str = modified
        return version, modified_str

    return "Unknown", "Unknown"


def get_attack_data(domain: str, update: bool = False):
    """Load and parse ATT&CK data for the selected domain."""
    bundle = load_local_bundle(domain)  # This should already return a dict
    objects = bundle.get("objects", [])

    print("✅ Parsing STIX objects...")

    # Initialize MemoryStore with list of objects
    memory_store = MemoryStore(stix_data=objects)

    # Now you can safely query
    techniques = memory_store.query([Filter("type", "=", "attack-pattern")])
    relationships = memory_store.query([Filter("type", "=", "relationship")])
    mitigations = memory_store.query([Filter("type", "=", "course-of-action")])
    groups = memory_store.query([Filter("type", "=", "intrusion-set")])

    return techniques, relationships, mitigations, groups