# 129 — Information analysis: what is inventoried about every table before anything is built on it

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-10-18, session 08, from the author's point, verbatim:

> So I was thinking, before anything gets built, there should be a business analysis phase, or
> rather an information analysis, to determine what's in the tables. Things to look out for are:
> granularity, meaning, temporal characteristics, relation to other tables. Can you store this
> somewhere? And also think of other things that should be inventoried before building anything?
> In terms of analysing the tables that are to be imported?

The four points are the author's. Items 5 to 26 below are the model's proposal in reply and are
**not ruled**; the author's point is itself tentative until he rules it. The open questions are in
`ARC-OP-36`. The document is **unreviewed** ([510](../50_process/510_external-review.md)). The
author's point is practitioner input and unsourced under [AGENTS.md](../../AGENTS.md) rule 8.
Nothing here is built.

The Wide World Importers examples are **observed**: read on 2026-10-18 from the header and first
data row of each named file in the extract `data/raw/wwi/2016-06-01/`, from its `manifest.json`,
and, for item 18, from one query through the sandbox's request folder. They illustrate an item;
they are not an analysis of the sandbox.

## What the phase is

Before a load, a vault structure or a mart is built on a table, the table would be analysed and
what is found recorded. This is the information analysis an experienced practitioner does by
hand, partly mechanised along the division of [070](../00_concept/070_task-allocation.md):
deterministic machinery measures, the agentic layer proposes, a person rules on meaning,
authority and purpose. It gathers into one phase work that the repository already describes in
pieces: profiling and sense-making ([110](110_capability-map.md)), temporal behaviour
([127](127_temporal-behaviour.md)), join knowledge ([128](128_join-knowledge.md)), and rows 6 to
13, 15, 41 and 42 of 070.

The case for a phase, rather than analysis as and when a build needs it, is that the defects the
mission names first — wrong joins, wrong grain, silently stale data
([001](../00_concept/001_mission.md)) — are cheapest to catch before any code depends on the
misreading. It would also give the builder of `ARC-OP-34`, and the independent re-derivation of
keys and grain ruled there, a defined input.

The phase would produce no separate report. Its output would be the `dataset` and `field` cards of
[120](120_context-layer.md), each finding an assertion carrying its claim type — *declared* (what
the source or its documentation says), *observed* (what the data shows) or *intended* (what a
person rules it should mean) — with its evidence. A table analysed this way stays analysed only
while the evidence holds; repeated profiling over loads, and drift detection
([126](126_context-gardening.md)), keep the findings current.

## The author's four

