---
id: wwi:fk:FK_Purchasing_SupplierTransactions_SupplierID_Purchasing_Suppliers
subject: wwi/across/relations/Purchasing.SupplierTransactions.SupplierID__Purchasing.Suppliers.SupplierID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.SupplierTransactions to Purchasing.Suppliers; up to 1,233 rows of Purchasing.SupplierTransactions per row of Purchasing.Suppliers.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 542df9b5000ffee23364ad50df9b8732b2917a3a0a2c6ffc0e28059364cb0f83
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_SupplierTransactions_SupplierID_Purchasing_Suppliers from Purchasing.SupplierTransactions.SupplierID to Purchasing.Suppliers.SupplierID, the primary key of Purchasing.Suppliers: each row of Purchasing.SupplierTransactions names at most one row of Purchasing.Suppliers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: In this extract 2,440 of 2,440 rows of Purchasing.SupplierTransactions name one of 7 referenced rows of Purchasing.Suppliers (of 13); children per referenced parent: from 2 to 1,233, median 14; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6feb4a3743493f3b | recheck=every new extract | text: Joined from Purchasing.SupplierTransactions to Purchasing.Suppliers, the result keeps the grain of Purchasing.SupplierTransactions: one row per row of Purchasing.SupplierTransactions. Joined the other way, each row of Purchasing.Suppliers repeats once per row of Purchasing.SupplierTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
