# nsdn — Handover 04: the canon was checked, the author corrected the check, and the capabilities are separate
## Written 2026-09-20 at the close of session 04; revised 2026-09-21 after the author's review

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect HEAD at the commit recording the author's review, on top
   of `cb8647a`.
2. `python tools/check_repo.py` — must pass before anything is changed. Expect 50 rows, all
   live, and 9 ADRs.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority on
   what is open; this handover is orientation only, and where the two disagree the register
   wins.
4. Then [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md),
   `CON-OP-10`, and the author's review block at the end of `ARC-OP-14`.

## Outstanding actions for the author, not the model

**The repository has still never been pushed.** `origin` is configured to
`https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the repository does
not exist on GitHub, and these sessions hold no credentials. The author creates the empty
repository — no README, no .gitignore, no licence — and runs `git push -u origin main` from
`C:\Git\business-intelligence`.

**`CON-OP-10`, the second faculty's name.** The author proposed *agents* or *agentic* on
2026-09-21; the row records the proposal and what a ruling should state. It is one word, it
is his, and it blocks the rename.

**`CON-OP-15`, what success means for each capability.** Partly answered by ADR-0009; the
rest is still his to rule.

## Where the project stands

Nine ADRs settled. Fifty register rows live.

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

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III as
separate capabilities per ADR-0009 — building and metadata first, with room for more — against
`CON-OP-5`, `CON-OP-6`, `CON-OP-7`, `CON-OP-11` and `CON-OP-4`, executing `CON-OP-9`'s rename
with the name the author rules in `CON-OP-10`.

## Why that task and not another

Four handovers have named it, and ADR-0009 removed the obstacle that kept moving. The only
thing left in its way is the name, which is the author's single word. **If the name is not
ruled, do `CON-OP-2` instead** — the break-even in columns, from published token prices — now
five handovers deferred and still the cheapest decisive number in the register.

## Traps and warnings

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
  *(The second faculty's own name is `CON-OP-10` and is open.)*
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
projection. The survey's findings were reviewed by the author but not by another model. Did
not push.
