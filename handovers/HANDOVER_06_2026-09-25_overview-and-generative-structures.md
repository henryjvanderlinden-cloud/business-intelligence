# nsdn — Handover 06: the overview was drawn, and the author's political theory turned out to describe warehouse decay
## Written 2026-09-25 at the close of session 05

> **STATUS: HISTORICAL (superseded 2026-09-26 by [HANDOVER_07](HANDOVER_07_2026-09-26_first-sandbox-steps.md)).**

---

## First actions

1. `git log --oneline -12` — expect HEAD at the commit that wrote this handover, on top of
   `22e7930`.
2. `python tools/check_repo.py` — must pass before anything is changed. Expect 57 register rows,
   all live, and 13 ADRs.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md) rows `CON-OP-16` and
   `CON-OP-17`, which are new, and [ADR-0013](../docs/20_decisions/0013-data-vault-or-equivalent.md).
   The register is the authority on what is open; this handover is orientation only.
4. For the whole framework on one page, open
   [080](../docs/00_concept/080_overview-for-discussion.md) at its last section and its schematic,
   [080_overview-schematic.svg](../docs/00_concept/080_overview-schematic.svg).

## Outstanding actions for the author, not the model

**Push.** Sixteen or more commits from this session are local only. The author pushes from
`C:\Git\business-intelligence`; these sessions hold no GitHub credentials.

**Rule `CON-OP-16`**: is maintenance effort per stable unit of landscape, with burden indicators
held steady, *the* success criterion, *a* criterion, or a diagnostic? **Rule `CON-OP-17`**: whether
cheaper building's savings may all go to more building. **`CON-OP-15`** remains his.

**React to the task table row by row** ([070](../docs/00_concept/070_task-allocation.md)), still
simmering from session 04.

## How to work with the author

**Plain English, numbered.** Findings in conversation are plain language and numbered so he can point
at items. He is an expert in BI; dense academic prose is hard for him to react to. Repository
documents can be fuller.

**Propose, let him react, write what he settles.** Draft in the conversation; have sol and astra
review, in parallel on different questions; show him the findings in plain English with a
recommendation per finding; integrate what he accepts; record rulings as ADRs. This session ran that
loop three times and he was content with it each time.

**Quote him verbatim.** Rulings and reactions are recorded word for word, in ADRs, review-note
dispositions and annotations.

**He reads the schematic himself.** He is its main audience and finds it readable; do not simplify it
unasked.

## What session 05 did

**080 brought up to date, and the SVG drawn.** Twelve main points replace the nine of 2026-09-24,
which are kept above them; points 7 (context system) and 8 (adjudication economy) are separate and
load-bearing by the author's ruling. The schematic is
[080_overview-schematic.svg](../docs/00_concept/080_overview-schematic.svg). Reviewed by sol (points)
and astra (picture); thirteen of fourteen findings integrated. Points are phrased as what the framework
*would* do, per rule 9 of [AGENTS.md](../AGENTS.md).

**ADR-0013: Data Vault or a functionally equivalent layer.** The author: Data Vault is the example,
"but I'd be hard pressed to find another". Equivalence is tested by three properties: all data, all
history (insert-only), integrated on business keys. A persistent staging area alone fails the third.

**The author's *Generative Structures* paper mapped onto nsdn.** GS (compendium folder 130, v004)
argues that capability and burden are coupled and that maintenance draws on the same budget as
growth, so a growing stack's upkeep eventually exhausts its budget. That is the life cycle of a data
warehouse. The mapping is
[2026-09-25-generative-structures-mapping](../docs/30_research/notes/2026-09-25-generative-structures-mapping.md),
reviewed by astra (the model) and sol (practice), with all findings integrated as annotations. It
produced `CON-OP-16` (a success measure) and `CON-OP-17` (how savings are spent).

## Task for the next session, in one sentence

Begin the candidate dataset survey, `EVI-OP-2`, for the first sandbox — now with a second
requirement besides shared entities: the sources must let a landscape grow source by source, so that
maintenance per stable unit can be measured as it grows (`CON-OP-16`).

## Why that task and not another

The framework is on one page and has been reviewed; ADR-0012 makes a sandbox on open data the next
step, and the survey needs no code. `CON-OP-16` now gives the sandbox something measurable beyond the
business-key bet, which sharpens what the survey is looking for.

The alternatives, in order, if the author prefers: take his rulings on `CON-OP-16` and `CON-OP-17`;
his row-by-row reaction to 070; price `CON-OP-2`.

## Traps and warnings

**The maintenance share alone is not a measure.** It measures spending, not adequacy, and is broken
outright in organisations by relabelling, rebuild resets, deferred maintenance and displaced effort.
Use the restated form in `CON-OP-16`, with its guards.

**Cheaper building does not lower the threshold.** In GS's model it only brings it nearer if savings
go to building more. Do not repeat the unconditional "cheaper building accelerates collapse" claim;
it was corrected.

**GS's architecture points are prose, not model.** The case for modular stacks rests on Simon and
Perrow as GS cites them; the equations contain no topology.

**Do not draft interaction candidates between value areas.** `CON-OP-17` was narrowed away from
ADR-0009; leave it as a question about allocation until the author rules.

**The compendium is a separate repository with its own conventions.** Access to
`C:\Git\compendium\papers\130_GS` was granted for this session only, read-only in practice. Do not
edit compendium files from this project.

**Cross-model review transport.** Unchanged from handover 05: Claude desktop reaches sol and astra
through a pinned Codex 0.153 in `C:\Tools\codex-0153`; do not upgrade it. One file per question keeps
passes under the bridge's time limit; sol and astra in parallel on different objects worked every
time this session. Model ids: `gpt-5.6-sol`, `gpt-6-astra` with `model_reasoning_effort` medium.

**Git mechanics.** Deletion in the connected folder is off by default and lapses when a session
restarts, so a stale `.git/index.lock` blocks the next commit. Request delete permission for the
folder, remove the lock, retry.

**The falsifiable core is still unreviewed** — that business keys are machine-proposable at a
precision worth a person's time. The author's conviction is the premise, not the evidence
(ADR-0012).

**Do not reword the mission statement to absorb findings.** Annotate it.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
- Separate capabilities, open list, no interaction owed — [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md).
- The second faculty is the agentic layer — [ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md).
- Assertions are the core record; one identity plane over separate stores; a publication gate —
  [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md).
- A generic framework; every implementation starts lean — [ADR-0012](../docs/20_decisions/0012-generic-framework-lean-start.md).
- Data Vault or a functionally equivalent layer, by the three-property test — [ADR-0013](../docs/20_decisions/0013-data-vault-or-equivalent.md).
- Points 7 and 8 of the overview stay separate; the adjudication band stays between humans and the
  agentic layer in the schematic — the author's rulings, recorded in 080.
- Seeded checks in adjudication stay, blinded and excluded from all estimates — recorded in
  [155](../docs/10_architecture/155_adjudication-economy.md).
- Do not review the context system on paper again; its next test is a sandbox.
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).

## What session 05 did not do

Did not start `EVI-OP-2` or any sandbox. Did not rule `CON-OP-15`, `CON-OP-16` or `CON-OP-17`. Did not
review rows 41–44 of 070. Did not decide the physical medium for assertions (`ARC-OP-7`). Did not price
anything for `CON-OP-2`. Did not draw a stripped presentation version of the schematic. Nothing was
built and no data was touched.
