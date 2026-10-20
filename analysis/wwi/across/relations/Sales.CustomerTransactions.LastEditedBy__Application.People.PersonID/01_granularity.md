---
id: wwi:fk:FK_Sales_CustomerTransactions_Application_People
subject: wwi/across/relations/Sales.CustomerTransactions.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.CustomerTransactions to Application.People; up to 6,127 rows of Sales.CustomerTransactions per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ca90f2c950a2c4a64ee09d7633667d75e7794af62bbcaa09e20c0949f4d66218
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a92a7b3915b28ffc | recheck=the foreign key changes | text: Declared foreign key FK_Sales_CustomerTransactions_Application_People from Sales.CustomerTransactions.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Sales.CustomerTransactions names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a92a7b3915b28ffc | recheck=every new extract | text: In this extract 97,242 of 97,242 rows of Sales.CustomerTransactions name one of 19 referenced rows of Application.People (of 1,111); children per referenced parent: from 3,827 to 6,127, median 5,250; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a92a7b3915b28ffc | recheck=every new extract | text: Joined from Sales.CustomerTransactions to Application.People, the result keeps the grain of Sales.CustomerTransactions: one row per row of Sales.CustomerTransactions. Joined the other way, each row of Application.People repeats once per row of Sales.CustomerTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
