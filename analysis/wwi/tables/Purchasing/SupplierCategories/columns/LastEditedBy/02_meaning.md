---
id: wwi:object:1861581670:column:3
subject: wwi/tables/Purchasing/SupplierCategories/columns/LastEditedBy
item: 02
topic: meaning
tier: best-effort
summary: The person who last changed the row: a staff member of Application.People, or person 1 (Data Conversion Only), the technical user of the initial load.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T07:28:00Z
step: S08-067
method: mechanical claims by prototypes/information_analysis/write_column_meanings.py from the catalogue and profile evidence; readings by claude-opus-5-5 from that evidence and Microsoft's description of the business (evidence 0f9e0d3eb9dd8048); script blob write_column_meanings.py ab6eb04a93fb24b0da04e43e0e5426fa51442758
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1419ef6b992982575960251d90234c9f5f46b72d6559f42f83b10ceb82e9e21f
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a84296fdd02696bb | recheck=a column type changes | text: Declared as int, not nullable.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a84296fdd02696bb | recheck=a foreign key changes | text: Refers to Application.People.PersonID (FK_Purchasing_SupplierCategories_Application_People, enabled and trusted).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4669dabe65f6b166 | recheck=every new extract | text: Observed: filled on 9 of 9 rows; 2 distinct values; from 1 to 16; values 1 (8), 16 (1).
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a84296fdd02696bb,4669dabe65f6b166 | recheck=a description is found | text: The person who last changed the row: a staff member of Application.People, or person 1 (Data Conversion Only), the technical user of the initial load.

## Reasoning

Mechanical claims from the catalogue and profile; any reading is the writer's, with its confidence.

## Uncertainties

None.

## For a person

None.
