---
id: wwi:fk:FK_Sales_Orders_ContactPersonID_Application_People
subject: wwi/across/relations/Sales.Orders.ContactPersonID__Application.People.PersonID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, roles, chasm, current versions, copy.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 51805da5178a316233382b96b4193aac7558e4460d848a9ce9951eeae31a4a1e
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ee4b745e92a6f252 | recheck=every new extract | text: Fan-out: joined from Application.People to Sales.Orders, a Application.People row repeats up to 150 times (median 114), so a measure of Application.People summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ee4b745e92a6f252 | recheck=a foreign key changes | text: Several paths between the same two tables: Sales.Orders also refers to Application.People through LastEditedBy, PickedByPersonID, SalespersonPersonID; a join of the two must say which role it means.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ee4b745e92a6f252 | recheck=every new extract | text: Chasm trap: Application.People also has other referring columns with several rows per parent (Purchasing.PurchaseOrders.ContactPersonID (up to 2,076 per parent), Sales.Invoices.AccountsPersonID (up to 22,333 per parent), Sales.Invoices.ContactPersonID (up to 144 per parent), Sales.Invoices.PackedByPersonID (up to 4,817 per parent), Sales.Invoices.SalespersonPersonID (up to 7,191 per parent), Sales.Orders.PickedByPersonID (up to 4,042 per parent), Sales.Orders.SalespersonPersonID (up to 7,539 per parent)); joining Sales.Orders and one of these through Application.People pairs every row of one with every row of the other for the same parent.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ee4b745e92a6f252 | recheck=the temporal type changes | text: Application.People is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.Orders that names a row of Application.People gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=ee4b745e92a6f252 | recheck=every new extract | text: Two routes agree: on all 73,653 rows where both are filled, ContactPersonID names the same row of Application.People as the route CustomerID -> Sales.Customers.PrimaryContactPersonID: in this extract ContactPersonID repeats that value.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
