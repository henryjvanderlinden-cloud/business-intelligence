# XREV 2026-10-26 — 146: fact tables and new questions, with ADR-0026 decision 6 — sol

```yaml
object:        docs/10_architecture/146_fact-tables-and-new-questions.md §2 and §3, with ADR-0026 decision 6, as committed in 68090d3.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch.
assignment:    assume the classification is unsafe; up to five requests that 146 classifies as minor or unchanged but that change
               an existing number, break additivity, corrupt the table or mislead; up to three wrong or missing
               considerations with the case each flips; the author's rulings not to be argued as preferences. First
               assigned to gpt-6-astra twice; astra wrote nothing, and the pass was re-sent to sol at 09:52.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 09 on 2026-10-26; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [a single-valued Type 2 dimension lookup with overlapping effective ranges duplicates fact rows and changes
               every existing additive total]. Resolved in the revised 146 §2 and §3, unreviewed; ADR-0026 annotated.
```

## sol's answer, verbatim

# Adversarial review of 146 sections 2–3 and ADR-0026 decision 6

## Request-level counterexamples

### 1. Coarsening a periodic snapshot across time

**Quote:** “Coarser is an aggregation and needs no change.” / **What is wrong:** Coarsening is safe only across dimensions on which every selected measure is additive. A balance in a periodic snapshot is semi-additive: summing daily balances into a month changes the meaning from month-end stock to stock-days, even though the query uses only existing rows, measures and dimensions. / **Case:** Table: `FactInventoryDaily`; grain: one row per product, warehouse and day; request: “show total inventory balance by product and year” by summing `OnHandQuantity`. Section 3 classifies this as **serve without change** because the requested grain is coarser. The result adds 365 daily states and materially overstates inventory. / **Correction:** Define “serve without change” as requiring a declared aggregation operator for every measure along every dimension being collapsed. For snapshot balances, a time roll-up must select an ending snapshot, compute an explicitly named average, or use a separately designed aggregate; an unspecified sum must not pass. / **Confidence:** High.

### 2. Adding a ratio as a same-grain measure

**Quote:** “A new measure at the same grain, from the same population, is the cheapest change there is.” / **What is wrong:** Same row grain and population do not make a measure additive or safe for the fact table’s default aggregation. Section 2 recognizes non-additivity, but the operative minor-extension definition does not require consideration 6 to pass and names any new same-grain measure. / **Case:** Table: `FactInvoiceLine`; grain: one row per posted invoice line; request: add `GrossMarginPercent = GrossMarginAmount / NetRevenueAmount`. The value is single-valued at every line and uses exactly the existing population, so section 3 admits it as a **minor extension**. A BI client that applies the fact table’s normal `SUM` aggregation reports the sum of line percentages; even `AVG` gives an unweighted result rather than `SUM(GrossMarginAmount) / SUM(NetRevenueAmount)`. / **Correction:** Limit minor measure extensions to measures with an explicit aggregation contract compatible with every exposed roll-up. A ratio may be exposed only as a governed derived metric over additive numerator and denominator measures, with direct summation disabled; otherwise the request is not a minor extension. / **Confidence:** High.

### 3. Adding a dimension through a non-lossless lookup

**Quote:** “Adding a dimension that has exactly one value per row is cheap.” / **What is wrong:** A business assertion that each fact has one value is not enough. The physical lookup must be total and many-to-one at the fact’s effective time. Overlapping Type 2 versions can turn one fact row into two rows while still giving each output row one segment value; an inner join can instead discard unmatched facts. Either operation changes existing measure totals without redefining a measure. / **Case:** Table: `FactSalesLine`; grain: one row per posted sales line; request: add the single-valued `CustomerSegmentKey`, resolved from a Type 2 customer-segment dimension using customer and sale date. Two segment versions overlap for one customer for three days. Section 3 calls the new single-valued dimension a **minor extension**; the join duplicates affected sales lines and increases existing `NetSalesAmount`. / **Correction:** A minor dimension extension must prove a lossless, temporally correct many-to-one lookup: exactly one dimension key for every fact row, including an explicit unknown member, with invariant fact-row count, fact keys and existing measure totals. Zero or multiple matches makes the change fundamental until the source or temporal rule is adjudicated. / **Confidence:** High.

### 4. Treating a mutable milestone as a cheap role-played date

**Quote:** “Adding a role-played dimension … is cheap.” / **What is wrong:** Role-playing a dimension is a presentation technique; it does not decide which version of a mutable business date belongs on the fact. Overwriting a revised promise date preserves one date key per row and leaves existing measure columns untouched, but destroys the historical promise against which performance was meant to be measured. / **Case:** Table: `FactOrderLineAccumulating`; grain: one row per order line, updated through fulfilment milestones; request: add `PromisedDeliveryDateKey` so users can report on-time delivery against the promised date. The source keeps only the latest revised promise. Section 3 classifies the new role-played date as a **minor extension**. A report run after a late promise revision now makes the same delivery appear on time and cannot reproduce the promise known when the order was accepted. / **Correction:** A role-played dimension is minor only when the fact already has, or can deterministically acquire, the intended immutable/version-qualified foreign key. A mutable forecast, milestone or “as-was” request must specify effective and knowledge-time semantics; if history is unavailable or row versioning is required, classify it as fundamental or as a new snapshot fact. / **Confidence:** High.

