---
id: wwi:fk:FK_Purchasing_SupplierTransactions_PaymentMethodID_Application_PaymentMethods
subject: wwi/across/relations/Purchasing.SupplierTransactions.PaymentMethodID__Application.PaymentMethods.PaymentMethodID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.SupplierTransactions to Application.PaymentMethods; up to 2,440 rows of Purchasing.SupplierTransactions per row of Application.PaymentMethods.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 9705f2163a8007cd2ca77ac3f144ba94ef7c97197931bb64bce99580e252478a
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=14b4d6fed181b8d4 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_SupplierTransactions_PaymentMethodID_Application_PaymentMethods from Purchasing.SupplierTransactions.PaymentMethodID to Application.PaymentMethods.PaymentMethodID, the primary key of Application.PaymentMethods: each row of Purchasing.SupplierTransactions names at most one row of Application.PaymentMethods.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=14b4d6fed181b8d4 | recheck=every new extract | text: In this extract 2,440 of 2,440 rows of Purchasing.SupplierTransactions name one of 1 referenced rows of Application.PaymentMethods (of 4); children per referenced parent: from 2,440 to 2,440, median 2,440; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=14b4d6fed181b8d4 | recheck=every new extract | text: Joined from Purchasing.SupplierTransactions to Application.PaymentMethods, the result keeps the grain of Purchasing.SupplierTransactions: one row per row of Purchasing.SupplierTransactions. Joined the other way, each row of Application.PaymentMethods repeats once per row of Purchasing.SupplierTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
