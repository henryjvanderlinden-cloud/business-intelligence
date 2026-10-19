---
id: wwi:fk:FK_Purchasing_PurchaseOrders_SupplierID_Purchasing_Suppliers
subject: wwi/across/relations/Purchasing.PurchaseOrders.SupplierID__Purchasing.Suppliers.SupplierID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 3d59c7196fb503ddc827836282e1c08c87f7e19face754e7b256c4d417da0956
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=every new extract | text: Fan-out: joined from Purchasing.Suppliers to Purchasing.PurchaseOrders, a Purchasing.Suppliers row repeats up to 1,056 times (median 10), so a measure of Purchasing.Suppliers summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=every new extract | text: Chasm trap: Purchasing.Suppliers also has other referring columns with several rows per parent (Purchasing.SupplierTransactions.SupplierID (up to 1,233 per parent), Warehouse.StockItemTransactions.SupplierID (up to 5,802 per parent), Warehouse.StockItems.SupplierID (up to 74 per parent)); joining Purchasing.PurchaseOrders and one of these through Purchasing.Suppliers pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=b03c22ce446e89d3 | recheck=the temporal type changes | text: Purchasing.Suppliers is system-versioned and the extract holds its current versions: joined in the extract, a row of Purchasing.PurchaseOrders that names a row of Purchasing.Suppliers gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
