# Sample Data Notes

This directory contains `fact_financials_sample.csv`, which provides dummy rows to demonstrate the "Mixed Grain" model.

## Sample Rows Breakdown:
1. **Row 1 (Segment_Row):** Represents specific project data for CUPP Core Advisory.
2. **Row 2 (Centre_Row):** Represents the total for CUPP. In this dummy example, it matches the segment row for simplicity, but in real use, it would be the sum of all CUPP segments.
3. **Row 3 (Entity_Row):** Represents the total for the CRDF Entity.
4. **Row 4 (Segment_Row):** Represents a Grant-funded project for CWAS.

## Testing
You can test the validation script against this sample:
```bash
python scripts/validate_fact_table.py data/sample/fact_financials_sample.csv
```
