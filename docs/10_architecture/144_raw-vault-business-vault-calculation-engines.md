# 144 — Raw vault, business vault and calculation engines

**Status: draft, partly ruled.** Written 2026-10-26, session 09, at the author's request to store what was discussed
and decided on 25 and 26 October. What the author ruled is recorded in
[ADR-0024](../20_decisions/0024-calculation-engines-are-a-versioned-source.md) and
[ADR-0025](../20_decisions/0025-engine-results-in-the-raw-vault.md); everything else here is proposed and
open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md). Unreviewed on another model. Subjunctive throughout: none of
what is described exists.

The Data Vault terms used below are the model's general knowledge of common practice as of mid-2026, not verified in
this session; under [AGENTS.md](../../AGENTS.md) rule 8 they are hypotheses about what practitioners do, and they are
used as the example layer of [ADR-0013](../20_decisions/0013-data-vault-or-equivalent.md).

## 1. Why this note exists

Handover 09 set the task of designing the generic integration layer for Wide World Importers. Before answering the
route and the two decisions put to him (whether the layer is bitemporal, and how derived measures are handled), the
author asked four questions, verbatim:

> Before I answer the questions, do you want to make a distinction between a raw vault and a business vault?

> Okay, and the raw vault would be by source, right? This is what I'm interested in, if we have e.g. done an
> acquisition of another company, with its own administration and corresponding quirks, do we set up a new structure
> for it, or does it all go into the entities that were set up for the initial source? So my question is, if we have
> administrations/databases that cover in essence the same business entities (multiple core banking systems, legacy
> core banking systems), do we set up a raw vault for each of them, or do we all cram them into the same raw vault, or
> is this something we handle at the business vault layer?

> can you tell me what the raw vault is for and what the business vault is for?

> Where do you place calculation engines? For any application of business rules and calculations (except for very
> basic addition and multiplication) I envisage to have calculation engines, which are more like software (think
> python programs) then doing it in SQL. The thing with calculation engines, is that they should have versioning, unit
> testing, inline documentation etc. I imagine building them with e.g. numpy and panda. If a calculation is performed,
> ideally it would store the value and the version of the calculation engine. I see this as a separate source. What do
> you thinkg?

This note sets out the answers as proposed, and the part the author ruled.

## 2. Two layers, two jobs

