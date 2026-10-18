# 129 — Information analysis: what is inventoried about every table before anything is built on it

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-10-18, session 08, from the author's point, verbatim:

> So I was thinking, before anything gets built, there should be a business analysis phase, or
> rather an information analysis, to determine what's in the tables. Things to look out for are:
> granularity, meaning, temporal characteristics, relation to other tables. Can you store this
> somewhere? And also think of other things that should be inventoried before building anything?
> In terms of analysing the tables that are to be imported?

The four points are the author's. Items 5 to 26 were the model's proposal in reply. **Ruled 2026-10-18 in
[ADR-0017](../20_decisions/0017-information-analysis-before-building.md):** all 26 items stay; the minimum is done
with hard effort and no guessing; every item carries a confidence level, reasoning and evidence where possible; the
analysis is never a hard gate; the first trial is the Wide World Importers sandbox. How the analysis is recorded is
proposed in [`analysis/README.md`](../../analysis/README.md) and not ruled; the open questions are in `ARC-OP-36`.
The document is **under review** ([510](../50_process/510_external-review.md)). The author's point is practitioner
input and unsourced under [AGENTS.md](../../AGENTS.md) rule 8. Apart from the first trial on `Sales.Orders`, nothing
here is built.

The Wide World Importers examples are **observed**: read on 2026-10-18 from the header and first
data row of each named file in the extract `data/raw/wwi/2016-06-01/`, from its `manifest.json`,
and, for item 18, from one query through the sandbox's request folder. They illustrate an item;
they are not an analysis of the sandbox.

## What the phase is

*Ruled 2026-10-18, [ADR-0020](../20_decisions/0020-analysis-describes-the-as-is.md):* while in the analysis stage, the
analysis describes the as-is. It records facts and warns about their consequences; it does not decide or propose
measures, reporting dates, designs or loading.

*Ruled 2026-10-18, [ADR-0019](../20_decisions/0019-information-analysis-in-two-rounds.md): the analysis runs in two
rounds.* Round 1 is per table and per column: items 1 to 3, 5 to 23, 27 and 28, with a table's declared foreign keys
under item 6. Round 2 is across tables: item 4, the cross-table part of item 16, and items 24 to 26 — how tables
relate, if at all, which cross-table peculiarities deserve a warning, and what an assumed or proven join means.

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

The phase would produce no separate report. Its output is the record of
[ADR-0018](../20_decisions/0018-information-analysis-record.md) in [`analysis/`](../../analysis/README.md): the
findings about a table or a column, which the `dataset` and `field` cards of [120](120_context-layer.md) would
show, and the findings about a pair of tables, recorded as relationship assertions in `relations/` as
[128](128_join-knowledge.md) requires. Each claim carries its type — *declared* (what the source or its documentation
says), *observed* (what the data shows), *implemented* (what code does) or *intended* (what a person rules it should
mean) — with its evidence. *Corrected 2026-10-18 after sol's review
([XREV](../30_research/notes/XREV_2026-10-18_information-analysis-consistency_sol.md)), which found that the first
wording left relationship findings no home; superseded wording, kept for provenance:* ~~Its output would be the `dataset` and `field` cards of [120](120_context-layer.md), each finding an assertion carrying its claim type — *declared* (what the source or its documentation says), *observed* (what the data shows) or *intended* (what a person rules it should mean) — with its evidence.~~

A table analysed this way stays analysed only while the evidence holds; repeated profiling over loads, freshness
computed from each file's provenance (ADR-0018), and drift detection ([126](126_context-gardening.md)) keep the
findings current.

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
not a person. *Added 2026-10-18 (ADR-0019, R15):* population includes **what the extracting account can see** —
whether the table carries a row-level security policy or masked columns, and whether the extracting account sees as
many rows as an unrestricted one. An extract through a restricted account looks complete while it is not.

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

## Added after the ruling

**27. Peculiarities: more than one thing in one table.** Added 2026-10-18 on the author's instruction, verbatim:

