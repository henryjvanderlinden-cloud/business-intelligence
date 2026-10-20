---
id: wwi:fk:FK_Sales_Invoices_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, roles, chasm, current versions, copy.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2ce83d3e97200a06f4d8df60b09a4948373b555ba7aa8f288282685f535571a5
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=every new extract | text: Fan-out: joined from Sales.Customers to Sales.Invoices, a Sales.Customers row repeats up to 144 times (median 109), so a measure of Sales.Customers summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=a foreign key changes | text: Several paths between the same two tables: Sales.Invoices also refers to Sales.Customers through BillToCustomerID; a join of the two must say which role it means.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=every new extract | text: Chasm trap: Sales.Customers also has other referring columns with several rows per parent (Sales.CustomerTransactions.CustomerID (up to 23,402 per parent), Sales.Customers.BillToCustomerID (up to 201 per parent), Sales.Invoices.BillToCustomerID (up to 22,333 per parent), Sales.Orders.CustomerID (up to 150 per parent), Warehouse.StockItemTransactions.CustomerID (up to 457 per parent)); joining Sales.Invoices and one of these through Sales.Customers pairs every row of one with every row of the other for the same parent.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=the temporal type changes | text: Sales.Customers is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.Invoices that names a row of Sales.Customers gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=every new extract | text: Two routes agree: on all 70,566 rows where both are filled, CustomerID names the same row of Sales.Customers as the route OrderID -> Sales.Orders.CustomerID: in this extract CustomerID repeats that value.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
