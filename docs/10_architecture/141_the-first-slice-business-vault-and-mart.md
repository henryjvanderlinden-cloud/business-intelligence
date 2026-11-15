# 141 — The first slice: a business vault and a mart for sales by customer segment

**Status: draft, proposed.** Written 2026-11-15, session 13, by Claude Fable 5.2, as the design owed by
[ADR-0039](../20_decisions/0039-first-use-case-and-where-marts-read-from.md), which rules the question, where the mart
reads from, where sales excluding tax is derived, and that a segment is shown as currently known. Everything else here
is proposed. Reviewed on sol the same day, which failed the first version on five points
([XREV](../30_research/notes/XREV_2026-11-15_141-first-slice_sol.md)); all five are applied below, in §2 items 5 and
7, §3 rules 2 and 4, §4, §5 and §9, and the revision is unreviewed. Nothing in it is built; the conditional is used for
what would be.

## 1. What this note does

It designs the shortest chain from a source extract to an answer for the first use case, sales over time by customer
segment: the smallest business vault the question needs, one dimensional mart, one analysis, and their tests. The
author's aim is generally applicable knowledge with Wide World Importers (WWI) as the example, so each section says
which part is a general rule and which part is WWI's. The general part is five kinds of object, each declared in a
small text file and generated ([ADR-0032](../20_decisions/0032-generated-sql-machinery.md)), and one rule for time.

## 2. One rule for time: every object above the raw vault is a function of a knowledge date (general)

1. Every row of the raw vault carries `load_date`, the knowledge time
   ([143](143_the-vault-generator.md) §4), and the raw vault is insert-only. So what the warehouse knew on any earlier
   date can be computed again from the rows with `load_date` up to that date.
2. Every business-vault and mart object would therefore be defined as one query with one parameter, `known_on`, that
   reads only raw-vault rows with `load_date <= known_on` and other objects at the same `known_on`.
3. The stored table is that query at the latest load date, rebuilt whole on every load (ADR-0015). The same query
   would be kept in the warehouse as a DuckDB table macro, `<object>__as_known(known_on)`, so "as known on" a date is a
   call, not a second structure. This is the "as of" view of
   [ADR-0027](../20_decisions/0027-bitemporal-integration-layer.md) decision 3 for knowledge time. Tried on DuckDB
   1.5.6 on 2026-11-15: a table macro takes a date, is stored in the database file, and is read from a read-only
   connection; it binds its tables when created, so it is created after the tables it reads.
4. Business time needs no structure in this slice: the only business time is the invoice's date, a column of the fact
   table, and "as of a business date" is a filter on it. Attributes without business time are shown as known
   (ADR-0039 decision 4).
5. **What the macro answers, and what it does not.** It answers what the *current* declarations and templates give
   on the deliveries dated up to that date. It does not answer what was published on that date, if a declaration or
   template has changed since; that comparison belongs to release regression (`ARC-OP-30`). And knowledge time is the
   date a delivery states, not the moment the warehouse received it (143 §4 item 2), so the answer is what the
   warehouse knew on that date only if deliveries were loaded in the order of their dates. The sandbox's runner
   enforces that (oldest first, each date the next one expected); a delivery loaded after a later-dated one would
   rewrite earlier knowledge without a trace in these rows. A generated test (§9 item 9) would fail when the record of
   runs shows such an order. Found by review, finding 2.
6. **Cost.** A call recomputes from the raw vault. That is right for 230,000 invoice lines; for a large fact table it
   would not be, and stored snapshots or knowledge-time ranges would be needed. Revisit then.
7. **What one clean source shows.** These rules and those of §3 are tried on one source in which every satellite and
   every link is filled from one table. They are stated for that case and claim nothing about several sources
   describing one key (§3 rule 2).

## 3. What is current in the raw vault, as known on a date (general)

The templates would apply four rules, each over rows with `load_date <= known_on` only.

1. **A hub key is known** when its hub row is among them.
2. **A satellite's current row** for a key is the last of its rows in source order (`source_ts`, `source_seq`). A
   satellite stores a source version only when it differs from the one before it in source order, and a late arrival
   is followed by a restatement of the next version (143 §6), so the last stored row holds the values of the latest
   source version known. This is an order only within one source table. A satellite whose rows have no `source_ts`
   has no source order, and a satellite or link filled from more than one table or source has no single order: which
   source's value stands is survivorship, a business rule that
   [144](144_raw-vault-business-vault-calculation-engines.md) §3 leaves to the business vault and nothing here
   designs. The generator would stop on either (neither is in this slice). Narrowed after review, finding 5.