> one more thing before we proceed, we should also test each table for peculiarities like multiple granularities in
> one table (a table containing both customer data and contract data apart from keys, or events/transactions and
> balances), I'm sure you can come up with more.

The tests below are the model's proposal and not ruled. Each names the peculiarity, the test that would find it, and a
Wide World Importers case where one was observed on 2026-10-18 in the 1 June extract. They matter because each one
breaks a build that assumes one table is one thing: a sum double-counts, a join fans out, or a filter silently drops
a kind of row.

*Several grains or entities in one table*

1. **Two entities side by side**: columns about another object riding along with the key's object (customer and
   contract, order and customer). Test: column groups that depend on something other than the key — constant within
   a non-key value. WWI: `Sales.Customers` carries a delivery address and a postal address, each a block of four
   columns.
2. **Events and states in one table**: transactions next to balances or levels. Test: a column that behaves as a
   level (carried forward, not summable over time) on rows that are otherwise events. WWI:
   `Sales.CustomerTransactions` holds invoice and payment events and an `OutstandingBalance`, non-zero on 56 of
   97,242 rows.
3. **Aggregates stored with detail**: totals of child rows held on the parent, which double-count when the parent is
   joined to its children. Test: a header column equal to a count or sum over its lines. WWI: `Sales.Invoices`
   `TotalDryItems` and `TotalChillerItems` equal the number of dry and chiller *lines* on all 70,566 invoices — and,
   despite the name, match the summed quantity on only 145.
4. **Measures at a higher grain repeated on lower-grain rows**: freight or a header discount on every line. Test: a
   measure constant within the parent key. Not observed in WWI yet.
5. **Detail and total rows together**: subtotal, rollup or "TOTAL" rows among detail rows. Test: rows whose measure
   equals the sum of other rows, or rows with an empty dimension. Not observed in WWI yet.
6. **A grain hidden inside a column**: a list of events or items embedded in one value. Test: parse the structured
   columns of item 11 and count elements. WWI: `Sales.Invoices.ReturnedDeliveryData` holds one or two delivery events
   per invoice.
7. **Several time grains**: daily and monthly snapshots, or periods of different length, in one table. Test: the
   spacing of the time column per key. Not observed in WWI yet.

*Several kinds of row in one table*

8. **Subtypes under one key**: rows of different kinds told apart by a type column or by which columns are filled.
   Test: the null pattern of every column per value of each low-cardinality column. WWI:
   `Warehouse.StockItemTransactions` holds issues (customer and invoice filled, quantity negative), receipts (supplier
   and purchase order filled, quantity positive) and stocktake adjustments (neither, either sign); `Application.People`
   holds employees, salespersons, system users, logon users and customer contacts in eight combinations of four flags.
9. **Exclusive arcs**: one of several reference columns filled, or one column referring to different tables by a type
   column. Test: mutually exclusive non-null patterns. WWI: `Sales.SpecialDeals` (item 13);
   `Sales.CustomerTransactions` has an invoice on invoice rows and a payment method on payment rows, never both.
10. **Rows of opposite meaning**: reversals, credit notes, storno entries. Test: a flag or type that flips the sign.
    WWI: `IsCreditNote` exists on `Sales.Invoices`; no credit note is present.
11. **Several levels of one hierarchy**: head offices and branches, groups and members, in one table. Test: a
    self-reference whose target is itself referenced. WWI: 400 of 663 customers are billed to another customer.
12. **Current and historical rows together**: versions with a current flag, or appended snapshots. Test: the key is
    unique only together with a date or flag. Not in a WWI base table; its `_Archive` tables keep history apart.
13. **Several companies, tenants or scenarios**: plan next to actual, one company next to another, keys unique only
    within one. Test: key uniqueness per partition. Not observed in WWI.
14. **Rows from another origin**: migrated or interfaced rows with other conventions. Test: profile split by creation
    date or editor. WWI: rows last edited by person 1, *Data Conversion Only* (item 7).

*Columns that are more than one thing*

