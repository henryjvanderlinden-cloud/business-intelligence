---
id: wwi:fk:FK_Warehouse_StockItemStockGroups_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Warehouse.StockItemStockGroups.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 02
topic: meaning
tier: minimum
summary: StockGroup assigned to this stock item (FK indexed via unique constraint)
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f670ef8177dead5b5e47d778557264c86a21981b8489110ca9c398831d260ed1
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=7c904e8d6f31eb57 | recheck=the description changes | text: The source describes Warehouse.StockItemStockGroups.StockGroupID as "StockGroup assigned to this stock item (FK indexed via unique constraint)".
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=7c904e8d6f31eb57 | recheck=every new extract, or a description changes | text: The other side of the bridge between items and groups.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
