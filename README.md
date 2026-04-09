# CRDF–CAF Financial Diagnostics Data Model Starter

A clean, blank, Power BI-ready financial data model starter for CRDF–CAF reporting.

## 🎯 Project Objective
This repository provides a standardized data model and templates for monthly financial reporting. It is designed to be populated manually by finance/admin teams and imported directly into Power BI.

---

## 📁 Repository Structure
* **`data/templates/`**: Master blank fact table (XLSX/CSV) and supporting dimension tables.
* **`data/sample/`**: Example dummy data to demonstrate the model grain.
* **`docs/`**: Data dictionary, Power BI model specs, and user guides.
* **`scripts/`**: Python utilities for generating templates and validating data.
* **`tests/`**: Automated tests to ensure template integrity.

---

## 🚀 Getting Started

### 1. Requirements
* Python 3.x
* Required libraries: `pandas`, `openpyxl`

```bash
pip install -r requirements.txt
```

### 2. Generate Templates
If you need to regenerate the blank templates:
```bash
python scripts/generate_templates.py
```

### 3. Data Entry
1. Open `data/templates/fact_financials_template.xlsx`.
2. Follow the instructions in `docs/data_entry_guide.md`.
3. Fill in the `Fact_Financials` sheet.

### 4. Validate Your Data
Before importing to Power BI, run the validation script:
```bash
python scripts/validate_fact_table.py path/to/your_populated_file.xlsx
```

---

## 📊 Power BI Modeling
This starter uses a **Star Schema** with a "Mixed Grain" approach:
* **Segment_Row**: Use for specific project data.
* **Centre_Row**: Use for aggregate centre data.
* **Entity_Row**: Use for aggregate entity data.

Refer to `docs/powerbi_model_spec.md` for relationship setup and filtering rules to avoid double-counting.

---

## ⚠️ Important Note
This project **does not** include automated data extraction (OCR/ERP integration). It expects the `Fact_Financials` template to be populated as the primary source of truth.
