# nsdn Open Points Register v1.0

**Status: authoritative.** Cut 2026-09-19, session 01. This file is the single
authoritative answer to *what is open?* for this project.
[`docs/00_concept/040_open-questions.md`](../docs/00_concept/040_open-questions.md) is
superseded as of this cut and retained for provenance; its numbering is preserved in the
`from` line of each migrated row.

Conventions — state tokens, supersession, identifiers, archiving — are in
[README.md](README.md). Enforcement is `python tools/check_repo.py`.

---

## §1 — Concept and argument (`CON`)

### CON-OP-1 — Is the three-tier autonomy claim original?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The structural / semantic / teleological tiering in
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) is the load-bearing
intellectual contribution of this project so far, and it has not been checked against
anybody else's work. The schema-matching and data-governance literatures have been
thinking about the structural-versus-semantic boundary for thirty years, and the
teleological layer resembles arguments from the decision-support tradition. If the
tiering is already standard, the contribution is the *mandate policy* built on it rather
than the distinction itself, and the framing should change accordingly.

Closes when [050_prior-art.md](../docs/00_concept/050_prior-art.md) carries a verdict on
this specific claim.

### CON-OP-2 — The economics have no number
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The argument rests on an unquantified premise: that per-token reasoning cost has fallen
far enough to make per-column, per-hypothesis machine reasoning affordable, while the
cost of a human doing the same has not moved. Nothing in this repository puts a figure
on it.

A back-of-envelope is cheap and should be done early, because the whole thesis is softer
than it sounds if the ratio is not dramatic: cost to profile one column, cost to
generate and evidence one hypothesis, cost per adjudicated assertion, against a
contractor day rate. Compute it against real token prices and a plausible landscape
size, and state the break-even in columns.

If the number is unflattering, that is a finding and belongs in the argument rather than
outside it.

### CON-OP-3 — What is the acceptance test for an automated analysis?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 11)*

"Interesting" is not measurable. "Changed a decision" is, but only retrospectively and
rarely. Without an acceptance test, Phase 3 cannot be evaluated and its failure mode —
statistically true irrelevance — will be invisible from inside the system.

### CON-OP-4 — Is the three-component framing distinct from existing human-in-the-loop discourse?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

[005_manifesto.md](../docs/00_concept/005_manifesto.md) claims that automated
sense-making is a third component rather than an assistant to the other two, and that the
binding constraint moves from construction to adjudication. Adjacent claims exist in the
centaur and human-in-the-loop literatures, in the augmentation-versus-automation
tradition, and in recent writing on agentic engineering.

**Narrowed 2026-09-19, same session, on defining the term.** Statability is now
decomposed in [005_manifesto.md](../docs/00_concept/005_manifesto.md) §III into
articulability, generality and stability, and the first of those is straightforwardly
Polanyi's tacit knowledge, whose role as a limit on automation is Autor's Polanyi's
paradox. That much is prior art and is now cited rather than asserted.

What remains to test is the specific claim that data semantics fail *generality* rather
than *articulability* — sayable by anyone who knows, with no general rule that would
produce them — and the consequence drawn from it: that learning a rule from examples,
the standard answer to Polanyi's paradox, cannot address this failure, because there is
no rule to learn. If that distinction is already made somewhere in the codification or
knowledge-management literature, the manifesto should cite it and the contribution
reduces to the mandate policy built on the distinction, which may still be enough.

Closing this row requires reading Autor 2014 in full and surveying the tacit-knowledge
literature far enough to be sure, not merely far enough to be comfortable.

**Superseded in part 2026-09-19 by
[XREV_2026-09-19_manifesto-statability_sol](../docs/30_research/notes/XREV_2026-09-19_manifesto-statability_sol.md)
Q3, verdict FAILS AS STATED.** The argument above conflates the object level with the
meta level. There is no general rule about *KLANTNR*; there is a perfectly general and
learnable rule about *how to infer what a column like KLANTNR means*, and
schema-matching research has been learning exactly that for two decades. Learning from
examples therefore does address a generality failure, and the claimed distinction from
Autor does not survive at the level of mechanism. "Situated inference" is, on this
reading, not shown to be distinct from pattern learning over a context window.

What may survive is weaker and empirical: cross-organisation schema matching has existed
for twenty years without dissolving the problem in practice, which suggests the general
inference function was right in principle and inadequate in performance until recently.
That is a claim about capability thresholds rather than about kinds, and the manifesto
should assert no more than it. Whether even that survives is what remains open here.

