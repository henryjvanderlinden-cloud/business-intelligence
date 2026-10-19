---
id: wwi:object:1669580986:column:4
subject: wwi/tables/Application/PaymentMethods/columns/ValidFrom
item: 02
topic: meaning
tier: best-effort
summary: The moment this version of the row became current: the period start of SQL Server's system-versioning, which the server sets from its own clock at the time of the change.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6ad07d5080cc67c9c57b9cf621509187e6f222d2624c74328488725ed956287d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=a column type changes | text: Declared as datetime2, not nullable, system-time period start.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d7ebcd1cb8412d2d | recheck=every new extract | text: Observed: filled on 4 of 4 rows; 2 distinct values; from 2013-01-01T00:00:00 to 2016-01-01T16:00:00.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=a description is found | text: The moment this version of the row became current: the period start of SQL Server's system-versioning, which the server sets from its own clock at the time of the change.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=36ced96da225b404 | recheck=every new extract | text: Every ValidFrom lies on or before the extract's simulated date 2016-06-01 (from 2013-01-01T00:00:00 to 2016-01-01T16:00:00).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
