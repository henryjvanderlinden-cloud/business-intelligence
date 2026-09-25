# nsdn — Handover 04: the canon was checked, the author corrected the check, and the capabilities are separate
## Written 2026-09-20 at the close of session 04; revised 2026-09-21 after the author's review

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect HEAD at the commit recording the author's review, on top
   of `cb8647a`.
2. `python tools/check_repo.py` — must pass before anything is changed. Expect 54 rows, all
   live, and 10 ADRs.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority on
   what is open; this handover is orientation only, and where the two disagree the register
   wins.
4. Then [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md),
   [ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md), and the author's review block
   at the end of `ARC-OP-14`.

## Outstanding actions for the author, not the model

**Pushing is the author's, and it happens.** The claim carried in Handovers 01–04 that the
repository had never been pushed was false and has been removed; the author pushes from
`C:\Git\business-intelligence`, and on 2026-09-21 local `main` tracked `origin/main` with
nothing ahead. These sessions hold no GitHub credentials and cannot verify the remote
directly.

**`CON-OP-15`, what success means for each capability.** Partly answered by ADR-0009; the
rest is still his to rule.

## Where the project stands

Ten ADRs settled. Fifty register rows live. **The second faculty is named: the agentic
layer** ([ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md)), with *agent* for a unit
of work inside it. The three faculties are the deterministic machinery, the agentic layer, and
the human faculty.

Session 04 checked seven claims in
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
against sources, in
[2026-09-20-canon-survey.md](../docs/30_research/notes/2026-09-20-canon-survey.md). The next
day the author reviewed the findings, and on three of the four points where he disagreed,
**practice outranked the literature**. What stands after his review:

**The capabilities are separate, and no link between them is owed.** ADR-0009 rules it:
the manifesto presents what the system does as separate capabilities — building known designs
cheaply, and proposing meaning (keys, identity, metadata) for people to rule on — with room
for more value areas: monitoring, troubleshooting, regression testing and a test framework,
and continuous improvement of methodology and metadata. Links are mentioned where they exist
and matter. `CON-OP-8` is ruled, and the whole interaction question is closed.

**The best case for cheap building is the projection from vault to marts.** The author's
mature architecture is layered — raw data, a Data Vault for complete record keeping, and
dimensional marts for self-service — and the record-keeping layers are never exposed as they
are. Building and maintaining the projection between the layers is the expensive hand work.
Rule versioning is the other strong case, because in practice rules live in the warehouse
and nothing versions them there.

**The best case for the metadata capability is the failure of human-made metadata.**
Catalogue implementations fail because people tire and lose context; generators like
WhereScape are only as good as the metadata they are fed. `ARC-OP-23` holds the caveat:
tireless generation helps most where the output can be checked mechanically, and least
where only a person can say whether a meaning is right.

**Corrections to the survey.** *Almost unused* stands for Anchor. Kimball is not a cost-side
rejection but the design that won on human cost — and the features skipped inside Kimball
are better evidence for cheap building than whole methods the canon rejected. The join
question is mostly beside the point, because join cost is paid when marts load;
`ARC-OP-22` survives only for trusted-but-unenforced keys on the marts themselves, and
`EVI-OP-6` is demoted.

## Task for the next session, in one sentence

*Revised 2026-09-21 on the author's direction; the previous task is below it, not deleted.*

Take the author's row-by-row reaction to
[070_task-allocation.md](../docs/00_concept/070_task-allocation.md) and revise the table with
him — slowly, per `ARC-OP-24`.

The draft has 43 tasks as chains (proposes, decides, executes, checks). It has been through two
external reviews, sol on 2026-09-21 and GPT-6 Astra on 2026-09-24, and the author accepted every
finding of both; rows 41–43, added on 2026-09-25, are unreviewed. It added a fourteenth
dimension to 060, *creating commitment*.

**The context system was designed on 2026-09-25**, and the author called it one of the key
factors for success. [120](../docs/10_architecture/120_context-layer.md) now distinguishes six
kinds of context and proposes one store with two views; five new documents follow it —
[122](../docs/10_architecture/122_context-retrieval.md) retrieval,
[124](../docs/10_architecture/124_context-write-back.md) write-back,
[126](../docs/10_architecture/126_context-gardening.md) gardening, which the author singled out,
[127](../docs/10_architecture/127_temporal-behaviour.md) temporal behaviour and
[128](../docs/10_architecture/128_join-knowledge.md) join knowledge. `ARC-OP-25` to `ARC-OP-27`
hold what is open. All six documents were reviewed the same day — astra on 120, 124 and 126,
sol on 122, 127 and 128 — and every finding was integrated; a crossed second pass followed.

