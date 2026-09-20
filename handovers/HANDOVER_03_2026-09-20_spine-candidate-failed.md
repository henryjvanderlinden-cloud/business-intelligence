# nsdn — Handover 03: the candidate spine failed review, and the manifesto has two theses
## Written 2026-09-20 at the close of session 03, for a fresh session

> **STATUS: CURRENT.**

---

## First actions

1. `git log --oneline -8` — expect head at the session 03 review commit.
2. `python tools/check_repo.py` — must pass before anything is changed.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority
   on what is open; this handover is orientation only, and where the two disagree the
   register wins.
4. Read
   [`../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md`](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md),
   then `CON-OP-8`, `CON-OP-11` and `CON-OP-4` in the register, in that order. `CON-OP-8`
   first, because it now carries the disposition the other two feed.

## Outstanding action for the author, not the model

**The repository has still never been pushed.** Unchanged from Handovers 01 and 02.
`origin` is configured to
`https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the repository
does not exist on GitHub, and these sessions hold no credentials. The author creates the
empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`. Visibility remains
undecided; the reasoning favoured private until the Mode 1 gate.

## Where the project stands

Session 03 ran the second external review pass, which `PRC-OP-1` had assigned at the close
of session 02, and filed it as
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md).
The object was `CON-OP-11`, chained across three word-capped questions in one thread to
`CON-OP-8` and `CON-OP-4`. All three returned adverse verdicts and they are consistent
with one another rather than three separate complaints.

Eight ADRs are settled. Forty-five register rows are live — the same forty-five as at the
close of session 02. Five were narrowed and none was opened, which is the first session
that has not grown the register. Nothing has been built, nothing has been verified, and no
data has been touched.

**`CON-OP-11` failed, on the repository's own evidence.** Domain size is not the axis that
explains codification; repayment is an expected-value quantity in which extension is one
multiplier among several. The counterexample came from
[`../docs/10_architecture/190_machine-authored-design-canon.md`](../docs/10_architecture/190_machine-authored-design-canon.md)
§3: Anchor-style 6NF has a discipline-wide domain and is almost unused. Maximal domain, no
adoption. What survives is the narrower claim that was already available — machine
authorship lowers one cost term — and the unification of the canon-cost and statability
arguments falls with the axis.

**`CON-OP-8` therefore came back live and has an answer.** The manifesto carries two
independent theses: machine authorship lowers the cost of expressing and maintaining
already-known designs as deterministic machinery, and contextual inference makes locally
situated semantic hypotheses cheap enough to propose while validation and adjudication
remain the limiting costs. Humans validate and authorise both. Neither is evidence for the
other. The cost is a manifesto with no single causal mechanism.

**`CON-OP-4`(ii) failed and (i) turned out to be prior art.** *There is no rule to learn*
is false as stated whichever way `CON-OP-11` resolves. And Boisot's I-Space already
separates codification from abstraction, which is the articulable-but-not-general
distinction §III leans on, some thirty years early. The contribution reduces to the mandate
policy — which the row had already conceded might be enough, and which
[ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md) has since made
load-bearing.

## Task for the next session, in one sentence

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III
as two declared theses per `CON-OP-8`, against `CON-OP-5`, `CON-OP-6`, `CON-OP-7`,
`CON-OP-11` and `CON-OP-4`, settling `CON-OP-10`'s naming and executing `CON-OP-9`'s
rename in the same pass.

## Why that task and not another

It is the same instrument Handover 02 named, and the review has made it both more urgent
and much better specified. The rewrite no longer has to decide which spine to use — that
is now `CON-OP-8`'s disposition — and instead has to write two theses honestly, say what
§III's second faculty is actually doing now that *there is no rule to learn* has gone, and
carry the Boisot concession. `CON-OP-13`'s residual travels with it, as before, because it
touches the same documents.

The alternatives are unchanged and still unstarted: the canon survey (`ARC-OP-14`), the
public dataset survey (`EVI-OP-2`), and the external review of the falsifiable core
(`PRC-OP-1`). **The canon survey has been promoted by this pass**, because under two theses
the canon half is the one that can be evidenced without code, and `CON-OP-8` now says
explicitly to expect it to firm up first. The dataset survey remains the one task that
makes progress regardless of how the argument turns out, and it has now been deferred
three times.

## Traps and warnings

**Boisot is unverified and a disposition rests on it.** The claim that the I-Space
anticipates articulable-but-not-general is the reviewer's, from general knowledge, under
[`../AGENTS.md`](../AGENTS.md) rule 8. It is now the most consequential unsourced
assertion in the repository. Do not write it into the manifesto as settled prior art
before somebody has read *Knowledge Assets*. `CON-OP-4` names the specific readings owed.

**`ARC-OP-16`, `ARC-OP-17` and `ARC-OP-18` are not void and must not be discarded with
`CON-OP-11`.** Each was argued from locally-general rules existing, not from domain size
explaining them, and locally-general rules survive the pass intact. They need re-deriving
from the expected-value framing, which is a different and smaller job than reopening them.
`ARC-OP-17` in particular — correlated error breaking the calibration story — is
independent of everything this pass touched and is still load-bearing.

**The two-thesis reading was supplied by the assignment, not discovered by the reviewer.**
Q2 gave three options and asked for one. The reviewer picked one and defended it, which is
weaker evidence than a finding it reached unprompted, and the model that wrote the options
is the model that drafted the object. Treat `CON-OP-8`'s disposition as the best available
reading rather than as an adjudicated result, and note that its own closing objection is
unanswered: two adjacent capability claims with no demonstrated interaction are a weaker
object than one thesis. The rewrite either argues the interaction or states its absence.

**The falsifiable core has now been stepped around twice.** Both passes reviewed the
argument rather than the claim everything rests on — that business keys are
machine-proposable at adjudication-worthy precision —
and [`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md)
still ranks it first. A third pass that again reviews prose would be a pattern rather than
a choice.

**The register did not grow this session, and that is a result worth keeping.** `PRC-OP-5`
and `PRC-OP-2` are still live and the pile is still unranked at forty-five rows. Narrowing
rows rather than opening them is what closing the register looks like from here.

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
  domain-size reading is still a candidate. Do not revive it without the evidence
  `CON-OP-11` now names.

## What session 03 did not do

No document was edited — per
[`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md),
a review note is not an edit and its dispositions become register rows.
[`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III still
carries its challenge banner and its unchanged text. No prior art was verified. No cost
arithmetic. No dataset survey. No code. No data. No push to GitHub. `CON-OP-12`,
`ARC-OP-17`, `ARC-OP-19` and `CON-OP-14` were named in the second-pass assignment and were
not reached.
