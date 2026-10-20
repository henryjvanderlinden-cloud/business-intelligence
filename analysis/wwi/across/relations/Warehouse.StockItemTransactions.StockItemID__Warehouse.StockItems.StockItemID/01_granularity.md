---
id: wwi:fk:FK_Warehouse_StockItemTransactions_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Warehouse.StockItemTransactions.StockItemID__Warehouse.StockItems.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockItemTransactions to Warehouse.StockItems; up to 1,769 rows of Warehouse.StockItemTransactions per row of Warehouse.StockItems.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 78540177fbf453018f99dd3faf7db85cb13d79118746359fed7bfcbad97c7655
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=62542871044e4b50 | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockItemTransactions_StockItemID_Warehouse_StockItems from Warehouse.StockItemTransactions.StockItemID to Warehouse.StockItems.StockItemID, the primary key of Warehouse.StockItems: each row of Warehouse.StockItemTransactions names at most one row of Warehouse.StockItems.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=62542871044e4b50 | recheck=every new extract | text: In this extract 236,843 of 236,843 rows of Warehouse.StockItemTransactions name one of 227 referenced rows of Warehouse.StockItems (of 227); children per referenced parent: from 118 to 1,769, median 1,056; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=62542871044e4b50 | recheck=every new extract | text: Joined from Warehouse.StockItemTransactions to Warehouse.StockItems, the result keeps the grain of Warehouse.StockItemTransactions: one row per row of Warehouse.StockItemTransactions. Joined the other way, each row of Warehouse.StockItems repeats once per row of Warehouse.StockItemTransactions that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
