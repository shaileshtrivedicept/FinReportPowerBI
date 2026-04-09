# Data Entry Guide — Financial Diagnostics

This guide helps finance and admin staff populate the financial data template for Power BI reporting.

## 1. Getting Started
1. Open `data/templates/fact_financials_template.xlsx`.
2. Navigate to the `Fact_Financials` sheet.
3. Ensure the top row (headers) is not modified.

## 2. The Mixed-Grain Model (Crucial)
This model supports data at different levels. You must label each row correctly using the `Record_Type` column:

| Record_Type | When to use | Example |
| :--- | :--- | :--- |
| **Segment_Row** | When entering data for a specific project/segment. | CWAS - Core Advisory |
| **Centre_Row** | When entering data aggregated at the Centre level. | CWAS Total |
| **Entity_Row** | When entering data aggregated at the Entity level. | CRDF Total |

**Why?** Power BI uses these labels to ensure it doesn't "double count" when you look at different reports.

## 3. Standard Labels
Use the dropdown menus in the Excel file for:
* **Entity** (CRDF, CAF, etc.)
* **Centre** (CUPP, CWAS, etc.)
* **Segment** (PMU, Grant, etc.)
* **Revenue_Type**
* **Record_Type**

## 4. Best Practices
* **Dates:** Use the last day of the month (e.g., `2025-10-31`).
* **Numbers:** Enter plain numbers. Do not include currency symbols or commas.
* **Blanks:** If a value is zero or not applicable, leave it blank or enter `0`. Do **not** enter `N/A` or `-`.
* **No Formulas:** Calculate values (like Gross Margin) before pasting into the template, or let the validation script check them. Do **not** put Excel formulas in the fact rows.

## 5. Validation
Before sending the file to the IT/Power BI team, run the validation script:
```bash
python scripts/validate_fact_table.py path/to/your_file.xlsx
```
Fix any **ERROR** messages before submission.
