# nsdn — working title: *neural synaptic data network*

A design repository for an agent-driven system that discovers, models, connects and
exploits the data landscape of an organisation with a high degree of autonomy.

The premise: building a data environment decomposes into a **deterministic** half
(data logistics — capture, movement, materialisation, scheduling) and a **contextual**
half (what the data means, how sets relate, which questions are worth asking, whether
an answer is still true). The deterministic half is already automated to a large
degree. The contextual half has always been the bottleneck, because it required a
scarce human who understood both the systems and the business. Language models are the
first tooling that can carry a meaningful share of that second half.

This repository exists, in its current phase, to **organise the thinking** before any
component is built. Prose first, then specifications, then code.

## Status

Phase 0 — concept consolidation. Nothing is built. Nothing is decided that an ADR
cannot reverse.

## How to read this repository

| Start here | For |
| --- | --- |
| [`handovers/CURRENT.md`](handovers/CURRENT.md) | **A fresh session starts here** — state, task, traps, what not to reopen |
| [`registers/OPEN_POINTS.md`](registers/OPEN_POINTS.md) | The authoritative answer to *what is open?* |
| [`docs/00_concept/010_vision.md`](docs/00_concept/010_vision.md) | The original brief, verbatim and unedited |
| [`docs/00_concept/020_critique.md`](docs/00_concept/020_critique.md) | What holds up in it, what does not, and what is missing |
| [`docs/10_architecture/100_system-overview.md`](docs/10_architecture/100_system-overview.md) | The system as currently conceived |
| [`docs/10_architecture/105_autonomy-tiers.md`](docs/10_architecture/105_autonomy-tiers.md) | The central reframing: autonomy is not uniform |
| [`docs/20_decisions/`](docs/20_decisions/) | Decision records — the authoritative log of what has been settled |
| [`docs/40_roadmap/410_first-vertical-slice.md`](docs/40_roadmap/410_first-vertical-slice.md) | What to build first |
| [`docs/50_process/500_working-method.md`](docs/50_process/500_working-method.md) | How the work itself is conducted |
| [`AGENTS.md`](AGENTS.md) | Conventions for language models working in this repository |

## Layout

```
registers/             The authoritative open-points register, and its archive
handovers/             One document per session, written for the next one
docs/00_concept/       Problem statement, critique, glossary, prior art
docs/10_architecture/  How the system is meant to work
docs/20_decisions/     Architecture decision records (ADRs)
docs/30_research/      Prior art notes, tool evaluations, external review passes
docs/40_roadmap/       Phasing and the first vertical slice
docs/50_process/       How the work is conducted: method, external review
tools/                 Mechanical checks — `python tools/check_repo.py`
spec/                  Machine-readable contracts (JSON Schema) for catalog artifacts
prototypes/            Throwaway code that answers one question
tests/                 Tests for anything that graduates out of prototypes/
```

## Conventions

- Documents are numbered so their order is stable and their filenames are citable.
  Numbers leave gaps; insert rather than renumber.
- Every substantive claim about the design belongs in a document; every *choice*
  belongs in an ADR. A document may describe an option; only an ADR adopts one.
- Nothing in `docs/` is load-bearing until an ADR references it.
- What is *open* lives in the register, never in a document and never in a conversation.
- A rule without a check is decoration. Run `python tools/check_repo.py` before
  committing.
