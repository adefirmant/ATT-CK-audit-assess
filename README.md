# AudiTT&CK
AudiTT&CK-is a CLI tool that generates predictive cybersecurity audit checklists based on real-world threat actor behavior. It maps adversary TTPs (Tactics, Techniques, and Procedures) from the MITRE ATT&amp;CK framework to their corresponding mitigation and detection controls — then outputs them in a standardized control objective format.

> 🎯 This tool turns threat intelligence into **actionable audit questions**, helping organizations align their cybersecurity controls with realistic threat scenarios.

---

## 🔍 Key Features

- ✅ Input: One or more MITRE ATT&CK **threat actors/groups**
- 📋 Output: Audit checklist (CSV/XLSX) in **control objective format**
- 📚 Based on MITRE ATT&CK’s **Mitigations** and **Detections**
- 🔀 Supports multiple threat actors at once
- 🧠 Separates **Mitigation** vs **Detection** controls
- 📌 Includes source **Threat Actor(s)** in each checklist row

---

## 📦 Installation

Clone the repo and install required dependencies:

```bash
git clone https://github.com/yourusername/threatauditgen.git
cd threatauditgen
pip install -r requirements.txt
