# 070 — Task allocation: which faculty does what in a BI implementation

**Status: working draft.** Endorsed by the author on 2026-09-21 as "what we are going for",
and deliberately not settled. The author's instruction for this document is to be slow to
settle it.

This document lists the tasks a Business Intelligence implementation involves, and for each
one says which faculty should do which step. It is the practical counterpart to
[060_faculty-inventory.md](060_faculty-inventory.md). That document says what each faculty is
good and bad at; this one applies it to real work.

The three faculties are the ones ruled in
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md) and
[ADR-0010](../20_decisions/0010-the-agentic-layer.md):

- **D**: deterministic machinery (SQL engines, ETL, schedulers, test runners). Models never
  operate in the data path ([ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md)).
- **A**: the agentic layer (LLMs plus a heartbeat, workflows, documented procedures and memory).
- **H**: humans.

## How it was made

The model drafted 28 tasks on 2026-09-21. External review on gpt-5.6-sol added fourteen
omissions and splits, disputed seven allocations, recommended the chain format used below,
and proposed a fourteenth dimension. The author agreed with all of it the same evening. The
review is recorded in
[XREV_2026-09-21_task-allocation_sol](../30_research/notes/XREV_2026-09-21_task-allocation_sol.md).

A second review, on GPT-6 Astra on 2026-09-24, found three further problems and tested the
patterns at the end of this document: a missing task (row 37), a missing check (row 34),
generation given to the wrong faculty (row 17), an overstated pattern, an unproven one, and a
runbook named as though it were a faculty (row 31). The author accepted all of it. The review
is recorded in [XREV_2026-09-24_task-allocation_astra](../30_research/notes/XREV_2026-09-24_task-allocation_astra.md).

## How to read the table

Each task is a **chain** rather than a single owner: who **proposes**, who **decides**, who
**executes**, and who **checks**. The **lead** is whoever decides; where nobody decides
because the task is purely mechanical, the lead is D.

A one-owner table hides too much. Take "testing": people define what counts as acceptable,
the agentic layer writes the cases, machinery runs them, and people accept any material
discrepancy. Under one owner that becomes "testing — agentic", which is wrong in three
places out of four.

Several of the reviewer's proposed splits are exactly a chain. Dashboards are an example:
the design decisions are human, the build is agentic, and refresh is deterministic. Those are
represented by the columns rather than as separate rows. Where a split separates genuinely
different work, it gets its own row. Source ownership and source extraction are an example.

**Why** gives the dimensions from [060](060_faculty-inventory.md) that decide the allocation:

1 how much must be spelled out · 2 cost and speed per run · 3 same answer every time ·
4 how it goes wrong · 5 cost of checking the work · 6 whether a mistake can be undone ·
7 what it knows and keeps in mind · 8 what it can see, including meetings, politics and the
unwritten · 9 whether it can settle a dispute between people · 10 whether it can handle the
never-seen-before · 11 whether it scales · 12 whether it notices the world changed ·
13 what it is allowed to do (mandate) · **14 whether it can create commitment** (new; see
below)

## The table

