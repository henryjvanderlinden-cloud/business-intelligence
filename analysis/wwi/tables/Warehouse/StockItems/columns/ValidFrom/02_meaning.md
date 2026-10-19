---
id: wwi:object:1314103722:column:24
subject: wwi/tables/Warehouse/StockItems/columns/ValidFrom
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=fbbc435f3d190ff0 | recheck=a column type changes | text: Declared as datetime2, not nullable, system-time period start.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7f977b924a38ef2c | recheck=every new extract | text: Observed: filled on 227 of 227 rows; 10 distinct values; from 2016-05-31T23:00:00 to 2016-05-31T23:12:00.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=fbbc435f3d190ff0 | recheck=a description is found | text: The moment this version of the row became current: the period start of SQL Server's system-versioning, which the server sets from its own clock at the time of the change.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e039bf38a52409e7 | recheck=every new extract | text: Every ValidFrom lies on or before the extract's simulated date 2016-06-01 (from 2016-05-31T23:00:00 to 2016-05-31T23:12:00).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
