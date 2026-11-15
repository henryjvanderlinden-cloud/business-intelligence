# ADR-0039 — The first use case is sales over time by customer segment; marts read only from the business vault

- **Status:** Accepted
- **Date:** 2026-11-15
- **Supersedes:** —
- **Superseded by:** —

## Context

Handover 13 set session 13 one task: a thin, end-to-end slice on the existing raw vault of Wide World Importers, one
mart and one analysis answering one business question, each step put to the author before it is built. Three things
it needs were open: the question itself; where a mart takes its data from
([`ARC-OP-37`](../../registers/OPEN_POINTS.md) item 8, proposed 2026-10-26 and not ruled); and the line between raw
vault and business vault ([144](../10_architecture/144_raw-vault-business-vault-calculation-engines.md) §2, not ruled).
[400](../40_roadmap/400_phasing.md) adds that marts require a decision register, which does not exist (`ARC-OP-12`).

On 2026-11-15 the model proposed three questions and recommended the first: A, where invoiced sales and gross profit
come from, by month, customer and stock item; B, how long an order takes and how many are late; C, what customers owe
at month end. It asked whether stock groups, which need a bridge
([146](../10_architecture/146_fact-tables-and-new-questions.md) consideration 8), belong in the first cut. The author
ruled at 16:43, verbatim:

> 14: A, that was also my initial idea, sales over time by customer segment/group (if we have that available) and maybe
> a forecast, but then we’re already over complicating things maybe.
> 15. Leave out stock groups initially

The model then checked that a segment is available (customer category and buying group give seven segments; the
segmentation has no recorded history in the source, `ARC-OP-37`), outlined the slice, and put four cases to him with a
recommendation on each, together with two further recommendations: to keep the forecast out of this slice, and to add
the stock item dimension later. He ruled at 16:57, verbatim:

> Agreed with all recommendations, please proceed. As an aside, is sales the common nomenclature for “omzet” (in Dutch)
> or would this be turnover?

## Options considered

**Where the mart reads from.** *Straight from the raw vault.* Its case: fewest objects, and for one mart the joins
could be written once. Rejected: every mart would repeat the same walk over links and the same choice of satellite
version, and two marts would come to disagree. *From the business vault only, which reaches the raw vault through
point-in-time and bridge structures.* Adopted: the walk and the choice of version are made once, in a named place,
and the mart selects, shapes and aggregates.

**Where sales excluding tax is derived.** The source delivers the amount including tax (`ExtendedPrice`) and the tax
(`TaxAmount`); the difference equals `Quantity` × `UnitPrice` on every line
(`analysis/wwi/tables/Sales/InvoiceLines/09_derived.md`, claim C2). *In the mart or the analysis.* Its case: it is one
subtraction. Rejected: a second mart would make it again, possibly differently, and 144 §2 has marts apply no rule
of their own. *In a calculation engine.* Its case: ADR-0024 puts business rules in engines. Rejected for this value:
ADR-0024 leaves basic arithmetic outside engines. *In the business vault.* Adopted.

**Which segment a past sale is shown under.** The source gives no business date for a customer's category or buying
group. *As it was at the invoice date, taking the source's edit time as a stand-in.* Its case: it is what a user
expects of history. Rejected: [ADR-0027](0027-bitemporal-integration-layer.md) decision 2 forbids presenting source
system time as business time. *As currently known.* Adopted, with earlier knowledge available "as known on" a date.

**The forecast.** *In this slice.* Its case: the author raised it, and a trend invites one. Rejected for now, on his
own doubt and because a forecast is a calculation beyond basic arithmetic, an engine's work under
[ADR-0024](0024-calculation-engines-are-a-versioned-source.md), which handover 13 puts out of this session's scope.

## Decision

1. **The first use case is sales over time by customer segment**, on invoiced sales and gross profit (question A).
   Stock groups are left out initially.
2. **A mart takes its data only from the business vault**, which reaches the raw vault through point-in-time and
   bridge structures. A mart never calculates. This rules what was still open on that point under `ARC-OP-37` item 8.
3. **"Sales" means the amount excluding tax**, derived as the delivered amount including tax less the delivered tax,
   **in the business vault**. This settles the line between raw vault and business vault of 144 §2 for this one case
   only; the line as a whole stays proposed.
4. **A customer's segment is shown as currently known.** Where the source gives no business time for an attribute,
   history is shown under the attribute's value as the warehouse now knows it, and is restated if the value changes;
   what the warehouse knew on an earlier date stays available. Source system time is not used as a stand-in.
5. **The decision this question serves**, the first entry of the decision register: "Which customer segments get sales
   attention, reviewed monthly by the sales manager (the author, standing in), from sales and gross profit per
   segment."
6. **The forecast stays out of this slice.** It is a candidate for a first calculation engine afterwards, on this mart.

Also recommended and not objected to, though he was invited to say so: the stock item's key stays on the fact table,
and its dimension is added later, together with stock groups.

## Consequences

The slice needs a business vault before it has a mart: at least a point-in-time structure for the customer, a bridge
from invoice line to invoice and customer, and the one derived value. They are generated from declarations, not
written by hand (ADR-0032); their design is owed in a note 141 under `docs/10_architecture/`, not yet written.

Decision 4 means a report on past sales can change when a customer changes segment, with no sale having changed. For
Wide World Importers nothing changes today, since no earlier version of a customer differs in category or buying
group; at a client it would, and the report must say under which knowledge date it was made.

Gross profit is taken as the source delivers it. The analysis record shows `LineProfit` equal to `Quantity` ×
(`UnitPrice` − the stock item's current `LastCostPrice`) on every line (`09_derived.md`, claim C3), so it is profit at
current cost, and is labelled so wherever it is shown.

The decision register gets its first entry before it has a ruled form; where it lives and what an entry holds are
to be proposed in note 141. Who maintains it at a real organisation stays open (`ARC-OP-12`): here the author stands in for a
manager who does not exist, which tests the mechanism and nothing about whether an organisation would keep it up.

Decisions 2 to 6 were ruled with one sentence on the model's recommendations, as ADR-0037 was; the general assessment
of 2026-11-14 (point 10) names that as thin adjudication. This decision is unreviewed on another model
([510](../50_process/510_external-review.md)).

**Revisit** decision 2 if a consumer needs data no business-vault object holds and building one costs more than the
mart; decision 3 when the raw/business line is ruled as a whole; decision 4 when a source delivers business time for
such an attribute, or a user needs history "as it was"; decision 6 when calculation engines are built.
