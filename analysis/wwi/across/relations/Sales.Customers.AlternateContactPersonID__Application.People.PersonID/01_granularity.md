---
id: wwi:fk:FK_Sales_Customers_AlternateContactPersonID_Application_People
subject: wwi/across/relations/Sales.Customers.AlternateContactPersonID__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Sales.Customers to Application.People; at most one row of Sales.Customers per row of Application.People in this extract.
confidence: medium
claims: 4
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fac8c1f490756d1a | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Customers_AlternateContactPersonID_Application_People from Sales.Customers.AlternateContactPersonID to Application.People.PersonID, the primary key of Application.People: each row of Sales.Customers names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fac8c1f490756d1a | recheck=every new extract | text: In this extract 402 of 663 rows of Sales.Customers name one of 402 referenced rows of Application.People (of 1,111); children per referenced parent: from 1 to 1, median 1; 402 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fac8c1f490756d1a | recheck=every new extract | text: Joined from Sales.Customers to Application.People, the result keeps the grain of Sales.Customers: one row per row of Sales.Customers (an inner join drops the 261 rows where AlternateContactPersonID is empty). Joined the other way, each row of Application.People repeats once per row of Sales.Customers that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=fac8c1f490756d1a | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Application.People is named by more than one row of Sales.Customers. No unique constraint on AlternateContactPersonID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
