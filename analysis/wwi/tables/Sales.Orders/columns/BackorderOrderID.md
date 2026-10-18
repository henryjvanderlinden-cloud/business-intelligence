---
item: column
subject: wwi/Sales.Orders/BackorderOrderID
status: proposed
confidence: high
finding: Set on the original order and holds the OrderID of the backorder split from it; the declared description says the reverse.
claims: [declared, observed, implemented]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E001, E003, E005, E007]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## 02 Meaning — confidence: high

**Declared** (E001): "If this order is a backorder, this column holds the original order number."

**Observed** (E007): the reverse. In all 7,546 filled rows the referenced order has a higher `OrderID`, an order date
on or after the row's own, the same customer and the same customer purchase order number. In all 7,546 the row's own
order has picking completed with no picker recorded — and these are the only such rows in the table. That is the
pattern of an order partly fulfilled whose remainder became a new order: the column sits on the original and points
to its backorder.

The contradiction is the finding: anyone building on the description would join the wrong way round.

## 06 Keys — confidence: high

A declared, enforced self-reference to `Sales.Orders.OrderID` (E003). All targets exist (E007). Each backorder has
exactly one original (7,546 distinct targets); 242 backorders have a backorder of their own.

## 03 Temporal — confidence: medium

Static in the daily simulation. Microsoft's `CreateCustomerOrders` inserts it as `NULL` and no daily procedure
read sets it (microsoft/sql-server-samples, read 2026-10-18 through a summarising fetch): all 7,546 backorder links
come from the generated 2013-2016 history, and the simulated days will add none.

## 07 Population — confidence: high

Filled on 7,546 of 73,653 rows (E005).

## Uncertainties

The rule that creates backorders is not in the daily simulation, so the observed meaning cannot be checked against its
implementation. `nsdn_reader` cannot read procedure definitions in the database (the query returned null).

## For a person

None: the data settles the direction. A person may want the source's description corrected in the context layer.