3. **A link is current** for its driving key when it is the link named in the current row of the link's effectivity
   satellite (rule 2 applied to it); an empty name there means no relationship.
4. **A key is present** when the latest row of its status-tracking satellite says `present` or `reappeared`. A key
   with no such row is not present: the status loader writes a row only for keys seen in a complete current extract,
   so a key the warehouse knows only from the source's history (deleted before the first load) has none, and the
   first version of this rule, "present unless absent", would have made a sale of it (review, finding 1). A hub
   without a status-tracking satellite has no evidence of presence, and the generator would stop on one. Absence is
   not deletion ([127](127_temporal-behaviour.md)), so a key that is not present would be left out of dimensions and
   fact tables, and a generated test would report how many were left out, as a warning. Whether the raw vault should
   itself record a key first seen only in history is a question for 143, not answered here.

## 4. The business vault: three kinds (general), seven objects (WWI)

**Point-in-time table**, `pit_<hub>`. One row per key of a hub, known and present, holding for each satellite the
declaration names the source version (`record_source`, `source_ts`, `source_seq`) of its current row. It holds
pointers, not values. WWI: `pit_invoice_line`, `pit_invoice`, `pit_customer`, `pit_customer_category`,
`pit_buying_group`, each naming its hub's main satellite only.

**Bridge**, `brg_<start>__<name>`. One row per key of a starting hub, holding the hub keys reached by walking declared
links, each step through the current link of rule 3. A walk is allowed only over links driven by the hub it leaves,
so every step gives at most one key and the bridge has exactly the rows of its starting hub. A step reaches a key
only when there is a current link and the hub key it names is itself known and present (rule 4); otherwise the key
is left empty and nothing is walked beyond it, and the bridge records per step why: `no link`, or `not present`. The
first version walked on through an absent invoice to its customer (review, finding 3). WWI: `brg_invoice_line__sale` (invoice line to invoice, from there to customer and to
bill-to customer, and invoice line to stock item) and `brg_customer__segment` (customer to customer category and to
buying group).

**Computed satellite**, `csat_<hub>__<name>`. One row per key, holding a value derived here by basic arithmetic from
the current row of a satellite, with the rule's name and version on every row and the ADR that ruled it in the
declaration. WWI: `csat_invoice_line__sales_amount`, with `sales_amount_excl_tax` = `ExtendedPrice` − `TaxAmount`
(rule `sales-amount-excl-tax`, version 1, ADR-0039 decision 3). The declaration would name an oracle where the source
offers one, here `Quantity` × `UnitPrice`, and a generated test would compare the two on every row.

Anything beyond basic arithmetic is an engine's (ADR-0024) and is not a computed satellite.

## 5. The mart: two kinds (general), three objects (WWI)

**Dimension.** One row per key of one hub, its attributes read through point-in-time tables and bridges, plus one
unknown member, so that every fact row finds exactly one row (146 consideration 8). Dimensions are conformed
(ADR-0026): declared once, outside any use case. WWI: `dim_customer` (customer identifier and name, customer
category, buying group, with the declared label "No buying group" where the customer has none, which is a state and
not a gap) and `dim_date`, a calendar generated by rule from the first invoice date to the end of the month of
`known_on`, with year, quarter, month, and whether the month is complete as known. The bill-to customer is a second
role of `dim_customer`, not a second dimension.

