# 124 — Context write-back: what the agentic layer records, and how it earns trust

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from a brainstorm with the author. Revised twice the same day after
external review: first on GPT-6 Astra
([XREV_2026-09-25_context-system_astra](../30_research/notes/XREV_2026-09-25_context-system_astra.md)
Q2), which separated re-checking from re-encountering, bound verification to exactly what was
tested, decoupled scope from trust, controlled the human queue, kept negative findings and
restricted merging; then on gpt-5.6-sol
([XREV_2026-09-25_context-system-r2_sol](../30_research/notes/XREV_2026-09-25_context-system-r2_sol.md)
Q2), which moved write-back from the end of a task to its whole duration, allowed one write to
reach several destinations, replaced the one-way ladder with a lifecycle, kept every candidate
outside the human queue, made expiry decidable and made merges reversible. Under
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md), what is written
back are assertions. Nothing here is built.

## The risks this addresses

Too little context is an obvious failure. The less obvious and more likely one is **too
much**: an agent that writes everything it notices back into the store, so that every future
retrieval returns noise. That is the catalogue decay
[145_entropy-and-pruning.md](145_entropy-and-pruning.md) describes for warehouse objects,
happening to the system's own memory. Two further risks: write-back that manufactures
*apparent* trust nothing earned, and write-back that is lost when a task fails.

## Write-back runs throughout a task, not only at its end

A task that crashes, is cancelled or fails part-way never reaches a final step, and loses
exactly the diagnostics needed to recover; a retry may then write everything twice. So
observations and actions are **appended as the task goes**, each carrying the task's run
identifier and an **idempotency key**, so that a retry does not duplicate them. The final step
only marks the run complete and adds the summary:

- **what was learned** that is not already in the store;
- **what was decided**, and by whom;
- **what is still open**, as a question, so the next agent does not rediscover it;
- the answers to the retrieval questions of [122_context-retrieval.md](122_context-retrieval.md).

**"Nothing new" is a valid result, and a common one.** A step that must always produce
something invites agents to invent marginal "learnings" to complete it.

## One package, several destinations

A single finding can matter in several places at once: an orphan rate is an observation, evidence
for a semantic hypothesis, and possibly a blocker for a workflow. Routing each write to exactly
one destination would drop some of those consequences or create disconnected copies. So each
write is one **immutable write-back package**, and explicit routing rules send **references** to
it to every consumer that needs it, recording each routing decision and any routing failure.

The consumers follow the chain of [070_task-allocation.md](../00_concept/070_task-allocation.md):

| Consumer | What it receives |
|---|---|
| **The facts store** | Facts a machine can check, after deterministic machinery has verified them — as the claim the check established, nothing wider (below) |
| **The adjudication candidates** | Claims about meaning, which only a person can rule on — see *keeping the human queue workable* |
| **Methodology review** | Proposed changes to templates, conventions, runbooks or recipes — row 38 of 070 |
| **The workflow store** | Approvals awaited, checkpoints, records of actions taken — never expire until the workflow closes |
| **The task journal** | Working notes, under the retention rules below |

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

## A lifecycle, not a ladder

The first draft had a promotion ladder — note, hypothesis, assertion, rule — which made trust look
like something that only increases. It is not: a later contradiction, a revoked approval or a
change in source behaviour has to be able to take a claim back down. And a *rule* is a claim with
a wider scope, not a more mature one.

So three things are recorded separately for every assertion:

- **lifecycle status** — `proposed`, `accepted`, `contested`, `superseded`, `retracted`. Any
  accepted claim can become contested or retracted;
- **evidence** — what supports it, in its evidence bundle ([120](120_context-layer.md));
- **authority** — whether someone with the mandate ruled it.

Human ruling and empirical evidence are **different routes** to acceptance and establish different
things; which one a claim needs is set by its type and by the acceptance rules of
[122](122_context-retrieval.md). A **rule** is an assertion whose scope is a set of objects; it is
accepted on its own evidence, never by promotion from a claim about one member. **Generalising a
claim to a wider scope creates a new proposed claim**, and recorded counterexamples say nothing
about members nobody examined. A working note that deserves to become a claim is written as a new
proposed assertion referring to the note.

## Keeping the human queue workable

Mandatory write-back can produce semantic claims faster than people can rule on them. A cap on
what may be submitted would help, but on its own it causes silent loss — agents would have to
choose what to drop — and it invites gaming by splitting tasks. So:

- **every candidate is kept**, in a candidate store outside the queue; nothing is lost because the
  queue is full;
- only a selection enters the **adjudication queue**, which has **service classes** (for example
  regulatory, consequential, routine), **ageing** so that rare but critical items cannot be starved
  by frequent ones, and an explicit **capacity** per reviewer role;
- duplicates are removed before anything reaches a person;
- related claims may be presented together, but **each claim gets its own decision** — a batch is
  never accepted or rejected wholesale.

Which candidates enter the queue at all is the question of the adjudication economy, which is
still open.

## What expires, and what is kept

Every note is created with a **retention class, an owner, a review date, a privacy ceiling** and,
when it expires, an **expiry reason**. That makes expiry a decision someone can apply, rather than
an estimate of "how likely this is to come back" that nobody owns.

- **Negative findings are kept**, in compact form — *tried X on Y, it failed because Z* — with the
  conditions under which it is worth revisiting.
- When a note expires, a **tombstone or harmless digest** is kept, so that a later search shows the
  question was considered.
- A note never outlives the retention its privacy ceiling allows.

## Merging

Near-duplicates are consolidated only when their **predicates and scopes are equivalent**. "Unique
per tenant" and "globally unique" are different claims; they are linked, not merged.
Consolidation is **reversible**: the original claims stay unchanged and are linked into a
canonical group, which can be split again if they later diverge by validity period or source
correction. Consolidations use **optimistic version checks**, so that two concurrent merges cannot
consolidate against stale state.

## Provenance

A write without source, time and author is rejected. Git supplies author and time where it is the
medium; the other stores record them per row.

## Open

`ARC-OP-25` covers write-back together with retrieval, since the two share a format and improve
each other.
