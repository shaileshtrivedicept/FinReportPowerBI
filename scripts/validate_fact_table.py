import pandas as pd
import os
import sys

def validate_fact_table(filepath):
    print(f"--- Validating: {filepath} ---")

    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath, sheet_name='Fact_Financials')
    else:
        print("Unsupported file format.")
        return False

    errors = []
    warnings = []

    # 1. Required columns exist
    required_cols = [
        "Month", "Month_Label", "FY", "Period_No", "Entity", "Centre", "Segment",
        "Revenue_Type", "Record_Type"
    ]
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")

    if errors:
        print("Critical Errors found in schema. Aborting further validation.")
        for e in errors: print(f"ERROR: {e}")
        return False

    # 2. Dropdown validation (Load dimensions)
    dims_dir = "data/templates"
    dropdowns = {
        "Entity": pd.read_csv(os.path.join(dims_dir, "dim_entity.csv"))["Entity"].tolist(),
        "Centre": pd.read_csv(os.path.join(dims_dir, "dim_centre.csv"))["Centre"].tolist(),
        "Segment": pd.read_csv(os.path.join(dims_dir, "dim_segment.csv"))["Segment"].tolist(),
        "Revenue_Type": pd.read_csv(os.path.join(dims_dir, "dim_revenue_type.csv"))["Revenue_Type"].tolist(),
        "Record_Type": pd.read_csv(os.path.join(dims_dir, "dim_record_type.csv"))["Record_Type"].tolist(),
    }

    for col, valid_values in dropdowns.items():
        invalid = df[~df[col].isin(valid_values) & df[col].notna()][col].unique()
        if len(invalid) > 0:
            errors.append(f"Invalid values in {col}: {invalid}")

    # 3. Accounting Identities
    # Fill NAs with 0 for numeric checks
    numeric_cols = [
        "Revenue", "Direct_Cost", "Gross_Margin", "Overhead_CEPT", "Overhead_Internal",
        "Total_Overhead", "Provision_Debtors", "Provision_Other", "Operating_Surplus",
        "Tax", "Net_Surplus", "AR_Closing", "AR_0_30", "AR_31_60", "AR_61_90",
        "AR_91_180", "AR_181_365", "AR_365_Plus"
    ]
    df_num = df[numeric_cols].fillna(0)

    # Gross_Margin = Revenue - Direct_Cost
    gm_diff = (df_num["Gross_Margin"] - (df_num["Revenue"] - df_num["Direct_Cost"])).abs()
    if (gm_diff > 1).any():
        errors.append("Accounting Identity Failed: Gross_Margin != Revenue - Direct_Cost")

    # Total_Overhead = Overhead_CEPT + Overhead_Internal
    oh_diff = (df_num["Total_Overhead"] - (df_num["Overhead_CEPT"] + df_num["Overhead_Internal"])).abs()
    if (oh_diff > 1).any():
        errors.append("Accounting Identity Failed: Total_Overhead != Overhead_CEPT + Overhead_Internal")

    # Operating_Surplus = Gross_Margin - Total_Overhead - Provision_Debtors - Provision_Other
    os_diff = (df_num["Operating_Surplus"] - (df_num["Gross_Margin"] - df_num["Total_Overhead"] - df_num["Provision_Debtors"] - df_num["Provision_Other"])).abs()
    if (os_diff > 1).any():
        errors.append("Accounting Identity Failed: Operating_Surplus != Gross_Margin - Total_Overhead - Provisions")

    # Net_Surplus = Operating_Surplus - Tax
    ns_diff = (df_num["Net_Surplus"] - (df_num["Operating_Surplus"] - df_num["Tax"])).abs()
    if (ns_diff > 1).any():
        errors.append("Accounting Identity Failed: Net_Surplus != Operating_Surplus - Tax")

    # 4. Ageing Check
    ageing_sum = df_num[["AR_0_30", "AR_31_60", "AR_61_90", "AR_91_180", "AR_181_365", "AR_365_Plus"]].sum(axis=1)
    ar_diff = (df_num["AR_Closing"] - ageing_sum).abs()
    if (ar_diff > 1).any():
        warnings.append("AR Ageing buckets do not sum up to AR_Closing")

    # 5. Duplicate Key Check
    key_cols = ["Month", "Entity", "Centre", "Segment", "Record_Type"]
    duplicates = df.duplicated(subset=key_cols, keep=False)
    if duplicates.any():
        warnings.append(f"Potential duplicate records found for keys: {key_cols}")

    # Summary
    print(f"Validation Summary for {os.path.basename(filepath)}:")
    print(f"Rows processed: {len(df)}")

    if not errors and not warnings:
        print("✅ All checks passed!")
    else:
        for e in errors:
            print(f"❌ ERROR: {e}")
        for w in warnings:
            print(f"⚠️ WARNING: {w}")

    return len(errors) == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_fact_table.py <path_to_file>")
    else:
        success = validate_fact_table(sys.argv[1])
        sys.exit(0 if success else 1)
