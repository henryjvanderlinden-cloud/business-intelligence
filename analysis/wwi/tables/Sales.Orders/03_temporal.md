---
item: 03
topic: temporal
subject: wwi/Sales.Orders
tier: minimum
status: proposed
confidence: medium
finding: Rows are inserted daily and updated in place once, when picking completes; no history in the source, no deletions seen; one transition observed.
claims: [declared, observed, implemented]
as_of: wwi 2016-06-01 manifest sha256 35b71b2e3ff4bb9e
evidence: [E001, E004, E005, E006, E008]
analysed_by: claude-opus-5-5
analysed_at: 2026-10-18
ruled_by: none
---

## Finding

On the six axes of [127](../../../../docs/10_architecture/127_temporal-behaviour.md):

1. **Mutation: overwritten in place.** The table is `NON_TEMPORAL_TABLE` (E004), so the source keeps no history.
   Between the extracts of 31 May and 1 June 2016, 58 rows were inserted and 6 updated; every update set
   `PickedByPersonID` and `PickingCompletedWhen` on an order not picked before, and moved `LastEditedBy` and
   `LastEditedWhen` (E006). No other column changed.
2. **Delivery: full extract per simulated day** — the sandbox's design (420 §11), not a property of the source.
3. **Effective dating: none.** There is no validity period. `OrderDate` is a business date (type `date`, E001);
   `LastEditedWhen` is a technical change time.
4. **Arrival latency: on time in the one day observed** — all 58 inserted orders are dated that day (E006).
5. **Correction: none observed.**
6. **Deletion: none observed** (0 rows gone, E006), and none in the history either: `OrderID` runs from 1 to 73,653
   without a gap (E005), unless deleted numbers were reused.

**Capture guarantee.** Daily full extracts see each order once a day. The only change observed is a single, final
one (picking completed), so daily capture loses nothing in this table *as far as one transition shows*; history in
the warehouse would be sampled history in 127's sense, exact only if no row changes twice in a day.

**Date roles.** `OrderDate` (raised), `ExpectedDeliveryDate` (both `date`), `PickingCompletedWhen` and
`LastEditedWhen` (`datetime2`, no time zone, E001). No expected date precedes its order date and no edit precedes
the order (E005).

**Lifecycle.** Raised, then picked. Picking can come long after the order: one of the six updated orders was dated
2015-12-29 (E006). 3,087 orders are not picked, the oldest from 2013-01-12, spread over every year (E005), and none of
their 3,149 lines has a picked quantity above zero (E008).

## Reasoning

The source declares no history, and the one transition shows exactly one kind of update. Microsoft's simulator
inserts new orders with picking empty and later sets picking on the header only when all lines are picked
(`CreateCustomerOrders`, `PickStockForCustomerOrders` in microsoft/sql-server-samples, read 2026-10-18 through a
summarising fetch, not end to end). Behaviour and implementation agree.

## Uncertainties

1. **One transition is not a pattern.** Corrections, deletions and late-arriving orders could exist and not show in a
   single day. Settled by comparing more simulated days; the quarter turn on 2016-06-30 is a natural point.
2. **Time zone of `PickingCompletedWhen` and `LastEditedWhen`: unknown.** Nothing in the catalogue states one.
3. **The 3,087 unpicked orders: unknown whether open backlog or an artefact of how the 2013-2016 history was
   generated.** Settled by watching whether old unpicked orders keep being picked as days advance.

## For a person

Which date does the business report orders by: `OrderDate`, or the picking date?
