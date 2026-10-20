---
id: wwi:fk:FK_Sales_Invoices_OrderID_Sales_Orders
subject: wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID
item: 01
topic: granularity
tier: minimum
summary: Sales.Invoices to Sales.Orders; at most one row of Sales.Invoices per row of Sales.Orders in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f8298521c727f76a5df7d60cceab9113551c38c8ab8ff1e0fdb8c864540f7bdf
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4fe6c2f192a15dd6 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Invoices_OrderID_Sales_Orders from Sales.Invoices.OrderID to Sales.Orders.OrderID, the primary key of Sales.Orders: each row of Sales.Invoices names at most one row of Sales.Orders.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4fe6c2f192a15dd6 | recheck=every new extract | text: In this extract 70,566 of 70,566 rows of Sales.Invoices name one of 70,566 referenced rows of Sales.Orders (of 73,653); children per referenced parent: from 1 to 1, median 1; 70,566 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4fe6c2f192a15dd6 | recheck=every new extract | text: Joined from Sales.Invoices to Sales.Orders, the result keeps the grain of Sales.Invoices: one row per row of Sales.Invoices. Joined the other way, each row of Sales.Orders repeats once per row of Sales.Invoices that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=4fe6c2f192a15dd6 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Sales.Orders is named by more than one row of Sales.Invoices. No unique constraint on OrderID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
