# Power BI Model Specification

## 1. Schema Architecture
* **Type:** Star Schema
* **Fact Table:** `Fact_Financials`
* **Dimensions:**
    * `Dim_Month`
    * `Dim_Entity`
    * `Dim_Centre`
    * `Dim_Segment`
    * `Dim_RevenueType`
    * `Dim_RecordType`

## 2. Relationships
All relationships are **1:Many** from Dimension to Fact, with **Single** cross-filter direction.

| From: Dimension (Column) | To: Fact (Column) |
| :--- | :--- |
| `Dim_Month[Month]` | `Fact_Financials[Month]` |
| `Dim_Entity[Entity]` | `Fact_Financials[Entity]` |
| `Dim_Centre[Centre]` | `Fact_Financials[Centre]` |
| `Dim_Segment[Segment]` | `Fact_Financials[Segment]` |
| `Dim_RevenueType[Revenue_Type]` | `Fact_Financials[Revenue_Type]` |
| `Dim_RecordType[Record_Type]` | `Fact_Financials[Record_Type]` |

## 3. Sorting Logic
To ensure charts display correctly, apply "Sort by Column" in Power BI:
* `Dim_Month[Month_Label]` sort by `Dim_Month[Sort_Order]`
* `Dim_Month[Month]` sort by `Dim_Month[Sort_Order]`
* `Dim_Entity[Entity]` sort by `Dim_Entity[Sort_Order]`
* `Dim_Centre[Centre]` sort by `Dim_Centre[Sort_Order]`
* `Dim_Segment[Segment]` sort by `Dim_Segment[Sort_Order]`

## 4. Row-Level Filtering (Mixed Grain)
Because the fact table contains data at multiple grains, visual-level or page-level filters **must** be applied:

* **Centre Reports:** Filter `Fact_Financials[Record_Type] = "Centre_Row"`
* **Segment Reports:** Filter `Fact_Financials[Record_Type] = "Segment_Row"`
* **Entity Reports:** Filter `Fact_Financials[Record_Type] = "Entity_Row"`

Failure to do this will result in inflated (double-counted) totals.
