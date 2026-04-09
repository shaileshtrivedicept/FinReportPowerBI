# Dashboard Specification

This document outlines the 5 core pages for the CRDF–CAF Financial Diagnostics Dashboard.

---

## Page 1: Chairman Summary
*High-level health check of the entire organization.*

* **KPI Cards:** Total Revenue, Operating Surplus, AR Closing, Cash Collection %.
* **Revenue Quality:** Stacked bar chart of Revenue by Revenue_Type (Earned vs Grant).
* **Surplus Waterfall:** Bridge from Gross Margin to Net Surplus.
* **Segment Viability Matrix:** Scatter plot (Revenue vs Margin %).
* **Entity Split:** Pie chart of Surplus by Entity (CRDF vs CAF).

---

## Page 2: Centre Diagnostics
*Deep dive into specific operational centres (e.g., CWAS, CUPP).*

* **Slicer:** Centre Name.
* **Monthly Trends:** Line chart showing Revenue vs Operating Surplus over time.
* **AR Ageing:** Bar chart showing the 0-30, 31-60... buckets for the selected centre.
* **WIP Monitor:** Gauge or card showing current WIP closing.
* **Summary Table:** Tabular view of all segments within the selected centre.

---

## Page 3: Segment Diagnostics
*Detailed analysis of revenue streams.*

* **Slicer:** Segment (PMU, Testing, Advisory).
* **Margin Analysis:** Comparison of Gross Margin % across different segments.
* **Contribution:** Tree map showing which segments contribute most to the total surplus.

---

## Page 4: Receivables & Integrity
*Focus on cash flow and balance sheet risk.*

* **AR Ageing Trend:** Area chart showing how different ageing buckets have grown/shrunk over months.
* **Bad Debt Risk:** Table of records where AR > 180 days is high.
* **Collection Efficiency:** Trend of Collections vs Revenue (Cash Conversion).
* **Provision Tracker:** Trend line of Provision_Debtors.

---

## Page 5: Variance Bridge
*Understanding changes over time.*

* **MoM Bridge:** Waterfall chart showing drivers of Surplus change from last month to current month.
* **YoY Bridge:** Comparison of current FY-to-date vs previous FY-to-date.
* **Top Drivers:** List of centres/segments with the largest positive and negative variance.
