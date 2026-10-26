# ADR-0027 — The integration layer is bitemporal on evidence, with source system time kept as a labelled third timestamp

- **Status:** Accepted
- **Date:** 2026-10-26
- **Supersedes:** —
- **Superseded by:** —

## Context

Handover 09 named, as decision 1 of the design of the generic integration layer, whether the layer is bitemporal. The
author's rulings on calculation engines already rest on a bitemporal structure
([ADR-0024](0024-calculation-engines-are-a-versioned-source.md), [ADR-0025](0025-engine-results-in-the-raw-vault.md)).
On 2026-10-26 at 11:29 he asked, verbatim, "Please expand on 8, and provide options and considerations."

Three clocks are in play, and in Wide World Importers they are distinct. Knowledge time is when the warehouse learned
something (its load time). Business valid time is when something was true in the business. Source system time is when
the source database recorded a change. What the source offers, from the analysis record (item 03 of each table, and
[127](../10_architecture/127_temporal-behaviour.md) on the axes):

- the event tables carry business dates (`OrderDate`, `InvoiceDate`, `TransactionDate`), and milestones carry stamps
  (`PickingCompletedWhen`, `ConfirmedDeliveryTime`, `FinalizationDate`) that are written back onto the row later, in
  place (`analysis/wwi/tables/Sales/Orders/03_temporal.md`, `Sales/Invoices/03_temporal.md`,
  `Sales/CustomerTransactions/03_temporal.md`);
- 17 tables are system-versioned, with full version histories whose period columns are database edit time, not
  business time: one `Application.Countries` version is stamped 2022 by a later edit
  (`Application/Countries/03_temporal.md`), every stock item got a new version between 23:00 and 23:12 on 2016-05-31
  (`Warehouse/StockItems/03_temporal.md`), and cities change in yearly batches (`Application/Cities/03_temporal.md`);
- `Sales.SpecialDeals` carries its own validity period (`StartDate`, `EndDate`; `Sales/SpecialDeals/03_temporal.md`);
- `Warehouse.StockItemHoldings` is overwritten daily and carries no history (`Warehouse/StockItemHoldings/03_temporal.md`),
  so the daily extracts give one sampled state per day;
- loading the history tables on the first day would give years of versions a single load date.

## Options considered

*A. Load time only*, with business and source times as ordinary attributes. Its case: standard Data Vault, the simplest
to build and query. Rejected: "as it was then" would be rebuilt by hand in every query, the first day's history would
collapse onto one load date, and the vault would be poorer in time than the engine results it holds.

*B. Bitemporal everywhere, with valid time forced* from the load date or the database stamp where the source gives
none. Its case: uniform. Rejected: it invents business time, which [127](../10_architecture/127_temporal-behaviour.md)
forbids ("Substituting load time invents when a value became true").

*C. Bitemporal everywhere, on evidence*: both axes in every satellite, valid time only from source evidence and
otherwise recorded as unknown. Its case: one structure, honest gaps. Adopted as the structure, with D's addition.

*D. Tri-temporal*: C plus source system time as a third axis in queries. Its case: keeps the source's own history in
order before the first load. Adopted in a light form: the third time is stored and labelled, not offered as a query
axis.

*E. One clock in the raw vault, two-axis structures built in the business vault only where needed.* Its case: the raw
vault stays as simple as possible. Rejected: every table that needs history would get its own construction, and it
runs against the engine rulings, which treat bitemporality as a property of the warehouse.

## Decision

The author ruled on 2026-10-26 at 12:03, verbatim: "Agree with your recommendations for 22 and 23." The
recommendations were:

1. **The integration layer is bitemporal on evidence (option D in a light form).** Every satellite carries knowledge
   time (load time) and business valid time. Valid time is filled only from source evidence and is otherwise
   explicitly unknown.
2. **Source system time is kept as a third, labelled timestamp.** It is used to order and load the source's own
   history (the system-versioned tables' history, loaded on the first day) and is never presented as business time.
3. **Marts expose "as of" views**, so that most users never handle more than one clock.
4. **Which column carries each table's business time is proposed by the agent layer for all 31 base tables from the
   analysis record (item 03), and the author rules only where the evidence is weak**, such as milestone stamps that are
   written back later.

## Consequences

Because the raw vault is insert-only, "valid to" is never stored; only "valid from" is stored, and "valid to" is derived
in views from the next row. Change detection includes the time columns, so a correction that moves only a date is kept
(127). Two-axis point-in-time structures are generated in the business vault, and their cost is in querying them
correctly rather than in building them, which is why marts hide them behind "as of" views.

Tables without business time, such as `Warehouse.StockItemHoldings`, have only knowledge time and source system time
where it exists; their history is labelled sampled (127), and no business-time query on them pretends otherwise.

The per-table proposal of decision 4 is work owed before the first load, under
[`ARC-OP-37`](../../registers/OPEN_POINTS.md); it follows the temporal axes of 127 and closes part of `ARC-OP-27` for
this sandbox.

This decision is unreviewed on another model ([510](../50_process/510_external-review.md)).

**Revisit** if the "unknown" valid time proves unworkable in queries, if source system time is found to be presented as
business time anywhere, or when a second source with different temporal behaviour is added.
