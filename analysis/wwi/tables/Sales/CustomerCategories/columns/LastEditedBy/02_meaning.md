---
id: wwi:object:2053582354:column:3
subject: wwi/tables/Sales/CustomerCategories/columns/LastEditedBy
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
input_schema_sha256: 3516219cd265a59d10aca95bacfbb1f3cf6b0bbbc898bec3a420ea5dff35f98e
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1da3725d368ce960 | recheck=a column type changes | text: Declared as int, not nullable.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1da3725d368ce960 | recheck=a foreign key changes | text: Refers to Application.People.PersonID (FK_Sales_CustomerCategories_Application_People, enabled and trusted).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0d7f5b9d8f038cc9 | recheck=every new extract | text: Observed: filled on 8 of 8 rows; 2 distinct values; from 1 to 9; values 1 (7), 9 (1).
- C4 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1da3725d368ce960 | recheck=a description is found | text: By its name and its foreign key to Application.People: the person who last changed the row.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e5d5c8603587cde6 | recheck=every new extract | text: 2 distinct editors: 7 rows by person 1, whose FullName is Data Conversion Only; 1 rows by employees (IsEmployee = 1 in Application.People).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
