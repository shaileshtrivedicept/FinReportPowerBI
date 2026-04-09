# Data Dictionary — CRDF–CAF Financial Diagnostics

## Fact Table: `Fact_Financials`

| Column | Type | Description |
| :--- | :--- | :--- |
| **Month** | Date | Month-end date (YYYY-MM-DD). |
| **Month_Label** | Text | Reporting label (e.g., Oct-25). |
| **FY** | Text | Financial Year (e.g., FY25-26). |
| **Period_No** | Integer | Month number within FY (1=Apr, 12=Mar). |
| **Entity** | Text | CRDF, CAF, or Combined. |
| **Centre** | Text | Specific centre name (e.g., CUPP, CWAS). |
| **Segment** | Text | Project segment (e.g., PMU, Core Advisory). |
| **Revenue_Type** | Text | Earned Fees, Grant, Fund Transfer, etc. |
| **Record_Type** | Text | **CRITICAL**: Segment_Row, Centre_Row, or Entity_Row. |
| **Revenue** | Number | Total income for the period. |
| **Direct_Cost** | Number | Direct expenses associated with revenue. |
| **Gross_Margin** | Number | `Revenue - Direct_Cost` |
| **Overhead_CEPT** | Number | Overheads payable to CEPT University. |
| **Overhead_Internal** | Number | Internal CRDF/CAF overheads. |
| **Total_Overhead** | Number | `Overhead_CEPT + Overhead_Internal` |
| **Provision_Debtors** | Number | Provision for doubtful debts. |
| **Provision_Other** | Number | Other accounting provisions. |
| **Operating_Surplus**| Number | `Gross_Margin - Total_Overhead - Provisions` |
| **Tax** | Number | Provision for income tax. |
| **Net_Surplus** | Number | `Operating_Surplus - Tax` |
| **AR_Closing** | Number | Total Accounts Receivable (closing balance). |
| **AR_0_30** | Number | AR Ageing: 0 to 30 days. |
| **AR_31_60** | Number | AR Ageing: 31 to 60 days. |
| **AR_61_90** | Number | AR Ageing: 61 to 90 days. |
| **AR_91_180** | Number | AR Ageing: 91 to 180 days. |
| **AR_181_365** | Number | AR Ageing: 181 to 365 days. |
| **AR_365_Plus** | Number | AR Ageing: Over 365 days. |
| **WIP_Closing** | Number | Work-in-Progress closing balance. |
| **Collections** | Number | Cash collected during the period. |
| **Notes** | Text | Qualitative notes / caveats. |
| **Source_Reference** | Text | Reference to source ERP/Ledger. |

---

## Recommended DAX Measures

### 1. Revenue & Surplus
* **Total Revenue** = `SUM(Fact_Financials[Revenue])`
* **Direct Cost** = `SUM(Fact_Financials[Direct_Cost])`
* **Gross Margin** = `[Total Revenue] - [Direct Cost]`
* **Gross Margin %** = `DIVIDE([Gross_Margin], [Total Revenue], 0)`
* **Operating Surplus** = `SUM(Fact_Financials[Operating_Surplus])`
* **Net Surplus** = `SUM(Fact_Financials[Net_Surplus])`
* **Net Margin %** = `DIVIDE([Net_Surplus], [Total Revenue], 0)`

### 2. Receivables & Collections
* **AR Closing** = `SUM(Fact_Financials[AR_Closing])`
* **AR Over 180 Days** = `SUM(Fact_Financials[AR_181_365]) + SUM(Fact_Financials[AR_365_Plus])`
* **AR Risk %** = `DIVIDE([AR Over 180 Days], [AR Closing], 0)`
* **Cash Collection** = `SUM(Fact_Financials[Collections])`
* **Cash Conversion %** = `DIVIDE([Cash Collection], [Total Revenue], 0)` (Caution: Timing differences)

### 3. WIP
* **Total WIP** = `SUM(Fact_Financials[WIP_Closing])`
