---
id: wwi:fk:FK_Purchasing_Suppliers_PrimaryContactPersonID_Application_People
subject: wwi/across/relations/Purchasing.Suppliers.PrimaryContactPersonID__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Purchasing.Suppliers to Application.People; at most one row of Purchasing.Suppliers per row of Application.People in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ff68524a21b6805b48bd5e32465e5f7d85bb212866ef33723e61130f4cc60986
last_checked_at: 2026-10-19T20:31:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c7f4a03e68330f9b | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_Suppliers_PrimaryContactPersonID_Application_People from Purchasing.Suppliers.PrimaryContactPersonID to Application.People.PersonID, the primary key of Application.People: each row of Purchasing.Suppliers names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c7f4a03e68330f9b | recheck=every new extract | text: In this extract 13 of 13 rows of Purchasing.Suppliers name one of 13 referenced rows of Application.People (of 1,111); children per referenced parent: from 1 to 1, median 1; 13 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c7f4a03e68330f9b | recheck=every new extract | text: Joined from Purchasing.Suppliers to Application.People, the result keeps the grain of Purchasing.Suppliers: one row per row of Purchasing.Suppliers. Joined the other way, each row of Application.People repeats once per row of Purchasing.Suppliers that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=c7f4a03e68330f9b | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Application.People is named by more than one row of Purchasing.Suppliers. No unique constraint on PrimaryContactPersonID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
