---
id: wwi:object:1314103722:column:11
subject: wwi/tables/Warehouse/StockItems/columns/IsChillerStock
item: 02
topic: meaning
tier: best-effort
summary: Whether the item must be kept chilled; true for 8 items.
confidence: low
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a2a70ec4f434c5caf3e43bfaa2fcb63886a956c95e50e40cbf6b01c6e0f40c7d
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=fbbc435f3d190ff0 | recheck=the description changes | text: The source describes it as "Does this stock item need to be in a chiller?" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=fbbc435f3d190ff0 | recheck=a column type changes | text: Declared as bit, not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7f977b924a38ef2c | recheck=every new extract | text: Observed: filled on 227 of 227 rows; 2 distinct values; from 0 to 1; values 0 (219), 1 (8).
- C4 | type=declared | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Context, not a description of this column: Microsoft: "Now, to meet food handling requirements, they must monitor the temperature in their chiller room and any of their trucks that have chiller sections."

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
