---
id: wwi:fk:FK_Warehouse_StockItemTransactions_PurchaseOrderID_Purchasing_PurchaseOrders
subject: wwi/across/relations/Warehouse.StockItemTransactions.PurchaseOrderID__Purchasing.PurchaseOrders.PurchaseOrderID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockItemTransactions to Purchasing.PurchaseOrders; up to 34 rows of Warehouse.StockItemTransactions per row of Purchasing.PurchaseOrders.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: abd4db31387266f8dd2ffeedb2855f9677180a94426c561e7b4f576d7d7fde6d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3057590bbabac1bd | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockItemTransactions_PurchaseOrderID_Purchasing_PurchaseOrders from Warehouse.StockItemTransactions.PurchaseOrderID to Purchasing.PurchaseOrders.PurchaseOrderID, the primary key of Purchasing.PurchaseOrders: each row of Warehouse.StockItemTransactions names at most one row of Purchasing.PurchaseOrders.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3057590bbabac1bd | recheck=every new extract | text: In this extract 8,367 of 236,843 rows of Warehouse.StockItemTransactions name one of 2,074 referenced rows of Purchasing.PurchaseOrders (of 2,076); children per referenced parent: from 1 to 34, median 3; 150 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=3057590bbabac1bd | recheck=every new extract | text: Joined from Warehouse.StockItemTransactions to Purchasing.PurchaseOrders, the result keeps the grain of Warehouse.StockItemTransactions: one row per row of Warehouse.StockItemTransactions (an inner join drops the 228,476 rows where PurchaseOrderID is empty). Joined the other way, each row of Purchasing.PurchaseOrders repeats once per row of Warehouse.StockItemTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
