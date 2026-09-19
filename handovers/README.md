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

- The handover is written at the *end* of a session, while the reasoning is still
  available, not reconstructed later from the diff.
- A handover does not duplicate the register. It points at rows; the rows hold the
  state. Where the two disagree, the register wins.
- When a session ends without completing its task, the handover says so plainly. A
  handover that reports success it did not achieve is worse than none, because the next
  session will build on it.
