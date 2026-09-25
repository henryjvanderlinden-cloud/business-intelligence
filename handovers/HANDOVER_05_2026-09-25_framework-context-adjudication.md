# nsdn — Handover 05: the framework took shape — task allocation, the context system, the adjudication economy
## Written 2026-09-25 at the close of session 04, which ran from 2026-09-20 to 2026-09-25

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect HEAD at the commit that wrote this handover, on top of
   `77d49de`.
2. `python tools/check_repo.py` — must pass before anything is changed. Expect 55 register rows,
   all live, and 12 ADRs.
3. Read [ADR-0012](../docs/20_decisions/0012-generic-framework-lean-start.md) first. It says what
   kind of thing this repository is now building: a generic framework, developed first, tested
   later in sandboxes on open data, with every implementation starting lean.
4. Then [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority on what
   is open; this handover is orientation only, and where the two disagree the register wins.
5. Then, for orientation: [070](../docs/00_concept/070_task-allocation.md) (who does what),
   [120](../docs/10_architecture/120_context-layer.md) (the context system) and
   [155](../docs/10_architecture/155_adjudication-economy.md) (the review queue).

## Outstanding actions for the author, not the model

**Push.** Seven or more commits from this session are local only. The author pushes from
`C:\Git\business-intelligence`; these sessions hold no GitHub credentials.

**React to the task table, row by row.** [070](../docs/00_concept/070_task-allocation.md) has 44
rows. The author endorsed its direction and accepted every review finding, but has not yet given
his own reaction to individual rows. He asked for time to let it simmer.

**`CON-OP-15`, what success means for each capability.** Still his to rule.

## How to work with the author

**Plain English, numbered.** In conversation the author wants findings in plain language, numbered
so he can point at items. He is an expert in BI and finds dense academic prose hard to react to.
Documents in the repository can be fuller, but the conversation is where he decides.

**Propose, let him react, write what he settles.** On 2026-09-21 he said the model was moving too
fast. The pattern that worked since: draft in the conversation, have sol and astra review, show
him the findings in plain English, integrate what he accepts, record rulings as ADRs.

**Practice outranks literature on how BI is actually done.** He corrected a sourced survey on three
points in one message. Ask what practice does.

**Quote him verbatim.** His own formulations are recorded word for word in the documents that grew
from them; keep them so.

## Where the project stands

Twelve ADRs. Fifty-five register rows, all live. Nothing is built; no data has been touched.

**The faculties and the capabilities are settled.** Three faculties — deterministic machinery, the
agentic layer ([ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md)), humans — act on data.
The manifesto presents separate capabilities with an open list of value areas and owes no link
between them ([ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md)).

**The task allocation exists.** [070](../docs/00_concept/070_task-allocation.md) lists 44 BI tasks as
chains — who proposes, decides, executes and checks — with reasons from the fourteen dimensions of
[060](../docs/00_concept/060_faculty-inventory.md). Rows 1–40 have had two external reviews; rows
41–44 have had none. `ARC-OP-24`.

**The context system is designed and has had two reviews.** [120](../docs/10_architecture/120_context-layer.md)
with [122](../docs/10_architecture/122_context-retrieval.md) retrieval,
[124](../docs/10_architecture/124_context-write-back.md) write-back,
[126](../docs/10_architecture/126_context-gardening.md) gardening,
[127](../docs/10_architecture/127_temporal-behaviour.md) temporal behaviour and
[128](../docs/10_architecture/128_join-knowledge.md) join knowledge — the last two from the author's
own practice. [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md)
rules its shape: assertions are the core record and cards are views of them; one identity plane over
separate stores; a publication gate. `ARC-OP-7` (physical medium, still open) and `ARC-OP-25` to
`ARC-OP-27`.

**The adjudication economy is designed and has had one review.**
[155](../docs/10_architecture/155_adjudication-economy.md): human attention as a fixed budget spent on
loss averted per minute, four lanes, levers, a control loop, the adjudication record and monitoring
workflows, and three implementation stages. `ARC-OP-28`.

**An overview for discussing the project with others** is stored verbatim as
[080](../docs/00_concept/080_overview-for-discussion.md): nine main points and an ASCII sketch of a
layered schematic. **It predates the context system and the adjudication economy**, and the SVG the
author asked for has not been drawn.

## Task for the next session, in one sentence

Bring [080](../docs/00_concept/080_overview-for-discussion.md)'s main points up to date with what was
decided since — the context system and the adjudication economy above all — and draw the SVG
schematic the author asked for, for discussing the framework with others.

## Why that task and not another

The author asked for the schematic on 2026-09-24 and it is the one requested deliverable still
undelivered. It is also the cheapest check that the framework hangs together: if its main points
cannot be drawn on one page, something is not yet understood.

The alternatives, in order, if the author prefers: take his row-by-row reaction to 070 when he is
ready; begin preparing the first sandbox — the candidate dataset survey `EVI-OP-2` — which
ADR-0012 now makes the next step after the framework; or price `CON-OP-2`, now joined by the weekly
budget report of 155 as the second number the economics need.

## Traps and warnings

**Do not review the context system on paper again.** Two rounds were done; the second was already
about implementation detail. The author agreed returns had diminished. Its next test is a sandbox.
One external review round per new document is proportionate; a second only where the first changed
the design substantially.

**Do not relitigate rigour against a lean start document by document.** ADR-0012 settles it:
framework documents describe the full design; where it matters, they end with how an implementation
grows into it in stages.

**A sandbox has no real people in it.** Anything that depends on business owners, stewards or
reviewers will be simulated there, and results must say so (ADR-0012).

**Cross-model review transport.** Codex 0.154 removed `codex mcp-server`, which is how Claude desktop
reaches sol and Astra. Claude desktop's codex entry points at a pinned copy in `C:\Tools\codex-0153`
— do not upgrade it. Its helper programs must be named without the platform suffix
(`codex-code-mode-host.exe`, not `…-x86_64-pc-windows-msvc.exe`). Reviewers can read repository
files; keep to one file per question to stay under the bridge's sixty-second ceiling, and run sol
and astra in parallel on different objects. Model ids: `gpt-5.6-sol`, `gpt-6-astra` (with
`model_reasoning_effort` medium). When 0.153 stops being accepted, the durable fix is a small bridge
running `codex exec`; nothing is built.

**Git mechanics.** Deletion in the connected folder is off by default and the permission lapses when
a session restarts, so git leaves `.git/index.lock` behind and the next commit fails. Request delete
permission for the folder, remove the lock, and retry.

**Check claims before carrying them.** A false "never pushed" line survived four handovers. Verify
anything checkable before repeating it.

**The falsifiable core is still unreviewed** — that business keys are machine-proposable at a
precision worth a person's time. The author is convinced of the agentic layer's value; ADR-0012
records that as the premise, not the evidence.

**The single-axis error recurs.** For any quantity a claim says scales, ask what else would have to
scale with it, and whether they are the same thing.

**Do not reword the mission statement to absorb findings.** Annotate it; guards have twice been lost
to rewrites for cadence.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
- Separate capabilities, open list, no interaction owed — [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md).
  Do not draft interaction candidates.
- The second faculty is the agentic layer — [ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md).
- Assertions are the core record; one identity plane over separate stores; a publication gate —
  [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md).
- A generic framework; every implementation starts lean — [ADR-0012](../docs/20_decisions/0012-generic-framework-lean-start.md).
- Seeded checks in adjudication stay, blinded and excluded from all estimates — the author's ruling,
  recorded in [155](../docs/10_architecture/155_adjudication-economy.md).
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).
- *Almost unused* for Anchor, and Kimball as the design that won on human cost, not one rejected on
  it — see `CON-OP-11` and `ARC-OP-14`.

## What session 04 did not do

Did not rewrite the manifesto's §III; the author placed it behind the framework. Did not update 080
or draw the SVG. Did not review rows 41–44 of 070. Did not decide the physical medium for assertions
(`ARC-OP-7`). Did not price anything for `CON-OP-2`. Did not start the dataset survey `EVI-OP-2` or any
sandbox. Did not read Date, Darwen and Lorentzos, or Linstedt and Olschimke. Nothing was built and no
data was touched.
