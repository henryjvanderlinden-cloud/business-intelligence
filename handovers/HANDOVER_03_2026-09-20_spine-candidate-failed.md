# nsdn — Handover 03: the candidate spine failed, the manifesto has two theses, and the mission is written down
## Written 2026-09-20 at the close of session 03, for a fresh session

> **STATUS: HISTORICAL (superseded 2026-09-20)**, by
> [HANDOVER_04_2026-09-20_canon-verified-second-interaction-refuted.md](HANDOVER_04_2026-09-20_canon-verified-second-interaction-refuted.md).
> Its instruction to verify rather than write was followed; its named task was not
> executed and travels forward.

---

## First actions

1. `git log --oneline -8` — expect head at `59f2207`.
2. `python tools/check_repo.py` — must pass before anything is changed.
3. Read [`../registers/OPEN_POINTS.md`](../registers/OPEN_POINTS.md). It is the authority on
   what is open; this handover is orientation only, and where the two disagree the register
   wins.
4. Then, in this order: `CON-OP-8`, because it carries the disposition everything else feeds;
   [`../docs/00_concept/002_mission-statement.md`](../docs/00_concept/002_mission-statement.md),
   whose changelog is the densest thing written today; and
   [`../docs/00_concept/060_faculty-inventory.md`](../docs/00_concept/060_faculty-inventory.md).

## Outstanding actions for the author, not the model

**The repository has still never been pushed.** Unchanged through three handovers. `origin`
is configured to `https://github.com/henryjvanderlinden-cloud/business-intelligence.git`, the
repository does not exist on GitHub, and these sessions hold no credentials. The author
creates the empty repository — no README, no .gitignore, no licence — and runs
`git push -u origin main` from `C:\Git\business-intelligence`.

**`CON-OP-15` is the author's to rule.** It asks what the success criterion is. A model can
sharpen it and has, four times; ratifying it is not a model's job.

## Where the project stands

Eight ADRs settled. Forty-seven register rows live, up from forty-five. Nothing built,
nothing verified, no data touched. Four external review passes were run today and all four
returned adverse verdicts.

**`CON-OP-11` failed.** Domain size is not the axis that explains codification; repayment is
an expected-value quantity in which extension is one multiplier among several. The
counterexample came from §3 of
[`../docs/10_architecture/190_machine-authored-design-canon.md`](../docs/10_architecture/190_machine-authored-design-canon.md):
Anchor-style 6NF has a discipline-wide domain and is almost unused.

**`CON-OP-8` came back live and has an answer.** Two independent theses — cheap authorship of
known deterministic designs, and cheap proposal of locally situated semantic hypotheses —
with humans validating and authorising both. Neither is evidence for the other. One
interaction candidate was proposed and refuted; the row now names the comparison that would
establish one.

**`CON-OP-4`(ii) failed and (i) is prior art.** *There is no rule to learn* is false as
stated, and Boisot's I-Space separates codification from abstraction some thirty years early.

**The faculty inventory exists and was reviewed.** Twelve capability dimensions plus mandate,
for allocating work between faculties. Review cut one dimension, added three, replaced its
allocation rule, and refuted the interaction candidate it offered.

**The mission is written down for the first time**, in two documents: 001 holds the author's
formulation verbatim with the arguments against it, 002 holds the current wording as a living
document at version 0.6 with a changelog of six versions. Four of the six were refused, and
the changelog records why — read it before rewording anything.

**The obstacle taxonomy collapsed at the end of the day.** On the author's argument and the
reviewer's concession, authoring, comprehension, query construction and optimisation are not
distinct obstacle classes but locations where lifecycle work accumulates. The consequences
are in `ARC-OP-14` and `ARC-OP-15`.

## Task for the next session, in one sentence

