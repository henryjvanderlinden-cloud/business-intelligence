---
id: wwi:fk:FK_Purchasing_SupplierTransactions_Application_People
subject: wwi/across/relations/Purchasing.SupplierTransactions.LastEditedBy__Application.People.PersonID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.SupplierTransactions to Application.People; up to 213 rows of Purchasing.SupplierTransactions per row of Application.People.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 761eee995677154cd8e1acaa7dae892a3dd5f6f01b4682ce4cf692b5c6a6724e
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2aeb8e19b4b97081 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_SupplierTransactions_Application_People from Purchasing.SupplierTransactions.LastEditedBy to Application.People.PersonID, the primary key of Application.People: each row of Purchasing.SupplierTransactions names at most one row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2aeb8e19b4b97081 | recheck=every new extract | text: In this extract 2,440 of 2,440 rows of Purchasing.SupplierTransactions name one of 19 referenced rows of Application.People (of 1,111); children per referenced parent: from 51 to 213, median 110; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=2aeb8e19b4b97081 | recheck=every new extract | text: Joined from Purchasing.SupplierTransactions to Application.People, the result keeps the grain of Purchasing.SupplierTransactions: one row per row of Purchasing.SupplierTransactions. Joined the other way, each row of Application.People repeats once per row of Purchasing.SupplierTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