## Why that task and not another

The author's words, 2026-09-21: the manifesto *"is just a start, and a working document"*;
*"the cost calculation depends on the entire methodology"*; the central bet *"hasn't been
settled yet. Let's be slow to settle. I want to get the conceptual framework first."* The
task-by-faculty allocation is that framework. It also gives `060`'s allocation rule
something to allocate, which it has never had.

## Previous task, superseded 2026-09-21

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III as
separate capabilities per ADR-0009 — building and metadata first, with room for more — against
`CON-OP-5`, `CON-OP-6`, `CON-OP-7`, `CON-OP-11` and `CON-OP-4`, executing `CON-OP-9`'s rename
to *faculties* and *the agentic layer* in the same pass, with the check ADR-0008 deferred.

Four handovers have named it. ADR-0009 removed the obstacle that kept moving and ADR-0010
removed the last blocker; nothing now stands in its way. `CON-OP-2` — the break-even in
columns, from published token prices — is five handovers deferred and remains the cheapest
decisive number in the register; do it next, or first if the rewrite is expected to run
long.

## Traps and warnings

**Cross-model review transport changed on 2026-09-22.** Codex 0.154.0 removed
`codex mcp-server`, which is how Claude desktop reaches sol and Astra. Claude desktop's codex
entry now points at a pinned 0.153 copy in `C:\Tools\codex-0153` — do not upgrade it. Its
helper programs must be named without the platform suffix (`codex-code-mode-host.exe`, not
`codex-code-mode-host-x86_64-pc-windows-msvc.exe`); since that was fixed on 2026-09-25,
reviewers can read repository files themselves. Keep to one file per question to stay under
the bridge's sixty-second ceiling. Model ids are `gpt-5.6-sol` and `gpt-6-astra`. When 0.153 stops being accepted, the
durable fix is a small bridge that runs `codex exec`; nothing is built.

**Check claims before carrying them.** The "never pushed" line survived four handovers and
a direct statement to the author without anyone running `git status -sb`. A handover is
orientation, not evidence; verify anything checkable before repeating it.

**Do not run ahead of the author.** On 2026-09-21 he said the model was moving too fast.
Propose, let him react, and write into the repository only what he has settled.

**Ask what practice does before reasoning from literature about how BI is done.** Session
04's survey was sourced and careful, and the author corrected it on Anchor adoption, Kimball's
role and the join question in one message. The literature describes methods; the author knows
which parts get implemented.

**This is not an academic paper.** The author's words in ADR-0009. The §III rewrite states
capabilities and the evidence for each; it does not anticipate every objection or argue
links for their own sake.

**The single-axis error was committed again in session 04.** An interaction candidate counted
tables where the quantity that matters is real business entities. For any quantity a claim
says scales, ask what else would have to scale with it, and whether they are the same thing.

**Naming a value area is not evidencing it.** ADR-0009 leaves the list open. Every area added
is one more claim that needs its own evidence.

**The falsifiable core is still unreviewed after five passes** — that business keys are
machine-proposable at a precision worth a person's time. `ARC-OP-23`'s uncheckable half is
the same question in another form.

**Git mechanics.** Deletion in the connected folder is off by default, so git leaves
`.git/index.lock` behind and the next commit fails. Request delete permission for the folder,
remove the lock, and retry.

**Do not reword the mission statement to absorb findings.** It was annotated instead, on
purpose; four of six versions were refused and guards have twice been lost to rewrites for
cadence.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(`ARC-OP-19`, `ARC-OP-22` and `ARC-OP-23` extend the tiering; none reopens it.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
  *(The second faculty is the agentic layer — [ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md).)*
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).
- **Separate capabilities, open list, no interaction owed** — [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md).
  Do not draft interaction candidates; two were refuted and the obligation is gone.
- **The amortisation-threshold synthesis.** `CON-OP-11` failed; its 6NF counterexample and
  the words *almost unused* both stand.
- **Kimball as a cost-side rejection.** Struck. Kimball as the design that won on human cost
  is live and is the better example.
- **The obstacle taxonomy.** Authoring versus runtime versus comprehensibility is where
  lifecycle work lands, not a classification of obstacles.

## What session 04 did not do

Did not execute the §III rewrite. Did not read Date, Darwen and Lorentzos, or Linstedt and
Olschimke. Did not price anything for `CON-OP-2`. Did not attempt `ARC-OP-14`'s second half,
which should now start from the features skipped inside Kimball and from the vault-to-mart
projection. The survey's findings were reviewed by the author but not by another model.
