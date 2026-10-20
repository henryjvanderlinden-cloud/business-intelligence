---
id: wwi:fk:FK_Sales_Invoices_OrderID_Sales_Orders
subject: wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID
item: 03
topic: temporal
tier: best-effort
summary: An invoice is dated on its order's date unless the order is a backorder: 4,464 of the 4,479 later invoices are for backorders.
confidence: unknown
claims: 5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=08065984b4454dc8 | recheck=the temporal type changes | text: Sales.Orders is not system-versioned: an earlier state of a row is not kept, so a row of Sales.Invoices can only be joined to the row as it is in the extract.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=08065984b4454dc8 | recheck=every new extract | text: Date order on 70,566 rows: child date after parent date 4,479; child date same day as parent date 66,087; days from Sales.Orders.OrderDate to InvoiceDate: from 0 to 1,116, median 0.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=08065984b4454dc8 | recheck=every new extract | text: By whether the order is a backorder: backorder, child date after order date: 4,464; not a backorder, child date after order date: 15; not a backorder, same day or before: 66,087.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=08065984b4454dc8 | recheck=every new extract, or a description changes | text: In this extract an invoice carries its order's date on 66,087 invoices; of the 4,479 dated later, 4,464 are for backorders, which keep the original order's date (Sales.Orders.BackorderOrderID 03) and are invoiced up to 1,116 days after it.
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a person or the generating script settles it | text: Why 15 invoices of orders that are not backorders are dated after their order is not established.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
