---
id: wwi:term:order
subject: wwi/across/terms/order
item: 25
topic: terms
tier: best-effort
summary: "Order" names three things: a row of Sales.Orders (a fulfilment order), a customer's order as placed (a chain of an original and its backorders), and a purchase order.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: A row of Sales.Orders is a fulfilment order; a customer's order as placed is a chain of an original and its backorders, so 73,653 rows are 66,107 placed orders (tables/Sales/Orders/27_peculiarities.md#C12).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: A backorder keeps the original's order date and is invoiced when supplied, up to 1,116 days later (across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/03_temporal.md#C3, #C4); the link runs from the original to the backorder, against its description (tables/Sales/Orders/columns/BackorderOrderID/02_meaning.md#C2).
- C3 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: A purchase order (Purchasing.PurchaseOrders) is WWI's order to a supplier, a different thing; the two share the word, not a key or a table.

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None beyond the linked claims.

## For a person

None.
