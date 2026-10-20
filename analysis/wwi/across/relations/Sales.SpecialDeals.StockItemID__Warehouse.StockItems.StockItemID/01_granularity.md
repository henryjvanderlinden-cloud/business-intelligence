---
id: wwi:fk:FK_Sales_SpecialDeals_StockItemID_Warehouse_StockItems
subject: wwi/across/relations/Sales.SpecialDeals.StockItemID__Warehouse.StockItems.StockItemID
item: 01
topic: granularity
tier: minimum
summary: Declared from Sales.SpecialDeals to Warehouse.StockItems, but no row refers in this extract.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: cb51b7d3e22c66c02dd5c59834e35811e045f9f0f4fb175a7adf37420a6c7be0
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cebff2440fa97c63 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_SpecialDeals_StockItemID_Warehouse_StockItems from Sales.SpecialDeals.StockItemID to Warehouse.StockItems.StockItemID, the primary key of Warehouse.StockItems: each row of Sales.SpecialDeals names at most one row of Warehouse.StockItems.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cebff2440fa97c63 | recheck=the column fills | text: In this extract no row of Sales.SpecialDeals names a row of Warehouse.StockItems: StockItemID is empty in all 2 rows.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
