# Conventions for agents working in this repository

This file is read by language models operating in this repository (Claude Code, Codex,
and successors). It is deliberately short. If it grows past two screens, it has failed.

## Start and end of a session

**Open** by reading [`handovers/CURRENT.md`](handovers/CURRENT.md) and
[`registers/OPEN_POINTS.md`](registers/OPEN_POINTS.md), then run
`python tools/check_repo.py` and confirm it passes before changing anything.

**Close** by updating the register rows your work touched, writing the next handover
(convention: [`handovers/README.md`](handovers/README.md)), repointing
[`handovers/CURRENT.md`](handovers/CURRENT.md), and running the check again. Register
updates travel in the same commit as the work they describe.

The full method is [`docs/50_process/500_working-method.md`](docs/50_process/500_working-method.md).

## What this repository is

A design repository for `nsdn`, an agent-driven data-infrastructure system. In its
current phase it contains prose, not software. Do not scaffold application code, CI
pipelines, package manifests or test harnesses unless an ADR in `docs/20_decisions/`
has adopted the thing being scaffolded.

## Rules

1. **Prose is the artifact.** Write in full sentences. Avoid bullet-heavy formatting in
   conceptual documents; reserve lists for things that genuinely enumerate.
2. **Preserve verbatim material.** `docs/00_concept/010_vision.md` is a transcript. Do
   not edit it, tidy it, or correct it. Disagreement goes in `020_critique.md`.
3. **Decisions go in ADRs; open questions go in the register.** If you find yourself
   choosing between two designs in a normal document, stop and write an ADR instead.
   ADR format is in `docs/20_decisions/0000-template.md`. Number sequentially; never
   renumber. If you find yourself noting something unresolved, put it in
   `registers/OPEN_POINTS.md` under its conventions — a question raised only in prose or
   only in conversation is a question that will be lost.
   **`RULED` is not `EXECUTED`**: a decision is not the work.
4. **Supersede, do not delete.** An ADR that is overtaken is marked `Superseded by
   ADR-NNNN` and left in place. The same discipline applies to design documents and to
   register rows: strike through and annotate rather than silently rewriting history.
   The word **superseded** is load-bearing and machine-read — in a register row, its
   first occurrence opens the historical block, and nothing after it is a current claim.
5. **Number with gaps.** Document filenames use a three-digit prefix with gaps of ten,
   so new material can be inserted without renumbering.
6. **One concept per file.** Files should be readable in isolation and cheap to load
   into a context window. If a file exceeds roughly 400 lines, split it.
7. **Cross-link explicitly.** Use relative markdown links. A concept mentioned but not
   linked is a concept that will be lost.
8. **Mark provenance on assertions.** When a document states something as fact about
   the outside world (a tool's capability, a benchmark, a legal constraint), say where
   it came from. Unsourced claims are treated as hypotheses.
9. **Do not invent progress.** Do not write documents that describe components as if
   they exist. Use the subjunctive for anything unbuilt.
10. **Commit granularly**, one coherent change per commit, with a message that says why
    rather than what.
11. **Write the check, not the sentence.** A convention you add to this repository is
    unenforced until `tools/check_repo.py` enforces it. Extend the checker in the same
    commit, or mark the convention as unenforced.
12. **Review on a different model.** Material you drafted is unreviewed by construction;
    see [`docs/50_process/510_external-review.md`](docs/50_process/510_external-review.md).

## Open questions

[`registers/OPEN_POINTS.md`](registers/OPEN_POINTS.md) is the authoritative register of
things not yet resolved. Adding a row is a contribution. Closing one is a contribution
that usually ends in an ADR. `docs/00_concept/040_open-questions.md` is superseded by it
and retained for provenance only.