Related to `CON-OP-1`; both close against
[050_prior-art.md](../docs/00_concept/050_prior-art.md).

### CON-OP-5 — Stability is not an independent condition of statability
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, from
[XREV_2026-09-19_manifesto-statability_sol](../docs/30_research/notes/XREV_2026-09-19_manifesto-statability_sol.md) Q1.

External review established that stability is not individually necessary. Effective-dated
reference tables and Type 2 dimensions encode changing tax rates, hierarchies,
classifications and code meanings deterministically: the fact changes, execution stays
correct, because transaction time selects the applicable version.

The defect in [005_manifesto.md](../docs/00_concept/005_manifesto.md) §III is a level
confusion — it does not distinguish the stability of the *fact* from the stability of the
*rule*, and Type 2 dimensioning is exactly the discipline's general rule for absorbing
unstable facts. The repair candidate, unratified: what resists encoding is *ungoverned*
change, change with no general form and no notification, which is a generality failure
about the change process rather than a condition of its own. If that repair holds,
statability reduces to two conditions plus `CON-OP-6`, and §III must be rewritten rather
than annotated.

### CON-OP-6 — Observability is a missing fourth condition
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, from the same pass, Q1.

The three conditions are not jointly sufficient. The reviewer's counterexample:
*attribute each sale to the customer's principal place of business at transaction time*
is articulable, general and stable, and still cannot execute if historical location was
never captured.

Observability — every fact the rule needs must be available, identifiable and reliable
enough at execution time — is a genuine omission rather than a refinement. The existing
three characterise the proposition; observability connects it to evidence. It also
connects §III to material the manifesto currently ignores: the original brief's bullet on
data gaps, and the enrichment phase in
[400_phasing.md](../docs/40_roadmap/400_phasing.md), which is precisely the business of
making unobservable things observable.

### CON-OP-7 — The articulability argument equivocates between conclusion and warrant
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, from the same pass, Q2. The sharpest finding of the pass.

**(a) Conclusion versus warrant.** §III argues from the sayability of a conclusion —
*these two records are the same customer* — and then claims a property of the knowledge.
The steward who knows it can state the conclusion and frequently cannot state the
cue-weighting that produced it: spelling, address history, household structure, source
reliability, timing, exceptions. That is Polanyi's condition, appearing in the middle of
the example §III uses to escape Polanyi.

Not conceded, and the disagreement is recorded rather than resolved: the reviewer's
counterexamples are *recognition* competencies, and the pass asserts without evidence
that they are central rather than marginal to warehouse construction. §III concedes
inarticulable recognition exists and calls the residue small. Which is right is
empirically settleable and neither side has measured it.

**(b) Distributed elicitation.** Where semantics exist only as a negotiated synthesis
across operations, finance, legal and system owners — no participant holding the
proposition whole — calling the eventual sentence "articulable" hides the cost of
producing it, and the categorical distinction becomes a gradient of elicitation cost.

This damages more than the definition. [005_manifesto.md](../docs/00_concept/005_manifesto.md)
§VII argues adjudication is viable *because* someone can always state the particular once
asked. If nobody holds it whole, there is no adjudicator to ask, and
[170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md) assumes a
mechanism weaker than it needs. `ARC-OP-3` is promoted from a detail to a load-bearing
component by this finding.

### CON-OP-8 — Should the canon-cost argument replace statability as the manifesto's spine?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, from the author's bitemporality observation; see
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md) §5.

[005_manifesto.md](../docs/00_concept/005_manifesto.md) §III is under challenge and
losing. A candidate replacement framing arrived the same day and from the author rather
than the model: *every methodology in this discipline is a compromise between correctness
and human maintenance cost, and the canon is full of designs rejected on the cost side of
that trade — a cost that has now collapsed.*

Two reasons to prefer it. It makes an empirically checkable claim about an existing
literature rather than a conceptual claim about kinds of knowledge that must survive
forty years of tacit-knowledge philosophy. And it yields a research programme that can be
executed without any code: survey the canon, separate designs rejected for authoring cost
from those rejected for runtime cost, re-evaluate the first set.

Against it: it is a narrower claim. It explains why *storage and modelling* designs change
and says nothing about the semantic inference that the rest of the architecture rests on.
It may be a better-supported thesis about a smaller thing, and the right answer may be
that the manifesto carries both with the canon argument first because it is defensible.

Decide as part of the §III rewrite, not separately.

---

## §2 — Architecture (`ARC`)

