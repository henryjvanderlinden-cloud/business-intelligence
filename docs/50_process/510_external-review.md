# 510 — External review passes

Adapted from the compendium repository's `XREV` convention, which was written after two
review passes on the same day differed only in framing and differed enormously in yield.
Those findings transfer directly and are the reason this file exists before the first
pass rather than after it.

An **external review note** records one review pass, on one object, by one model other
than the one that drafted it.

## Naming

```
XREV_<YYYY-MM-DD>_<object-slug>_<model>.md
```

Filed in [`../30_research/notes/`](../30_research/notes/). A second reader's rebuttal
appends `_counter-<model>`. Date rather than serial number, so a note can be filed
without allocating a register row first.

Examples:

```
XREV_2026-09-26_autonomy-tiers_sol.md
XREV_2026-09-26_autonomy-tiers_counter-opus5.md
XREV_2026-09-26_machine-proposable-keys_sol.md
```

## Required front matter

```yaml
object:        the file and section under test
reviewer:      model, transport, working directory
assignment:    what the model was asked; what was declared out of scope
second reader: who set the assignment, and what material is unreviewed by construction
verdict:       HOLDS UNDER [conditions] / FAILS [+ counterexample] / UNDETERMINED [+ what is owed]
```

The verdict line is mandatory and must take one of those three shapes. A pass that
cannot produce one was not scoped tightly enough.

## Assignment design

Four rules, carried over because they were learned from a measured difference in yield
rather than from taste.

**One object per pass.** A whole-corpus read returns one sound observation wrapped in a
generic verdict; a single-object refutation returns counterexamples. Chain a long
assignment across replies in one thread; do not widen the prompt. The device bridge here
also times out in the region of a minute, which enforces the same discipline mechanically.

**Supply the apparatus.** Give explicit file and section references for the object, the
documents that depend on it, and the objections the repository has already stated
against itself. A reviewer that has not seen a document's own admitted weaknesses will
return them as findings, and that output is worthless.

**Ask a question with a determinate answer.** "Does this follow; if not, what minimal
assumption makes it follow; if it fails, give the counterexample." Never "assess this".

**Forbid general assessment explicitly.** Models supply one unprompted, it is the
weakest thing they produce, and it dilutes the finding.

Adversarial framing — *assume the claim is wrong and try to show it* — has outperformed
neutral framing. Refute before proving: a plausible-looking defence of a keystone claim
is the most expensive kind of wrong output this project can absorb.

## What this project's review passes are for

The compendium reviews theorems. This repository has no theorems; it has load-bearing
empirical and conceptual claims, and they are what a pass should attack. The standing
list, in descending order of how much depends on them:

1. That business keys and cross-source entity identity are machine-proposable at a
   precision making adjudication worthwhile — the falsifiable core.
2. That the structural / semantic / teleological tiering is a real distinction rather
   than a restatement of an existing one (`CON-OP-1`).
3. That a model adds evidence beyond what profiling, naming and query logs already
   supply (`EVI-OP-3`).
4. That an organisation will maintain a decision register (`ARC-OP-12`).
5. That the economics work (`CON-OP-2`).

An object not on this list can still be reviewed; these are the ones whose failure would
cost the most.

## Discipline

- A review note is not an edit. Its dispositions become register rows; documents change
  later, deliberately.
- Material added by the model that *set* the assignment is unreviewed by construction,
  must be marked as such in the note, and must be reviewed on a different model before
  it is folded in.
- A note that finds nothing is filed anyway, with its verdict. A pass that is never
  recorded because it was unproductive makes the review history look better than it was.
