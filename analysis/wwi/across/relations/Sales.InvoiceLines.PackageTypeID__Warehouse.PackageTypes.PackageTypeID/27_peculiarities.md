---
id: wwi:fk:FK_Sales_InvoiceLines_PackageTypeID_Warehouse_PackageTypes
subject: wwi/across/relations/Sales.InvoiceLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions, copy.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 940bd3cfc340d9c1959aa30e56159aa759298a180269b0a08c28d0bfa3e8b891
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=every new extract | text: Fan-out: joined from Warehouse.PackageTypes to Sales.InvoiceLines, a Warehouse.PackageTypes row repeats up to 217,959 times (median 4,714.5), so a measure of Warehouse.PackageTypes summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=every new extract | text: Chasm trap: Warehouse.PackageTypes also has other referring columns with several rows per parent (Purchasing.PurchaseOrderLines.PackageTypeID (up to 5,779 per parent), Sales.OrderLines.PackageTypeID (up to 221,108 per parent), Warehouse.StockItems.OuterPackageID (up to 175 per parent), Warehouse.StockItems.UnitPackageID (up to 210 per parent)); joining Sales.InvoiceLines and one of these through Warehouse.PackageTypes pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=the temporal type changes | text: Warehouse.PackageTypes is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.InvoiceLines that names a row of Warehouse.PackageTypes gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=every new extract | text: Two routes agree: on all 228,432 rows where both are filled, PackageTypeID names the same row of Warehouse.PackageTypes as the route StockItemID -> Warehouse.StockItems.UnitPackageID: in this extract PackageTypeID repeats that value.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
