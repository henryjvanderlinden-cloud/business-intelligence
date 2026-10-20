---
id: wwi:object:1314103722
subject: wwi/tables/Warehouse/StockItems
item: 09
topic: derived
tier: best-effort
summary: RecommendedRetailPrice = UnitPrice x 1.3 x (1 + TaxRate / 100), rounded half up, on every item.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a2a70ec4f434c5caf3e43bfaa2fcb63886a956c95e50e40cbf6b01c6e0f40c7d
last_checked_at: 2026-10-20T20:06:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: RecommendedRetailPrice equals UnitPrice x 1.3 x (1 + TaxRate / 100) rounded half up to cents on 227 of 227 items. The formula was found by inspecting the ratio RecommendedRetailPrice / UnitPrice first (most common: 1.4304 on 7, 1.4950 on 110, 1.4951 on 19, 1.4952 on 19, 1.4954 on 42).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: So the recommended retail price is the selling price with a 30% mark-up, tax included; that this is the source's rule rather than a pattern of the sample data is a reading.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: LastCostPrice (Warehouse.StockItemHoldings) is not a fixed share of UnitPrice: 74 distinct exact ratios over the 227 items (37 when rounded to 2 decimals).

## Reasoning

measures.py recomputes the values that the table's columns suggest are computed from others and compares them with the stored ones, row by row; where a formula was found by inspecting ratios first, that is said. A formula that holds on every row of the extract is observed; that it is the source's own rule is a reading.

## Uncertainties

None.

## For a person

None.
