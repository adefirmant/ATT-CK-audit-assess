import pandas as pd

def write_to_excel(data, output_file):
    df = pd.DataFrame(data)

    print(f"🧾 Columns in DataFrame: {list(df.columns)}")

    expected_columns = [
        "Technique ID", "Technique Name", "Control Type",
        "Control Objective", "Group", "Description"
    ]

    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        raise ValueError(f"❌ Missing expected columns in DataFrame: {missing}")

    # Deduplicate based on these key columns
    df.drop_duplicates(
        subset=["Technique ID", "Technique Name", "Control Type", "Control Objective", "Group"],
        inplace=True
    )

    # Reorder columns for clarity
    df = df[expected_columns]

    df.to_excel(output_file, index=False)
    print(f"✅ Audit checklist written to {output_file}")
