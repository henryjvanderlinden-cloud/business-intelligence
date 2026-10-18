---
item: 07
topic: population
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: medium
finding: All 73,653 orders of 2013-01-01 to 2016-06-01 for 663 customers, backorders included; no placeholder found; no cancellation status exists; 3,087 never picked.
claims: [observed]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E005, E007, E008]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

1. **Range:** `OrderDate` from 2013-01-01 to 2016-06-01; 2016 is a part year (E005).
2. **Customers:** 663, all present in `Sales.Customers`; every order's contact is its customer's primary contact (E008).
3. **Backorders are rows of the population**, 7,546 of them (E007). A count of orders includes them unless excluded.
4. **No placeholder customer or order was found** — no customer name containing "unknown", "test", "dummy" or "n/a",
   and `OrderID` runs from 1 to 73,653 without a gap (E005, E008); this is a name search, not proof. A technical user
   does appear: 5 rows were last edited by person 1, *Data Conversion Only*, who is not an employee and cannot log on
   (E008).
5. **No status column.** Cancelled, rejected or on-hold orders cannot be told apart from others; whether such orders
   exist is unknown.
6. **3,087 orders never picked**, from every year since 2013 (E005).
7. **Weekly pattern:** no orders on Sundays and about half the volume on Saturdays (E005).
8. **Empty columns:** `Comments`, `DeliveryInstructions` and `InternalComments` are empty in every row, and
   `IsUndersupplyBackordered` is 1 in every row (E005).

## Reasoning

Counts are exact over the whole extract, hence high confidence on each number. The overall confidence is medium
because two questions about who is in the population — cancellations, and the meaning of the unpicked orders — cannot
be answered from the data.

## Uncertainties

1. **Cancellations: unknown.** There is no column for them; whether WWI cancels orders by deleting them, or never, is
   not established. Settled by watching for deletions over many days, or by the source's documentation.
2. **Unpicked orders: unknown** whether they are a real backlog or an artefact of the generated history (see
   [03_temporal.md](03_temporal.md)).

## For a person

Should never-picked orders older than some age count as open orders in reports, or be excluded?