### ARC-OP-1 — How is a source discovered rather than registered?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 4)*

The crawler image is the most evocative element of the original brief and the most
legally fraught. [150_trust-and-blast-radius.md](../docs/10_architecture/150_trust-and-blast-radius.md)
proposes inventory-driven discovery with inferred-source *proposals*, but does not
settle whether active discovery is in scope at all.

### ARC-OP-2 — What evidence promotes a joinability hypothesis to a business-key assertion?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 7)*

A stated threshold is needed or the system floods the adjudication queue or silently
asserts nonsense. [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) rules
that thresholds are set from measured precision against a held-out adjudication set
rather than from judgement, which makes this row dependent on `EVI-OP-1`.

### ARC-OP-3 — How is disagreement between two adjudicators represented?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 8)*

Semantics are contested in real organisations. A model admitting only one answer records
whichever arrived last, and silently discards the more interesting finding — that two
named people believe different things about the same column.

### ARC-OP-4 — How does an assertion age?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 9)*

A confirmed fact about a system re-platformed two years later is no longer true and
nothing in the data says so. Falsifiers and review dates are proposed in
[120_context-layer.md](../docs/10_architecture/120_context-layer.md); the decay policy
itself is unspecified.

### ARC-OP-5 — Per-source reliability is not modelled
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The design calibrates autonomy globally — one precision figure per job type per model.
It should almost certainly be calibrated *per source*: how often were our inferences
about this system subsequently overturned? Sources differ enormously in how well their
structure predicts their semantics, and a source with a poor record should generate
hypotheses that are ranked lower and adjudicated earlier, not the same ones with the
same confidence.

This is a genuine addition to the architecture rather than a question about it, and it
costs almost nothing once the held-out adjudication set exists, because the labels are
already being produced.

### ARC-OP-6 — Information-gain ranking is biased toward what is already understood
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The adjudication queue in [170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md)
ranks questions by how many downstream hypotheses they unblock. High-degree entities —
customer, product, order — unblock the most, and are precisely the entities an
organisation already understands well. The adjudications that carry real information may
be low-degree: the obscure code list, the one table nobody remembers.

Pure information gain will systematically under-ask exactly where the system is most
ignorant. Some counterweight is needed — expected surprise, or uncertainty-weighted
gain — and the naive formulation should not be implemented without one.

### ARC-OP-7 — Context layer: files, graph, or both?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 12)*

[120_context-layer.md](../docs/10_architecture/120_context-layer.md) argues for markdown
cards in git with a derived, disposable graph index, and states the honest objections —
git discomfort past roughly a hundred thousand files, and history thrashing from
high-frequency profile updates. The most consequential unmade decision in the
architecture; it should be settled by an ADR and not by drift.

### ARC-OP-8 — What is the unit of agent work?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 13)*

[130_agent-loop.md](../docs/10_architecture/130_agent-loop.md) argues for many short,
idempotent, independently retryable jobs over a long-running loop. Almost certainly
right; unratified, and with unexamined implications for how state passes between jobs.

### ARC-OP-9 — Model routing policy
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 14)*

Which model, at which tier, for which job, and who decides. Dependent on `CON-OP-2`,
since routing is an economic question before it is a capability question.

### ARC-OP-10 — What does the human interface actually look like?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 16)*

Pull requests, a web application, a chat surface, or a weekly digest. Determines whether
adjudication happens at all, which makes it the highest-stakes interface question and
the one most likely to be answered by default.

### ARC-OP-11 — SQL dialect normalisation
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 6)*

`sqlglot` is the candidate in
[180_technology-posture.md](../docs/10_architecture/180_technology-posture.md),
unevaluated. Blocks `EVI-OP-3`.

### ARC-OP-12 — Who maintains the decision register?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 10)*

The teleological anchor is a hard dependency for everything at Tier 3, and it is
maintained by people who have no immediate incentive to maintain it. If there is no
answer to this, Phase 3 has no foundation and the honest move is to say so early.

### ARC-OP-13 — Is the rule set a third temporal axis, or something else?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

Derived data is a function of raw data and of the logic that refined it, and that logic
versions independently of both valid time and transaction time. Whether this is properly
a third time axis, a dimension on the derivation rather than on the fact, or simply
content-addressed rule provenance carried per row, is unsettled and the choice has large
consequences for storage and for query formulation.

The three questions it must answer are in
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md) §1:
what we now believe was true then; what we reported then; and what we would have reported
then knowing what we know now. A design that cannot distinguish the second from the third
cannot support audit or restatement, which is most of why anyone wants this.

