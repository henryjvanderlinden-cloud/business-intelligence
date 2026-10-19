---
id: wwi:object:1474104292:column:7
subject: wwi/tables/Warehouse/StockItemHoldings/columns/TargetStockLevel
item: 02
topic: meaning
tier: best-effort
summary: Named a target stock level but described as "Typical quantity ordered": the name and the description disagree.
confidence: unknown
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: bb1ea17573cd7d7073444df38e148e0a4fc7ac5b6c6bc1078e0bd538c0085e24
last_checked_at: 2026-10-19T09:21:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: the description changes, or every new extract
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77 | recheck=the description changes | text: The source describes it as "Typical quantity ordered" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77 | recheck=a column type changes | text: Declared as int, not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a4dfbd2511423ab3 | recheck=every new extract | text: Observed: filled on 227 of 227 rows; 13 distinct values; from 2 to 500.
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=documentation or a person settles it | text: Which of the two meanings holds is not established from the data.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