Rewrite [`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III as
two declared theses per `CON-OP-8`, against `CON-OP-5`, `CON-OP-6`, `CON-OP-7`, `CON-OP-11`
and `CON-OP-4`, settling `CON-OP-10`'s naming and executing `CON-OP-9`'s rename in the same
pass.

## Why that task and not another

It is the same instrument Handover 02 named, and four passes have made it both more urgent
and far better specified. The rewrite no longer chooses a spine; it must write two theses
honestly, say what the second faculty does now that *there is no rule to learn* has gone,
carry the Boisot concession, and either argue the interaction or state its absence.
`CON-OP-13`'s residual travels with it.

**But consider `ARC-OP-14` first, and consider it seriously.** The canon survey is now
load-bearing for three separate things: `CON-OP-8`'s outstanding interaction comparison, the
mission's assumption that Data Vault's burden is the kind machine authorship can absorb, and
the verification of §190's own unchecked claims. It needs no code, it is executable in Mode 1,
and it has been deferred in every handover so far. `EVI-OP-2`, the public dataset survey,
remains the task that makes progress regardless of how the argument turns out and has now
been deferred four times.

## Traps and warnings

**The drafting model collapses multi-term calculations onto single axes, repeatedly.**
`CON-OP-11` did it with domain size. The inventory's first allocation rule did it with
verifiability, the day after. Treat any single-axis explanation drafted here as suspect on
sight, and ask what the other terms were.

**Protections get lost when clauses are rewritten for cadence, and the loss is invisible to
the drafter.** Version 0.2's unification came back through a governance clause after the
causal claim had been guarded against. Version 0.4 moved the abundance guard out of the
measure and into a clause about who sets priorities, where it constrained nothing. Both
times the rewrite looked like a tightening. Check guards against what they constrain, not
against whether the words are still present.

**§3 of the canon document is carrying a proxy, and two findings landed on it today.** Its
6NF example refuted `CON-OP-11` in the morning and survives as a case of lifecycle burden.
Its inference from object count and join complexity to human incomprehensibility does not
survive the evening, because tooling can present a comprehensible semantic view over a
complex physical model. Anything reasoning from table counts to what a human can understand
is using a proxy. `ARC-OP-15` now says so.

**Boisot is unverified and a disposition rests on it.** Rule 8 applies. Do not write it into
the manifesto as settled prior art before somebody reads *Knowledge Assets*. `CON-OP-4` names
the readings owed.

**`ARC-OP-16`, `ARC-OP-17` and `ARC-OP-18` are not void with `CON-OP-11`.** Each was argued
from locally-general rules existing, not from domain size explaining them. `ARC-OP-17` —
correlated error breaking the calibration story — is independent of everything four passes
touched and is still load-bearing.

**The falsifiable core is unreviewed after four passes.** Every pass has reviewed the
argument rather than the claim everything rests on: that business keys are machine-proposable
at adjudication-worthy precision. That is a pattern, not a choice, and a fifth pass on prose
would confirm it.

**Today produced apparatus and no verification.** Two concept documents, three review
sittings, a dozen narrowings, and not one number, source or measurement. `PRC-OP-2` exists
for exactly this. **The next session should verify something rather than write something.**

**Transport lesson.** Supplying the apparatus does not require the reviewer to *read* the
apparatus. A pass timed out at the bridge's sixty-second ceiling when the prompt named five
documents, and succeeded when the apparatus was summarised inline and the reading cut to one
file. [`../docs/50_process/510_external-review.md`](../docs/50_process/510_external-review.md)
does not yet say this and should.

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
- Data is the substrate; the three are faculties; each has a mandate; a faculty is never named
  after its implementation — [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).
  *(The second faculty's own name is `CON-OP-10` and is open. The collective noun is not.)*
- Prose-first, supersede-never-delete, numbered with gaps — [ADR-0002](../docs/20_decisions/0002-repository-layout.md)
  and [`../AGENTS.md`](../AGENTS.md).
- **The amortisation-threshold synthesis.** `CON-OP-11` was reviewed and failed. It stays
  `OPEN` because §III still needs a replacement for statability, not because the domain-size
  reading is a candidate. *(The 6NF counterexample stands. Reading it as evidence about
  comprehensibility does not — see `ARC-OP-15`.)*
- **The auditability interaction.** Tried, refuted, recorded against `CON-OP-8`. Do not
  re-propose it without the comparison that row names.
- **The obstacle taxonomy.** Authoring cost versus runtime cost versus comprehensibility is
  not a classification of obstacle kinds; it is a description of where lifecycle work lands.
  Conceded by the reviewer that first proposed it. Runtime cost and the adjudication surface
  remain separate accounts, for the reasons in 002.

## What session 03 did not do

No prior art verified. No cost arithmetic — `CON-OP-2` now has four more named quantities and
still no numbers. No dataset survey. No code. No data. No push.
[`../docs/00_concept/005_manifesto.md`](../docs/00_concept/005_manifesto.md) §III was not
edited and still carries its challenge banner; both new documents sit beside it rather than
replacing it. `CON-OP-12`, `ARC-OP-19` and the falsifiable core were named for review and not
reached.
