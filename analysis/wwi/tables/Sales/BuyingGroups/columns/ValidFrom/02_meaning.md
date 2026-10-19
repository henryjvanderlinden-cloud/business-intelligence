---
id: wwi:object:1957582012:column:4
subject: wwi/tables/Sales/BuyingGroups/columns/ValidFrom
item: 02
topic: meaning
tier: best-effort
summary: The moment this version of the row became current, set by SQL Server's system-versioning (period start). It is the clock time of the change, which in WWI usually but not always matches simulated time (Application.Countries has a version stamped 2022-10-07).
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 297115804655cf4216c6a4fddc22ea28db74d9e3dc4eab79962b9172a801b9a3
last_checked_at: 2026-10-19T07:28:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ee1eebac15b0a67f | recheck=a column type changes | text: Declared as datetime2, not nullable, system-time period start.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f25d3c1535c3ec51 | recheck=every new extract | text: Observed: filled on 2 of 2 rows; 1 distinct value; from 2013-01-01T00:00:00 to 2013-01-01T00:00:00; always at midnight.
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ee1eebac15b0a67f,f25d3c1535c3ec51 | recheck=a description is found | text: The moment this version of the row became current, set by SQL Server's system-versioning (period start). It is the clock time of the change, which in WWI usually but not always matches simulated time (Application.Countries has a version stamped 2022-10-07).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