### 5. Adding a header-grain amount to a line-grain fact

**Quote:** “A new measure at the same grain and population … [is a] minor extension.” / **What is wrong:** “At the same grain” is left as a property of the requested output column, but a measure also has a source measurement grain. Merely repeating a header amount onto each line produces a numeric value on every fact row without converting the measurement to line grain. / **Case:** Table: `FactInvoiceLine`; grain: one row per invoice line; request: add `InvoiceFreightAmount` from the invoice header to every line, for the same set of posted invoices already represented. The request can be described mechanically as a new measure populated on every existing row, so the section 3 rule admits it as a **minor extension**. Summing by customer or month multiplies each invoice’s freight by its line count; joining the column can also change previously correct net-revenue-plus-freight calculations. / **Correction:** Require lineage grain to equal fact grain before a measure is minor. A coarser-grain amount must remain in a fact table at its natural grain or be allocated by an explicit, governed, reconciliation-preserving rule whose residual and reversals are defined; choosing such an allocation is fundamental. / **Confidence:** High.

## Kimball-style modelling omissions or errors

### 6. Additivity is not a property of a measure alone

**Quote:** “Additive measures can be summed along every dimension; semi-additive ones (a balance) not along time; non-additive ones (a rate, a ratio) not at all.” / **What is wrong:** The classification needs an aggregation matrix, not a three-way label attached only to the measure. Additivity can depend on the dimension, hierarchy, fact-table type and requested operator; distinct counts and snapshot quantities are common cases where a valid aggregate at one level cannot be re-aggregated at another. / **Case:** `FactInventoryDaily` at product–warehouse–day grain, request for yearly inventory, flips from **serve without change** to **not servable by an unspecified aggregation** once time-specific additivity is enforced. / **Correction:** Record, and make the classifier evaluate, the permitted aggregation operator for each measure-by-dimension pair and the permitted re-aggregation of derived results. / **Confidence:** High.

### 7. Dimension cardinality must include referential and temporal integrity

**Quote:** “single-valued at the grain” / **What is wrong:** Kimball-style dimensional integrity requires more than one conceptual attribute value per event. The fact must carry one valid surrogate key selected under a stated slowly-changing-dimension rule, with late-arriving and unknown-member behavior; the lookup must neither fan out nor filter the fact. / **Case:** `FactSalesLine` at posted-line grain, request for customer segment through overlapping Type 2 ranges, flips from **minor extension** to **fundamental data/temporal-rule repair** because uniqueness at event time is not established. / **Correction:** Replace “single-valued” with “exactly-one, lossless, effective-time-correct surrogate-key resolution for every fact row,” and make violations non-minor. / **Confidence:** High.

### 8. Source measurement grain and allocation are missing

**Quote:** missing / **What is wrong:** The considerations ask whether the new measure is at the target table’s grain but never separately establish the grain at which the source measurement occurred or whether an allocation changed it. Dimensional modelling keeps a fact at the grain at which it was captured unless a separately named allocation rule produces reconciled atomic facts. / **Case:** `FactInvoiceLine` at invoice-line grain, request to copy invoice-header freight to each line, flips from **minor extension** to **new header-grain fact or fundamental governed allocation** when source grain is considered. / **Correction:** Add a required consideration: declare the source measurement grain, prove it equals the fact grain, and otherwise require either a separate fact table or an adjudicated allocation with reconciliation to the source total. / **Confidence:** High.

VERDICT: FAILS [a single-valued Type 2 dimension lookup with overlapping effective ranges duplicates fact rows and changes every existing additive total]

## Dispositions

1. **Accepted.** Coarsening must respect each measure's aggregation contract (considerations 1 and 6; serve without
   change).
2. **Accepted.** A minor measure needs an aggregation contract; ratios are stored as numerator and denominator.
3. **Accepted.** A minor dimension needs a total, many-to-one, effective-time-correct lookup with row count, keys and
   totals unchanged, checked rather than assumed (consideration 8).
4. **Accepted.** A role-played key must be known as it was at the event; overwritten values are not minor
   (consideration 9).
5. and 8. **Accepted.** The source measurement grain decides, folded into consideration 5.
6. and 7. **Accepted**, folded into considerations 6 and 8.
ADR-0026 gains a dated note that 146 §3 states the preconditions for "minor"; decision 6 is not altered, since its own
proviso is that no existing number changes.