The model proposed that the integration layer be split into a raw vault and a business vault, as
[140](140_data-vault-automation.md) already assumes ("The raw vault is mechanical. The business vault ... encodes
interpretation") and as [ADR-0015](../20_decisions/0015-sandbox-warehouse-dbt-duckdb.md) already builds into the
sandbox ("the raw vault is insert-only; the business vault and marts are rebuilt on each run"). Neither says where the
line between the two falls. The proposal, not yet ruled:

**The raw vault is the warehouse's memory.** It would keep everything every source delivered, integrated on business
keys and stamped with when it arrived, so that nothing is ever lost and any past state can be reconstructed. It serves
five purposes: nothing is lost (all the data and all the history, insert-only, the first two properties of ADR-0013);
integration on identity where identity is certain (hubs join sources only on keys that mean the same thing); audit and
lineage (what system X said about this on date Y, and when we received it); the base for rebuilding everything
downstream; and the signal that a source changed, since a difference in the raw vault can only come from a source. It
holds no business rules, and nobody reports from it directly. It is generated from the key declarations by
templates; the only human judgement in it is the keys. The only transformations allowed are technical and loss-free:
hashing keys, mapping types without loss, and splitting attributes into satellites by source and rate of change.

**The business vault is the warehouse's understanding.** It would turn the memory into business meaning once, in one
reusable place, before any report: values the source does not store, business rules, integration the raw vault cannot
do with certainty (matching across key spaces, readings of roles, inferred links), views over time (as-of,
point-in-time, bitemporal where a report needs them), and helper structures such as point-in-time and bridge tables so
that marts stay simple. Everything in it can be rebuilt from the raw vault and from stored engine results (section
4); its objects are proposed by agents and ruled on by a person, and each cites the decision or measure it serves.

Raw vault, business vault and marts then form a chain in which marts select and shape but never calculate, so that two
marts cannot compute "revenue" in two ways. Two questions place an object: *did a system say this?* puts it in the raw
vault; *would it change if a rule changed tomorrow?* puts it in the business vault. The first question was first
proposed as *did a source say this?*; it was widened when calculation engines became a source (section 4).

## 3. Several sources for the same business entities

The author's case is an acquisition, or several core banking systems, legacy and current, describing the same
customers and accounts. The proposal, not yet ruled, is one raw vault, split by source where descriptions live and
shared only where identity is genuinely shared:

1. **Satellites are always per source.** The acquired company's customer data gets its own satellite on the same hub;
   two sources never write to one satellite, so each keeps its own quirks, history and load times, and which system
   said what is always visible.
2. **Hubs are per business concept, not per source.** Two sources share a hub key only when their keys are the same
   identifier with the same meaning. IBAN 123 in system A is the same account as IBAN 123 in system B, and the raw
   vault integrates them without interpretation. Customer 42 in one core banking system and customer 42 in an acquired
   one are different people: they may share the hub, but each key carries a code for its key space (often called a
   collision code), so the two 42s stay two rows.
3. **Links are shared only for the same declared relationship.** A relationship that only one system holds gets its
   own link.
4. **Matching across key spaces is interpretation, and belongs in the business vault.** That customer 42 in A is
   customer 9137 in B, concluded from name, date of birth, address or a national identifier, is a judgement with a
   confidence; it becomes a same-as link with its evidence, adjudicated and not generated. The first sandbox was
   exactly this problem: its match proposals between PAR and OpenStreetMap were candidate same-as links
   ([142](142_the-data-model.md) §1).
5. **A mapping that a source delivers loads as raw.** A migration's old-to-new number table is a fact delivered by a
   system, not an inference of ours, and loads into the raw vault as a same-as link.
6. **The integrated view is built in the business vault** from those links, and is rebuilt when a matching rule
   changes; the raw vault is untouched.

The two alternatives were rejected in the proposal. A separate raw vault per source is a persistent staging area with
hub-shaped tables; it fails the third property of ADR-0013 (integration on business keys) and pushes every join across
systems downstream. Loading everything into the first source's structures, without satellites per source and without
key-space codes, silently merges different customers who share a number and loses which system said what, which a bank
needs for lineage ([152](152_bcbs-239.md)). This agrees with the financial-services note
[030](../60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md) §1 and §2, which keeps the raw
vault source-aligned and asks each key's issuer or collision scope to be resolved and crosswalks asserted explicitly.

The hard part is again the keys ([140](140_data-vault-automation.md)): for each concept, whether an identifier has the
same meaning across sources. A shared hub key should need evidence for that.

## 4. Calculation engines

**Ruled** ([ADR-0024](../20_decisions/0024-calculation-engines-are-a-versioned-source.md)): business rules and
calculations beyond basic arithmetic are performed by calculation engines, which are software rather than SQL, with
versioning, unit tests and inline documentation; every result is stored with the version of the engine that produced
it; the engines' output is a separate source; the boundary between SQL and engine is as in item 1 below; on a new
version everything is recomputed when compute and storage allow, and a new version is new data even when the values
are the same; corrected inputs are handled by rerunning, using bitemporality.

The engines would be deterministic machinery, outside both vaults: agents may write them, but agents do not run in the
data path ([ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md)), and the machinery keeps working when the
agent layer is down. Their results would come back into the warehouse as an internal source, labelled as derived and
under their own source code, so that they are never taken for operational data.

Proposed with it, not yet ruled:

1. **The boundary** (ruled): anything with a rounding decision, a condition that carries business meaning, an
   allocation, or logic over time is an engine's; SQL keeps joins, filters and basic addition and multiplication with
   no rounding decision. On this rule even an order's value is an engine's, because of the rounding of tax.
2. **A version is the code and its locked dependencies.** The same engine code on another version of numpy or pandas
   can give other numbers, so the dependencies are pinned in a lock file and the lock is part of the version.
3. **Every result row records what it was computed from**: the engine and its version, a run identifier, and the as-of
   of its inputs (which load, or which point in time). Without the as-of, a version does not reproduce a figure.
4. **Insert-only, versions side by side.** A new version adds rows and never overwrites; a mart chooses which version
   it shows. Running two versions on the same inputs measures the impact of a release, which is what
   [`ARC-OP-30`](../../registers/OPEN_POINTS.md) asks of every release note. Because the author ruled that a new version
   is new data, change detection on engine results includes the version, and not only the values.
5. **Money is never binary floating point.** pandas and numpy default to binary floats, which cannot hold most cent
   amounts exactly and so round some half-up cases to the cent wrongly; the source rounds invoice-line tax half up to
   the cent. Money is held as integer cents or as Python `Decimal`.
6. **A fixed order without cycles**: load the raw vault, build the business vault, run the engines, load their
   results, build the marts. An engine that reads its own earlier results, such as a running balance, says so.
7. **The source's own computed columns are test oracles.** The analysis record shows the source's tax formula
   reproduced on every invoice line (`analysis/wwi/tables/Sales/InvoiceLines/09_derived.md#C1`); such claims become
   unit tests.
8. **Results are keyed at their full calculation grain, and a run may deserve identity of its own.** Note
   [030](../60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md) §5 asks that each engine
   output be modelled at its full grain, with run and model version (and scenario or horizon where they apply) in the
   key, so that two runs or scenarios do not collide and a later run's correction does not look like ordinary history
   (items 2 and 3); and, where runs are shared lineage objects, a hub and links for them rather than row attributes
   (item 4). Whether WWI needs run hubs is open.

**Time.** An engine result has two times: the period it describes and when it was computed. The author's answers to
recomputation and to corrections both rest on a bitemporal structure ("using a bitemporal database structure, we can
time travel"), so engine results are bitemporal by his ruling. Whether the integration layer as a whole is bitemporal,
decision 1 of handover 09, remains to be put formally, though his answers point that way.

**Where engine results land: the raw vault** (ruled 2026-10-26 in
[ADR-0025](../20_decisions/0025-engine-results-in-the-raw-vault.md)), under the engine's own source code and labelled
as derived. The raw-vault test is therefore *did a system say this?*. Note
[030](../60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md) §2 item 5, which had placed
calculated values in the business vault, is corrected to agree.

**When full recomputation cannot be afforded** (ruled in the same ADR): first recompute from a cut-off date onwards;
if that is still too much, apply the new version going forward only; every step of this fallback is adjudicated by a
person.

## 5. What this means for Wide World Importers

There is one source, so nothing is shared yet, but two cheap choices would keep the door open: satellites named after
their source from the first load (for example `sat_customer__wwi`), and a key-space code on every hub key from the
start, because WWI's keys are integers the database assigns (`analysis/wwi/tables/Sales/Orders/06_keys.md#C1`), and
whether they are known outside the database is not established (`#C7`); a second company's `CustomerID` 42 would
collide.

In the raw vault would sit orders, order lines, invoices and transactions as delivered, including the source's own
computed columns (`TaxAmount`, `ExtendedPrice`, `LineProfit` on invoice lines): the source's calculations are facts
about the source. Also there: the SQL Server history tables, the declared links including both `CustomerID` and
`BillToCustomerID` on invoices, and the audit columns in a satellite of their own, so that they do not make rows look
changed when no business value changed (the distortion principle, [ADR-0021](../20_decisions/0021-position-in-the-schema.md)).

In engines or in the business vault would sit an order's value, which the source stores nowhere
(`analysis/wwi/tables/Sales/OrderLines/08_measures.md#C6`); our own recomputation of invoice tax and its
reconciliation to the source's figure; the matching of payments to invoices, for which the source holds no key
(`analysis/wwi/across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C2`); the readings of the two
customer roles; which of the two meanings of "orders" a report uses; any stock position worked out from the movements,
which does not agree with the holdings (`analysis/wwi/tables/Warehouse/StockItemHoldings/09_derived.md#C1`); and all
as-of views.

## 6. Grey zones put to the author

1. **Technical conversion in the raw vault.** Only loss-free conversions, or also tidying such as trimming spaces? The
   proposal is loss-free only, since tidying is already interpretation.
2. **Values that cannot be fully rebuilt later.** `LineProfit` equals quantity times the difference between unit price
   and the item's cost price as it stands in the extract (`analysis/wwi/tables/Sales/InvoiceLines/09_derived.md#C3`),
   and whether it follows later changes of cost is not established. That cost price sits in
   `Warehouse.StockItemHoldings`, which is not versioned and is overwritten daily, so the raw vault holds only the one
   state per day that the extracts catch. Rebuilding from the raw vault is only as good as what it captured, which
   makes completeness of capture ([127](127_temporal-behaviour.md), the capture guarantee) matter more than usual here.

## 7. Marts

On 2026-10-26 the author asked whether marts are derived from the raw and business vault, and proposed a dimensional
model for every distinct use case. He then ruled that dimensions are conformed and shared, that design is mainly about
fact tables, and that extending a fact table for a new question is a fundamental, adjudicated decision
([ADR-0026](../20_decisions/0026-conformed-dimensions-and-fact-table-changes.md)). The considerations for that decision
are drafted in [146](146_fact-tables-and-new-questions.md).

## 8. What this note does not decide

The raw/business line (section 2, apart from engine results, which are ruled), the rules for several sources
(section 3), the conditions on engines (section 4, items 2 to 8), whether the layer as a whole is bitemporal, and
where marts take their data from are open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md). The declaration language and the model files of
[142](142_the-data-model.md) remain under `ARC-OP-29` and `ARC-OP-20`.
