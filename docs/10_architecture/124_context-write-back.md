# 124 — Context write-back: what the agentic layer records, and how it earns trust

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from a brainstorm with the author, and revised the same day after
external review on GPT-6 Astra, recorded in
[XREV_2026-09-25_context-system_astra](../30_research/notes/XREV_2026-09-25_context-system_astra.md)
Q2. The review separated re-checking from re-encountering, bound verification to exactly what
was tested, decoupled scope from trust, capped the human queue, kept negative findings, and
restricted merging. Nothing here is built.

## The risk this addresses

Too little context is an obvious failure. The less obvious and more likely one is **too
much**: an agent that writes everything it notices back into the store, so that every future
retrieval returns noise, and true entries become indistinguishable from stale ones. That is
the catalogue decay [145_entropy-and-pruning.md](145_entropy-and-pruning.md) describes for
warehouse objects, happening to the system's own memory. A second risk is that write-back
manufactures *apparent* trust that nothing earned.

## Every task ends with write-back — which may be empty

Write-back is a mandatory last step of every task. The task records:

- **what was learned** that is not already in the store;
- **what was decided**, and by whom;
- **what is still open**, as a question card, so the next agent does not rediscover it;
- the answers to the retrieval questions of [122_context-retrieval.md](122_context-retrieval.md).

**"Nothing new" is a valid result, and a common one.** A step that must always produce
something invites agents to invent marginal "learnings" to complete it.

## Write-back is sorted by the chain

The chain from [070_task-allocation.md](../00_concept/070_task-allocation.md) decides where a
write goes:

| What is written back | Route |
|---|---|
| A fact a machine can check (a count, a uniqueness, an orphan rate) | Deterministic machinery verifies it, then it goes in as evidenced — as the claim the check established, nothing wider (below) |
| A claim about meaning (what a column means, which records are the same customer) | Enters as inferred and joins the human adjudication queue; a pull request against the card, as [120](120_context-layer.md) proposes |
| A change to how things are done (a template, convention, runbook or recipe) | Goes to methodology review, row 38 of 070 |
| Workflow state (an approval awaited, a checkpoint, a record of an action taken) | Goes to the durable workflow store of [120](120_context-layer.md); never expires until the workflow is closed |
| A working note about this task | Goes to the task journal, and expires unless promoted or retained as a negative finding |

### A check establishes only what it checked

"Machine-checkable" does not mean the machine checked the right claim. A uniqueness test that
excludes nulls, or looks at one partition, would otherwise admit "this column is unique". So
every verification is bound to its explicit **predicate, population, exclusions and result**,
and only the claim those establish is admitted: *unique among non-null values in the 2026
partition*, not *unique*.

### Re-checking is not re-encountering

An agent that finds its own proposed claim already in the store must not treat that as a
re-check. **The *last verified* date changes only after a recorded verification.** How often a
claim is encountered is tracked separately, because repetition would otherwise manufacture
freshness.

## The promotion ladder

Context earns trust by climbing a ladder:

1. **note** — something observed during a task; lives in the task journal;
2. **hypothesis** — a stated claim with a falsifier, worth checking;
3. **assertion** — a claim with evidence or a human ruling, carrying the full record of
   [120](120_context-layer.md) and the trust dimensions of [122](122_context-retrieval.md);
4. **rule** — a claim that holds over a *set* of objects, with its scope and counterexamples;
   the card kind `ARC-OP-16` asks for.

**Scope and trust are independent.** Evidence about one dataset does not become a rule for a
whole source family by being promoted. Generalising a claim to a wider scope creates a **new
hypothesis** that needs its own validation; recorded counterexamples say nothing about members
nobody examined.

## Keeping the human queue workable

Mandatory write-back can produce semantic claims faster than people can rule on them, burying
the consequential ones. So:

- each task has a **cap** on the claims it may submit for adjudication;
- the queue is **prioritised by consequence and by reuse** — how much depends on the claim;
- **related claims are batched** into one request rather than arriving separately.

## What expires, and what is kept

Unpromoted notes expire after a set period, removed by the gardening jobs of
[126_context-gardening.md](126_context-gardening.md). But expiry by lack of reference would
favour popular notes over valuable ones: a failed approach nobody looks at expires, and next
quarter someone repeats the investigation. So:

- **negative findings are kept**, in compact form — *tried X on Y, it failed because Z* — with
  the conditions under which it is worth revisiting;
- retention is decided by **how likely the question recurs and how costly it is to
  rediscover**, not by how often a note was referenced.

## Merging

Near-duplicates are merged only when their **predicates and scopes are equivalent**. "Unique
per tenant" and "globally unique" are different claims; they are linked, not merged. When
claims are merged, both provenances are kept.

## Provenance

A write without source, time and author is rejected. Git supplies author and time for cards;
the facts store and the workflow store record them per row.

## Open

`ARC-OP-25` covers write-back together with retrieval, since the two share a format and improve
each other.
