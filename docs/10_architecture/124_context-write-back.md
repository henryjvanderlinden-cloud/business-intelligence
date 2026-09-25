# 124 — Context write-back: what the agentic layer records, and how it earns trust

Part of the context system described in [120_context-layer.md](120_context-layer.md). Drafted
2026-09-25, session 04, from a brainstorm with the author. Nothing here is built.

## The risk this addresses

Too little context is an obvious failure. The less obvious and more likely one is **too
much**: an agent that writes everything it notices back into the store, so that every future
retrieval returns noise, and true entries become indistinguishable from stale ones. That is
the catalogue decay [145_entropy-and-pruning.md](145_entropy-and-pruning.md) describes for
warehouse objects, happening to the system's own memory.

## Every task ends with write-back

Write-back is a mandatory last step of every task, not an optional courtesy. The task
records three things:

- **what was learned** that is not already in the store;
- **what was decided**, and by whom;
- **what is still open**, as a question card, so the next agent does not rediscover it.

It also answers the retrieval question from
[122_context-retrieval.md](122_context-retrieval.md): what was needed and not found, and what
was loaded and not used.

## Write-back is sorted by the chain

Not everything written back is treated the same. The chain from
[070_task-allocation.md](../00_concept/070_task-allocation.md) decides where it goes:

| What is written back | Route |
|---|---|
| A fact a machine can check (a count, a uniqueness, an orphan rate) | Deterministic machinery verifies it, then it goes straight in as **evidenced** |
| A claim about meaning (what a column means, which records are the same customer) | Enters as **inferred** and joins the human adjudication queue; a pull request against the card, as [120](120_context-layer.md) proposes |
| A change to how things are done (a template, convention, runbook or recipe) | Goes to methodology review, row 38 of 070 |
| A working note about this task | Goes to the task journal, and expires unless promoted |

The split between facts a machine can check and claims only a person can judge is the same
one `ARC-OP-23` draws for metadata. It is what lets the agentic layer write freely where
writing is safe, while keeping the human queue for what needs a human.

## The promotion ladder

Context earns trust by climbing a ladder:

1. **note** — something observed during a task; lives in the task journal;
2. **hypothesis** — a stated claim with a falsifier, worth checking;
3. **assertion** — a claim with evidence or a human ruling, carrying the full assertion record
   from [120](120_context-layer.md) (what, provenance, when, confidence, falsifier, scope);
4. **rule** — a claim that holds over a *set* of objects, with its scope and counterexamples;
   this is the card kind `ARC-OP-16` asks for.

**Anything not promoted expires.** Notes that nobody references and nobody promotes are
removed after a set period by the gardening jobs in
[126_context-gardening.md](126_context-gardening.md). That keeps the store lean without anyone
having to decide to delete things.

## Guarding against noise

- **Write only what is new.** Before writing, the agent checks whether the store already holds
  the fact; if it does, it confirms it (updating *last re-checked*) rather than adding a copy.
- **Near-duplicates are merged**, by the gardening jobs, with both provenances kept.
- **Provenance is mandatory.** A write without source, time and author is rejected. Git
  supplies author and time for cards; the facts store records them per row.

## Open

`ARC-OP-25` covers write-back together with retrieval, since the two share a format and
improve each other.
