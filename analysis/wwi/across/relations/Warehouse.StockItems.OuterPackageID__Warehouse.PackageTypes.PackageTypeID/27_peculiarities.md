---
id: wwi:fk:FK_Warehouse_StockItems_OuterPackageID_Warehouse_PackageTypes
subject: wwi/across/relations/Warehouse.StockItems.OuterPackageID__Warehouse.PackageTypes.PackageTypeID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, roles, chasm, current versions.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 9a090c85fa6cc4c111163aea7274c174e4b3f701c4e4219649dddeafc9c848a2
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0405540c22176c22 | recheck=every new extract | text: Fan-out: joined from Warehouse.PackageTypes to Warehouse.StockItems, a Warehouse.PackageTypes row repeats up to 175 times (median 43), so a measure of Warehouse.PackageTypes summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0405540c22176c22 | recheck=a foreign key changes | text: Several paths between the same two tables: Warehouse.StockItems also refers to Warehouse.PackageTypes through UnitPackageID; a join of the two must say which role it means.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0405540c22176c22 | recheck=every new extract | text: Chasm trap: Warehouse.PackageTypes also has other referring columns with several rows per parent (Purchasing.PurchaseOrderLines.PackageTypeID (up to 5,779 per parent), Sales.InvoiceLines.PackageTypeID (up to 217,959 per parent), Sales.OrderLines.PackageTypeID (up to 221,108 per parent), Warehouse.StockItems.UnitPackageID (up to 210 per parent)); joining Warehouse.StockItems and one of these through Warehouse.PackageTypes pairs every row of one with every row of the other for the same parent.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=0405540c22176c22 | recheck=the temporal type changes | text: Warehouse.PackageTypes is system-versioned and the extract holds its current versions: joined in the extract, a row of Warehouse.StockItems that names a row of Warehouse.PackageTypes gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
