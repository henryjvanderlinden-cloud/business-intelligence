---
id: wwi:fk:FK_Purchasing_PurchaseOrderLines_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Purchasing.PurchaseOrderLines.StockItemID__Warehouse.StockItems.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Purchasing.PurchaseOrderLines to Warehouse.StockItems; up to 966 rows of Purchasing.PurchaseOrderLines per row of Warehouse.StockItems.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 38fdfd243c9ed6f7b59255a3dfd294ea9e2ad3b9f430630e60396efa12da272c
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9d18f1c0055b3877 | recheck=the foreign key changes | text: Declared foreign key FK_Purchasing_PurchaseOrderLines_StockItemID_Warehouse_StockItems from Purchasing.PurchaseOrderLines.StockItemID to Warehouse.StockItems.StockItemID, the primary key of Warehouse.StockItems: each row of Purchasing.PurchaseOrderLines names at most one row of Warehouse.StockItems.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9d18f1c0055b3877 | recheck=every new extract | text: In this extract 8,376 of 8,376 rows of Purchasing.PurchaseOrderLines name one of 227 referenced rows of Warehouse.StockItems (of 227); children per referenced parent: from 1 to 966, median 1; 206 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9d18f1c0055b3877 | recheck=every new extract | text: Joined from Purchasing.PurchaseOrderLines to Warehouse.StockItems, the result keeps the grain of Purchasing.PurchaseOrderLines: one row per row of Purchasing.PurchaseOrderLines. Joined the other way, each row of Warehouse.StockItems repeats once per row of Purchasing.PurchaseOrderLines that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
