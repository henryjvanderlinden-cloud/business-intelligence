# Conventions for agents working in this repository

This file is read by language models operating in this repository (Claude Code, Codex,
and successors). It is deliberately short. If it grows past two screens, it has failed.

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
3. **Decisions go in ADRs.** If you find yourself choosing between two designs in a
   normal document, stop and write an ADR instead. ADR format is in
   `docs/20_decisions/0000-template.md`. Number sequentially; never renumber.
4. **Supersede, do not delete.** An ADR that is overtaken is marked `Superseded by
   ADR-NNNN` and left in place. The same discipline applies to design documents:
   strike through and annotate rather than silently rewriting history.
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

## Open questions

`docs/00_concept/040_open-questions.md` is the register of things not yet resolved.
Adding to it is a contribution. Answering one is a contribution that ends in an ADR.
