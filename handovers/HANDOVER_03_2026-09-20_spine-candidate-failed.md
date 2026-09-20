# nsdn — Handover 03: the candidate spine failed review, and the manifesto has two theses
## Written 2026-09-20 at the close of session 03, for a fresh session

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect head at the session 03 commits.
2. `python tools/check_repo.py` — must pass before anything is changed.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority
   on what is open; this handover is orientation only, and where the two disagree the
   register wins.
4. Read `CON-OP-8` first, then `CON-OP-11` and `CON-OP-4`. `CON-OP-8` carries the
   disposition the other two feed. Then
   [`../docs/00_concept/060_faculty-inventory.md`](../docs/00_concept/060_faculty-inventory.md)
   and [`../docs/00_concept/001_mission.md`](../docs/00_concept/001_mission.md), which are
   new and unratified. The mission's current wording is
   [`../docs/00_concept/002_mission-statement.md`](../docs/00_concept/002_mission-statement.md),
   a living document — read its changelog before rewording anything, because three
   formulations have already been refused and the reasons are recorded there.

## Outstanding action for the author, not the model

**The repository has still never been pushed.** Unchanged from Handovers 01 and 02.
`origin` is configured to
`https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the repository
does not exist on GitHub, and these sessions hold no credentials. The author creates the
empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`. Visibility remains
undecided; the reasoning favoured private until the Mode 1 gate.

**`CON-OP-15` is the author's to rule and nobody else's.** It asks what the success
criterion is. A model can sharpen it and has; ratifying it is not a model's job.

## Where the project stands

Session 03 ran two external review passes and produced two new concept documents. Eight
ADRs are settled. Forty-seven register rows are live, up from forty-five: five were
narrowed by the first pass with none opened, then `ARC-OP-21` and `CON-OP-15` were opened
by the work that followed. Nothing has been built, nothing has been verified, and no data
has been touched.

**`CON-OP-11` failed, on the repository's own evidence.** Domain size is not the axis that
explains codification; repayment is an expected-value quantity in which extension is one
multiplier among several. The counterexample came from
[`../docs/10_architecture/190_machine-authored-design-canon.md`](../docs/10_architecture/190_machine-authored-design-canon.md)
§3: Anchor-style 6NF has a discipline-wide domain and is almost unused. Maximal domain, no
adoption.

**`CON-OP-8` therefore came back live and has an answer.** The manifesto carries two
independent theses — cheap authorship of known deterministic designs, and cheap proposal
of locally situated semantic hypotheses — with humans validating and authorising both.
Neither is evidence for the other, and the cost is a manifesto with no single causal
mechanism.

**`CON-OP-4`(ii) failed and (i) turned out to be prior art.** *There is no rule to learn*
is false as stated whichever way `CON-OP-11` resolves, and Boisot's I-Space already
separates codification from abstraction some thirty years early.

**The faculty inventory is new and was reviewed the same session.** It scores the three
faculties on twelve capability dimensions plus mandate, for the purpose of allocation. The
second pass cut one dimension, added three, replaced its allocation rule outright, and
refuted the interaction candidate it offered for `CON-OP-8`. All of that is folded in;
[`../docs/30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md`](../docs/30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md)
holds what it said before.

**The mission is recorded for the first time**, verbatim from the author in 001 and as a
living statement in 002, which has been through review and is at version 0.3. Four
arguments were made against the author's formulation — that *orders of magnitude* is two claims of which only coverage
survives, that *let loose* names the failure mode the mandate structure exists to prevent,
that bundling a technology set dates the mission, and that the formulation quietly asserts
the conjunction `CON-OP-8` just separated.

## Task for the next session, in one sentence

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III
as two declared theses per `CON-OP-8`, against `CON-OP-5`, `CON-OP-6`, `CON-OP-7`,
`CON-OP-11` and `CON-OP-4`, settling `CON-OP-10`'s naming and executing `CON-OP-9`'s
rename in the same pass.

## Why that task and not another

It is the same instrument Handover 02 named, and two review passes have made it both more
urgent and much better specified. The rewrite no longer chooses a spine — that is
`CON-OP-8`'s disposition — and instead must write two theses honestly, say what the second
faculty does now that *there is no rule to learn* has gone, carry the Boisot concession,
and either argue the interaction or state its absence. `CON-OP-13`'s residual travels with
it, as before.

**`ARC-OP-14`, the canon survey, has been promoted twice over.** Under two theses it is the
half that can be evidenced without code, and the refuted interaction candidate left behind a
comparison that needs it: whether machine authorship changes the availability, coverage or
maintenance cost of validation evidence relative to an otherwise equivalent conventionally
authored warehouse. The dataset survey (`EVI-OP-2`) remains the task that makes progress
regardless of how the argument turns out, and it has now been deferred three times.

