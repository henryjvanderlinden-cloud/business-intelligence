---
id: wwi:fk:FK_Purchasing_SupplierTransactions_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Purchasing.SupplierTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 01
topic: granularity
tier: minimum
summary: Purchasing.SupplierTransactions to Purchasing.PurchaseOrders; at most one row of Purchasing.SupplierTransactions per row of Purchasing.PurchaseOrders in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 53939878d4705e61c16bdf86d6ceb01b27fa5dfaf25b382fcafe47549cacadf9
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_SupplierTransactions_PurchaseOrderID_Purchasing_PurchaseOrders from Purchasing.SupplierTransactions.PurchaseOrderID to Purchasing.PurchaseOrders.PurchaseOrderID, the primary key of Purchasing.PurchaseOrders: each row of Purchasing.SupplierTransactions names at most one row of Purchasing.PurchaseOrders.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=every new extract | text: In this extract 2,074 of 2,440 rows of Purchasing.SupplierTransactions name one of 2,074 referenced rows of Purchasing.PurchaseOrders (of 2,076); children per referenced parent: from 1 to 1, median 1; 2,074 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=every new extract | text: Joined from Purchasing.SupplierTransactions to Purchasing.PurchaseOrders, the result keeps the grain of Purchasing.SupplierTransactions: one row per row of Purchasing.SupplierTransactions (an inner join drops the 366 rows where PurchaseOrderID is empty). Joined the other way, each row of Purchasing.PurchaseOrders repeats once per row of Purchasing.SupplierTransactions that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=b04c588a7e630450 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Purchasing.PurchaseOrders is named by more than one row of Purchasing.SupplierTransactions. No unique constraint on PurchaseOrderID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
