---
id: wwi:fk:FK_Purchasing_SupplierTransactions_TransactionTypeID_Application_TransactionTypes
subject: wwi/across/relations/Purchasing.SupplierTransactions.TransactionTypeID__Application.TransactionTypes.TransactionTypeID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.SupplierTransactions to Application.TransactionTypes; up to 2,074 rows of Purchasing.SupplierTransactions per row of Application.TransactionTypes.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 171fcc7bdbc87d1828b65385be1041f51ef993396301648c56409d8a28b74db3
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=5d7d7a1fbebd64b4 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_SupplierTransactions_TransactionTypeID_Application_TransactionTypes from Purchasing.SupplierTransactions.TransactionTypeID to Application.TransactionTypes.TransactionTypeID, the primary key of Application.TransactionTypes: each row of Purchasing.SupplierTransactions names at most one row of Application.TransactionTypes.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=5d7d7a1fbebd64b4 | recheck=every new extract | text: In this extract 2,440 of 2,440 rows of Purchasing.SupplierTransactions name one of 2 referenced rows of Application.TransactionTypes (of 13); children per referenced parent: from 366 to 2,074, median 1,220; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=5d7d7a1fbebd64b4 | recheck=every new extract | text: Joined from Purchasing.SupplierTransactions to Application.TransactionTypes, the result keeps the grain of Purchasing.SupplierTransactions: one row per row of Purchasing.SupplierTransactions. Joined the other way, each row of Application.TransactionTypes repeats once per row of Purchasing.SupplierTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