15. **Overloaded columns**: one column whose meaning depends on the row type, the company or the period. Test: the
    distribution per type and over time, and a change point. Not observed in WWI yet.
16. **Repeating groups**: `Phone1`, `Phone2`; `Month01` to `Month12`. Test: column-name patterns. Not in WWI.
17. **Units or currencies varying within one column**: amounts in several currencies, quantities in several units,
    with the unit elsewhere or nowhere. Test: a unit column, and the distribution of magnitudes per item. WWI:
    `Sales.InvoiceLines.Quantity` counts *Each*, *Packet*, *Pair* or *Bag* by the line's `PackageTypeID`, fixed per
    stock item, so a sum of quantity across items adds unlike units.
18. **A grain that changes at a date**: one row per order before a cutover, one per shipment after. Test: the
    multiplicity of the key per period. Not observed in WWI.

**28. Arithmetic policy.** Added 2026-10-18 on sol's review
([XREV](../30_research/notes/XREV_2026-10-18_information-analysis-inventory-gaps_sol.md)) and the author's agreement
(ADR-0019): the precision the source calculates with, its rounding mode, where it rounds (per line or per document),
and how residues are treated. Best effort. It decides whether recomputed values (item 9) reconcile with the source's
own: recomputing tax per line and summing, where the source rounds tax per invoice, gives wrong tax, gross revenue and
margin.

Findings under tests 1 to 9 and 11 to 13 bear directly on granularity, which is a minimum item; whether they are
done with the minimum's hard effort is put to the author (`ARC-OP-36`).

## Who does what

Machinery could measure most of items 6, 7, 8, 9, 10, 11, 15 and 17 and harvest 18. The agentic
layer would propose role, grain, meaning, date roles, copies, hierarchies, processes, synonyms
and entities (1, 2, 3, 5, 12, 13, 24, 25, 26), and draft the rest from what the machinery found.
A person would rule where the item is meaning, authority or purpose: meaning and business keys
(2, 6), reconciliation anchors (16), sensitivity and legal basis (19), ownership (20), and scope
(21). This follows 070 and adds no new allocation; whether it holds is part of `ARC-OP-24`.

## When the analysis of a table is done

*Ruled 2026-10-18, [ADR-0017](../20_decisions/0017-information-analysis-before-building.md).* The **minimum** —
granularity, temporal characteristics, role, keys, population and sensitivity (items 1, 3, 5, 6, 7, 19) — is done
with hard effort and no guessing: what cannot be established is written down as an uncertainty, with what would
settle it. The other items are best effort. Every item states a confidence level and its reasoning, with evidence
wherever there is any. The analysis is **never a hard gate**: an uncertain or incomplete analysis travels with the
build as a known uncertainty. Whether a build on an uncertain minimum is flagged by a quality gate is `ARC-OP-33`'s
question.

~~One shape would be a minimum dossier without which nothing is built on a table … The other shape is a full
inventory of every table before the first build.~~ Superseded by the ruling above; kept for provenance.

## How it is recorded

*Ruled 2026-10-18, [ADR-0018](../20_decisions/0018-information-analysis-record.md).* [`analysis/README.md`](../../analysis/README.md)
is the operating manual: a folder per source, schema, table and column; a file per item; a line per claim;
content-addressed evidence; provenance and computed freshness in every file. The first worked example is
[`analysis/wwi/tables/Sales/Orders/`](../../analysis/wwi/tables/Sales/Orders/), the minimum items and item 27. Its
most useful finding so far is a contradiction: `BackorderOrderID` is declared to point from a backorder to its
original and in the data points the other way.

## Prior art

Information analysis is long-established practice. Fact-oriented modelling (NIAM, later FCO-IM),
largely developed in the Netherlands, fixes meaning and identity by verbalising facts with example
populations; Kimball's dimensional design makes declaring the grain its second step, after
choosing the business process. Both are stated from general knowledge and unsourced under rule 8;
`ARC-OP-36` owes the citations if they are to carry weight.
