---
item: 06
topic: keys
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: high
finding: OrderID is the declared primary key, unique in the data and the only key; it is a meaningless number, not a time proxy; CustomerPurchaseOrderNumber is not a key.
claims: [declared, observed]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E001, E002, E003, E005, E007]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

1. **`OrderID`** is the primary key `PK_Sales_Orders` (E002), an `int` described as "Numeric ID used for
   reference to an order within the database" (E001), and unique over 73,653 rows (E005). No other unique constraint
   is declared.
2. **It carries no meaning.** It mostly rises with `OrderDate` but not strictly: 215 inversions (E005). It must not
   be used to order by time.
3. **`CustomerPurchaseOrderNumber` is not a key**: 9,984 distinct values over 73,653 rows (E005), and an order and its
   backorders share one (E007).
4. **Foreign keys:** six, all enabled and trusted (E003) — `CustomerID`, `SalespersonPersonID`,
   `PickedByPersonID`, `ContactPersonID`, `LastEditedBy`, and the self-reference `BackorderOrderID`.
5. **Self-reference:** `BackorderOrderID` points from an order to the backorder split from it, the opposite of
   its declared description; see [`columns/BackorderOrderID.md`](columns/BackorderOrderID.md).

## Reasoning

Key and uniqueness are declared and observed, and agree. For a Data Vault hub the business key would be `OrderID`:
it is the source system's own identifier and there is no better candidate inside the table.

## Uncertainties

1. **Key stability: probably stable, not proven.** `OrderID` runs from 1 to 73,653 without a gap (E005), so no
   number was lost to a deletion; reuse of a deleted number would hide exactly that. Settled by watching deletions and
   re-insertions over many days.
2. **Whether `OrderID` is known outside the database** (on documents sent to customers) is not established; the
   description says "within the database".

## For a person

None for the minimum.
