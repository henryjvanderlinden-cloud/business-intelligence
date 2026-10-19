---
id: wwi:object:194099732:column:3
subject: wwi/tables/Warehouse/StockGroups/columns/LastEditedBy
item: 02
topic: meaning
tier: best-effort
summary: By its name and its foreign key to Application.People: the person who last changed the row.
confidence: low
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py d323750bb7f53a5d89ef6436d25f033e9ecfabd0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e95d0e414e870e18e624d3a1e63d4219e1116a6fc359fd638fb4ba9a22247f02
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=a column type changes | text: Declared as int, not nullable.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=a foreign key changes | text: Refers to Application.People.PersonID (FK_Warehouse_StockGroups_Application_People, enabled and trusted).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f17e21d7a1059397 | recheck=every new extract | text: Observed: filled on 10 of 10 rows; 2 distinct values; from 1 to 9; values 1 (9), 9 (1).
- C4 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=38f00eb780b1f6ea | recheck=a description is found | text: By its name and its foreign key to Application.People: the person who last changed the row.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=038152a4a9260062 | recheck=every new extract | text: 2 distinct editors: 9 rows by person 1, whose FullName is Data Conversion Only; 1 rows by employees (IsEmployee = 1 in Application.People).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
