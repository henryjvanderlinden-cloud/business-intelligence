---
id: wwi:object:94623380
subject: wwi/tables/Sales/OrderLines
item: 09
topic: derived
tier: best-effort
summary: No derived column; UnitPrice and TaxRate are the item's current values on almost every line.
confidence: high
claims: 1
written_by: claude-opus-5-5
written_at: 2026-10-20T20:06:00Z
step: S08-112
method: measures by prototypes/information_analysis/measures.py (blob 89f3c0d7d2fd53e7e60d4575675beeac0ebb43e8), claims by write_measures.py (blob 8f679dc60353e6e20d24f22fad398861cc10b5ab); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c00930db9c641c1b31801c17473429ceaa1b6c45519761d89148dd23ed44a1e7
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b05dba876c35f098 | recheck=every new extract | text: UnitPrice equals the stock item's current UnitPrice on 231,064 of 231,581 lines, TaxRate its current TaxRate on 231,581.

## Reasoning

measures.py recomputes the values that the table's columns suggest are computed from others and compares them with the stored ones, row by row; where a formula was found by inspecting ratios first, that is said. A formula that holds on every row of the extract is observed; that it is the source's own rule is a reading.

## Uncertainties

None.

## For a person

None.
