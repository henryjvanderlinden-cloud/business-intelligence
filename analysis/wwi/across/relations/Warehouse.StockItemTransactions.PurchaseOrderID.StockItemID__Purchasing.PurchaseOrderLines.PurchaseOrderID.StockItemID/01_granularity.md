---
id: wwi:relation:Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Warehouse.StockItemTransactions to Purchasing.PurchaseOrderLines; at most one row of Warehouse.StockItemTransactions per row of Purchasing.PurchaseOrderLines in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 664bf3ce1e6055fd58b043e3d15e68a5454133c32d67454d5cd298527fed3ba5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3f3748bd53d11df3 | recheck=a constraint is declared | text: No foreign key or unique constraint declares this relation; Purchasing.PurchaseOrderLines.PurchaseOrderID + StockItemID is unique in the extract.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3f3748bd53d11df3 | recheck=every new extract | text: In this extract 8,367 of 236,843 rows of Warehouse.StockItemTransactions name one of 8,367 referenced rows of Purchasing.PurchaseOrderLines (of 8,376); children per referenced parent: from 1 to 1, median 1; 8,367 parents have exactly one.
- C3 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3f3748bd53d11df3 | recheck=every new extract | text: Joined from Warehouse.StockItemTransactions to Purchasing.PurchaseOrderLines, the result keeps the grain of Warehouse.StockItemTransactions: one row per row of Warehouse.StockItemTransactions (an inner join drops the 228,476 rows where PurchaseOrderID + StockItemID is empty). Joined the other way, each row of Purchasing.PurchaseOrderLines repeats once per row of Warehouse.StockItemTransactions that names it (C2); this rests on the parent combination being unique in this extract, which nothing declares.
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=3f3748bd53d11df3 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Purchasing.PurchaseOrderLines is named by more than one row of Warehouse.StockItemTransactions. No unique constraint on PurchaseOrderID + StockItemID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
