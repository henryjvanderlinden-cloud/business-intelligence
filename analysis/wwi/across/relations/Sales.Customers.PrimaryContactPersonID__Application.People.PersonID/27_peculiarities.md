---
id: wwi:fk:FK_Sales_Customers_PrimaryContactPersonID_Application_People
subject: wwi/across/relations/Sales.Customers.PrimaryContactPersonID__Application.People.PersonID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: roles, current versions, one-to-one not enforced.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: beb4a67d9dbf8afd5b69421099df2d5f90e9db6ba0e71faac346f5906ff90ecc
last_checked_at: 2026-10-20T05:51:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f987fc172b77fd7a | recheck=a foreign key changes | text: Several paths between the same two tables: Sales.Customers also refers to Application.People through AlternateContactPersonID, LastEditedBy; a join of the two must say which role it means.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f987fc172b77fd7a | recheck=the temporal type changes | text: Application.People is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.Customers that names a row of Application.People gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=f987fc172b77fd7a | recheck=a second row refers to the same parent | text: One row of Sales.Customers per row of Application.People holds only in this extract: nothing declares PrimaryContactPersonID unique, so several referring rows per parent are allowed, and a join that counts on one per parent rests on the extract.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
