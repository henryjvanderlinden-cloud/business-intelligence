---
id: wwi:object:1026102696:column:8
subject: wwi/tables/Purchasing/PurchaseOrders/columns/IsOrderFinalized
item: 02
topic: meaning
tier: best-effort
summary: Whether the purchase order is finalized; false for 2 orders.
confidence: low
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: adb80ef2e4b8c472bfbd6569b8b3340fe525f86fe4769f74faa03e1e6624864a
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=the description changes | text: The source describes it as "Is this purchase order now considered finalized?" (declared, not verified against behaviour beyond the claims below).
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=a column type changes | text: Declared as bit, not nullable.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=6883f497d8b4086d | recheck=every new extract | text: Observed: filled on 2,076 of 2,076 rows; 2 distinct values; from 0 to 1; values 1 (2,074), 0 (2).
- C4 | type=declared | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Context, not a description of this column: Microsoft: "Periodically, WWI pays suppliers for items that were on purchase orders. The payments often occur some time after they receive the goods."

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
