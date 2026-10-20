---
id: wwi:fk:FK_Warehouse_StockItemStockGroups_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Warehouse.StockItemStockGroups to Warehouse.StockGroups; up to 91 rows of Warehouse.StockItemStockGroups per row of Warehouse.StockGroups.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f670ef8177dead5b5e47d778557264c86a21981b8489110ca9c398831d260ed1
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=the foreign key changes | text: Declared foreign key FK_Warehouse_StockItemStockGroups_StockGroupID_Warehouse_StockGroups from Warehouse.StockItemStockGroups.StockGroupID to Warehouse.StockGroups.StockGroupID, the primary key of Warehouse.StockGroups: each row of Warehouse.StockItemStockGroups names at most one row of Warehouse.StockGroups.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract | text: In this extract 442 of 442 rows of Warehouse.StockItemStockGroups name one of 9 referenced rows of Warehouse.StockGroups (of 10); children per referenced parent: from 14 to 91, median 42; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract | text: Joined from Warehouse.StockItemStockGroups to Warehouse.StockGroups, the result keeps the grain of Warehouse.StockItemStockGroups: one row per row of Warehouse.StockItemStockGroups. Joined the other way, each row of Warehouse.StockGroups repeats once per row of Warehouse.StockItemStockGroups that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
