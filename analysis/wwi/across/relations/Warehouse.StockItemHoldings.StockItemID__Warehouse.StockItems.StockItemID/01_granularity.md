---
id: wwi:fk:PKFK_Warehouse_StockItemHoldings_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Warehouse.StockItemHoldings.StockItemID__Warehouse.StockItems.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Warehouse.StockItemHoldings to Warehouse.StockItems; at most one row of Warehouse.StockItemHoldings per row of Warehouse.StockItems in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b911d56bc82bd130674e5d6a47ad718692a501ce79aad5ff7705e796f49d301d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ccdab44e36137145 | recheck=the foreign key changes | text: Declared foreign key PKFK_Warehouse_StockItemHoldings_StockItemID_Warehouse_StockItems from Warehouse.StockItemHoldings.StockItemID to Warehouse.StockItems.StockItemID, the primary key of Warehouse.StockItems: each row of Warehouse.StockItemHoldings names at most one row of Warehouse.StockItems.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ccdab44e36137145 | recheck=every new extract | text: In this extract 227 of 227 rows of Warehouse.StockItemHoldings name one of 227 referenced rows of Warehouse.StockItems (of 227); children per referenced parent: from 1 to 1, median 1; 227 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ccdab44e36137145 | recheck=every new extract | text: Joined from Warehouse.StockItemHoldings to Warehouse.StockItems, the result keeps the grain of Warehouse.StockItemHoldings: one row per row of Warehouse.StockItemHoldings. Joined the other way, each row of Warehouse.StockItems repeats once per row of Warehouse.StockItemHoldings that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ccdab44e36137145 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Warehouse.StockItems is named by more than one row of Warehouse.StockItemHoldings. No unique constraint on StockItemID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