Prior art is likely and unexamined: SQL:2011 temporal features, bitemporal modelling
literature, and event-sourcing practice all bear on it.

### ARC-OP-14 — Survey the canon for designs rejected on human-cost grounds
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The research programme implied by
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md):
go through the modelling canon, identify designs that were correct and rejected, and
separate **rejected for authoring and maintenance cost** from **rejected for runtime
cost**. Only the first set is straightforwardly re-opened by machine authorship;
conflating the two would license designs that are still slow.

Candidates listed in §3 of that document: rule-versioned bitemporality, 6NF and anchor
modelling, insert-only storage, exhaustive column-level lineage, per-fact provenance,
explicit units and grain, redundant physical representations, maximum-granularity
assertions.

First half of the work is verification: the claims in that document about Anchor
Modelling, SQL:2011 and the stated rejection reasons for Kimball and 6NF are from general
knowledge and unchecked. Needs no code and is executable in Mode 1, which makes it a
third candidate for the next session alongside `PRC-OP-1` and `EVI-OP-2`.

### ARC-OP-15 — Machine-optimal storage owes a human-comprehensible adjudication surface
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The direct tension between
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
and the rest of this project. If ruling is the scarce act, everything a human must rule on
must be comprehensible to a human — and a four-thousand-table anchor model is not. The
presumed resolution is that the physical model optimises for machine authorship while the
adjudication surface optimises for human comprehension, both generated from one
declaration.

That is an assertion, not a design. Until it is one, every argument in this repository
for machine-friendly verbosity is writing a cheque that
[170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md) has to cash.

---

## §3 — Evidence and measurement (`EVI`)

### EVI-OP-1 — Ground truth for the falsifiable core
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 2, residual after
[ADR-0006](../docs/20_decisions/0006-project-mode.md))*

Public practice data supplies genuine messiness but no answer key for cross-source
entity identity, and the project's central claim is a precision figure. The resolution
proposed in [410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md)
is a hand-built sample of a few hundred entities, frozen before development and partly
held back.

Closes when a candidate source pair is selected and the sample exists.

### EVI-OP-2 — Candidate public dataset survey
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 3)*

Sources must be independently built, must genuinely share entities, and must permit
identity to be established by hand for a sample. Dutch public registers are the leading
candidate on structural grounds. The survey needs no code and is the natural first
substantive task of Mode 1.

### EVI-OP-3 — Query logs as evidence
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

Query logs record joins that humans already believed were valid. They are usually
available, cheap to parse, and — the hypothesis — may carry more key evidence than
profiling does, at a fraction of the cost.

If that is true it partially undercuts the project's own thesis in an interesting way:
the most valuable semantic evidence would not be model-generated at all, but merely
model-*interpreted*. Worth knowing early, and it is a prototype rather than a debate. In
a public-data setting there are no query logs, which is a limitation of the Mode 2
environment worth stating alongside the result.

### EVI-OP-4 — Minimum viable profiling pass
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 5)*

How much joinability evidence do sketch-based methods yield across two schemas, at what
cost, without moving data? Determines whether profiling is affordable at landscape scale
and whether it is *permissible*, which matters more.

---

## §4 — Process (`PRC`)

### PRC-OP-1 — PARTLY DISCHARGED — external review of the repository
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. First pass run the same day; the row stays open because
one document of twenty-two has been reviewed and the falsifiable core has not.

**First pass, 2026-09-19:**
[XREV_2026-09-19_manifesto-statability_sol](../docs/30_research/notes/XREV_2026-09-19_manifesto-statability_sol.md)
— manifesto §III on gpt-5.6-sol, adversarial, three determinate questions, FAILS on all
three. Dispositions opened as `CON-OP-5`, `CON-OP-6`, `CON-OP-7`, and folded into
`CON-OP-4`. Note that the assignment was set by the model that drafted the object, so the
question selection is unreviewed by construction.

Still unreviewed: everything else, including the falsifiable core — that business keys
are machine-proposable at adjudication-worthy precision — which
[510_external-review.md](../docs/50_process/510_external-review.md) ranks first.

Every document here was drafted by one model in one session, which by the model-switch
rule in [500_working-method.md](../docs/50_process/500_working-method.md) makes the
whole repository unreviewed by construction. The argument currently has exactly one
reader and that reader wrote it.

