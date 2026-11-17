# nsdn — working title: *neural synaptic data network*

A design repository for an agent-driven system that discovers, models, connects and
exploits the data landscape of an organisation with a high degree of autonomy.

The argument in one paragraph is in
[`docs/00_concept/005_manifesto.md`](docs/00_concept/005_manifesto.md). The premise:
building a data environment decomposes into a **deterministic** half
(data logistics — capture, movement, materialisation, scheduling) and a **contextual**
half (what the data means, how sets relate, which questions are worth asking, whether
an answer is still true). The deterministic half is already automated to a large
degree. The contextual half has always been the bottleneck, because it required a
scarce human who understood both the systems and the business. Language models are the
first tooling that can carry a meaningful share of that second half.

This repository began by **organising the thinking** before any component was built: prose first, then
specifications, then code. It now holds working prototypes as well, each adopted by an ADR.

## Status

*Updated 2026-11-17, session 13.* Formally still Phase 0 of
[`400`](docs/40_roadmap/400_phasing.md) (Mode 1 of [ADR-0006](docs/20_decisions/0006-project-mode.md)): the gate into
the next phase is a decision taken on a date, and it has not been taken. In practice the Wide World Importers sandbox
has gone further:

- **Built and running daily on the author's machine:** a simulated SQL Server source and its daily full extracts; the
  analysis record of its 31 tables ([`analysis/`](analysis/README.md)); the raw vault declared as text
  ([`model/`](model/README.md)) and generated as plain SQL by the vault generator
  ([`prototypes/vault_generator/`](prototypes/vault_generator/README.md)), 216 tables loaded into DuckDB by the
  runner, with 777 tests per load; a schema viewer; a PostgreSQL catalogue pass for a client database. Since
  2026-11-16, one thin slice on top of it ([141](docs/10_architecture/141_the-first-slice-business-vault-and-mart.md),
  ADR-0039, ADR-0040): a generated business vault, one mart and one analysis of sales by customer segment, with 39
  more tests per load, the decision register's first entry ([`registers/decisions/`](registers/decisions/README.md))
  and the first findings note ([`findings/`](findings/README.md)).
- **Not built:** any mart beyond that slice, calculation engines, the agent layer beyond a chat session and conventions, the
  adjudication queue. The falsifiable core of [`410`](docs/40_roadmap/410_first-vertical-slice.md), whether business
  keys and entity identity across sources can be machine-proposed, is untested: Wide World Importers is one clean
  source.

Nothing is decided that an ADR cannot reverse. The latest state is always in
[`handovers/CURRENT.md`](handovers/CURRENT.md).

## How to read this repository

| Start here | For |
| --- | --- |
| [`handovers/CURRENT.md`](handovers/CURRENT.md) | **A fresh session starts here** — state, task, traps, what not to reopen |
| [`registers/OPEN_POINTS.md`](registers/OPEN_POINTS.md) | The authoritative answer to *what is open?* |
| [`docs/00_concept/001_mission.md`](docs/00_concept/001_mission.md) | What the project is for — the author's end game, and the four parts of it that are not yet true |
| [`docs/00_concept/002_mission-statement.md`](docs/00_concept/002_mission-statement.md) | **The mission in one paragraph** — a living document, with a changelog of what was cut |
| [`docs/00_concept/005_manifesto.md`](docs/00_concept/005_manifesto.md) | **The argument, stated plainly** — what changes when a third component arrives |
| [`docs/00_concept/060_faculty-inventory.md`](docs/00_concept/060_faculty-inventory.md) | The three faculties compared on common dimensions, for deciding which gets which work |
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
docs/00_concept/       Mission, manifesto, original brief, critique, glossary, prior art,
                       faculty inventory
docs/10_architecture/  How the system is meant to work
docs/20_decisions/     Architecture decision records (ADRs)
docs/30_research/      Prior art notes, tool evaluations, external review passes
docs/40_roadmap/       Phasing and the first vertical slice
docs/50_process/       How the work is conducted: method, external review, record keeping
docs/60_domain-knowledge/  Findings per industry, for future reference
analysis/              The analysis record: per-table claims with evidence and confidence
model/                 The raw vault declared as text, read by the generator and the viewer
records/               The step log, sessions, audits, assets and sources
tools/                 Mechanical checks — `python tools/check_repo.py`
spec/                  Machine-readable contracts (JSON Schema) for catalog artifacts
prototypes/            Code that answers one question; the WWI sandbox and the vault generator run from here
tests/                 Tests for anything that graduates out of prototypes/
data/, scratch/        Not in git: extracts and the warehouse; working files
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
