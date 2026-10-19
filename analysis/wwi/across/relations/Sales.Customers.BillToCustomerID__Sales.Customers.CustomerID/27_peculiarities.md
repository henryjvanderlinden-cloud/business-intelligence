---
id: wwi:fk:FK_Sales_Customers_BillToCustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Customers.BillToCustomerID__Sales.Customers.CustomerID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions, see claims.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 322b8ef89e7e34e9806b2e1358ab74a9d24b9654de5dc47a8037c02969f8d8bd
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=759491e6befc86cb | recheck=every new extract | text: Fan-out: joined from Sales.Customers to Sales.Customers, a Sales.Customers row repeats up to 201 times (median 1), so a measure of Sales.Customers summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=759491e6befc86cb | recheck=every new extract | text: Chasm trap: Sales.Customers also has other referring columns with several rows per parent (Sales.CustomerTransactions.CustomerID (up to 23,402 per parent), Sales.Invoices.BillToCustomerID (up to 22,333 per parent), Sales.Invoices.CustomerID (up to 144 per parent), Sales.Orders.CustomerID (up to 150 per parent), Warehouse.StockItemTransactions.CustomerID (up to 457 per parent)); joining Sales.Customers and one of these through Sales.Customers pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=759491e6befc86cb | recheck=the temporal type changes | text: Sales.Customers is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.Customers that names a row of Sales.Customers gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=759491e6befc86cb | recheck=every new extract, or a description changes | text: Self-reference in a system-versioned table: which head office a branch was billed to on an earlier date is in Sales.Customers_Archive, not here.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
