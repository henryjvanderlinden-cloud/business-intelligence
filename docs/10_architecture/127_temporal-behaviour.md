# 127 — Temporal behaviour: how each table and attribute behaves over time

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from the author's point, verbatim:

> What's more, I think we also need to assess per attribute or table, the knowledge part of
> your remark number 1, what to do with timelines, like static facts, or type 2 SCD, even more
> context.

This is practitioner input and unsourced under [AGENTS.md](../../AGENTS.md) rule 8. Nothing
here is built.

## Two different questions

For every table, and for every attribute that matters, there are two questions, and they are
often confused:

1. **How does the source behave?** What does it do when something changes?
2. **What do we want to keep?** What history should the warehouse hold and present?

The answers differ, and the gap between them is where warehouses silently go wrong. A source
that overwrites a customer's segment in place cannot be made to show history the warehouse
never captured.

## How sources behave

Per attribute, or per table where the whole table behaves alike:

| Class | Behaviour | Example |
|---|---|---|
| **Static** | Set once, never changes, except by correction | date of birth, order date |
| **Overwritten** | Source keeps only the current value | customer address in many CRMs |
| **Versioned in source** | Source keeps its own history | a policy system with effective dates |
| **Event / append-only** | New rows only; old rows never change | transactions, log entries |
| **Periodic snapshot** | The whole state is re-delivered at intervals | a monthly balance extract |
| **Soft-deleted** | Rows are flagged rather than removed | an *is_active* column |
| **Hard-deleted** | Rows disappear without trace | many operational tables |
| **Corrected retroactively** | Past values are fixed after the fact | financial adjustments |
| **Late-arriving / backdated** | Rows arrive after the period they describe | claims, returns |

Per table, the delivery mechanism matters as well: full refresh, incremental, or change data
capture, and whether deletes are visible at all.

## What we choose to keep

The Data Vault layer keeps every change it sees ("all the data, all the time"), so the vault
itself is not where most of this choice is made. The choice matters in four places:

- **What the vault can see at all.** If a source overwrites faster than the load runs,
  intermediate values are lost before the vault sees them. Load frequency must be set against
  observed change frequency.
- **Mart design** — row 15 of [070](../00_concept/070_task-allocation.md): per attribute,
  type 1 (current value only), type 2 (full history), type 6 (both), *as-was* versus *as-is*
  reporting; and bitemporal treatment where retroactive corrections matter, with rule
  versioning where derivations change
  ([190](190_machine-authored-design-canon.md) §1).
- **Joins across time** — a join between two historised tables has to be *as of* a date on
  both sides; see [128_join-knowledge.md](128_join-knowledge.md).
- **Erasure** — row 37 of 070: a history the warehouse keeps is a history it may have to
  delete from.

## Who does what

Following the chain of 070:

- **Deterministic machinery measures** across successive loads: per column, how often values
  change, whether rows are overwritten or appended, whether date columns only increase, and
  whether rows disappear.
- **The agentic layer classifies** each table and attribute into the classes above, with the
  evidence, and **proposes** the treatment.
- **A person decides** the treatment, because it encodes business meaning, audit obligations
  and correction policy (row 15).
- **Deterministic machinery monitors** whether observed behaviour still matches the recorded
  class. A mismatch is drift, and goes to gardening
  ([126_context-gardening.md](126_context-gardening.md)).

## Where it is recorded

As **knowledge**, in the sense of [120](120_context-layer.md): a temporal section in the front
matter of each dataset and field card, holding the class, the evidence, the confidence, the
chosen treatment and who decided it. The raw measurements stay in the landscape-facts store;
only the conclusion is on the card.

## A caveat that matters

A single snapshot cannot tell *static* from *rarely changing*, nor *hard-deleted* from *not yet
loaded*. Classification needs several loads, so it starts as a hypothesis and firms up over
time. Late-arriving and retroactively corrected data are the hardest to detect, because both
look normal until someone reconciles a past period.

`ARC-OP-27` holds what is open.
