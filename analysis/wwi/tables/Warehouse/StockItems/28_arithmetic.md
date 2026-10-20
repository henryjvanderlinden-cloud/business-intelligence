---
id: wwi:object:1314103722
subject: wwi/tables/Warehouse/StockItems
item: 28
topic: arithmetic
tier: best-effort
summary: Prices in decimal(18,2), rates and weights in decimal(18,3); the recommended retail price rounded half up.
confidence: high
claims: 2
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract | text: Rounding UnitPrice x 1.3 x (1 + TaxRate / 100) to cents reproduces RecommendedRetailPrice by: half up 227, half to even 218, half down 148, truncation 117, unrounded 104, of 227 items; all values are positive, so half up is not told apart from rounding ties towards positive infinity.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=277c0ec49cddab1c | recheck=every new extract, or a schema change | text: UnitPrice and RecommendedRetailPrice are decimal(18,2); TaxRate and TypicalWeightPerUnit decimal(18,3), using at most 0 and 2 decimals.

## Reasoning

measures.py rounds each recomputed value to cents by four modes (half up, half to even, half down, truncation) and counts the rows each reproduces; the declared precision and scale come from the catalogue, the decimals used from the extract.

## Uncertainties

None.

## For a person

None.