## Traps and warnings

**The same drafting error has now occurred twice in two days.** `CON-OP-11` collapsed a
multi-term expected-value calculation onto domain size; the inventory's first allocation
rule collapsed the same kind of calculation onto verifiability. Both were written by the
same model, both were refuted on the same grounds, and the second was written the day after
the first was refuted. Treat any single-axis explanation drafted here as suspect on sight.

**Boisot is unverified and a disposition rests on it.** The claim that the I-Space
anticipates articulable-but-not-general is the reviewer's, from general knowledge, under
[`../AGENTS.md`](../AGENTS.md) rule 8. Do not write it into the manifesto as settled prior
art before somebody reads *Knowledge Assets*. `CON-OP-4` names the readings owed.

**`ARC-OP-16`, `ARC-OP-17` and `ARC-OP-18` are not void and must not be discarded with
`CON-OP-11`.** Each was argued from locally-general rules existing, not from domain size
explaining them. `ARC-OP-17` in particular is independent of everything both passes touched
and is still load-bearing.

**Two documents in `00_concept/` have the weakest provenance in the repository.**
[`../docs/00_concept/001_mission.md`](../docs/00_concept/001_mission.md) was written by a
model from a prompt the author explicitly flagged as unconsidered, and its candidate
mission statement is narrower than what he said in three places. He should read it
adversarially and say where the narrowing is wrong. The inventory is firmer, having been
reviewed, but was still drafted and revised inside one exchange.

**The reviewer was told which attack to make.** Q3 of the second pass named the attack it
expected to be fatal and the reviewer agreed. A reviewer told where to strike is a weaker
instrument than one that finds the spot, and the agreement is discounted accordingly in the
note. This is the assignment problem `PRC-OP-1` records, worsening rather than improving.

**The falsifiable core is unreviewed after three passes.** Every pass has reviewed the
argument rather than the claim everything rests on — that business keys are
machine-proposable at adjudication-worthy precision. That is now a pattern, not a choice.

**Transport lesson worth keeping.** Supplying the apparatus does not require the reviewer
to *read* the apparatus. The second pass timed out at the bridge's sixty-second ceiling
when the prompt asked for five documents, and succeeded when the apparatus was stated
inline and the reading cut to one file.
[`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md)
does not yet say this and should.

**The register grew again.** Net two rows, after a first pass that narrowed five and opened
none. Both new rows are real — `ARC-OP-21` is an architectural gap with no existing home,
`CON-OP-15` is a question rule 3 forbids leaving in prose — but `PRC-OP-2` and `PRC-OP-5`
are still live and the pile is still unranked at forty-seven.

**Git mechanics.** Deletion in the connected folder is disabled by default, so git leaves a
stale `.git/index.lock` and temporary objects behind after a commit until deletion is
permitted. If git misbehaves, check for `.git/index.lock` first.

## Do not reopen

- Models never operate in the data path — [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md).
- Autonomy is tiered — [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).
  *(`ARC-OP-19` asks whether the enumeration is complete. That extends the tiering; it does
  not reopen it.)*
- Argument, then proof of concept on public data, then offering — [ADR-0006](../docs/20_decisions/0006-project-mode.md).
- `nsdn` as the handle, the biological metaphor kept private — [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md).
- The register, handover and enforcement apparatus — [ADR-0007](../docs/20_decisions/0007-register-and-handover-apparatus.md).
- Data is the substrate; the three are faculties; each has a mandate; a faculty is never
  named after its implementation — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
  *(The second faculty's own name is `CON-OP-10` and is open. The collective noun is not.)*
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).
- **The amortisation-threshold synthesis.** `CON-OP-11` was reviewed and failed. It stays
  `OPEN` because §III still needs a replacement for statability, not because the
  domain-size reading is still a candidate.
- **The auditability interaction.** Tried, refuted, and recorded against `CON-OP-8`. Do not
  re-propose it without the comparison that row now names.

## What session 03 did not do

No prior art was verified, and Boisot remains the most consequential unsourced claim here.
No cost arithmetic — `CON-OP-2` is untouched and now has four more named quantities and
still no numbers. No dataset survey. No code. No data. No push to GitHub.
[`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III was not
edited and still carries its challenge banner: both new documents are additions beside it,
not a rewrite of it. `CON-OP-12`, `ARC-OP-19` and the falsifiable core were named for
review and not reached.
