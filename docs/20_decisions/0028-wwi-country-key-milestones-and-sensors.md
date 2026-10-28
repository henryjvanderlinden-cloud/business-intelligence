# ADR-0028 — Wide World Importers: the country is keyed on ISO 3166-1; existence is dated by the event and each milestone is a satellite of its own; the sensor tables as proposed

- **Status:** Accepted
- **Date:** 2026-10-28
- **Supersedes:** —
- **Superseded by:** —

## Context

[147](../10_architecture/147_wwi-concepts-keys-and-business-time.md) proposes step A for Wide World Importers (WWI):
the hubs and business keys of the 31 base tables, and each table's business time under
[ADR-0027](0027-bitemporal-integration-layer.md) decision 4. After two failed review passes on sol, all applied
([keys](../30_research/notes/XREV_2026-10-26_147-keys_sol.md),
[business time](../30_research/notes/XREV_2026-10-26_147-business-time_sol.md)), it put three cases with weak evidence to
the author (147 §6). The rest of 147 remains proposed under [`ARC-OP-37`](../../registers/OPEN_POINTS.md).

The three cases. First, whether the country is keyed on its ISO 3166-1 alpha-3 code without a key-space code: all 190
codes conform to the published list, read second-hand (`analysis/wwi/tables/Application/Countries/06_keys.md#C6`),
but the source refers to countries by its own identifier. Second, how business times written back onto a row later
(picking, delivery confirmation, finalisation, the latest receipt) enter valid time: option (b), dating a whole version
by its latest milestone, failed review, because an order raised in December and picked in June would not exist in an
"as of" query for January. Third, whether the two undescribed sensor tables are taken as proposed, their columns read
from their names.

The author ruled on 2026-10-28 at 10:23, verbatim:

> 1. Okay.
> 2. Sounds good. In Kimball terms, this would be an accumulating fact table, but we should indeed separate them out,
> make separate rows of it. So are they also satellites? I'll leave it up to you.
> 3. Okay.

## Options considered

For the milestones, 147 §6 item 2 set out three options: (a) every version valid from the event date, milestone stamps
plain attributes; (b) a version valid from the latest milestone it shows; (c) the event's existence valid from its
event date and each milestone a fact of its own at its own grain, valid from its stamp. The author chose (c), and left
its form in the vault to the model. For that form there were three candidates:

*Milestone columns in the event's main satellite.* Its case: one satellite per source row. Rejected: the satellite's
one valid time cannot date both the event and its milestones, which is the failure of (b).

*A satellite per milestone on the hub of the thing it dates.* Its case: each satellite row is one assertion with its
own valid time, written insert-only; a corrected stamp is simply a newer row of the same satellite; the split has the
stated reasons 144 §2 asks for, a different assertion with its own business time and a markedly different rate of
change (written once, later). Adopted.

*A milestone event link* (a non-historised link from the hub to a milestone type). Its case: milestones of every kind
in one structure. Rejected for now: the milestones carry different attributes (who picked, who received, the delivery
data), and a correction to an event row has no natural place in an insert-only event link.

## Decision

1. **The country hub is keyed on `IsoAlpha3Code` in the ISO 3166-1 namespace, without a key-space code**, as proposed in
   147 §3 item 1. Relationships that reach a country through the source's `CountryID` resolve it to the ISO code
   deterministically from the same extract.
2. **Option (c): an event's existence is valid from its event date, and each milestone is a separate fact, at its own
   grain, valid from its own stamp.** In the author's words, the milestones are separated out into separate rows.
3. **Each milestone is a satellite of its own** (the author delegated the form, verbatim: "So are they also
   satellites? I'll leave it up to you."), hanging on the hub of the thing it dates: picking on the sales order, and
   separately on the sales order line; delivery confirmation on the invoice; finalisation on the customer ledger
   entry; the latest receipt on the purchase-order line. A row is written when the source first shows the stamp, and
   again when the stamp changes; the newer row supersedes the older over its whole claimed validity from its knowledge
   time on.
4. **What the author called an accumulating fact table is built in the marts**, as a Kimball accumulating snapshot
   with one row per order, invoice or line and a column per milestone, from these satellites; the vault keeps the
   milestones as separate rows ([ADR-0026](0026-conformed-dimensions-and-fact-table-changes.md) governs that fact
   table).
5. **The two sensor tables are taken as proposed** (147 §3 items 21 and 22): hubs for the cold-room sensor and the
   vehicle, readings as events, `RecordedWhen` as business time.

## Consequences

The four consequences of 147 §5 apply to the milestone satellites: a retained stamp dates only its own milestone;
corrections supersede at the later knowledge time, so "valid to from the next row" (ADR-0027) is derived within one
knowledge-time slice; milestones between two daily extracts are sampled, and an "as of" answer between observations is
not claimed correct; the supplier ledger's `FinalizationDate` dates nothing until a settlement is seen written back.
Changes the source does not date (finalising a purchase order or a purchase-order line) stay in the main satellite with
unknown valid time.

A mart that reports how long orders take to pick or invoices to be paid reads these satellites; the lag between two
milestones is then a derived measure, and an engine's where it involves a rule ([ADR-0024](0024-calculation-engines-are-a-versioned-source.md)).

Decision 3 settles part of step C ahead of it, for the milestones only; the satellites of everything else remain open
under `ARC-OP-37` item 1. Decision 3 is the model's, under the author's delegation, and is unreviewed on another model
([510](../50_process/510_external-review.md)).

**Revisit** if a milestone is found that is written more than once in the source's own process, if the marts' lag
measures cannot be computed correctly from sampled milestones, or if the source turns out to correct stamps often
enough that the supersession rule needs a structure of its own.