**1. Granularity.** What one row represents, stated in business terms ("one order line", "one
stock item's current holding"), together with the key that makes it so — declared and observed
separately, since a declared key is often absent and an observed one may hold only by accident.
Grain can also be mixed within one table, and then it must be stated per population. Grain under
filters, and grain as the precondition of every join, are in [128](128_join-knowledge.md).

**2. Meaning.** What business event or object the table records, and what each column means:
its definition, its unit, what a null means (unknown, not applicable, not yet), and the meaning of
each code. Meaning is where the source's own word and the business's word most often part, so it
is the item that most needs a person's ruling.

**3. Temporal characteristics.** The six axes and the capture guarantee of
[127](127_temporal-behaviour.md). One addition is proposed under item 12 below, and one here:
**date roles**. A row usually carries several dates — ordered, expected, picked, invoiced,
delivered, last edited — and the inventory should record which exist, what each means, and which
the business reports by. WWI's `Sales.Orders` alone carries `OrderDate`, `ExpectedDeliveryDate`,
`PickingCompletedWhen` and `LastEditedWhen`.

**4. Relation to other tables.** Joinable pairs, key roles, cardinality in layers, referential
integrity and join risks, as in [128](128_join-knowledge.md).

## Further items proposed

### What the table is

**5. Role.** Whether the table holds master or reference data, transactions or events, a
snapshot or current state, a bridge between two others, the source's own history of another
table, configuration, or an audit log. Role decides more of the design than any other single
fact: hub, link or satellite; fact or dimension; or not loaded at all. WWI's manifest marks 17 of
its 48 tables as `HISTORY_TABLE` (the `_Archive` tables, the source's own history of a
system-versioned table, not separate entities); `Warehouse.StockItemStockGroups` is a bridge;
`Application.SystemParameters` is configuration.

**6. Keys and identity.** The declared primary key; candidate business keys; whether a key is a
meaningless number or carries meaning; whether keys are stable, or reused, reassigned or recycled
after deletion; composite keys; and self-references. WWI's `Sales.Orders.BackorderOrderID` and
`Sales.Customers.BillToCustomerID` point back into their own tables.

**7. Population.** What the table contains and what it leaves out: placeholder and technical
rows, test data, several companies or tenants in one table, rows that are cancelled, inactive or
soft-deleted. A count, a sum or a join that does not know the population is wrong without any
error. WWI's `Application.People` begins with person 1, *Data Conversion Only*, a technical row,
not a person.

### What is in it

**8. Measures and how they add up.** Which columns are quantities, and whether they are additive,
semi-additive (summable across items but not across time, like balances and stock levels) or
non-additive (prices, rates, percentages); their unit, currency, whether tax is included, and the
sign convention. WWI's `Warehouse.StockItemHoldings.QuantityOnHand` is a level, not a movement;
`Warehouse.StockItemTransactions.Quantity` is negative for an issue (−10 in the first row);
`TaxRate` is a percentage (15.000).

**9. Derived columns.** Values the source computed from other values. They can be taken as they
are or recomputed, and either way the formula, once observed, is a ready-made plausibility check
([162](162_test-framework.md)). In the first row of WWI's `Sales.InvoiceLines`, `ExtendedPrice`
is quantity times unit price plus tax: 10 × 230.00 + 345.00 = 2 645.00. `LineProfit` appears to
be derived as well, from a cost the line does not carry; that is unverified.

**10. Codes, flags and special values.** Domains and code lists, the lookup tables that decode
them, the polarity of each flag, and magic values standing for something else — a far-future
date, a zero or −1 key, `N/A`, an empty string that is not a null. Also rows of opposite meaning
in one table. WWI uses `ValidTo` 9999-12-31T23:59:59.9999999 for "current", and
`Sales.Invoices.IsCreditNote` puts credit notes in the invoice table, which bears on grain, sign
and every revenue total.

**11. Types and formats.** Declared against actual types; dates held as text; decimal separator
and locale; character encoding; the time zone of timestamps, and daylight saving; structures
embedded in a column (JSON, XML, geometry, delimited lists); binary content. In WWI,
`Sales.Invoices.ReturnedDeliveryData` holds a JSON list of delivery events,
`Warehouse.StockItems.CustomFields` and `Tags` are JSON, `Sales.Customers.DeliveryLocation` is a
geographic point, and no timestamp states its zone.

**12. Values copied at the time.** Values copied onto a transaction when it happened — a price,
a description, an address — as opposed to looked up from master data. The copy is the truth as
at the event; the master is the truth now. Knowing which is which decides whether a report needs
a point-in-time join at all. WWI's `Sales.OrderLines` carries its own `Description` and
`UnitPrice`; `Sales.Invoices.DeliveryInstructions` holds an address.

**13. Hierarchies and many-valued structures.** Parent-child relationships, levels, ragged
hierarchies, many-to-many relationships, and rows whose scope varies by which column is filled.
WWI has city, state or province, and country; stock items in many stock groups; and
`Sales.SpecialDeals`, where a deal applies to a stock item or a stock group and to a customer, a
buying group or a customer category, according to which columns are filled.

### Where it comes from and how good it is

**14. Provenance in the source.** Which process, screen or interface creates and changes rows;
whether they are typed by a person, generated by the system or fed from another system; whether
this system is the record or a copy (070 row 6); and the audit columns. All WWI tables but three
carry `LastEditedBy`, and its temporal tables `ValidFrom` and `ValidTo`; the three exceptions,
`Warehouse.ColdRoomTemperatures`, its archive and `Warehouse.VehicleTemperatures`, hold sensor
readings, which no person edits.

**15. Quality profile.** Nulls, uniqueness, duplicates, orphans, value ranges, rules between
columns (an order is picked after it is placed), and rules between tables (header totals equal
the sum of their lines). Measured by machinery; every rule that holds becomes a standing check.

**16. Reconciliation anchors.** A total outside the table that it must agree with: a ledger, a
control report in the source application, a figure the business knows by heart. Without one the
warehouse can only be shown to agree with itself. WWI offers internal anchors (customer
transactions against invoices) but no external one; that limit of the sandbox should be stated
rather than discovered.

**17. Volume and change rate.** Rows, bytes, growth per load, the spread of rows over time, and
how many rows change between loads. These decide full or incremental loading and partitioning,
and they are measured, not guessed. Between WWI's extracts of 31 May and 1 June 2016, 15 of 48
tables changed (handover 08).

**18. Existing documentation.** A data dictionary, column comments, vendor documentation, and
the people who know. Harvested first, so that a person is asked only what is written nowhere.
The WWI database holds a `Description` extended property on 34 tables and 280 columns (query of
2026-10-18 as `nsdn_reader`); these are *declared* meaning, to be checked against the data like
any other declaration.

### Governance and purpose

**19. Sensitivity.** Personal data, special categories, commercially confidential values and
credentials; the legal basis, the retention obligation, and who may see them (070 rows 36 and 37).
Recorded before the first load, because masking decided afterwards has already failed once.
WWI's `Application.People` holds `HashedPassword`, `EmailAddress` and `PhoneNumber`.

**20. Ownership.** A business owner who can rule on meaning, a technical owner, a steward. Without
a named person, "a person rules" has nobody to address.

**21. Demand and scope.** Which questions, reports or users need the table, which columns are
never used or always empty, and therefore whether it is imported now, later or not at all. Not
everything that exists has to be loaded (070 row 4; the demand justification on cards in
[120](120_context-layer.md)).

**22. Structural stability.** How often the structure changes, vendor upgrades, customisations,
and general-purpose columns whose meaning differs by company or period. JSON columns such as
WWI's `CustomFields` are where structure can change without any schema change.

**23. Extraction constraints.** Access route, load windows, the load on the source, and whether
the tables are extracted consistently with one another, so that no line arrives without its
header. Largely the capture guarantee of [127](127_temporal-behaviour.md) and 070 row 7; listed
here so the inventory is complete in one place.

### Across tables

Four items belong to the landscape rather than to one table.

**24. Business processes and lifecycles.** Which tables together record one process — WWI's
order to cash runs through orders, order lines, picking, invoices, invoice lines, customer
transactions and stock movements — and the life of a record through its statuses: which states
are final, and which rows can still change. The lifecycle says, for instance, until when an
invoice can still be corrected, and so feeds the correction axis of 127.

**25. Synonyms and homonyms.** The same meaning under different names, and different meanings
under one name, across tables and sources, with the copy that is authoritative. `TaxRate` appears
in WWI on stock items, order lines and invoice lines.

**26. Entities and subject areas.** Which business entities (customer, product, person,
supplier) appear in which tables and sources: the `entity` cards of
[120](120_context-layer.md), and the first sketch of the hubs.

## Who does what

Machinery could measure most of items 6, 7, 8, 9, 10, 11, 15 and 17 and harvest 18. The agentic
layer would propose role, grain, meaning, date roles, copies, hierarchies, processes, synonyms
and entities (1, 2, 3, 5, 12, 13, 24, 25, 26), and draft the rest from what the machinery found.
A person would rule where the item is meaning, authority or purpose: meaning and business keys
(2, 6), reconciliation anchors (16), sensitivity and legal basis (19), ownership (20), and scope
(21). This follows 070 and adds no new allocation; whether it holds is part of `ARC-OP-24`.

## When the analysis of a table is done

Open, and the author's to rule (`ARC-OP-36`). One shape would be a **minimum dossier** — grain,
keys, role, population, temporal class and sensitivity (items 1, 3, 5, 6, 7, 19) — without which
nothing is built on a table, with the other items completed as the build reaches them. Whether
that minimum is a quality gate, and whether it blocks, is `ARC-OP-33`'s question. The other shape
is a full inventory of every table before the first build, which is more thorough and slower to
first result.

## Prior art

Information analysis is long-established practice. Fact-oriented modelling (NIAM, later FCO-IM),
largely developed in the Netherlands, fixes meaning and identity by verbalising facts with example
populations; Kimball's dimensional design makes declaring the grain its second step, after
choosing the business process. Both are stated from general knowledge and unsourced under rule 8;
`ARC-OP-36` owes the citations if they are to carry weight.
