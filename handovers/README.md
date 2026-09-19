# Handovers — convention

A handover is a document written *for the next session*, by the session that is ending.
It exists because a fresh session — a new model, a new context window, or the author
three months later — starts cold, and the expensive failure is not forgetting what was
decided but silently reopening it.

Adapted from the compendium repository's `handovers/` series.

## Naming

```
HANDOVER_<NN>_<YYYY-MM-DD>_<slug>.md
```

Sequential, never renumbered, never deleted. [CURRENT.md](CURRENT.md) points at the live
one and is the file a fresh session reads first.

## Required structure

**Status block.** The first thing in the file. Either the handover is current, or it
carries a line beginning `**STATUS: HISTORICAL (superseded <date>)**` naming its
successor. A handover without a status block cannot be trusted, because nothing in it
says whether it still describes the world.

**Where we stand.** Repository state: expected HEAD, what the last session changed, what
to verify before proceeding. A fresh session's first action is stated explicitly and is
usually `git log --oneline -5` plus reading the register.

**This session's task, in one sentence.** If it does not fit in a sentence it is more
than one session.

**Scope.** What is in, what is out, and against which register rows.

**Traps and warnings.** What the previous session got wrong, nearly got wrong, or
suspects. This is the section with the highest value per line and the one most often
skipped.

**Do not reopen.** Settled rulings that a fresh session, lacking context, will be
tempted to relitigate. Each with its ADR.

## Discipline

- **Only the current state has to be right.** Revise the handover as often as the session
  produces insight worth carrying; rewrite it whole at close if it has become a
  patchwork. The file is under version control, so revising in place loses nothing and
  the intermediate states stay recoverable. Do not annotate a handover with an account of
  its own editing history — git holds that, and the next session does not need it.
- What the rule actually guards against is **reconstruction after the fact**: writing the
  handover days later from the diff, once the reasoning has evaporated. Write while the
  reasoning is still available.
- A handover does not duplicate the register. It points at rows; the rows hold the
  state. Where the two disagree, the register wins.
- When a session ends without completing its task, the handover says so plainly. A
  handover that reports success it did not achieve is worse than none, because the next
  session will build on it.

Note that supersede-don't-delete, which governs
[`../registers/README.md`](../registers/README.md) and the design documents, is *not* the
rule here. That discipline exists because superseded argument carries the reasoning that
produced a ruling, and losing it leaves the ruling unexplained. A handover carries no
argument that the register does not already hold, so git is sufficient retention for it.
