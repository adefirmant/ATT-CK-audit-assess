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
git clone https://github.com/adefirmant/AudiTT-CK.git
cd audiTT-CK
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python audittack.py --groups APT29 FIN7 --domain enterprise
```

### Options

| Option      | Description                                                   |
|-------------|---------------------------------------------------------------|
| `--groups`  | Threat actor(s) from MITRE ATT&CK (e.g., APT29, FIN7)         |
| `--domain`  | MITRE ATT&CK domain: `enterprise`, `mobile`, or `ics`         |
| `--output`  | Output filename (default: `audit_checklist.xlsx`)             |

---

## 📝 Sample Output

| Tactic           | Technique ID | Technique Name              | Control Type | Control Objective                                                                 | Threat Actor(s) |
|------------------|--------------|------------------------------|---------------|-----------------------------------------------------------------------------------|------------------|
| Execution        | T1059.001    | PowerShell                   | Mitigation    | Ensure execution of unauthorized programs or scripts is restricted using application control or similar mechanisms. | APT29, FIN7 |
| Execution        | T1059.001    | PowerShell                   | Detection     | Ensure logging and alerting are implemented for PowerShell activity to detect and respond to suspicious behavior. | APT29, FIN7 |
| Defense Evasion  | T1070        | Indicator Removal on Host    | Mitigation    | Ensure access to resources targeted by Indicator Removal on Host is limited via segmentation and ACLs. | APT29, FIN7 |
| Defense Evasion  | T1070        | Indicator Removal on Host    | Detection     | Ensure logging and alerting are implemented for Indicator Removal on Host activity to detect and respond to suspicious behavior. | APT29, FIN7 |

---

## 💡 Use Case

**Predictive Audit Planning**  
Instead of using generic checklists, auditors can tailor cybersecurity audits based on real threat actors relevant to an organization’s sector or geography.

**Risk-Based Defense Validation**  
Security teams can verify if key controls are in place for tactics used by known APTs, ransomware gangs, or nation-state actors.

---

## 🧱 Architecture

- Parses MITRE ATT&CK data from STIX/TAXII
- Extracts `techniques` linked to threat actors
- Fetches corresponding `mitigations` and `detections`
- Translates into control objectives
- Outputs Excel/CSV

---

## 🛡️ Frameworks Used

- [MITRE ATT&CK](https://attack.mitre.org/)
- [STIX/TAXII](https://oasis-open.github.io/cti-documentation/)
- Python libraries: `stix2`, `pandas`, `argparse`

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute support for:
- Custom domains or datasets
- Mapping to specific compliance standards (e.g., NIST, ISO, CIS)
- Export to PDF/Markdown or GRC platforms  
Feel free to open an issue or PR.

---

## 📄 License

MIT License – see [`LICENSE`](LICENSE) for details.