| # | Task | Proposes | Decides | Executes | Checks | Why |
|---|---|---|---|---|---|---|
| | **Business** | | | | | |
| 1 | Find out what the business needs | H elicits; A structures and drafts | H | — | H | 8, 13 |
| 2 | Acceptance criteria and business sign-off | A drafts | H | — | H | 13 |
| 3 | Agree KPI definitions, e.g. *net revenue* | A surfaces conflicts, drafts options | H | D encodes | H | 9 |
| 4 | Prioritise scope | A drafts options and estimates | H | — | H | 13 |
| 5 | Data contracts, SLAs, source-owner responsibilities | A drafts | H | D monitors | D flags; H enforces | 13 |
| | **Sources** | | | | | |
| 6 | Source ownership and authority: which source is the real one, shadow systems, politics | H; A prompts from scans | H | — | H | 8 |
| 7 | Connectivity, extraction, change data capture, ingestion | A configures | H grants access | D | D | 3 |
| 8 | Profile the data | — | — | D | D | 2, 3 |
| 9 | Business keys and cross-source matching ⚠ | A | H | D implements | D evidence, then H | 10, 5 |
| 10 | Technical metadata: harvesting, lineage capture, schema comparison, catalogue sync | — | — | D | D | 12, 3 |
| 11 | Business metadata: descriptions, near-duplicates, hygiene, ambiguity flags | A | H rules on meaning | A writes to catalogue | D where checkable; H otherwise | 4, 7 |
| 12 | Master and reference data stewardship, survivorship rules | A drafts candidate rules | H | D | H | 9 |
| 13 | Data-quality rules: define, run, quarantine | A drafts from profiles | H defines | D runs and quarantines | D | 8, 3 |
| | **Design** | | | | | |
| 14 | High-level architecture: layers, platform | A drafts options | H | — | H | 6, 13 |
| 15 | Historisation and grain choices | A recommends | H | — | H | 13 |
| 16 | Detailed model from the high-level design plus metadata | A | H reviews | D deploys | D | 7, 11 |
| | **Build** | | | | | |
| 17 | Generate code: DDL, load logic, vault-to-mart projection | D instantiates approved templates where metadata fully determines the output; A writes only what the templates cannot express | H approves the meaning of A's additions | D | D via tests | 1, 3 |
| 18 | Load and transformation runs | — | — | D | D | 3, 6 |
| 19 | Orchestration: dependencies, retry policy, recovery paths, backfills | A designs | H approves the policy; routine runs follow it | D runs the schedule | D | 10, 3 |
| 20 | Deployment: versioning, CI/CD, environment promotion, rollback | A writes pipelines | H for production | D | D | 6 |
| 21 | Performance engineering and capacity planning | A diagnoses and proposes | H | D benchmarks | D | 10, 3 |
| | **Test** | | | | | |
| 22 | Write tests and a regression suite | A writes | H, against row 2 | D runs | D | 11, 3 |
| 23 | Reconciliation: source, vault, marts, Finance, legacy outputs | A explains gaps | H accepts discrepancies | D | D | 5, 13 |
| 24 | Check the numbers against business reality | A prepares | H | — | H | 8, 9 |
| | **Deliver** | | | | | |
| 25 | Marts, physical implementation | A generates | H approves | D | D | 1 |
| 26 | Semantic layer: which measures, relationships, defaults and perspectives users see; then its implementation | A drafts and generates | H | D | D | 8, 13, 1 |
| 27 | Dashboards and reports: audience, questions, interaction and visual choices; build; refresh | A builds | H decides audience, questions, visuals | D refreshes and renders | H | 8, 1, 3 |
| 28 | Documentation and training material | A writes and keeps current | H | — | H | 12 |
| 29 | User acceptance, adoption, retiring legacy reports | A analyses usage, drafts migration plans | H | H | H | 14, 8 |
| | **Run** | | | | | |
| 30 | Monitor loads, quality and anomalies | D detects; A explains, prompted by the heartbeat | H when action is needed | D | D | 12 |
| 31 | Troubleshooting | A diagnoses | Routine cases under an H-approved runbook: D where its conditions are coded, A where an agent applies it; H for consequential or contested cases | D | D | 10, 3, 13 |
| 32 | Operational recovery: retries, replay, backfill, disaster recovery | A plans | H when consequential | D | D | 6 |
| 33 | Source schema drift | D detects; A proposes the adaptation | Non-breaking changes under H-approved rules; H for breaking changes | D | D | 12, 6 |
| | **Change and govern** | | | | | |
| 34 | Impact analysis of a change | D from lineage, dependencies and query logs; A interprets gaps and business consequences | H | — | D verifies how far recorded dependencies reach; H confirms the affected business uses, including exports and manual reports lineage cannot see | 3, 5 |
| 35 | Approve production changes, especially destructive ones | A prepares | H | D | D | 6, 13 |
| 36 | Access, privacy, legal basis | A drafts | H | D enforces | D | 13 |
| 37 | Retention, erasure and controlled historical correction across raw data, vault, marts and backups | A plans the implementation: which records, which layers | H decides policy and exceptions | D executes and verifies it reached every layer | H checks policy compliance | 6, 13 |
| 38 | Improve the methodology over time | A detects recurring friction, drafts improvements | H leads | — | H | 13 |
| | **Use** | | | | | |
| 39 | Ad-hoc analysis | A generates hypotheses | H interprets and communicates | D retrieves and calculates | H | 10, 3, 8 |
| 40 | Turn insights into action | A may draft options | H | H | H | 13, 9, 6, 14 |

⚠ Row 9 is the project's unsettled central bet: that the agentic layer can propose business
keys accurately enough to be worth a person's time to check.

## The fourteenth dimension: creating commitment

Proposed by the reviewer and accepted by the author. It is the ability to gain trust, change
behaviour, negotiate adoption, and get people to give up familiar reports or processes.

It is not dimension 8, because seeing the politics is not the same as persuading people. It
is not dimension 13 either, because having the mandate does not guarantee adoption. It passes
[060](060_faculty-inventory.md)'s test for a dimension because it flips an allocation. Without
it, most of row 29 would go to the agentic layer, which can write the training material,
analyse usage and draft the migration plan. With it, the lead goes to humans.

**D:** none. **A:** can prepare the case, but has no standing that makes people commit.
**H:** the only faculty that can, and only a person the others trust.

## What the table shows so far

These patterns are observations, not rulings.

- **D executes almost everything that runs on data**, and checks almost everything that can be
  checked mechanically.
- **A mostly writes and explains.** It drafts code, metadata, tests, documentation and options,
  and it diagnoses problems. It proposes far more often than it decides, and it never decides
  anything that is consequential or contested.
- **H decides contested meaning, commitments and consequential exceptions; routine decisions
  may follow H-approved rules** (rows 19, 31, 33), and H checks wherever the only check is
  judgement. *Revised after the second review:* approving a procedure is not the same as
  deciding each case under it.
- **A runbook is an artifact, not a faculty.** Whoever applies it decides: D where its
  conditions are coded, A where an agent interprets it, H where a person does. A row that
  names a runbook must say which.
- **Where a template fully determines the output, D should generate it, not A** (row 17).
  That suggests the agentic layer's larger job is writing and maintaining the templates and
  rules that deterministic machinery then runs, rather than producing each output itself.
  Rows 16, 25 and 26 may deserve the same split; not yet examined.
- **Handoffs may be where cost sits — a hypothesis, not a finding.** The rows show where
  faculties hand work to each other; whether those handoffs dominate cost needs their
  procedures, frequency and review effort described, and none of that exists yet.
- **Erasure and correction constrain history-keeping** (row 37). "All the data, all the time"
  in the vault has to coexist with obligations to delete or correct, and that tension has to
  be settled in the historisation design (row 15), not discovered afterwards.

## Open

This list is not complete, and its grain has not been tested against a real implementation.
The author has not yet given his own reaction to the individual rows. Two external reviews are
done, on sol and on Astra. `ARC-OP-24` holds the status.
