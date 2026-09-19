# ADR-0007 — Adopt the compendium's register, handover and enforcement apparatus

- **Status:** Accepted
- **Date:** 2026-09-19

## Context

This project will run over a long period in many short sessions, with different models,
long gaps, and an author whose attention is divided. That is exactly the situation in
which state is lost: what was open, what was merely ruled rather than done, what a
previous session suspected but did not write down.

The author's compendium repository has been operating under that pressure for months and
has developed an apparatus for it — an authoritative open-points register with explicit
state tokens, a handover series, an external-review convention, and mechanical checks —
each part of which was added after a specific failure. The register's state convention,
for instance, exists because the register was found unable to answer *what is open?*: its
`Status` column held the status a row had when it was opened, current state lived
elsewhere, nothing said so, and five rows ended up asserting two contradictory things at
once. The checks exist because four written rules had already failed at the hands of the
corpus that wrote them.

Inheriting these is cheap. Relearning them is not.

## Options considered

*Start minimal and add apparatus when a failure demands it.* Honest, and it is how the
compendium arrived at its own conventions. Rejected because the failures are already
known, their cost is already paid, and the argument for waiting is really an argument
for repeating them.

*Copy the compendium's apparatus wholesale, including its scale.* Rejected. That register
is 640KB and carries months of argument; this project has one week of thinking. Copying
the size along with the shape would produce ceremony in place of work.

*Adopt the conventions, not the scale.* Adopted.

## Decision

The following are adopted, adapted where this project differs:

**An authoritative open-points register**, `registers/OPEN_POINTS.md`, with explicit
state tokens in a fixed position, the `RULED` versus `EXECUTED` distinction, the
partial-settlement rule, supersession by the load-bearing word *superseded*, scoped
identifiers that are never reused, and archive rules documented before the first cut.
`docs/00_concept/040_open-questions.md` is superseded by it and retained for provenance.

**A handover series**, `handovers/`, with a status block, a stated first action, a
one-sentence task, traps and warnings, and an explicit do-not-reopen list. `CURRENT.md`
points at the live handover.

**An external-review convention**, `docs/50_process/510_external-review.md`, adapting
the compendium's XREV practice — one object per pass, supply the apparatus, ask a
question with a determinate answer, forbid general assessment, adversarial framing — to
a repository whose load-bearing objects are claims rather than theorems.

**Mechanical enforcement**, `tools/check_repo.py`, standard library only, under the
compendium's rule that a newly-written rule is unenforced until something mechanical
enforces it.

Two deliberate deviations are recorded. The register uses one heading per row rather than
a markdown table, because its rows carry argument, because partial loads suit the
retrieval constraint this project argues for elsewhere, and because it avoids the
pipe-escaping trap that silently broke five compendium rows. And the archive apparatus is
documented but unused until the register warrants a cut.

## Consequences

Sessions acquire a fixed opening and closing ritual, which is overhead on a short session
and the whole value on a long gap.

The register becomes the authority on what is open, which means a question raised only in
conversation is a question that will be lost — a discipline that has to be actively kept.

The apparatus now exceeds the work it administers, which is acceptable at this size and
stops being acceptable quickly. `PRC-OP-2` holds that concern open deliberately.

`tools/check_repo.py` will need extending as conventions are added. A convention added
without a check is decoration, and this ADR is the reason that sentence is enforceable
rather than aspirational.
