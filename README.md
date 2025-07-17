# AudiTT&CK
AudiTT&CK-is a CLI tool that generates predictive cybersecurity audit checklists based on real-world threat actor behavior. It maps adversary TTPs (Tactics, Techniques, and Procedures) from the MITRE ATT&CK framework to their corresponding mitigation and detection controls — then outputs them in a standardized control objective format.

> 🎯 This tool turns threat intelligence into actionable audit checklist, helping organizations align their cybersecurity controls with realistic threat scenarios.

---

## 🚀 Features

- Maps techniques used by selected MITRE ATT&CK threat groups
- Generates both mitigation and detection control objectives
- Merges control descriptions into actionable audit items
- Auto-updates the latest MITRE ATT&CK STIX data
- Supports **Enterprise**, **Mobile**, and **ICS** domains

---

## 📦 Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧑‍💻 Usage

Run the tool using:

```bash
python audittack.py
```

Then follow the prompts:

1. **Select ATT&CK Domain**:
    ```
    1. Enterprise
    2. Mobile
    3. ICS
    ```

2. **Enter Threat Actor Group(s)**:
    - Comma-separated group names  
      Example: `APT29`, `FIN7,APT28`

3. **Enter Output Filename**:
    - Do **not** include `.xlsx` — it will be added automatically

4. **Update MITRE Data**:
    - The tool shows your current local version
    - Choose whether to update to the latest online version

---

## 📤 Output

The tool generates an Excel file with audit checklist items.

| Column           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `Technique ID`   | MITRE ATT&CK technique ID (e.g., `T1059`)                                   |
| `Technique Name` | Technique name (e.g., `Command and Scripting Interpreter`)                  |
| `Control Type`   | Either `Mitigation` or `Detection`                                          |
| `Control Objective` | Plain-language description of the control to be audited                 |
| `Group`          | Threat actor group associated with the technique                            |
| `Description`    | Merged control description (mitigation + detection guidance)                |

---

## 🌐 STIX Data Source

MITRE ATT&CK STIX files are used to power the tool.  

### 🔍 Local Files

Stored in the `/data` directory:

- `enterprise-attack.json`
- `mobile-attack.json`
- `ics-attack.json`

### 🔄 Auto-Update

- The tool can fetch the latest versions from:
  - [https://github.com/mitre/cti](https://github.com/mitre/cti)
- It checks and shows:
  - `x_mitre_attack_spec_version`
  - `modified` timestamp from STIX metadata

---

## 📂 Folder Structure

```
audittack/
├── audittack.py
├── utils/
│   ├── attck_client.py
│   ├── audit_generator.py
│   └── writer.py
├── data/
│   ├── enterprise-attack.json
│   ├── mobile-attack.json
│   └── ics-attack.json
├── output/
│   └── audit_checklist.xlsx
└── README.md
```

---

## 🧪 Sample Run

```bash
python audittack.py
```

```
Select ATT&CK Domain:
1. Enterprise
2. Mobile
3. ICS
Enter choice [1-3]: 1

📦 Local ATT&CK version: 14.1 | Last modified: 2025-04-20
🔁 Do you want to update the MITRE ATT&CK data? (y/n): y
🎯 Enter threat actor group(s), comma-separated (e.g. APT29, FIN7): APT29
📄 Enter output filename (without .xlsx): audit_apt29
```

✅ Output file: `output/audit_apt29.xlsx`

---

## 📜 License

MIT License  
© 2025 [adeftriangga](https://github.com/adefirmant)

---

## 🙌 Credits

MITRE ATT&CK® is a registered trademark of The MITRE Corporation.  
This project is not affiliated with MITRE.

---
