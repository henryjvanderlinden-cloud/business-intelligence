# 127 — Temporal behaviour: how each table and attribute behaves over time

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from the author's point, verbatim:

> What's more, I think we also need to assess per attribute or table, the knowledge part of
> your remark number 1, what to do with timelines, like static facts, or type 2 SCD, even more
> context.

Revised the same day after external review on gpt-5.6-sol, recorded in
[XREV_2026-09-25_context-system_sol](../30_research/notes/XREV_2026-09-25_context-system_sol.md)
Q2, which replaced a single list of classes with independent axes, corrected an overstatement
about what the Data Vault keeps, and added capture guarantees, a stricter test for deletion and
monitoring of temporal order. The author's point is practitioner input and unsourced under
[AGENTS.md](../../AGENTS.md) rule 8. Nothing here is built.

## Two different questions

For every table, and for every attribute that matters, there are two questions, and they are
often confused:

1. **How does the source behave?** What does it do when something changes?
2. **What do we want to keep?** What history should the warehouse hold and present?

The answers differ, and the gap between them is where warehouses silently go wrong. A source
that overwrites a customer's segment in place cannot be made to show history the warehouse
never captured.

## How sources behave: independent axes

A single classification loses information, because the behaviours combine: an append-only
event can arrive late; a versioned source can also correct retroactively and soft-delete; a
periodic snapshot can overwrite values. So behaviour is recorded on six independent axes,
per attribute or per table where the whole table behaves alike:

| Axis | Values | Example |
|---|---|---|
| **Mutation** | static · overwritten in place · versioned in the source · append-only | date of birth · CRM address · policy with effective dates · transactions |
| **Delivery** | full refresh · periodic snapshot · incremental · change data capture · audit log | a monthly balance extract · a CDC stream |
| **Effective dating** | none · business-effective dates · source validity periods | *valid from* columns in the source |
| **Arrival latency** | on time · late-arriving or backdated | claims and returns arriving after their period |
| **Correction** | none · corrected retroactively | financial adjustments to closed periods |
| **Deletion** | none · soft (flagged) · hard (row disappears) · explicit delete events | an *is_active* flag · a CDC delete record |

## The capture guarantee

**Loading more often can never guarantee complete history.** If a value changes twice between
two loads, the intermediate state is invisible however often the warehouse polls, so observed
change frequency always understates true volatility.

Every source therefore records its **capture guarantee**: whether it can deliver every
transition (change data capture, an audit log, or versions kept in the source) or only samples
of state. Where complete transition history is required, the source must provide one of those
mechanisms. Otherwise the warehouse's history is labelled **sampled**, and presented as such —
never as full history.

## What the Data Vault layer keeps

The mature architecture puts a Data Vault between raw data and the marts to keep "all the data,
all the time". That holds only if the loading guarantees it, and several things can break it:

- **Append-only loading must be guaranteed and checked.** Faulty load logic can update
  satellites in place.
- **Hash-difference rules suppress repeated values.** That is usually intended, but it means the
  vault records *changes*, not every delivery.
- **Deletion and effectivity need explicit structures** — records of deletes and of validity
  periods — because they are not ordinary attribute changes.
- **Two timestamps, always:** when something was true in the business (source-effective time)
  and when the warehouse loaded it (load time). A raw vault cannot tell a retroactive correction
  from a genuinely new business state by load order alone; only source effective dates or
  explicit correction markers can.

## What we choose to keep

Given what the vault can see, the choices sit in four places:

- **Capture** — per source, whether a sampled history is acceptable, or a stronger capture
  mechanism must be arranged.
- **Mart design** — row 15 of [070](../00_concept/070_task-allocation.md): per attribute,
  type 1 (current value only), type 2 (full history) or type 6 (both); *as-was* versus *as-is*
  reporting; bitemporal treatment where retroactive corrections matter; and rule versioning where
  derivations change ([190](190_machine-authored-design-canon.md) §1).
- **Joins across time** — a join between historised tables has to be *as of* a date on both
  sides; see [128_join-knowledge.md](128_join-knowledge.md).
- **Erasure** — row 37 of 070: a history the warehouse keeps is a history it may have to delete
  from.

## Absence is not deletion

A row that disappears between two loads may have been deleted — or the extract may have been
partial, a filter may have changed, pagination may have failed, a partition may be late, or a
source read may have failed. Treating every absence as a deletion creates false tombstones and
wrong historical status.

So a disappearance is classified as a deletion only with **evidence that the extract was
complete**: control totals, watermarks, the expected partitions present, a successful run
status — and preferably an explicit delete event from the source. The same principle governs
the context store's own housekeeping ([126](126_context-gardening.md)).

## Who does what

Following the chain of 070:

- **Deterministic machinery measures** across successive loads: per column, how often values
  change, whether rows are overwritten or appended, whether date columns only increase, and
  whether rows disappear — with the completeness evidence above.
- **The agentic layer classifies** each table and attribute on the six axes, with the evidence,
  and **proposes** the treatment and any need for stronger capture.
- **A person decides** the treatment, because it encodes business meaning, audit obligations and
  correction policy (row 15).
- **Deterministic machinery monitors** both the values and the **order of time** (below).
  Observed behaviour that no longer matches the recorded axes is drift, and goes to gardening.
  **Policy exceptions** — a correction to a closed period, a missing delete trail — go to the
  accountable data owner, not to routine gardening.

## Monitoring the order of time

Monitoring values alone misses a whole class of errors: backfilled records, replayed batches,
duplicate events, out-of-order change data capture and gaps in source sequences all leave
plausible-looking values while corrupting the timeline. So deterministic machinery also
monitors:

- **sequence continuity** — gaps in source sequence numbers or CDC positions;
- **latency** — the difference between when an event happened and when it was ingested;
- **replays and duplicates** — the same delivery or event arriving twice;
- **closed periods** — reconciliation of periods that should no longer change.

## Where it is recorded

As **knowledge**, in the sense of [120](120_context-layer.md): a temporal section in the front
matter of each dataset and field card, holding the six axes, the capture guarantee, the evidence,
the confidence, the chosen treatment and who decided it. The raw measurements stay in the
landscape-facts store; only the conclusions are on the card, with their evidence snapshots.

## A caveat that matters

A single snapshot cannot tell *static* from *rarely changing*, nor *hard-deleted* from *not yet
loaded*. Classification needs several loads, so it starts as a hypothesis and firms up over
time. Late-arriving and retroactively corrected data are the hardest to detect, because both
look normal until someone reconciles a past period.

`ARC-OP-27` holds what is open.
