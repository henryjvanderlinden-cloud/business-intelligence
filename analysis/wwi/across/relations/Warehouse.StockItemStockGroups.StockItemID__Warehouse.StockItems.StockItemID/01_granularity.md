---
id: wwi:fk:FK_Warehouse_StockItemStockGroups_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Warehouse.StockItemStockGroups.StockItemID__Warehouse.StockItems.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockItemStockGroups to Warehouse.StockItems; up to 3 rows of Warehouse.StockItemStockGroups per row of Warehouse.StockItems.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 31a3157d276a40f52264dd5f31bc6562c96fa4aaf725c9afb6efb0dbebf0ab36
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0c5855fa293df6a7 | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockItemStockGroups_StockItemID_Warehouse_StockItems from Warehouse.StockItemStockGroups.StockItemID to Warehouse.StockItems.StockItemID, the primary key of Warehouse.StockItems: each row of Warehouse.StockItemStockGroups names at most one row of Warehouse.StockItems.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0c5855fa293df6a7 | recheck=every new extract | text: In this extract 442 of 442 rows of Warehouse.StockItemStockGroups name one of 227 referenced rows of Warehouse.StockItems (of 227); children per referenced parent: from 1 to 3, median 2; 94 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0c5855fa293df6a7 | recheck=every new extract | text: Joined from Warehouse.StockItemStockGroups to Warehouse.StockItems, the result keeps the grain of Warehouse.StockItemStockGroups: one row per row of Warehouse.StockItemStockGroups. Joined the other way, each row of Warehouse.StockItems repeats once per row of Warehouse.StockItemStockGroups that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