The first external pass should attack the two claims everything else rests on: the
three-tier distinction (`CON-OP-1`) and the assertion that business keys are
machine-proposable at useful precision. Adversarial framing, one object per pass, per
[510_external-review.md](../docs/50_process/510_external-review.md).

### PRC-OP-2 — Keep the apparatus proportionate to the work
**⚠ STATE: HELD**
Opened 2026-09-19, session 01. Resume when the register exceeds roughly forty live rows
or the first archive cut is contemplated.

This repository has acquired a register, a handover series, a process convention and a
checker while containing no code and one week of thinking. The apparatus is justified
here because it was inherited whole from a project where it was learned expensively, and
because it costs almost nothing at this size — but ceremony that exceeds the work is a
real failure mode, and a project that spends its Mode 1 perfecting its own bureaucracy
has found a comfortable way to avoid testing its thesis.

Held rather than open because the correct response is vigilance, not action.

**First instance, 2026-09-19, same session.** The model read the compendium's rule about
writing handovers at session end as forbidding mid-session revision, and recorded ordinary
working as a process defect. The author corrected it: revision as insight arrives is the
normal order of business, this is uncharted territory, and git already holds whatever
crosses sessions. Convention imported without the failure that motivated it, then enforced
beyond its intent — exactly the mode this row exists to watch. The general form is now in
[500_working-method.md](../docs/50_process/500_working-method.md).

### PRC-OP-4 — The drafting-to-challenging ratio was about five to one
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, as a finding about the session that produced this
repository.

Two contributions in session 01 changed the direction of the work: the external
adversarial pass, which found three defects in the manifesto's central section, and the
author's own observation about bitemporality, which produced
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
and a candidate replacement for the manifesto's spine.

Neither came from the model drafting on its own. Everything that *did* come from the
model drafting on its own — twenty architecture and concept documents — remains the least
tested material here, and the one section of it that was tested failed on every question
asked.

The session spent roughly five parts drafting to one part challenging. The ratio should
be closer to one to one, and the way to get there is not to draft less but to attack each
substantial document as it is produced rather than at the end of a session. Whether that
becomes a standing rule in
[500_working-method.md](../docs/50_process/500_working-method.md) is what this row
decides; it should be decided from a second session's evidence, not from this one's.

### PRC-OP-5 — The register is a pile, not a queue
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

Thirty-one live rows, no priority, and dependencies stated only in prose where they were
noticed. `ARC-OP-2` waits on `EVI-OP-1`; `ARC-OP-9` waits on `CON-OP-2`; `CON-OP-5`,
`CON-OP-6` and `CON-OP-7` all feed one rewrite and should be worked together; `CON-OP-8`
must be decided inside that rewrite rather than before it.

The irony is exact and worth stating rather than enjoying quietly. This project's
sharpest architectural argument is that an unranked queue of open questions wastes the
scarce resource that has to answer them, and that ranking should be by what a resolution
unblocks — `ARC-OP-6`. The register violates its own finding.

Triage is a cheap next-session task: record blocking relationships, and mark the rows
that close together. Resist inventing a scoring scheme; the compendium's experience is
that structure added before it is needed becomes structure that lies.

### PRC-OP-3 — Cross-model review is unwired
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 15)*

Codex is registered as a local MCP server and reachable from these sessions, so the
transport exists. What does not exist is the convention for *this* repository: which
objects get reviewed, on what cadence, and how disagreement is recorded.
[510_external-review.md](../docs/50_process/510_external-review.md) adapts the
compendium's XREV convention; it has not been exercised once.

---

## §5 — Commercial premises (`BIZ`)

### BIZ-OP-1 — The adjudication hedge may not be priced
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The project's strategic premise, stated by the author: work is getting scarce, rates are
under pressure, and the response is to move to where the remaining human contribution
is — adjudication, the judgement that the data cannot supply.

The uncomfortable version, recorded here rather than left in conversation because it is
the premise most likely to be wrong: *if* rates are under pressure because capability is
being commoditised, then adjudication capacity may be commoditised on the same schedule,
merely later. The hedge assumes the market can identify and will pay for judgement that
is hard to demonstrate in advance and only visible when it is absent. That assumption is
not obviously true, and it has not been examined anywhere in this repository.

The falsifier is observable and worth watching deliberately: whether engagements
increasingly buy *review and assurance* of machine-built data work as a distinct,
separately priced service, or whether that work is absorbed into delivery at the old
rate. Evidence either way belongs in this row.

Recording it does not make the strategy wrong. A hedge with a stated failure condition
is a better hedge than one without.