**Fact table.** A stated grain, a stated intent citing a decision of the decision register (§7), keys, and measures,
each with its aggregation contract (146 consideration 6). WWI: `fct_invoice_line`, a transaction fact table, one row
per invoice line present, **whatever its walk reached**: a line whose invoice or customer was not reached keeps its
row and its amounts, on the unknown member of the dimension and with an empty invoice date, so that no amount
disappears and the totals still equal what the source delivered, and a generated test counts such rows, as a warning.
The row holds the invoice date; the keys of customer, bill-to customer and stock item (the last without a
dimension yet, ADR-0039); invoice and line identifiers; `is_credit_note`; and five measures. Four may be summed along
every dimension: `sales_amount_excl_tax`, `tax_amount`, `sales_amount_incl_tax`, and
`gross_profit_at_current_cost` (the source's `LineProfit`, named for what the analysis record shows it to be).
`quantity` may be summed within one stock item only, since across items it adds packages of different kinds. A margin
is not stored: it is the sum of profit over the sum of sales.

A mart object reads point-in-time tables, bridges, computed satellites and, through a point-in-time table's pointers,
the satellites they point at. It joins and selects; it computes nothing (ADR-0039 decision 2).

## 6. The analysis (WWI, with a general shape)

One declared query on the mart, `sales_by_customer_segment_month`: per month and segment (category and buying group),
sales excluding tax, gross profit at current cost, and the number of invoices, with incomplete months marked. Its
result would be a table in the warehouse and a short findings note written by the agent layer from that result,
stating the knowledge date, the decision it serves and that profit is at current cost. Proposed place:
`findings/<decision>/`. How the result leaves the author's machine is to be settled while building, since the
sandbox's DuckDB cannot write files (handover 13).

## 7. The decision register (general, proposed)

One small file per decision, `registers/decisions/DEC-<nnnn>_<slug>.md`, in the grammar of
[`model/README.md`](../../model/README.md): the decision in one sentence, its owner, its cadence, the evidence it
uses now, its status, and the ADR that recorded it. Every fact table and every analysis would cite one, and the
checker would refuse one that does not. First entry, worded in ADR-0039 decision 5: DEC-0001, which customer segments
get sales attention. Who keeps such a register up at a real organisation stays open (`ARC-OP-12`).

## 8. Declarations and the generator (general)

New folders beside `model/raw_vault/`: `model/business_vault/` (`pits/`, `bridges/`, `computed/`), `model/marts/`
(`dimensions/`, `facts/`) and `model/analyses/`, in the existing grammar. The generator (0.4.0) would get one template
per kind, write each object as a table rebuilt on every load with its `__as_known` macro, stop on any pattern it does
not support, and keep the header that names declaration and template. `tools/check_repo.py` would be extended in the
same commit (rule 11 of `AGENTS.md`): every reference resolves; a walk leaves a hub only over links that hub drives;
every measure has a contract; every fact table and analysis cites a decision; every computed value cites an ADR.

## 9. Tests, generated with the objects

1. **Grain.** The fact table's key is unique, and it has exactly as many rows as there are invoice lines known and
   present.
2. **Nothing lost or multiplied on the way.** Each point-in-time table, bridge and computed satellite has exactly the
   keys of its hub that are known and present.
3. **Reconciliation.** The sum of each measure equals the sum of the same column over the current rows the source
   delivered in this load (the staging table), which does not pass through the vault's own rules. It checks totals only; test 10 checks rows.
4. **Lookups.** Every fact row finds exactly one row in `dim_customer` for each role; rows landing on the unknown
   member or left without an invoice date are counted, as a warning. Every key a bridge reached is a key known and
   present in its hub.
5. **The oracle** of §4, on every row.
6. **Plausibility**, as warnings while `ARC-OP-31` is open: a credit note appears (none exists, and its sign is
   unknown); a complete month without sales; the latest complete month outside half to double the median of the
   twelve before it.
7. **Replay**, in the cloud suite: after two loads, each object's macro at the first date equals the table stored
   after the first load.
8. **Memory**, in the cloud suite: the build under the 2 GB budget of the author's machine.
9. **Order of loads.** No batch was first loaded successfully after a later-dated one, read from the record of runs
   (`nsdn_meta.dbt_invocations`); an error, since §2 item 5 depends on it.
10. **Lineage, row by row.** Tests 1 to 5 check counts, totals and arithmetic, and would all pass if two lines swapped
    customers and amounts (review, finding 4). So for the load date, the fact table joined to its dimensions is
    compared row by row with the same lines built from the delivered rows by the source's own identifiers: the
    staging tables of invoice lines, invoices and customers joined on `InvoiceID` and `CustomerID`, giving for every
    delivered line its invoice, date, customer, bill-to customer, stock item, category, buying group and amounts. The
    two sets must be equal in both directions. This path uses no hash key, link, effectivity row, point-in-time
    table or bridge, so it is evidence independent of them; it shares only the staging tables' typing of columns.
    It holds for the load date only, since staging keeps one delivery. The generator would derive it from the
    declarations, which already name the source column behind every link end.

## 10. Not decided here

The stock item dimension and stock groups; the forecast; engines; access rules, though a mart would inherit the
highest sensitivity class among its inputs (the invoice lines are `confidential`); quality gates (`ARC-OP-33`);
several sources ([144](144_raw-vault-business-vault-calculation-engines.md) §3); what counts as a distinct use case.
