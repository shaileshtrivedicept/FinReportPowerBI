import pandas as pd
import os

def test_fact_template_columns():
    csv_path = "data/templates/fact_financials_template.csv"
    assert os.path.exists(csv_path)

    df = pd.read_csv(csv_path)
    expected_cols = [
        "Month", "Month_Label", "FY", "Period_No", "Entity", "Centre", "Segment",
        "Revenue_Type", "Record_Type", "Revenue", "Direct_Cost", "Gross_Margin",
        "Overhead_CEPT", "Overhead_Internal", "Total_Overhead", "Provision_Debtors",
        "Provision_Other", "Operating_Surplus", "Tax", "Net_Surplus", "AR_Closing",
        "AR_0_30", "AR_31_60", "AR_61_90", "AR_91_180", "AR_181_365", "AR_365_Plus",
        "WIP_Closing", "Collections", "Notes", "Source_Reference"
    ]
    assert list(df.columns) == expected_cols

def test_fact_xlsx_exists():
    assert os.path.exists("data/templates/fact_financials_template.xlsx")
