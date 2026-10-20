---
id: wwi:fk:FK_Warehouse_StockItemStockGroups_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 06
topic: keys
tier: minimum
summary: Warehouse.StockItemStockGroups.StockGroupID refers to the primary key Warehouse.StockGroups.StockGroupID, enforced.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f670ef8177dead5b5e47d778557264c86a21981b8489110ca9c398831d260ed1
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=the foreign key changes | text: Child side: Warehouse.StockItemStockGroups.StockGroupID, int, not nullable; a foreign key, enabled and trusted; on delete no action.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=the primary key changes | text: Parent side: Warehouse.StockGroups.StockGroupID, the declared primary key of Warehouse.StockGroups.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract | text: No other column of Warehouse.StockGroups that is unique in this extract holds all values of StockGroupID: the primary key is the only key the values fit.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
