---
id: wwi:object:2018106230:column:24
subject: wwi/tables/Sales/Invoices/columns/LastEditedBy
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
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a column type changes | text: Declared as int, not nullable.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a foreign key changes | text: Refers to Application.People.PersonID (FK_Sales_Invoices_Application_People, enabled and trusted).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract | text: Observed: filled on 70,566 of 70,566 rows; 19 distinct values; from 2 to 20.
- C4 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a description is found | text: By its name and its foreign key to Application.People: the person who last changed the row.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=41edc876c984c8e3 | recheck=every new extract | text: 19 distinct editors: 70,566 rows by employees (IsEmployee = 1 in Application.People).

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
