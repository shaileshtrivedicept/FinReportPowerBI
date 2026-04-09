# Validation Rules — Financial Diagnostics

The `scripts/validate_fact_table.py` script enforces the following rules to ensure data integrity before Power BI ingestion.

## 1. Schema Integrity
* All required columns must be present.
* No missing headers allowed.

## 2. Referential Integrity (Dropdowns)
* Values in `Entity`, `Centre`, `Segment`, `Revenue_Type`, and `Record_Type` must match the master lists in the `data/templates/dim_*.csv` files.

## 3. Accounting Identities (Tolerance: ±1)
The script checks for mathematical consistency across rows:
* **Gross Margin:** `Revenue - Direct_Cost`
* **Total Overhead:** `Overhead_CEPT + Overhead_Internal`
* **Operating Surplus:** `Gross_Margin - Total_Overhead - Provision_Debtors - Provision_Other`
* **Net Surplus:** `Operating_Surplus - Tax`

## 4. Balance Sheet Logic
* **AR Consistency:** The sum of all ageing buckets (`AR_0_30` + `AR_31_60` + ...) should approximately equal `AR_Closing`.

## 5. Duplicate Prevention
* A **Warning** is issued if multiple rows exist for the same combination of:
    `Month + Entity + Centre + Segment + Record_Type`
* In a mixed-grain model, there should usually be only one unique record for this combination.
