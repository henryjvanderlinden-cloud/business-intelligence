---
item: 01
topic: granularity
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: high
finding: One row is one order as WWI fulfils it (a customer order or a backorder split from one), identified by OrderID; a customer's order as placed can span several rows.
claims: [declared, observed]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E001, E002, E004, E005, E007, E008]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

One row per order header. `OrderID` is the declared primary key (E002) and is unique over all 73,653 rows (E005).
The lines are in `Sales.OrderLines`: every order has between one and five lines and every line belongs to an
existing order (E008).

A row is not always a customer's order as placed. 7,546 rows have been split: their remainder became a new row, a
backorder, with its own `OrderID`, the same customer and the same `CustomerPurchaseOrderNumber` (E007; see
[`columns/BackorderOrderID.md`](columns/BackorderOrderID.md)). 242 backorders were split again. So one purchase
order of a customer can be two, three or more rows.

## Reasoning

Declared and observed agree on the key, so the row grain is high confidence. The table's own description, "Detail of
customer orders" (E004), says *detail*, but the lines live elsewhere and every column is order-level; the word is
taken to mean "details about", not "line detail". The split into backorders is observed without exception over the
whole population and has a plausible mechanism (partial fulfilment), so it is part of the grain finding rather than
an uncertainty.

## Uncertainties

None about the row grain. Which grain the business means by "an order" is a question of meaning, below.

## For a person

Does "number of orders" count rows (fulfilment orders, backorders included) or customer purchase orders (one chain of
original plus backorders)? The two differ by 7,546 on the current extract.
