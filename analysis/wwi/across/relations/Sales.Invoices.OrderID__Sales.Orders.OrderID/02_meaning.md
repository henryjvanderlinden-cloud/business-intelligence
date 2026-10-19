---
id: wwi:fk:FK_Sales_Invoices_OrderID_Sales_Orders
subject: wwi/across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID
item: 02
topic: meaning
tier: minimum
summary: The order the invoice was made from; at most one invoice per order in this extract; orders without an invoice are not yet invoiced.
confidence: low
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: f8298521c727f76a5df7d60cceab9113551c38c8ab8ff1e0fdb8c864540f7bdf
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4fe6c2f192a15dd6 | recheck=the description changes | text: The source describes Sales.Invoices.OrderID as "Sales order (if any) for this invoice".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4fe6c2f192a15dd6 | recheck=every new extract, or a description changes | text: The order converted into this invoice. No invoice lacks an order in this extract, although the column is nullable (07).
- C3 | type=declared | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Context, not a description of this column: Microsoft's description of the business says WWI invoices customers "typically by converting the order to an invoice".
- C4 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=4fe6c2f192a15dd6,af410313550bceb2 | recheck=every new extract, or a description changes | text: The 3,087 orders without an invoice (07) are as many as the orders with no PickingCompletedWhen in Sales.Orders (3,087); that they are the same orders is not checked row by row.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether the uninvoiced orders are exactly the unpicked ones is not checked row by row.

## For a person

None.
