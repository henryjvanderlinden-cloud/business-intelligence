---
id: wwi:fk:FK_Warehouse_StockItemStockGroups_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions, see claims.
confidence: high
claims: 4
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract | text: Fan-out: joined from Warehouse.StockGroups to Warehouse.StockItemStockGroups, a Warehouse.StockGroups row repeats up to 91 times (median 42), so a measure of Warehouse.StockGroups summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract | text: Chasm trap: Warehouse.StockGroups also has other referring columns with several rows per parent (Sales.SpecialDeals.StockGroupID (up to 2 per parent)); joining Warehouse.StockItemStockGroups and one of these through Warehouse.StockGroups pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=the temporal type changes | text: Warehouse.StockGroups is system-versioned and the extract holds its current versions: joined in the extract, a row of Warehouse.StockItemStockGroups that names a row of Warehouse.StockGroups gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C4 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7c904e8d6f31eb57 | recheck=every new extract, or a description changes | text: Many-to-many: an item is in up to 3 groups (the relation on StockItemID, 01), so a measure of items reached through groups is counted once per group.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
