import json
import os
from collections import defaultdict

def load_control_templates(path="control_templates.json"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        print("⚠️  control_templates.json not found. Using default templates.")
        return {
            "mitigation": "Implement appropriate control to mitigate {technique_name}.",
            "detection": "Ensure logging and alerting are implemented for {technique_name} activity to detect and respond to suspicious behavior."
        }

def generate_audit_items(techniques, relationships, mitigations, groups, group_list, templates):
    mitigation_map = defaultdict(list)
    technique_map = {}
    detection_map = {}

    for rel in relationships:
        if rel.get("relationship_type") == "mitigates":
            source_ref = rel.get("source_ref")
            target_ref = rel.get("target_ref")
            mitigation_map[target_ref].append(source_ref)

    for m in mitigations:
        mitigation_map[m["id"]] = m

    for t in techniques:
        technique_map[t["id"]] = t
        detection_map[t["id"]] = t.get("x_mitre_detection", "")

    audit_items = []
    seen_items = set()

    for group in groups:
        if group.get("name") not in group_list:
            continue
        used_techniques = [
            rel["target_ref"] for rel in relationships
            if rel.get("source_ref") == group["id"] and rel.get("relationship_type") == "uses"
        ]
        for tid in used_techniques:
            if tid not in technique_map:
                continue
            tech = technique_map[tid]
            tid_str = tech.get("external_references", [{}])[0].get("external_id", tid)
            technique_name = tech.get("name", "Unknown Technique")
            group_name = group.get("name", "Unknown Group")

            # Mitigation Control
            for mid in mitigation_map.get(tid, []):
                mit = mitigation_map.get(mid)
                if not mit:
                    continue
                mitigation_text = templates["mitigation"].format(technique_name=technique_name)
                full_text = mitigation_text.strip()
                key = (tid_str, technique_name, "Mitigation", full_text, group_name)
                if key not in seen_items:
                    audit_items.append({
                        "Technique ID": tid_str,
                        "Technique Name": technique_name,
                        "Control Type": "Mitigation",
                        "Control Objective": full_text,
                        "Group": group_name,
                        "Description": mit.get("description", "")
                    })
                    seen_items.add(key)

            # Detection Control
            detection_description = detection_map.get(tid, "")
            if detection_description:
                detection_text = templates["detection"].format(technique_name=technique_name)
                full_text = detection_text.strip()
                key = (tid_str, technique_name, "Detection", full_text, group_name)
                if key not in seen_items:
                    audit_items.append({
                        "Technique ID": tid_str,
                        "Technique Name": technique_name,
                        "Control Type": "Detection",
                        "Control Objective": full_text,
                        "Group": group_name,
                        "Description": detection_description.strip()
                    })
                    seen_items.add(key)

    print(f"✅ Generated {len(audit_items)} unique audit checklist items.")
    return audit_items
