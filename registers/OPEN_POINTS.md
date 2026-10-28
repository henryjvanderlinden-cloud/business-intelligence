# nsdn Open Points Register v1.0

**Status: authoritative.** Cut 2026-09-19, session 01; extended 2026-09-20, session 02.
This file is the single authoritative answer to *what is open?* for this project.
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

**Narrowed 2026-09-20, session 03, and deliberately not widened.** [060_faculty-inventory.md](../docs/00_concept/060_faculty-inventory.md)'s
allocation rule names five quantities where this row names two: instruction, execution,
mandatory verification, remediation, and probability-weighted residual harm, subject to a
limit on irreversible downside. External review accepted that rule and then objected to it
on this row's grounds — none of the five has a number here.

The temptation is to grow this row to cover all five. It should not: the break-even in
columns remains the cheapest and most decisive number available, it can be computed today
from published token prices and a plausible landscape size, and it is the one that decides
whether the thesis is dramatic or merely true. The other four are named in the grid so that
they are not forgotten, and they are priced after the first number exists, not before.

Note also that verification cost — not production cost — is where the grid locates the
economic argument. A back-of-envelope that prices only generation answers the wrong
question if verifying a semantic assertion costs what producing it cost. The envelope
should therefore carry a second line: cost per adjudicated assertion, against cost per
proposed one.

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

**Narrowed 2026-09-20, session 03, by external review.** Reviewed on gpt-5.6-sol —
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md)
— and the second half failed while the first was found defensible but not novel.

**(ii) fails**, and it fails without depending on `CON-OP-11`'s result, which is worth
stating because the two findings could otherwise look like one finding counted twice. A
learner need not discover a universal rule mapping every column name to its meaning; it
may learn a landscape-local regularity, or a general inference function from contextual
evidence to probabilistic semantic hypotheses. Where no object-level rule exists the
machine is performing learned, fallible inference — not executing an unstated
deterministic rule. The first pass established the meta-level version of this; this pass
removes the remaining escape, so §III's residual formulation *there is no rule to learn*
is false as stated whichever way `CON-OP-11` resolves. The rewrite must say what the
second faculty is doing instead, and the reviewer's formulation is usable: learned
inference to probabilistic local hypotheses, which is a claim about performance and
calibration rather than about kinds of knowledge, and a considerably more modest thing to
assert.

**(i) survives as prior art, not as a contribution.** Boisot's I-Space is the close match:
it separates codification from abstraction as independent axes, which licenses knowledge
that is highly codified yet concrete and context-bound, and substantially anticipates
*articulable but not general*. Hayek's knowledge of the particular circumstances of time
and place is the adjacent account, though he does not consistently establish that such
knowledge is readily articulable. Cowan, David and Foray supply the codebook-cost argument
for why codifiable knowledge stays uncodified. Nonaka and Takeuchi are the loosest fit:
SECI emphasises context without cleanly isolating generality from articulability. On that
reading the manifesto cannot claim the distinction itself, and the contribution reduces to
the mandate policy built on it — which this row already conceded might be enough, and
which [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md) has since made
load-bearing.

Per [`../AGENTS.md`](../AGENTS.md) rule 8, the characterisation of Boisot above is the
reviewer's, stated from general knowledge, and is a hypothesis until somebody reads the
source. It is the most consequential unverified claim in the repository, because a
disposition now rests on it.

**What is owed is now specific**, which replaces this row's previous instruction to survey
the literature far enough to be sure: Boisot, *Knowledge Assets*, the sections defining
codification and abstraction; Hayek, *The Use of Knowledge in Society*; Cowan, David and
Foray, *The Explicit Economics of Knowledge Codification and Tacitness*; Nonaka 1994 with
the Nonaka–Takeuchi SECI chapters; and Autor 2014 in full. Then the holdout test folded
into `EVI-OP-5`. Closes against
[050_prior-art.md](../docs/00_concept/050_prior-art.md) with `CON-OP-1` and `CON-OP-12`.

**Superseded 2026-09-20, session 03.** The session-02 narrowing immediately below rests on
`CON-OP-11`, which failed review the same day; nothing from here to the end of this row is
a current claim. Retained for provenance.

**Narrowed further 2026-09-20, session 02.** `CON-OP-11` proposes a reading that concedes
the mechanism finding below rather than resisting it: the claim becomes one about the
*domain size* at which a generalisation repays its own authorship, not one about a kind of
knowledge. On that reading, what this row must still establish is exactly what the
historical block below already concedes may survive — an empirical claim about capability
thresholds — and the prior art that bounds it is `CON-OP-12` as much as the
tacit-knowledge literature.

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
**✅ STATE: RULED 2026-09-21**
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

**Narrowed 2026-09-20, session 03, by external review.** The either/or is live again and
has an answer. Reviewed on gpt-5.6-sol —
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md)
— which denied the unification `CON-OP-11` proposed and then refused both single-spine
options. Demoting semantic inference would make the manifesto sturdier only by amputating
the premise much of the architecture depends on; subordinating the canon argument to
statability would hitch the better-supported claim to the one the first pass damaged, and
would misdescribe known-design automation as evidence about knowledge.

The disposition is that the manifesto carries **two independent theses** and says so:
machine authorship lowers the cost of expressing and maintaining already-known designs as
deterministic machinery, and contextual inference makes locally situated semantic
hypotheses cheap enough to propose while validation and adjudication remain the limiting
costs. Humans validate and authorise both. Neither is evidence for the other: bitemporality
and exhaustive lineage demonstrate cheaper implementation, not better semantic discovery,
and schema interpretation demonstrates better hypothesis generation, not that elaborate
physical designs have become affordable to operate.

The cost is explicit and should not be softened in the rewrite. The manifesto loses a
single causal mechanism and must establish two capability changes, two cost curves and two
failure regimes; their conjunction may be historically important but is not conceptually
necessary, since either could have occurred without the other.

**The obligation this creates is the reviewer's own closing objection**, and adopting the
two-thesis reading does not discharge it: two adjacent capability claims with no
demonstrated interaction are a weaker object than one thesis. There may be an interaction
— a landscape whose deterministic machinery is cheap to regenerate is one where a revised
semantic assertion is cheap to propagate — but this repository has not made that argument
and must not assume it can. The §III rewrite either makes it or states its absence.

**The first interaction candidate was tried and refuted, 2026-09-20, session 03.** Per
[XREV_2026-09-20_faculty-inventory_sol](../docs/30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md)
Q3: the proposal was that deterministic auditability — all state explicit, the landscape
materialised and queryable — is a precondition for verifying the second faculty's semantic
output, so cheap deterministic authorship is what makes cheap semantic inference checkable.
It fails because a materialised, queryable landscape does not depend on *cheap machine*
authorship: conventional warehouses have supplied explicit transformations, lineage and
recomputation for decades, so the argument connects the second thesis to materialisation in
general rather than to the first thesis. Two lesser objections also land — many semantic
claims are validated against people or authoritative documentation rather than against data
at all, and auditability of machinery is not the same property as verifiability of an
interpretation.

**What survives is a test rather than an argument**, and it is the useful residue: *for
semantic hypotheses whose validation depends on recomputable structural evidence, cheaper
authorship and maintenance of evidence-producing artifacts may reduce validation cost or
widen the evidence economically available.* To become the interaction this row demands, the
project must show that machine authorship changes the availability, coverage or maintenance
cost of validation evidence **relative to an otherwise equivalent conventionally authored
warehouse**. That comparison is concrete enough to run once `ARC-OP-14`'s canon survey
exists, which is a second reason to promote that survey.

Note also what (c) costs procedurally. This row's attraction was that the canon argument
yields a research programme executable without code. Under two theses that stays true of
one and false of the other, so the halves will not be evidenced at the same rate: expect
the canon half to firm up via `ARC-OP-14` while the semantic half waits on `EVI-OP-1`.

**The comparison this row demands arrived early, and it points away from the first thesis.**
Per [2026-09-20-canon-survey](../docs/30_research/notes/2026-09-20-canon-survey.md) §1.7 and F4: Data Vault already presupposes generation, and a mature
metadata-driven ecosystem — WhereScape, VaultSpeed, AutomateDV, Varigence — generates vault
structures and loading logic today with no language model in the pipeline. What those
generators require as input is the model metadata: which entity is a hub, what the business
key is, which relationships are links. That input is the **second** thesis's output. So in
the one case the mission statement names, the first thesis's machinery already exists
conventionally and the binding input is semantic. The §III rewrite must not claim machine
authorship as the thing that makes Data Vault attainable without meeting this.

**A second interaction candidate, drafted 2026-09-20, session 04, and unreviewed.** It
composes F3 and F4 of the survey: the designs the first thesis makes affordable are
decomposed designs; decomposed designs perform only where key constraints are declared and
trusted (`ARC-OP-22`); those constraints are semantic assertions about identity, which is
what the second faculty proposes and a human adjudicates. If it holds, the first thesis
*generates demand* for the second, and the volume of key adjudication scales with the
decomposition cheap authorship enables.

Two conditions on using it. Its direction is adverse as readily as favourable — a coupling
in which thesis 1 loads the scarce faculty thesis 2 feeds is not mutual support, and must
not be written as though it were. And it has the same shape as the candidate refuted above,
so the first objection to test is whether the dependency is on *cheap machine* authorship or
merely on decomposition, which a conventionally authored 6NF warehouse would share. It was
drafted by the model working in this repository and is unreviewed by construction; per
`PRC-OP-3` it goes to another model before the manifesto touches it.

**Reviewed and refuted the same day, 2026-09-20, session 04.** Per [XREV_2026-09-20_canon-survey-interaction_sol](../docs/30_research/notes/XREV_2026-09-20_canon-survey-interaction_sol.md) it fails on
the axis its own warning named: a conventionally authored 6NF warehouse uses many narrow
tables and relies on declared, non-enforced keys for join elimination, so it incurs the same
adjudication demand with no machine authorship anywhere. The dependency attaches to
decomposition, exactly as the first candidate's attached to materialisation.

A second objection is the more useful one and was not anticipated here: **most of the keys
decomposition generates are mechanical consequences of the decomposition or surrogates, not
hypotheses about business identity.** Forty attribute tables restate one identity decision;
they do not pose forty. The quantity that would have to scale is the number of independently
uncertain identities, and that is not the same quantity as table count — which is the
single-axis error the traps keep recording, committed again.

The minimal premise that would rescue it, quoted from the pass: *the marginal decompositions
made economical specifically by machine authorship require previously unknown business-key or
cross-source identity assertions, and acceptable performance requires optimisations that
depend on declaring those assertions.* Nothing establishes either conjunct. **Two interaction
candidates have now been refuted on the same axis**, and a third should not be drafted
without first stating how it attaches to *cheap machine authorship* rather than to a property
conventional warehouses already have.

**The pass also corrected this row's own reasoning, and the correction outlives the
candidate.** This row holds that two adjacent capability claims with no demonstrated
interaction are a weaker object than one thesis, and the survey extended that to say an
adverse coupling "is not mutual support." The reviewer answers that a demonstrated adverse
coupling is *stronger* evidence that the theses describe one system, because it supplies a
causal relation; adverse concerns the interaction's consequences, not the strength of the
evidence for it. This repository has been conflating the strength of the object with the
attractiveness of the conclusion. **The §III rewrite is therefore not obliged to find a
favourable interaction, and must stop treating the absence of a favourable one as the absence
of one** — including where the honest finding is that the first thesis makes the second's
scarce faculty scarcer.

**Ruled 2026-09-21 by the author, in [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md).** Neither argument is the spine. The
manifesto presents separate capabilities — building known designs cheaply, and proposing
meaning for people to rule on — with room left for more value areas, and it owes no
interaction between them. A link is mentioned where it exists and matters. That removes the
obligation recorded above as the reviewer's closing objection, and with it the reason to
draft further interaction candidates; the two refuted ones stay here as history, as does the
reviewer's point about adverse coupling, which the ruling makes moot rather than wrong. The
§III rewrite is still owed, which is why this row is `RULED` and not `EXECUTED`.

**Superseded 2026-09-20, session 03.** The session-02 narrowing is retained below for
provenance; its premise did not survive review, and nothing after this line is a current
claim about this row.

**Narrowed 2026-09-20, session 02.** The either/or this row poses may be a false choice.
`CON-OP-11` proposes that statability and the canon-cost argument are one claim at two
altitudes — the collapse of the domain size at which a generalisation repays its own
authorship — in which case the canon argument is that claim's instance in the design
literature, locally-general semantics is its instance in the landscape, and the objection
recorded immediately above, that the canon argument says nothing about semantic inference,
dissolves rather than being traded away. Decide with `CON-OP-11`, still inside the §III
rewrite.

### CON-OP-9 — RULED — what the three things are called, and whether data is one of them
**✅ STATE: RULED 2026-09-20**
Opened 2026-09-19, session 01, from the author's question about vocabulary. Ruled
2026-09-20, session 02, by the author; recorded as
[ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md).

**The ruling.** Data is the **substrate** and is not a member of the set. The three things
that act on it are **faculties**. Each faculty's grant of authority — what it is entitled
to do, as distinct from what it is able to do — is its **mandate**, the author's own term
from [010_vision.md](../docs/00_concept/010_vision.md). A faculty is named by its function
and never by its implementation, which forecloses *the LLM*, *the model* and *the AI* as
names of the second faculty.

**Residuals, which is why this row is `RULED` and not `EXECUTED`.** The repository says
*components* throughout and has not been renamed; the rename lands with the §III rewrite
and not before, for the reason the historical block below gives. The enforcing check is
owed in the same commit as the rename and is deliberately absent until then, per
[ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md). And the second
faculty still has no name, which is `CON-OP-10` and is blocking.

**Superseded 2026-09-20 by the ruling above.** The candidate survey that produced it
follows, retained because a ruling without its argument is a ruling nobody can revisit.

[005_manifesto.md](../docs/00_concept/005_manifesto.md) calls them **components**, which
is serviceable and under-claims. The distinction it draws is not only what each can do
but what each is *entitled* to do — machinery executes and asserts nothing, sense-making
proposes, humans rule and set purpose. That is an authority structure, and
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) is an assignment of
mandates rather than of capabilities.

**A category question comes first.** Data is not a member of the set. The three do work;
data is what they work on. Proposed: data is the **substrate**, the three are the things
that act on it. Fixing this matters more than the collective noun, because a list mixing
material with agency is why no single word fits all four.

**Candidates, with their costs.** *Faculties* — a power to do a kind of work, carrying
authority in the older sense, with no collision anywhere in data or machine-learning
vocabulary; the objection is that faculties conventionally belong to one mind, which
smuggles back the organism metaphor [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md)
set aside. *Capacities* — the same work without that implication, duller, safe.
*Powers* or *offices* — carry the authority dimension most exactly, and "office" is
principled rather than accidental given §VII's argument that this infrastructure is
substantially a bureaucratic artifact; the cost is register, since the author writes
political theory and the vocabulary may read as imported. *Tiers* or *layers* — ruled
out, both for implying a stacking that is false and for colliding with the autonomy tiers.
*Agents* or *actors* — unusable, total collision with "AI agent".

**Provisional recommendation, unratified:** data is the substrate; the three are
faculties; each has a **mandate**. The last term is the author's own, from the original
brief — "a properly instructed LLM with enough mandate" — which makes the vocabulary for
the authority dimension native rather than imported.

**Do not rename across the repository until this closes.** A collective noun is a
rhetorical choice, the §III rewrite is already owed, and renaming twice costs more than
deciding late.

### CON-OP-10 — RULED — What is the second faculty called, now that it designs as well as interprets?
**✅ STATE: RULED 2026-09-21**
Opened 2026-09-20, session 02, as the residual of `CON-OP-9`.

[ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md) rules that a faculty
is named by its function and never by its implementation, which forecloses *the LLM*, *the
model* and *the AI* and leaves the second faculty without a name. The difficulty is that
its work has grown since
[100_system-overview.md](../docs/10_architecture/100_system-overview.md) named the
capability **Sense-making**. The author's formulation on 2026-09-20 was *analysis and
design*, and the second half of that is not covered anywhere in the current architecture:
choosing a modelling pattern, a historisation strategy, a grain or a compile target is not
sense-making, and `ARC-OP-19` records that the autonomy tiers cannot classify it either.

The candidates carry the same kind of cost the collective noun did. *Sense-making* is
accurate for the semantic half and silent on the design half. *Analysis* is the author's
word and collides with the automated analyses of Phase 3, which are an artifact the system
produces rather than a faculty that produces them — a collision landing exactly where the
teleological tier is already weakest. *Interpretation and design* avoids both and is
longer. *Design* alone drops the semantic half, which is the larger half.

This is cheap to decide and it blocks, because every document the §III rewrite touches
needs the word. Decide inside that rewrite, with `CON-OP-9`'s rename.

**Proposal from the author, 2026-09-21, not yet ruled: *agents* or *agentic*.** His ground
is that the faculty is not a model but a working system — a heartbeat (in his musical terms,
a MIDI clock), workflows, documented procedures, memory, and LLMs. Two things the ruling
should state rather than leave to interpretation. [ADR-0008](../docs/20_decisions/0008-faculties-substrate-mandate.md) rejected *agents* as the
collective noun for all three faculties because of the collision with "AI agent"; that
objection was to calling the humans and the deterministic engines agents too, and it does
not bite on the one faculty that is in fact built from agents. And the same ADR forbids
naming a faculty after its implementation; the author's description names the arrangement
rather than the model, which is within the rule's intent — it was written to stop *the LLM*
being the name — but the ruling should say so. The architecture already uses *agent* for the
unit of work ([130_agent-loop.md](../docs/10_architecture/130_agent-loop.md), `ARC-OP-8`), so
*agentic* for the faculty and *agent* for its workers would be consistent.

**Ruled 2026-09-21 by the author: the agentic layer**, recorded as
[ADR-0010](../docs/20_decisions/0010-the-agentic-layer.md), which states both readings of
ADR-0008 explicitly. An *agent* is a unit of work inside the layer. `RULED` rather than
`EXECUTED` because the rename across the repository is owed with `CON-OP-9`, in the §III
rewrite.

### CON-OP-11 — Is the amortisation threshold, rather than statability, the manifesto's spine?
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from the author's distinction between broad and specific
generalisations.

The author's formulation: the second faculty applies **broad generalisations** — design
patterns such as Data Vault, which hold across the discipline — and **specific
generalisations**, which hold only for the particular systems, organisation and
administration in question.

[005_manifesto.md](../docs/00_concept/005_manifesto.md) §III has no place for the second
kind. It runs on a binary: knowledge is general, and migrates into deterministic
machinery, or it is particular with a domain of one, and cannot. The external pass broke
that binary at precisely this point — Q3 found that there is no general rule about
*KLANTNR* but there is a perfectly general and learnable rule about how to infer what a
column like *KLANTNR* means.

The distinction supplies the missing middle term, and it does so by conceding Q3 rather
than resisting it. Generalisations are not general or particular; they occupy an axis of
**domain size**. Data Vault holds across the discipline. A convention that one ERP
instance suffixes its foreign keys a particular way, or that one administration extended
rather than replaced its code lists in a migration, holds over four hundred columns in one
landscape and nowhere else. That is not a fact with a domain of one. It is a rule with a
domain of four hundred, and it was never written down — not because it is unstatable, but
because discovering, stating, testing and maintaining it never repaid a human at that
domain size.

Stated that way, this row and
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
are one claim at two altitudes: **the threshold of domain size at which a generalisation
repays its own authorship has collapsed.** Broad generalisations were always above the
threshold, and the canon adopted them subject to the maintenance-cost compromises §3 of
that document lists. Specific generalisations were always below it, so the discipline
handled them one instance at a time and called the handling *the human factor*.

Nothing about the *kind* of knowledge is at issue on this reading, which is why it
survives an attack §III did not. It is also why `CON-OP-8` may pose a false choice.

Against it, recorded because the synthesis is suspiciously tidy and arrived at the moment
a tidy synthesis was most welcome: it was produced by the model from the author's
distinction inside a single exchange and has been examined by nobody; it has not been
checked against the codification literature, which is `CON-OP-4`; and the structural half
of what it calls a specific generalisation already has a mechanised literature, which is
`CON-OP-12`. Its falsifier is `EVI-OP-5`.

Decide inside the §III rewrite, together with `CON-OP-5`, `CON-OP-6`, `CON-OP-7` and
`CON-OP-8`.

**Narrowed 2026-09-20, session 03, by external review.** Reviewed on gpt-5.6-sol —
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md)
— and the domain-size axis failed. Repayment is an expected-value quantity — expected
reuse, value per correct application and stability, set against discovery, validation,
execution and maintenance cost — in which extension is one multiplier among several. This
row promoted one benefit proxy into the governing axis.

The counterexample is the repository's own apparatus. Anchor-style 6NF has a
discipline-wide domain and
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
§3 records it as almost unused, on object-count and join-complexity grounds: maximal
domain, no adoption. In the other direction a two-value regulatory mapping is carefully
authored because it executes on every transaction and is stable. Cardinality predicts
neither case.

What survives is the narrower claim that was already available before this row was
opened: machine authorship lowers one cost term, the generation and maintenance of
deterministic machinery. The unification with the canon-cost argument falls with the axis,
and it falls on the ground `CON-OP-8` had already stated against itself — in the canon
case the generalisation is known and what changed is the cost of expressing it; in the
semantic case the rule must be inferred from noisy local evidence and validation may
dominate generation. To rescue the axis, this row must show that adoption varies
systematically with extension size while frequency of use, stakes, stability, confidence
and elicitation cost are held roughly constant. `EVI-OP-5` as scoped does not measure that.

The row stays `OPEN` because the §III rewrite must still decide what replaces statability;
what this row proposed is no longer a candidate. `ARC-OP-16`, `ARC-OP-17` and `ARC-OP-18`
are not void with it — each was argued from locally-general rules existing, not from domain
size explaining them — but each now needs re-deriving from the expected-value framing
rather than inheriting this row's premise.

**The counterexample was checked 2026-09-20, session 04, and survives its own wording.** Per
[2026-09-20-canon-survey](../docs/30_research/notes/2026-09-20-canon-survey.md) §1.3, *almost unused* fails as stated: the Anchor paper self-reports
production use in insurance, logistics and retail, an OLTP system managing a million
customers, and warehouses to a terabyte. That is the method's own authors reporting, so it
is weak evidence of adoption, and it defeats only the absolute wording. What the
counterexample needs is that Anchor is rare *relative to what a discipline-wide domain would
predict*, and nothing found contradicts that. The refutation stands; the sentence carrying
it should not be requoted in its original form, and this repository has no adoption figure
for any methodology.

**Corrected 2026-09-21 by the author: *almost unused* stands.** The deployments the Anchor
paper reports are its own authors', clustered around Stockholm and the university that
teaches the method. Against the thousands of organisations that do not use it, that is
proximity, not adoption. The block above over-corrected on weak evidence, and its instruction
not to requote the original wording is withdrawn. The claim remains an estimate without a
figure.

### CON-OP-12 — Locally-general rules are already mined mechanically, and the claim must narrow accordingly
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, alongside `CON-OP-11`.

Functional-dependency and denial-constraint discovery — the Metanome line of work and its
successors — mines rules that hold over one particular dataset and nowhere else,
automatically, and has done for roughly fifteen years. That is the structural half of what
`CON-OP-11` calls a specific generalisation, and it is neither new nor model-produced.
Stated without that qualification the claim is refutable in one sentence by anyone who
knows the literature, which is the most expensive kind of wrong this project can publish.

What the mining literature does not cover is the half the author means: conventions about
**meaning and administration** rather than about data shape. *Every table in this ERP
instance suffixes its foreign keys this way* is shape, and is mined. *This administration
extended rather than replaced its code lists in the 2019 migration, so a code's meaning
depends on the date it was issued* is not recoverable from the data at all, and is what
the second faculty is claimed to supply.

Per [`../AGENTS.md`](../AGENTS.md) rule 8 the characterisation above is stated from general
knowledge and is unverified; it is a hypothesis until sourced. Closes against
[050_prior-art.md](../docs/00_concept/050_prior-art.md) with a verdict on the mining
literature and an explicit statement of the boundary. Related to `CON-OP-1` and
`CON-OP-4`; all three close against the same document.

### CON-OP-13 — RULED — the sources are sensory, the integrated store is memory
**✅ STATE: RULED 2026-09-20**
Opened and ruled 2026-09-20, session 02, on the author's refinement of the organism
metaphor.

[010_vision.md](../docs/00_concept/010_vision.md) calls the data sources the
organisation's sensory information, and
[020_critique.md](../docs/00_concept/020_critique.md) §5 accepts sensing as one of the
three places the metaphor earns its keep. Integrated, historical, retained data is not
sensation in any organism, and calling it so obscures what the system actually does.

**The ruling, in the author's terms:** data in flight is sensory; from the moment it is
captured and stored it is **memory**. The sources and the real-time surfaces are the
sensory apparatus, the integrated historical store is memory, and the faculties are what
turn the first into the second.

Two consequences, which is why this is worth a row rather than being a matter of taste.
It names the step the loose usage was concealing: no organism stores its sensory stream,
and the operation that turns sensation into memory is a selection that discards nearly
everything — which is
[145_entropy-and-pruning.md](../docs/10_architecture/145_entropy-and-pruning.md)'s
argument arriving from the metaphor's own logic rather than as a correction to the brief.
And it is an instance of [ADR-0003](../docs/20_decisions/0003-codename-nsdn.md) working as
intended: the analogy is productive as a private heuristic at exactly the point where its
loose use was misleading.

**Residual, which is why this row is `RULED` and not `EXECUTED`:** the distinction is in
no document. It belongs in [020_critique.md](../docs/00_concept/020_critique.md) §5 and in
[030_glossary.md](../docs/00_concept/030_glossary.md), and lands when the concept documents
are next revised. Per [`../AGENTS.md`](../AGENTS.md) rule 2,
[010_vision.md](../docs/00_concept/010_vision.md) is a verbatim transcript and is not
corrected.

### CON-OP-14 — Is the human faculty's mandate adjudication alone, or adjudication, elicitation and purpose?
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from the author's statement that ideally the human is there
only for final adjudication.

That statement understates the human mandate by one function, and the repository says so
twice. [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) Tier 3 and
[170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md) Surface 3 both
hold that the system does not originate purpose: it works against a decision register that
people maintain, and an artifact that cannot cite an entry is not built. Maintaining that
register is origination, not adjudication, and
[400_phasing.md](../docs/40_roadmap/400_phasing.md) states what a system without one
produces — statistically true irrelevance, at scale.

**The move that would rescue the statement**, recorded because it is interesting rather
than because it is endorsed: the system observes what decisions an organisation actually
makes — which reports are produced and consumed, which queries recur, which numbers are
demanded at which cadence — and *proposes* a decision register for a human to rule on.
Origination then collapses into adjudication and the author's sentence becomes true.

Three objections to it. Nothing in the architecture currently supports the observation
step. It inverts the dependency in `ARC-OP-12`, which assumes the register is a human
input that may simply never be supplied. And it risks the worst available version of the
teleological failure: a register inferred from what an organisation already measures
contains, by construction, nothing about what it should be deciding and is not, which is
precisely the failure
[105_autonomy-tiers.md](../docs/10_architecture/105_autonomy-tiers.md) names at Tier 3.

**The second objection is `CON-OP-7(b)` and is already established.** Adjudication
presupposes an adjudicator who holds the proposition. Where semantics exist only as a
negotiated synthesis across operations, finance, legal and system owners, with no
participant holding it whole, there is nobody to rule and the cost reappears as
**elicitation**. A mandate stated as adjudication alone assumes away the cost the external
pass found to be the real one.

The candidate formulation, unratified: the human faculty's mandate is **adjudication,
elicitation and purpose**, with elicitation a first-class expense rather than a
precondition that will be arranged. Whether purpose can be collapsed into adjudication by
the move above is what this row decides. Related to `ARC-OP-12`.

**Narrowed 2026-09-20, session 03, with a capability-side argument.** [060_faculty-inventory.md](../docs/00_concept/060_faculty-inventory.md)
dimension 9 — negotiation and value-setting — was added by external review on the test that
a dimension must flip an allocation. It flips this one. Inferring a metric's likely meaning
from documentation goes to the second faculty; defining *net revenue* where Finance and
Sales hold conflicting legitimate interests goes to a human, and specifically to one with
the authority to bind both, which is not any human.

The point is that the second faculty's barrier here is **standing, not skill**. It can
surface the conflict, enumerate the positions and draft a reconciliation; it cannot make
anyone accept one, and no increase in capability changes that. So where a semantic question
is actually a contested value question wearing a definitional costume — which is a large
share of the hard cases in this discipline — the work is not adjudication of a proposal at
all. It is settlement between parties, which is the elicitation cost this row exists to
name, arriving from the capability side rather than from `CON-OP-7(b)`'s distribution
argument. Two independent routes to the same conclusion strengthens the candidate
formulation without settling it.

### CON-OP-15 — What is the success criterion, and is it one claim or two?
**⛔ STATE: OPEN**
Opened 2026-09-20, session 03, from the author's statement of the end game, recorded
verbatim in [001_mission.md](../docs/00_concept/001_mission.md).

The author's formulation is *increase development speed and quality by orders of
magnitude*. Three things in it need deciding before it can be a criterion rather than an
ambition.

**Speed of what, and quality of what.** Speed admits an orders-of-magnitude claim; quality
does not, because quality is bounded above and nothing is a hundred times more correct than
correct. The claim becomes coherent only when quality is replaced by a quantity with room
to move. Two candidates are recorded in
[001_mission.md](../docs/00_concept/001_mission.md): defect density, and **coverage** — the
share of the landscape modelled at all, which moves by orders of magnitude if modelling
cost collapses, without any single artifact being better than good human work. Coverage is
the stronger reading and is not yet ratified.

**Whether it is one claim or two.** Read against `CON-OP-8`, speed is the first thesis and
coverage is the second, so the author's formulation asserts their conjunction — precisely
the interaction external review has so far refused to grant. This row must not be used to
smuggle that conjunction in. What the formulation supplies is a hypothesis with a known
provenance: a practitioner of twenty-six years expects the halves to be one thing. That is
a reason to look harder for the interaction before conceding there is none, and it is not
evidence that one exists.

**Against what it is measured.** A speed claim without a defect-rate floor is the ordinary
way this discipline produces fast rubbish, and nothing currently states the floor.
`EVI-OP-1` owes the ground truth any such measurement needs.

Closes in an ADR, and the ratification is the author's rather than a model's. Depends on
`CON-OP-2` for the arithmetic and on `CON-OP-8` for whether the criterion is unitary.
Related to `BIZ-OP-1`, since the offering's shape — method, product or practice — changes
what evidence the criterion needs.

**Narrowed 2026-09-20, session 03, by external review.** The wording now lives in
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md), a living document
with a changelog; this row holds the question, that document holds the current answer. Per
[XREV_2026-09-20_mission-statement_sol](../docs/30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
two things are settled enough to record.

**A coverage measure must be value-weighted by people or it rewards legible abundance.** The
candidate measure — coverage gained per unit of human adjudication — is maximised by
modelling thousands of easy, stable, low-value tables under one coarse bulk approval,
scoring well while diverting scarce experts from the few consequential claims and enlarging
the trusted surface. The repair is to measure coverage *of what people have prioritised*,
and the repair is forced rather than chosen: deciding consequence is exactly what
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) forbids the system to do, so
the weighting cannot come from the system.

**That makes this row depend on `ARC-OP-12`**, which asks who maintains the decision
register and records that it may simply never be supplied. If no one maintains it, the
mission has no value weighting, the measure reverts to abundance, and the criterion is
unmeasurable rather than merely unmeasured. This is a harder dependency than the ones
already listed and should be treated as such.

**The finding generalises past this row.** Any coverage-shaped measure the project adopts
inherits the same defect, including in
[410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md).

**Narrowed again 2026-09-20, session 03, on the author's correction.** The author rejected
the *understanding* framing as academic drift and restated the objective as building a
landscape at lower cost and higher quality, with coverage an aspect of quality rather than a
separate measure. Both are adopted in
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md) version 0.5.

**The criterion now has a concrete falsifiable test**, which is the most useful thing to
happen to this row: *whether ordinary teams can implement and maintain otherwise-appropriate
designs, Data Vault among them, whose principal obstacle is modelling labour, without higher
defect rates or disproportionate validation cost.* It replaces an unfalsifiable
orders-of-magnitude claim with something that can be run.

**Its load-bearing assumption is unverified and is named as such.** The test selects designs
by the kind of obstacle, so it holds only where modelling labour genuinely is the principal
obstacle. Operational and cognitive complexity may dominate instead — which is exactly what
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
§3 records for Anchor-style 6NF and what refuted `CON-OP-11`. Establishing which obstacle
dominates for Data Vault belongs to `ARC-OP-14`'s canon survey, and the residual — that a
machine-optimal design still owes a human-comprehensible surface — is `ARC-OP-15`.

**The human-prioritisation guard was lost and restored.** Version 0.4 moved it from the
measure into a clause about who sets priorities, where it constrained nothing. A guard
stated as authority is not a guard on a scorecard.

**Partly answered 2026-09-21 by [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md).** *One claim or two* is answered for the
capabilities: they are separate, the list is open, and no conjunction is asserted, so the
concern above about smuggling an interaction in through this row no longer applies. What
success means for each capability, and the value-weighting problem, remain open and remain
the author's to rule.

**Superseded in part 2026-09-20, session 03**, by version 0.6: the test no longer selects
designs by *principal obstacle is modelling labour* but by *total lifecycle burden currently
exceeding ordinary teams' time, budget and validation capacity*, with an added guard against
displacing the burden downstream. The author's argument and the reviewer's concession are in
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md)'s changelog; the
consequence for the canon survey is in `ARC-OP-14`. Everything below this line about the
obstacle classification is retained for provenance and is not a current claim.

### CON-OP-16 — Is the maintenance share the measure of success?
**⛔ STATE: OPEN**
Opened 2026-09-25, session 05, from the author's *Generative Structures* paper, mapped onto this
project in
[2026-09-25-generative-structures-mapping](../docs/30_research/notes/2026-09-25-generative-structures-mapping.md)
at his request and accepted by him.

The paper's one distinctive prediction is that in any growing stack of capability the **maintenance
share** — the fraction of effort spent keeping the existing stock working rather than extending it —
rises secularly, and approaches exhaustion before breakdown. In a data landscape that is the familiar
path to the rebuild. The candidate criterion: nsdn succeeds if the maintenance share stays flat or
falls as the landscape grows, at an unchanged defect rate.

It is a candidate for `CON-OP-15`, where it would give *lower cost at higher quality* a trajectory
rather than a snapshot, and a second figure for `CON-OP-2` next to the break-even in columns. It is
measurable in a sandbox: add sources one at a time and log agent-minutes and human-minutes, split
between maintaining and building. The weekly budget report of
[155_adjudication-economy.md](../docs/10_architecture/155_adjudication-economy.md) already counts
human minutes and would need that split. Owed: a definition of *maintaining* versus *building* that a
log can apply without judgement; whether agent effort and human effort are summed, weighted or kept
apart; and the author's ruling on whether this is the criterion, a criterion, or a diagnostic.

**Narrowed 2026-09-25, session 05, by external review**, recorded in
[XREV_2026-09-25_generative-structures-mapping_astra](../docs/30_research/notes/XREV_2026-09-25_generative-structures-mapping_astra.md)
and [XREV_2026-09-25_maintenance-share_sol](../docs/30_research/notes/XREV_2026-09-25_maintenance-share_sol.md),
all findings accepted by the author. **The share on its own fails as a measure.** It measures
spending, not adequacy — it can stay flat while burden grows — and in an organisation it is broken
outright by relabelling maintenance as new work, by rebuilds booked as new programmes, by deferred
maintenance, and by upkeep displaced to analysts, business users and vendors.

The candidate is restated: **maintenance effort per stable unit of landscape, while burden indicators
hold steady.** Stock is counted in stable operational units — supported sources, governed data
products, dependencies, service commitments — not in releases or tickets. Burden indicators are
maintenance backlog age, unsupported components, control exceptions, recovery-test results and
severity-weighted defects in absolute terms, not only as rates. In the paper's model this trend
estimates θ, whether burden grows faster than the landscape. The share is kept as a diagnostic.

Guards, all owed: classify work by counterfactual — *would it be needed merely to keep existing
service running?* — with a sample audited independently, which answers the first owed item above;
charge rebuilds and dual running to lifecycle maintenance unless they deliver independently valued
capability; count effort across everyone who does it, not only the team, which is the principle that
cost must not simply move elsewhere; report human attention, compute cost and elapsed recovery time
separately, never as one effort total, consistent with
[155](../docs/10_architecture/155_adjudication-economy.md); and compare at fixed capacity, so that a
sponsor's budget cut or expansion does not move the measure.

**Not yet computable, 2026-09-26, session 06.** Two sources and then three more at once were acquired;
none has been refreshed, so none counts as stock and no epoch can be compared. The blind audit found work
class reliable in only 7 of 15 steps, so the numerator cannot yet be trusted either (`PRC-OP-6`).

### CON-OP-17 — Does cheaper building owe a pairing with the maintenance value areas?
**⛔ STATE: OPEN**
Opened 2026-09-25, session 05, from the same note as `CON-OP-16`.

In the paper's terms, the *cheaper building* value area raises capability, while *metadata*,
*monitoring, troubleshooting and testing* and *continuous improvement* raise maintenance efficiency.
With burden coupled to capability, faster building without better maintenance reaches the point of an
unmaintainable landscape sooner. If that holds, cheaper building is safe only in company with at
least one maintenance value area — an interaction between value areas, which
[ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md) rules is not owed.

This row records the question and deliberately drafts no interaction candidate, per the handover's
standing instruction. It is the author's to rule whether it reopens ADR-0009, is answered by it — the
capabilities stay separate as claims while an implementation is advised to adopt them together — or is
dismissed. `CON-OP-16` would supply the evidence either way: a sandbox that builds cheaply without the
maintenance capabilities should show the maintenance share rising.

**Narrowed 2026-09-25, session 05, by external review** on GPT-6 Astra, recorded in
[XREV_2026-09-25_generative-structures-mapping_astra](../docs/30_research/notes/XREV_2026-09-25_generative-structures-mapping_astra.md)
and accepted by the author. In the paper's model the cost of building does not move the threshold; it
only brings it nearer if the savings are spent on building more. The question is therefore narrower
than an interaction between value areas: **whether the savings from cheaper building are all spent on
more building, or partly on maintenance.** That is a question about how an implementation allocates
its capacity, and it probably no longer bears on ADR-0009. It remains the author's to rule. The
evidence is now the restated measure of `CON-OP-16` — maintenance per stable unit, with burden
indicators — rather than the share.

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

**2026-09-20, session 02.** `ARC-OP-18` proposes the counterweight this row asks for, and
proposes it as a replacement for the ranking quantity rather than as a correction to it:
rank by the **scope of the rule a question settles** rather than by the degree of the
entity it concerns. Scope is computable, it measures what a ruling actually buys, and it
carries no bias toward the already-understood — the obscure administration with one
unreadable convention governing three hundred columns ranks high precisely because nobody
understands it. Work this row with `ARC-OP-18` and `ARC-OP-17`.

### ARC-OP-7 — Context layer: files, graph, or both?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 12)*

[120_context-layer.md](../docs/10_architecture/120_context-layer.md) argues for markdown
cards in git with a derived, disposable graph index, and states the honest objections —
git discomfort past roughly a hundred thousand files, and history thrashing from
high-frequency profile updates. The most consequential unmade decision in the
architecture; it should be settled by an ADR and not by drift.

**A candidate answer, 2026-09-25, not a ruling:** *both, split by kind.*
[120_context-layer.md](../docs/10_architecture/120_context-layer.md) now distinguishes five
kinds of context. Knowledge, decisions and know-how would be cards in git, which keeps the audit
trail where it matters; landscape facts, which are high-volume and volatile, would live in a
database written by deterministic machinery, with only conclusions promoted to cards; working
memory would live in an expiring task journal. The derived graph and search index span all of
them and stay disposable. This meets both of the objections recorded above. It still wants an
ADR.

**Revised the same day:** six kinds, not five. External review in [XREV_2026-09-25_context-system_astra](../docs/30_research/notes/XREV_2026-09-25_context-system_astra.md) separated
durable **workflow state** — awaited approvals, checkpoints, records of actions taken — from
expiring working memory, and added evidence snapshots and a version manifest so the split
across stores cannot silently lose the evidence behind a ruling.

**Partly answered 2026-09-25 by [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md), ruled by the author.** The logical model is
decided: assertions are the canonical record, cards are generated views of them, and separate
stores share one identity plane with policy-filtered indexes and a publication pipeline. The
**physical medium for assertions** — git, a database, or both — is not decided, and 120's
audit-log argument for git now applies to assertions rather than to cards. This row stays open for
that.

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

**2026-09-20, session 02.** `CON-OP-14` records a proposal that would invert this row's
dependency rather than answer it — the system proposing a decision register from observed
decision behaviour, for a human to rule on — together with the reason it may produce the
worst available version of the Tier 3 failure instead of a solution. Neither row is
decided; this one should not be closed by the other without that objection being met.

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

**The survey's classification changed 2026-09-20, session 03.** It was to separate designs
rejected for authoring cost from those rejected for runtime cost. That distinction was
dissolved by the author and conceded by external review in [XREV_2026-09-20_mission-statement_sol](../docs/30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
third sitting: authoring, comprehension, query construction and optimisation are not
distinct obstacle classes but **locations where lifecycle work accumulates**, and naming
only the first of them *labour* arbitrarily privileges where the work happens. 6NF is the
case in point — it does not avoid modelling labour so much as relocate it into query
authoring and performance tuning.

**So the survey should classify each design by where its lifecycle work accumulates**, and
report that as a distribution rather than as a rejection reason. Two things stay outside
the labour account and should be recorded separately for each candidate: runtime and compute
cost, which is not effort though it draws on the same budget and whose bindingness is now an
empirical question given columnar execution and join elimination; and the adjudication
surface, per `ARC-OP-15`.

This makes the survey the instrument that settles whether Data Vault's burden is in fact
the kind machine authorship can absorb, which
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md) version 0.6 names as
its load-bearing empirical assumption. That promotes this row again.

**First half discharged 2026-09-20, session 04**, in [2026-09-20-canon-survey](../docs/30_research/notes/2026-09-20-canon-survey.md). The row stays `OPEN`
because the second half — re-evaluating the designs that survive — is not attempted, and
because the survey changed which designs are eligible for it.

Four verification verdicts. Anchor's schema-evolution property holds. SQL:2011 supplies
valid and transaction time and is silent on versioning derivation logic, so the rule-set
axis is outside the standard rather than underused. The Kimball attribution **fails**: he
argues two reasons, understandability and predictable query performance, and holds
normalised ER modelling to be unsuitable for decision support rather than
correct-but-expensive, so §190 §3 loses one of its three headline examples. *Almost unused*
for Anchor fails as worded — its authors self-report production use in insurance, logistics
and retail — while the counterexample that sentence carried against `CON-OP-11` survives in
substance.

The classification produced the finding this row did not anticipate. **The eight candidates
are not eight of a kind**: three are designs with a rejection history, two are artifacts the
system emits, and three are declaration disciplines. Explicit units, currencies, timezones
and grain is the clean case — its cost was never authorship but semantic determination, so
it belongs to the second thesis and is misfiled under the first. Assertions at maximum
granularity are bound by adjudication volume, which is the scarce faculty rather than a
cost cheap authorship relieves. Presenting either as an instance of *correct-but-unaffordable
designs now affordable* counts the first thesis's dependencies as its evidence.

Two consequences leave this row. The runtime relief the programme rests on is conditional
and is now `ARC-OP-22`; the measurement it needs is `EVI-OP-6`. The Data Vault assumption
this row was promoted to settle came back adverse — see `CON-OP-8`.

**Reviewed by the author 2026-09-21.** Five corrections and additions, all from practice
rather than literature, and on three of the four points where they disagreed with the survey
they outrank it.

**The strongest case for cheaper building is not in §190's list as written.** It is the
projection from the record-keeping layer into the marts. The architecture the author calls
mature is layered — raw data, then a Data Vault for complete record keeping ("all the data,
all the time"), then dimensional marts for self-service because they are human-readable —
and the vault and temporal layers are never exposed as they are. Building and maintaining
that projection is expensive hand work wherever it is done. It is the candidate *redundant
physical representations*, which should lead the list.

**Rule-versioned bitemporality is strengthened.** One can argue rules have no place in a
warehouse, but in practice they are applied there — not everything can be a separate
calculation engine — so the warehouse is where rule versions must be tracked, and SQL:2011
does not track them.

**Kimball returns in a reversed role**: the design that won *because* it is cheap for humans,
accepting known weaknesses with evolving environments, new sources, and overlapping data
such as that of acquired companies. Kimball's own strategies for those, and the conceptually
harder parts of the method, are seldom implemented. **Features skipped inside the most-used
method are better evidence for the building capability than whole methods the canon
rejected**, and the survey's second half should look there first.

**Explicit units and grain, and maximum-granularity assertions, belong to the metadata
capability**, not to cheap building. Under [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md) that is a reassignment, not a loss.

**Sign-off work scales with real business entities and their keys, not with tables.** Forty
attribute tables restate one identity decision. That bounds the metadata workload.

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

**2026-09-20, session 02.** The presumed resolution this row calls an assertion rather than
a design now has a candidate shape: `ARC-OP-20`'s constitution-and-legislation partition,
with `ARC-OP-19` asking the prior question of who rules a design claim at all. `ARC-OP-18`
raises the same comprehension problem one level up, since ruling on a convention means
ruling on a claim about objects the adjudicator cannot see. Work the four together.

**Sharpened 2026-09-20, session 03.** Per [XREV_2026-09-20_mission-statement_sol](../docs/30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
third sitting, two statements that this row previously left implicit.

First, comprehensibility does not reduce to cost. Adjudication capacity is labour, but it is
scarce, specialised and non-fungible, so a representation that stops a qualified person from
reliably judging a claim fails
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md)'s mandate as a **quality**
problem rather than as an expense. An organisation cannot buy its way out of it the way it
can buy compute.

Second, and this is the constructive half: that is not a verdict against complex physical
models. Tooling can present a comprehensible semantic view over a complex physical one, so
**the thing to assess is the adjudication surface, not the object count.** Every argument in
this repository that reasons from table counts to human comprehensibility — including
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
§3 on Anchor — is using a proxy, and this row is where the proxy is replaced by the thing
itself.

### ARC-OP-16 — The context layer has no card kind for a rule that holds over a set of objects
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from `CON-OP-11`.

If specific generalisations are real, they must be **artifacts**. A local rule that exists
only in a context window is re-derived inconsistently from job to job, carries no
provenance, cannot be adjudicated and cannot be pruned — which is to say it has none of
the properties [120_context-layer.md](../docs/10_architecture/120_context-layer.md) exists
to guarantee, and the system would be reasoning through something it cannot inspect.

That document's card kinds are `source`, `dataset`, `field`, `entity`, `metric`,
`decision`, `hypothesis`, `assertion`, `artifact` and `question`. Every one of them is
about an object, or about a proposition concerning an object. None is about a rule holding
over a *set* of objects.

What such a kind needs beyond the standard assertion record is a declared **scope** — the
set of objects over which the rule is claimed to hold, stated as a URN pattern or as an
enumeration — together with the counterexamples found inside that scope, which are what
distinguish a rule from a coincidence. The rest of the assertion record applies unchanged:
provenance, confidence, falsifier, review date. A rule card is also the natural unit of
the pruning discipline in
[145_entropy-and-pruning.md](../docs/10_architecture/145_entropy-and-pruning.md), since a
convention invalidated by a migration takes its dependent assertions with it.

Depends on `ARC-OP-7`, which has not settled whether the context layer is files, a graph,
or both, and which this row makes more consequential rather than less.

**Shape settled 2026-09-25 by [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md):** a rule is an **assertion type** whose scope is a
set of objects, not a separate card kind, and — per
[124](../docs/10_architecture/124_context-write-back.md) — it is accepted on its own evidence, never
by promotion from a claim about one member. What remains open is the scope syntax and how
counterexamples are recorded.

### ARC-OP-17 — Rule-mediated inference produces correlated error, and the calibration story assumes independence
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from `CON-OP-11`. The most consequential of the rows that
distinction generated.

[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) rules that thresholds at the
semantic tier are set from measured precision against a held-out adjudication set, and
[160_evaluation-and-regression.md](../docs/10_architecture/160_evaluation-and-regression.md)
builds the instrument. Both treat the system's errors as roughly independent: sample the
rulings, score the hypotheses, obtain a precision figure that means something.

A system reasoning through locally-general rules does not produce independent errors. One
wrong convention yields four hundred assertions that are all wrong, in the same direction,
for the same reason. A uniformly sampled held-out set then misestimates precision badly
and in whichever direction the sample happened to fall — reporting near-perfect precision
on a landscape riddled with one systematic mistake, or catastrophic precision on a
landscape carrying only that one.

This is not a refinement of the measurement. It undermines the mechanism by which autonomy
is granted at Tier 2, which is the mechanism
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) rests on, and it does so
without announcing itself, because a precision figure computed the current way looks
exactly as trustworthy as one computed correctly.

It also subsumes `ARC-OP-5`: per-source reliability is the coarse version of the same
observation, and rule scope is the sharper one, since a convention may span sources and a
source may host several conventions. The candidate repair is `ARC-OP-18` and the two
should be worked together.

### ARC-OP-18 — Stratify adjudication by rule rather than sampling over instances
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, as the candidate repair for `ARC-OP-17` and the largest
gain available from `CON-OP-11`.

If assertions cluster under rules, the correlation that breaks calibration is also the
leverage. Put the convention to the human, not the four hundred columns it governs. One
ruling then buys the whole block, and adjudication burden — the quantity
[410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md) identifies as
determining whether humans keep participating at all — falls by the block size rather than
by a constant factor. This is the mechanism by which the manifesto's claim that
adjudication is viable becomes arithmetic rather than hope.

Two existing rows change shape as a consequence, and both are annotated above. `ARC-OP-6`
gains the counterweight it asks for, in the form of scope-of-rule as the ranking quantity.
`EVI-OP-1`'s hand-built answer key must be constructed to **span rules** rather than to be
a random sample of entities, or it measures the system's performance on whichever
conventions it happened to include.

What is unresolved is what a human is actually shown. Ruling on a convention means ruling
on a claim about four hundred objects the adjudicator cannot see, which is the same
comprehension problem as `ARC-OP-15` at a different scale, and a ruling given on a
summary is worth what the summary was. Some evidence discipline is owed here — a sample of
instances drawn adversarially rather than favourably, and an explicit record of the
counterexamples the system found and discounted.

**Placed 2026-09-25** in [155_adjudication-economy.md](../docs/10_architecture/155_adjudication-economy.md):
ruling on patterns rather than instances is the main lever on review cost, and precedent — later
cases auto-accepted under an accepted rule, monitored and sampled — is its largest multiplier. Audit
sampling there is stratified by rule for the reason this row gives.

### ARC-OP-19 — Design is a fourth kind of claim and the autonomy tiers do not classify it
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from the author's statement that the second faculty designs
as well as interprets.

*Choose Data Vault for this source; historise at this grain; compile a redundant star for
these consumers; do not copy this source at all.*
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) cannot classify such a claim.
It is not **structural**, since it is not computable from the data and the catalogue. It is
not **semantic**, since it is not about meaning, identity or authority. It is not
**teleological**, since it is not about what is worth knowing. It is a **design claim**,
and what adjudicates it is a principle rather than a fact — a different act from the one
[170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md) Surface 1 is
built for, and one that a source owner is not the right person to perform.

At present such claims would enter the system as Tier 1, on the strength of
[140_data-vault-automation.md](../docs/10_architecture/140_data-vault-automation.md)'s
*mechanical given keys*, which is true of hub and satellite generation from a declared key
set and false of everything above it.
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
§3 opens a whole space of these choices and does not say who makes them.

**This does not reopen [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md).** The
tiering stands and is on the do-not-reopen list; the question is whether its enumeration is
complete. Whether the answer is a fourth tier, a cross-cutting classification, or the
constitution-and-legislation partition in `ARC-OP-20` is what this row decides.
`ARC-OP-15` is the visible edge of the same problem and should be worked with it.

### ARC-OP-20 — Which methodologies, declaration languages, execution engines and principles are admissible
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, from the author's statement that design and architectural
principles should drive tool and methodology choices.

That statement runs two layers together, and separating them is the first half of this row.
The **constitution** is what machinery may exist at all: which modelling methodologies are
admissible, in which declaration language artifacts are expressed, on which execution
engine they run, and under which architectural principles the choice was made. The
**legislation under it** is which hubs, which satellites, which capture cadence, which
compile target — instance design, made by the second faculty and adjudicated.

The constitution is not open to the machine. A second faculty free to choose its own tools
produces heterogeneous machinery across one landscape, which forfeits the regenerability
that [180_technology-posture.md](../docs/10_architecture/180_technology-posture.md) treats
as the point of the posture and, with it, the reproducibility
[ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md) exists to protect. It
is settled once, by a human, in ADRs.

What is open is the constitution's **content**, and nothing in this repository has adopted
any of it. [180_technology-posture.md](../docs/10_architecture/180_technology-posture.md)
lists candidates — DuckDB, sqlglot, dbt-core, AutomateDV, sketch libraries, OpenLineage —
and says in as many words that nothing is adopted. The principles that would justify a
choice are stated there as four properties — declarative over imperative, regenerable,
small files with stable identity, boring and well documented — and have never been
ratified as principles, which means they currently operate as preferences wearing a
principle's clothing.

Three things are owed, in this order. Ratify the principles. State the admissible
methodology set with the reason each is admissible, which is where `ARC-OP-14`'s canon
survey lands and is the point at which
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
§4's separation of authoring cost from runtime cost becomes load-bearing rather than
cautionary. Only then adopt a declaration language and an execution engine, each in its own
ADR. Adopting tools before the principles are ratified produces the ordinary outcome, which
is a stack chosen by familiarity and a principle written afterwards to justify it.

Depends on `ARC-OP-19` for who rules a design claim at all, and on `ARC-OP-11` for the
SQL-dialect question any declaration language must answer.

**The author's statement, 2026-10-06, session 07:**

> Yes. And I’d like the code base for the data warehouse to sit in git. So rather to have ascii files than proprietary binaries. And rather more small files than a few large ones (easier diffing)

This makes the fourth of 180's candidate properties, small files with stable identity, a stated wish of the author
rather than only the model's preference, though not yet a ratified principle. It widens to the whole warehouse
codebase what [142](../docs/10_architecture/142_the-data-model.md) proposes for the data model: text files in git,
no proprietary binaries, many small files rather than a few large ones, so that every change shows as a readable
diff and can be attributed to a release note (`ARC-OP-30`). It also works as a filter on tools: a tool whose
artefacts are binary files would be inadmissible unless it has a text format. Examples, from the model's general
knowledge and not checked here: classic SSIS packages and Power BI `.pbix` files fail it; dbt-style SQL and YAML,
and Power BI's newer PBIP/TMDL text format, would pass.

**Reviewed 2026-10-07, session 07:** [sol](../docs/30_research/notes/XREV_2026-10-07_text-file-codebase_sol.md) and [astra](../docs/30_research/notes/XREV_2026-10-07_text-file-codebase_astra.md) both FAIL the
paragraph above. Its SSIS example is wrong: ordinary `.dtsx` packages are XML text, though with noisy diffs (the
`.ispac` deployment file is a zip container). And it claims more than the author said: his "rather" became
"inadmissible", stable identity and readable diffs for every change were added, and release-note attribution was
presented as following from diffs, where `ARC-OP-30` concerns output differences. Small files are also 180's third
property, not its fourth. Both reviewers found no conflict with 142, 180 or an ADR.

Recommended to the author, not ruled:

5. Correct the SSIS example and the property number.
6. Apply the preference to hand-authored source; allow generated or atomic files (dependency lock files, generated
   manifests) and keep runtime artefacts (databases, data files) out of its scope; read "ASCII" as UTF-8 text.
7. Grain is one coherent concept per file, not the smallest possible file: too fine a split scatters one change over
   many files and costs agents more reads.
8. Reword the paragraph to his own strength — binaries strongly disfavoured, not banned — and mark the link to
   release-note attribution as the model's proposal.

**Ruled 2026-10-07 by the author** on recommendations 5 to 8:

> 5. agree
> 6. okay
> 7. okay
> 8. agree

Accepted, and correcting the paragraph above: ordinary SSIS `.dtsx` packages are XML text and are not an example of a
binary format, and small files are 180's third property, not its fourth (5); the preference applies to hand-authored
source, with generated or atomic files such as lock files and manifests allowed, runtime artefacts such as databases
and data files out of its scope, and "ASCII" read as UTF-8 text (6); the grain is one coherent concept per file, not
the smallest possible file (7); binaries are strongly disfavoured, not banned, and the link to release-note
attribution is the model's proposal (8). This is a ruling on how his statement is read, not yet the ratification of
180's principles that the row asks for.

**Sandbox engine ruled 2026-10-11, session 08:** for the Wide World Importers sandbox only, the author chose a DuckDB file as warehouse and dbt-core with dbt-duckdb for transformations ([ADR-0015](../docs/20_decisions/0015-sandbox-warehouse-dbt-duckdb.md), [420 §12](../docs/40_roadmap/420_next-sandbox-setup.md)): "let's go with dbt-core and dbt-duckdb". It is a lean-start choice for one implementation under ADR-0012, made before the principles were ratified; the framework's constitution, which this row asks for, stays open.

### ARC-OP-21 — No faculty self-reports incompetence, so out-of-depth detection has no home
**⛔ STATE: OPEN**
Opened 2026-09-20, session 03, from [XREV_2026-09-20_faculty-inventory_sol](../docs/30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md) Q1.

Each faculty fails to announce that it is out of its depth, and each fails differently.
Deterministic machinery has no representation of its own scope and proceeds confidently on
well-formed input that violates its assumptions. The second faculty is fluent at the
boundary of competence, which is what makes `ARC-OP-17`'s correlated error dangerous rather
than merely annoying. Humans usually know and frequently do not say, because admitting it
carries a political cost.

This was drafted as a capability dimension in [060_faculty-inventory.md](../docs/00_concept/060_faculty-inventory.md) and cut, on the ground that
it flips no allocation: it applies to all three faculties equally, so no unit of work moves
because of it. What survives is a **requirement on the architecture** rather than a property
of any faculty. Nothing in
[100_system-overview.md](../docs/10_architecture/100_system-overview.md) or
[110_capability-map.md](../docs/10_architecture/110_capability-map.md) currently provides
it, and the omission is invisible precisely because each faculty looks confident.

What would close this row is a stated detection mechanism that does not rely on a faculty
reporting on itself — candidates being coverage of the evidence a claim rests on, distance
from adjudicated precedent (which is dimension 10 of the grid), and disagreement between
independently prompted attempts. Each is a hypothesis; none is designed. Related to
`ARC-OP-17`, `ARC-OP-18` and `ARC-OP-5`, and bears on
[160_evaluation-and-regression.md](../docs/10_architecture/160_evaluation-and-regression.md),
which currently assumes error is detectable by evaluation after the fact rather than
flagged at the point of production.

### ARC-OP-22 — The performance of decomposed designs depends on key constraints no engine enforces
**⛔ STATE: OPEN**
Opened 2026-09-20, session 04, from [2026-09-20-canon-survey](../docs/30_research/notes/2026-09-20-canon-survey.md) §1.4.

Every argument in this repository that treats the join objection to 6NF, anchor-style
modelling and Data Vault as answered by columnar execution is relying on join elimination,
and join elimination is conditional in a way the documents do not state.
[Snowflake](https://docs.snowflake.com/en/user-guide/join-elimination) removes a redundant
join only where the `UNIQUE`, `PRIMARY KEY` or `FOREIGN KEY` constraint is declared **and**
carries `RELY`; `NORELY` is the default; standard tables are not enforced, so "you are
responsible for enforcing constraints on the data"; and where integrity fails, "the query
results might differ." BigQuery requires the same declarations as `NOT ENFORCED` and warns
that violated constraints may return incorrect results.

**Narrowed within the hour, 2026-09-20, session 04**, by [XREV_2026-09-20_canon-survey-interaction_sol](../docs/30_research/notes/XREV_2026-09-20_canon-survey-interaction_sol.md) Q2. Join elimination
is one optimisation among many, not a general condition of decomposed-design performance:
columnar storage, partition and micro-partition pruning, clustering, predicate and projection
pushdown, join ordering, caching, materialised views and prejoined serving layers are all
available, and many workloads touch few narrow relations at modest volume. This row is
therefore **not** a claim that decomposed designs need `RELY` to perform. It is a claim about
what follows **where a project chooses to declare such constraints**, which nsdn plausibly
would, and that is narrower and still live.

The consequence is architectural rather than operational. **A business-key assertion stops
being only a semantic claim and becomes a runtime-correctness dependency.** If a key the
second faculty proposed and a human ratified is wrong, the engine does not merely record a
wrong interpretation; it silently returns wrong rows, and it does so in queries that never
mention the mistaken table. That interacts with `ARC-OP-2` on what evidence promotes a
joinability hypothesis to a business-key assertion, with `ARC-OP-4` on how an assertion
ages — a `RELY` constraint that was true in 2026 and is false in 2027 fails silently — and
with [150_trust-and-blast-radius.md](../docs/10_architecture/150_trust-and-blast-radius.md),
because the blast radius of a mistaken key is now the whole query workload rather than one
model.

Three things are owed. Whether a declared-and-trusted constraint is a tier-appropriate
artifact for `ADR-0005`'s autonomy tiers at all, given that asserting it delegates
correctness to unverified data. Whether the system should verify constraints it declares
rather than trusting them, and what that costs — which is measurable and belongs with
`EVI-OP-6`. And whether the adjudication surface of `ARC-OP-15` must present the constraint
*and its consequences* to whoever rules on it, since ruling on a key without seeing that it
licenses join elimination is ruling on something other than what is being decided.

**Narrowed again 2026-09-21 by the author.** Decomposed models — 6NF, Anchor, Data Vault,
temporal — are never to be exposed to end users as they are; they are processed into marts
with a clear purpose, preferably dimensional. Join cost is paid once, when the marts load, by
materialisation, which predates columnar engines. For the record-keeping layers the `RELY`
question is therefore mostly beside the point. The dependency survives where
trusted-but-unenforced constraints are most tempting: on the dimensional marts themselves,
where eliminating dimension joins from filter-only queries is the whole attraction, and a
wrong key silently corrupts a dashboard. The row is kept for that layer only.

**Given a consequence 2026-09-25 by [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md):** the **publication gate**. A mart is published
only when the tests on its data version have passed; a failing test blocks publication and revokes
the `RELY` or `NOT ENFORCED` assertions that depend on the failed claim before consumers see the
data. This row's dependency is now controlled, not only described.

### ARC-OP-23 — Which metadata work can a machine do without a person checking every item?
**⛔ STATE: OPEN**
Opened 2026-09-21, session 04, from the author's review of the canon survey.

The author's observation from practice: metadata catalogue implementations — Collibra is the
one named — fail widely because people lack the attention span and context to keep
descriptions accurate, flag near-duplicates and maintain hygiene; the work is boring, and it
degrades. Good metadata therefore exists only for the obviously valuable attributes, and
metadata-driven generators such as WhereScape are only as good as that metadata. A model does
not tire and holds far more context, which makes machine-assisted metadata the strongest case
the project has for the metadata capability. This is practitioner testimony and unsourced
under rule 8; it is nonetheless the best evidence for that capability now in the repository.

The open question is where such work can be verified without a person checking each item.
Some of it can be checked mechanically: near-duplicate detection, a description that
contradicts the profiled data, units that do not match observed ranges, grain that disagrees
with the keys, a description that disagrees with lineage. There, tirelessness is the whole
advantage. Some of it cannot: whether a description of what a column *means* is right has no
check but a person or an authoritative source. Tireless generation there produces more to
review without making review easier — the legible abundance the coverage guard in
[002_mission-statement.md](../docs/00_concept/002_mission-statement.md) exists to prevent.

The design owes a split of metadata tasks into those two kinds, and a mandate for each under
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md). Related to `EVI-OP-1`, since the uncheckable half is the falsifiable core in
another form, and to `ARC-OP-21`.

### ARC-OP-24 — The task allocation is a working draft awaiting review
**⛔ STATE: OPEN**
Opened 2026-09-21, session 04, on the author's direction.

[070_task-allocation.md](../docs/00_concept/070_task-allocation.md) lists 39 BI implementation
tasks as chains (who proposes, who decides, who executes, who checks), with the reason for
each taken from [060_faculty-inventory.md](../docs/00_concept/060_faculty-inventory.md). The
author endorsed its direction and accepted every finding of the first external review. He has
not yet reacted to individual rows and has asked that it be settled slowly.

Owed before it can be treated as a framework rather than a draft: the author's own row-by-row
reaction; a second external review on a different model; a test of the list's completeness
and grain against a real implementation; and a description of what the handoffs between
faculties cost, which the table makes visible and nothing in the repository yet prices. This
is also the first time [060](../docs/00_concept/060_faculty-inventory.md)'s allocation rule
has had concrete work to allocate, so the table is the natural place to test that rule.

**Second review done 2026-09-24, on GPT-6 Astra**, recorded in
[XREV_2026-09-24_task-allocation_astra](../docs/30_research/notes/XREV_2026-09-24_task-allocation_astra.md)
and accepted in full by the author. The table now has 40 rows. Still owed: the author's own
row-by-row reaction, a test against a real implementation, and a description of what the
handoffs cost, which the table's patterns now state as a hypothesis rather than a finding. Two
questions the review opened and nobody has examined: whether rows 16, 25 and 26 need the same
template-versus-agent split as row 17, and how erasure obligations (row 37) bound the
historisation choices in row 15.

**Rows 41–43 added 2026-09-25**, from the context-system design: temporal behaviour per
table and attribute, and join knowledge with cardinality in three layers — both the author's —
and maintaining the context system. Row 37 now reaches the context store. The table has 43
rows; the three new ones have not been externally reviewed.

**First observation against real work, 2026-09-26, session 06**, from the step log. For row 9 the model
decided every matching choice (seven decide steps) and the author decided none, executing lookups
instead; for row 7 the author executed every acquisition by hand, because neither environment could reach
a Dutch data source. The allocation was bypassed rather than tested: no matching choice was put to the
author as a decision. See [2026-09-26-session-06-post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md), lesson 3.

### ARC-OP-25 — Context recipes and write-back are proposed, not designed
**⛔ STATE: OPEN**
Opened 2026-09-25, session 04, from a brainstorm with the author.

[122_context-retrieval.md](../docs/10_architecture/122_context-retrieval.md) proposes a context
recipe per task type — anchor, what to load, zoom level, budget, minimum trust — and
[124_context-write-back.md](../docs/10_architecture/124_context-write-back.md) proposes a
mandatory write-back sorted by the chain of
[070_task-allocation.md](../docs/00_concept/070_task-allocation.md), with a promotion ladder
from note to rule and expiry for anything not promoted. Owed: a recipe format; where recipes
live; how the after-task measurements are collected; the expiry period; and a first handful of
recipes written for real task types, which is the only way to learn whether the idea holds. The
rule rung of the ladder depends on `ARC-OP-16`.

**Reviewed 2026-09-25** in [XREV_2026-09-25_context-system_astra](../docs/30_research/notes/XREV_2026-09-25_context-system_astra.md) (write-back) and [XREV_2026-09-25_context-system_sol](../docs/30_research/notes/XREV_2026-09-25_context-system_sol.md) (retrieval); every finding
integrated. Recipes are now composable, risk-triggered and fail closed; context comes in facets
rather than one zoom hierarchy; trust is recorded per claim on several dimensions; write-back
allows "nothing new", caps and prioritises what it sends to people, keeps negative findings and
separates re-checking from re-encountering. Newly owed: the **benchmark tasks** with known
required evidence, against which retrieval is measured — without them the measures in
[122](../docs/10_architecture/122_context-retrieval.md) cannot be taken.

**Second review 2026-09-25**, crossed — sol on write-back, astra on retrieval — all findings
integrated. Retrieval now begins with a baseline risk screen and has fixed rules for combining
recipes, checks that claims fit together across versions, and scores completion and justified
abstention separately. Write-back now runs throughout a task with idempotency keys, routes one
package to several consumers, replaces the ladder with a lifecycle that can go down as well as up,
keeps every candidate outside the human queue, and makes expiry and merging decidable and
reversible. **Which candidates enter the human queue at all** is raised as its own question on
2026-09-25 and is not answered here.

### ARC-OP-26 — One store, two views: agent context and the human metadata catalogue
**⛔ STATE: OPEN**
Opened 2026-09-25, session 04, from a brainstorm with the author.

The context store the agents need and the catalogue people use could be one store with two
views, per [120_context-layer.md](../docs/10_architecture/120_context-layer.md). If so, the
metadata value area of [ADR-0009](../docs/20_decisions/0009-separate-capabilities-open-value-areas.md)
and the context system become one investment, and the catalogue stays current because agents
depend on it rather than because people are asked to maintain it — the failure `ARC-OP-23`
records. Unexamined: whether what people need from a catalogue and what agents need from
context are close enough to share a store, and what the human view would look like, which is
[170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md)'s territory.

**Reviewed 2026-09-25** in [XREV_2026-09-25_context-system_astra](../docs/30_research/notes/XREV_2026-09-25_context-system_astra.md) Q1. Two conditions now recorded in
[120](../docs/10_architecture/120_context-layer.md): a shared store needs access, publication
and executable-authority boundaries enforced before retrieval, not just two presentations; and
agents depending on the catalogue does not by itself keep it current, so every assertion needs
a revalidation trigger and an owner.

**Refined 2026-09-25 by [ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md):** not one store but one identity plane over separate stores,
with policy-filtered indexes — so that even the existence of a sensitive object or draft claim is
not revealed — and an explicit publication pipeline to the human catalogue.

### ARC-OP-27 — Temporal behaviour and join knowledge are rarely enforced, so they must be observed, asserted and monitored
**⛔ STATE: OPEN**
Opened 2026-09-25, session 04, from the author's two points recorded verbatim in
[127_temporal-behaviour.md](../docs/10_architecture/127_temporal-behaviour.md) and
[128_join-knowledge.md](../docs/10_architecture/128_join-knowledge.md).

Sources seldom declare how their data behaves over time, and seldom enforce cardinality or
referential integrity; the author singles out cardinality as among the most important and "not
always implemented 'hard'". Both documents therefore record the knowledge in layers — what is
declared, what deterministic machinery observes, what a person asserts — and turn assertions
into standing tests whose violations are drift. Owed: how many loads are needed before a
temporal class or an observed cardinality can be trusted; the exact front matter for the
temporal section and for the proposed `relationship` card kind; and how drift is prioritised
against everything else in the adjudication queue. Related to `ARC-OP-22`, since a `RELY`
constraint on a mart is an asserted cardinality the engine will not check, and to `ARC-OP-2`
on what evidence promotes a joinability hypothesis.

**Reviewed 2026-09-25** in [XREV_2026-09-25_context-system_sol](../docs/30_research/notes/XREV_2026-09-25_context-system_sol.md) Q1–Q2; every finding integrated. Temporal
behaviour is now six independent axes plus a **capture guarantee** per source, with history
labelled *sampled* where complete transitions cannot be captured; the claim that the vault keeps
every change is qualified; deletion requires evidence of a complete extract; the order of time
is monitored, not only values. Join knowledge now records grain and population, key roles,
declared uniqueness and inclusion separately with their enforcement state, directional and
segmented referential integrity, and requires **query-level tests** before a relationship is used.

**Second review 2026-09-25** by astra on 127 and 128; all findings integrated. Temporal:
effective time may be unknown and is then recorded as such, with observed-state history separated
from business-valid history; change detection includes temporal metadata; deletion additionally
needs a comparable population and a consistent snapshot, else it is *unresolved*; capture
guarantees state demonstrated coverage, not capability. Joins: per-fact reconciliation with
attribution cases, uniqueness tested after the join's own transformations, a defined allocation
origin for bridges, and the publication gate of ADR-0011.

### ARC-OP-28 — The adjudication economy is modelled, not calibrated
**⛔ STATE: OPEN**
Opened 2026-09-25, session 04, from the author's question how to keep the human review queue to a
responsible minimum while limiting the risk of faulty assumptions.

[155_adjudication-economy.md](../docs/10_architecture/155_adjudication-economy.md) states the
problem as spending a fixed budget of human attention where it averts the most expected loss —
p × L × (1 − d) × r against review cost h — subject to hard rules for mandate, irreversibility and
regulation; sorts candidates into four lanes (auto-accept, accept provisionally, human, park);
names the levers that shrink the queue; and specifies the structured adjudication record and the
monitoring workflows the author asked for, with tightening automatic and loosening approved by a
person. Owed: how p, L and d are estimated before any audit history exists; initial thresholds and
sampling rates; who sets the weekly budget per reviewer role; how data about individual reviewers
is kept proportionate; and an external review. This row is the adjudication half of `CON-OP-2`: the
weekly budget report is the number that decides whether the economics hold. Related to `ARC-OP-6`,
`ARC-OP-15`, `ARC-OP-17`, `ARC-OP-18` and `CON-OP-15`, which it draws together.

**Reviewed 2026-09-25** on GPT-6 Astra (the model) and gpt-5.6-sol (organisational practice),
recorded in [XREV_2026-09-25_adjudication-economy_astra](../docs/30_research/notes/XREV_2026-09-25_adjudication-economy_astra.md)
and [XREV_2026-09-25_adjudication-economy_sol](../docs/30_research/notes/XREV_2026-09-25_adjudication-economy_sol.md);
all eleven findings integrated. The problem is now stated as loss averted — loss without review
minus loss with review, including delay and reviewer-induced error — per human minute, with numeric
ranges rather than bands and the reviewer's detection recorded, not assumed. Human-lane items carry a
decision owner, delegate, deadline and explicit default; service classes have objective entry
criteria and reserved capacity; tightening that would exceed capacity quarantines or throttles
instead; audits are random within strata, with exploration samples and independent confirmation;
reviewer data is reported for groups, never individuals. The author ruled that **seeded checks stay,
blinded and excluded from all estimates**, and that rigour versus a lean start is a question of
implementation: [ADR-0012](../docs/20_decisions/0012-generic-framework-lean-start.md). 155 now ends
with three implementation stages. Newly owed: the evidence required to promote a provisional claim,
the reserved-capacity shares, and how a sandbox with simulated business owners exercises any of
this.

---

### ARC-OP-29 — Is the data model a first-class, navigable part of the context layer?
**⛔ STATE: OPEN**
Opened 2026-09-26, session 07, from the author's observation that the first sandbox did no visible data
modelling.

The author wants a data model — conceptual, logical, technical — that people use to communicate and keep the
big picture, that drives warehouse automation through templates with deterministic loading patterns, that is
connected to metadata for meaning and loading patterns, and that both people and the agentic layer can
navigate. His reference is SAP PowerDesigner: full code generation, but hard to navigate and heavy with
ballast. He prefers open source or parts built here.

[142_the-data-model.md](../docs/10_architecture/142_the-data-model.md) drafts an answer: the model is text
declarations, one file per object, under the context layer's identifiers; only the meaningful part is
declared and everything mechanical is generated; objects are navigated along dimensions — at least
conceptual to concrete and raw to refined, with subject area, source, time and status as candidates; people
see a generated static HTML site, agents read the files and a derived index. The author ruled on 2026-09-26
that the graphical representation is for human consumption only and need not be machine-readable.

Open: whether to adopt this shape at all; which further dimensions are real; the declaration language, which
falls under `ARC-OP-20`; and how this relates to `ARC-OP-15` and `ARC-OP-26`, for which the HTML site is a
candidate surface. Closes with an ADR, after a hand-written model of one real case has been generated into
the HTML view. The draft is unreviewed.

### ARC-OP-30 — Release regression: every output change attributed to a release note, on frozen data
**⛔ STATE: OPEN**
Opened 2026-09-28, session 07, by the author:

> For proper regression testing after every update of the codebase, you would need release notes that
> explain what changes were made, why and what the intended impact is. Do you think this also needs to
> documented somewhere? And do you agree with this claim? The way we do regression testing at my current
> employer is that the same set of data is used for three months at a time, but every day a new snapshot is
> made with the then current codebase, and it is compared to previous day's snapshot. Any changes must be
> attributed either to one of the release notes, or it is proper regression that must be solved.

Nothing in the design covered this. [160](../docs/10_architecture/160_evaluation-and-regression.md) tested
data changing under fixed code — determinism, quality contracts, semantic regression — and never code
changing under fixed data, and no document or record said what a change was expected to do to the output:
ADRs say why a design was chosen, the step log what work was done, commit messages why a change was made.

The same day, answering the proposed refinements, the author added from his practice:

> 6. the developer checks that the change has the intended consequence. The team's dedicated tester checks
> for regression (by others)
> 7. yes, freeze the clock, one reference date per quarter year
> 8. True that's what we do. And then a plausibility check between the two dates (usually a quarter year
> apart)
>
> Document all of this somewhere (probably 160 then) + register row as you proposed.

The method is now recorded in 160 under *Release regression — frozen data, moving code*: frozen data and one
reference date per quarter; a daily snapshot with the current code, diffed against the previous day's; every
difference attributed to a release note or treated as a regression; the developer checks the intended
consequence, a separate tester the regression; no code deployed on the quarter turn, and a plausibility check
between the two reference dates.

Proposed by the model and **not ruled**: that release notes state their intended impact in a form a diff can
be matched against, including "no change expected"; that in nsdn context changes — adjudicated assertions,
rule versions, metric definitions — are a second legitimate source of attribution beside code release notes,
which bears on `ARC-OP-13`; and that most of the loop is run by agents and deterministic machinery, the author
seeing only the unattributed residue and the quarterly plausibility check.

Open: whether the method is adopted, by ADR; the form and location of release notes (one per release, tied to
a commit, machine-readable, distinct from ADRs and the step log); what counts as an output for the snapshot;
how the diff and its residue are summarised; and where the frozen copy and its reference date come from in the
next sandbox (`EVI-OP-7`). Nothing is to be built before code exists to release.

**Reviewed 2026-09-28, session 07, and failed by both reviewers**:
[sol](../docs/30_research/notes/XREV_2026-09-28_release-regression_sol.md) on the base method,
[astra](../docs/30_research/notes/XREV_2026-09-28_release-regression-adaptations_astra.md) on the nsdn
adaptations. The common finding: **attribution is not acceptance.** A difference that falls inside what a
release note or a logged context change declared can still be wrong — a duplicated invoice inside a declared
revenue change, an extra exclusion inside a genuine definition change, a second customer wrongly accepted by a
reviewing agent that shares the author's mistaken premise. Sol adds two more: two releases on one day whose
effects interact cannot be attributed separately, and a correct root change leaves its downstream consequences
looking like regressions unless they are derived through lineage.

Recommended to the author on 2026-09-28: (1) an expected impact is stated as executable expected deltas plus
invariants that must not move (row counts, cardinality, reconciliation totals), checked independently against
the actual before and after outputs; (2) changes deployed together are snapshotted one at a time in a fixed
order, or carry one joint expectation; (3) a note declares the root impact and its downstream closure is derived
through versioned lineage; (4) context changes carry the same executable expectation as code, and each snapshot
is pinned to the context version it ran with; (5) a reviewing agent validates against the stated expectation and
the actual outputs, not the author's explanation, and anything it cannot confirm stays residue for a person.

**Ruled 2026-09-29 by the author** on the five recommendations, numbered as they were put to him in the
conversation, where 4 was the reviewing agent and 5 the context changes:

> 1. agree, expected impact is usually in the release notes (which entitities / tables etc)
> 2. maybe that is workable if CI/CD is properly implemented, and a regression test can be run after every
> integration. For humans this is unworkable, but for an agentic layer this might be an option. Maybe put this
> remark in, also.
> 3. okay
> 4. yes
> 5. yes

All five accepted; the second with his qualification, that snapshotting after every change is workable only
with proper CI/CD and a regression run per integration — unworkable for people, possibly an option for an
agentic layer. Integrated into 160 under *Amended after review*, with his remark verbatim. The amendment is
unreviewed. The row stays open on adoption, which needs an ADR, and on the items listed above as open.

**Postponed 2026-10-11, session 08.** The frozen copy that 420 §6 expected to come free does not exist: since the disk ruling the job keeps only the newest three extracts, and nothing writes to `data/frozen/`. The author postponed fixing it ([420 §12](../docs/40_roadmap/420_next-sandbox-setup.md), G): "let's postpone for now." The quarter turn on 2016-06-30 is the natural moment to raise it again.

### ARC-OP-31 — Plausibility as back-of-the-envelope checks, and the test framework by root cause
**⛔ STATE: OPEN**
Opened 2026-10-06, session 07, by the author:

> Secondly, next to regression testing we also need (constant) plausibility testing as a means of sanity
> checks, probably on production, where data can change daily, to make sure that we don’t get weird double
> counting, etc. Also for every transition of the fixed reference date / fixed data set, when the test data
> set is updated. Can you check if that’s already documented in the appropriate place?

The check found it about half documented and scattered: Level 2 of
[160](../docs/10_architecture/160_evaluation-and-regression.md) (expectations generated from profiles), the
standing join tests of [128](../docs/10_architecture/128_join-knowledge.md) (fan-out, aggregate and per-fact
reconciliation, behind the publication gate of
[ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md)), the temporal monitoring
of [127](../docs/10_architecture/127_temporal-behaviour.md) (duplicates, replays, closed periods), row 23 of
[070](../docs/00_concept/070_task-allocation.md) (reconciliation, with no design behind it), and one sentence
in 160 on a plausibility check between the two reference dates at the quarter turn. Missing were checks on
the published outputs themselves, a rule that a new frozen data set passes the suite on its own before it
becomes the baseline, and any statement of what a failure does. The author asked for the gaps to be drafted.

**Redefined 2026-10-06 by the author**, after the first draft below had been reviewed twice and amended once:

> Wait a second. Let's discuss plausibility. Plausibility means that by and large, the data is plausible. It
> doesn't state that it's 100% correct. It is a first line of defense against grave errors, load failures
> etcetera. It doesn't need to catch all errors. It is a quick survey of what comes in, and how it is
> transformed, to do a sanity check to catch a wide range of (unexpected) errors. Let's not over engineer this.
> We also have unit tests (not sure if that's already in the documentation) that should cover design flaws. So
> let's take if from the root causes, some examples: A data load has not arrived: should be covered by the
> plausibility tests. A batch was loaded twice: plausibility test. Debit equals credit is a different type of
> test, not a plausibility test, although it should be in the test framework and it is a very simple sanity
> check. Okay, so maybe part of ongoing plausibility testing. Uniqueness issues, also part of plausibility, but
> more of the "regular" test framework. Let's work from the angle of plausibility tests, unit tests, whatever
> other tests there are, and root causes, such as loading issues, modelling issues, unexpected edge cases, data
> quality issues. The reviewers are applying insanely strict expectations, on plausibility checks, which should
> be more like back of the envelope sanity checks, to quickly and regularly check for issues on those parts of
> the data where a 'hard' check is difficult (like changing daily amounts).

The model agreed that its draft, and the review assignments it wrote, had held plausibility to a standard of
completeness; found that unit tests were not documented anywhere; and put two questions to him — whether to
keep the admission check on a new frozen set (ruling 2 below), and whether debits-equal-credits belongs in data
tests or in plausibility. **Ruled the same day:**

> A over-engineering for now. B agreed, in data tests. Please proceed with documenting the rest.

**Current state.** Plausibility is a set of soft, back-of-the-envelope checks on every load and at the quarter
turn — did each load arrive, are counts and totals roughly as usual, does roughly the expected volume pass
through each layer — that warn and ask rather than block: 160, *Plausibility*. The kinds of test (unit tests,
data tests, plausibility checks, release regression, semantic regression and agent evaluation) and which root
cause each is meant to catch first are in the new [162](../docs/10_architecture/162_test-framework.md). Of the
earlier rulings, the reconciliation against a verified report within a bandwidth and the scoped domain equations,
debits equal credits among them, are data tests in 162; the admission check on a new frozen set is dropped for
now; the recommendations numbered 8 to 11 lapse unruled. The first draft and everything that followed from it
is moved verbatim to
[2026-10-06-plausibility-first-draft](../docs/30_research/notes/2026-10-06-plausibility-first-draft.md). The
redraft and 162 are unreviewed.

Open: adoption, by ADR; which loads and totals are watched first, and how wide the bands are; the tooling for
unit and data tests and where each is declared. Nothing is to be built before there is a sandbox to run it on.

**Redraft reviewed 2026-10-06** by [sol](../docs/30_research/notes/XREV_2026-10-06_test-framework_sol.md), this time
under the author's framing — rough soft checks against gross errors, not completeness — and **failed** on one
common gross cause: a file loaded into the wrong tenant or partition, with the expected schema and a similar
volume, passes every kind of test described. Its other findings: data tests cannot catch valid-looking bad values
such as a source switching from euros to cents, so plausibility is the first line there; comparisons with the
previous load, weekday or trend will fire on public holidays and month-ends; and having the agentic layer diagnose
every warning before it is shown is over-engineered.

Recommended to the author on 2026-10-06, not ruled: (12) a data test owns **delivery identity** — each load is
checked against what it claims to be: source, tenant, business date, partition, and a manifest or control total
where the source supplies one; (13) in 162's table, *data quality at the source* gets plausibility as first line
for gross shifts such as a change of unit, with data tests first for structural faults; (14) plausibility compares
like with like on a business calendar — same weekday, holiday or month-end status — and the arrival schedule lists
the days on which no load is expected; (15) a warning shows the observed value, the usual range, the difference
and the load concerned, and the agentic layer diagnoses only when someone opens it.

**Ruled 2026-10-06 by the author** on 12 to 15: "yes, looks good, please process" All four accepted and integrated: delivery
identity is a data test, and *data quality at the source* is split by kind of fault, with a row added for a load
routed to the wrong tenant or partition, in [162](../docs/10_architecture/162_test-framework.md); like-for-like
comparison on a business calendar, the arrival schedule and the shape of a warning in 160, *Plausibility*. The
amendment is unreviewed.

*Everything from here to the end of this row is superseded by the redefinition above, and kept for provenance.*


Drafted the same day in 160 under *Plausibility — does the output still make sense?*, unreviewed. Proposed by
the model and **not ruled**: seven families of deterministic checks on published outputs — reconciliation
along the chain, uniqueness at the declared grain, conservation rules from the domain, consistency across
outputs, completeness, closed periods, and movement within bands — the first six hard and the seventh soft;
their invariants declared as adjudicated assertions and shared with the invariants release notes must name
(`ARC-OP-30`); one suite run on every production load, at every baseline change (the new frozen set first on
its own, then the comparison between reference dates), and after a release; a hard failure blocking
publication of the affected outputs, extending ADR-0011 from relationships to outputs; and the suite itself
tested by injecting known defects into the simulated source of `EVI-OP-7`.

Open: whether it is adopted, by ADR; which outputs are in scope first; thresholds and how bands are derived;
whether a hard failure blocks the affected outputs or the whole publication; who may accept a discrepancy and
whether acceptance expires; where and in what format checks are declared. Nothing is to be built before there
is a sandbox to run it on.

**Reviewed 2026-10-06, session 07, and failed** by
[sol](../docs/30_research/notes/XREV_2026-10-06_plausibility_sol.md): reconciliation through the chain is not
independent evidence. Its counterexamples: during a migration a week's invoices arrive from both the old and the
new system under different document numbers, and every one of the seven families passes; a quarter copy with
facts to 30 June and dimensions extracted on 2 July passes both baseline steps, though the baseline never existed
at one cut; and an invoice header that includes tax, freight and rounding, or a late posting to a period closed
in finance but not legally locked, fails a hard check routinely until discrepancies are accepted mechanically.

Recommended to the author on 2026-10-06, not ruled: (1) every additive financial measure is also checked against
an independently sourced control total at business-population and period grain — a figure from outside the
chain being tested — and sources that may carry the same business event carry a tested assertion that their
populations are exclusive, or a canonical business-event identity; (2) admitting a new frozen set first verifies
every input's source version, high-water mark, effective cut, row count and checksum against the declared cut,
and reproduces the production run under the same code and assertion versions, because plausibility is not proof
of a baseline's integrity; (3) a domain equation is hard only for a stated accounting state and with its
reconciling components and tolerances written into it, expected late postings are effective-dated exceptions with
an owner and an expiry, and every new rule starts soft and is promoted on its observed false-alarm rate.

**Ruled 2026-10-06 by the author** on the three recommendations:

> 1. agreed with the check on the additive financial measures. This can be done when there is a verified
> report, like external reporting or an approved balance sheet or profit and loss statement. We can then
> verify that it should be within a certain bandwith of this externally verified number. Agree with the
> overlap.
> 2. okay
> 3. yes, see also my remarks regarding rule 1.

All three accepted. The first with his qualification: the independent figure is a **verified report** —
external reporting, an approved balance sheet or profit and loss statement — and the check is that the measure
falls **within a stated bandwidth** of that externally verified number; the third with tolerances taken the same
way. Integrated into 160 under *Amended after review* in the Plausibility section; the amendment is unreviewed.
The row stays open on adoption, which needs an ADR, on the bandwidths, and on the items listed above as open.

**Amendment reviewed 2026-10-06 and failed** by
[sol](../docs/30_research/notes/XREV_2026-10-06_plausibility-amendment_sol.md). The mixed-cut frozen set and the
routine hard-check failures are now caught; the cross-system duplicate is not, because a verified report is
periodic and arrives after the daily figures are published. Two new holes: a new debit-equals-credit rule that
starts soft publishes a one-sided journal with only a question; and a bandwidth on an exact identity lets a real
imbalance inside the band pass. The second comes from the model's sentence in 160 that every hard tolerance is a
bandwidth "in line with the first change" — an extension of the author's remark on rule 3, not his words.

Recommended to the author on 2026-10-06, not ruled: (8) the verified-report check is retrospective — when the
report arrives, already published figures for that period are reconciled to it and flagged if outside the band —
and during a known overlap, such as a migration or a new source carrying events another already carries,
publication of the affected measures waits on a canonical business-event identity or an independent control at
the publication grain, or the overlapping feed is held back until the periodic control exists; (9) a new rule is
calibrated on replayed or shadow data before it goes live, and an invariant the source guarantees by construction
— debits equal credits — may start hard; (10) admission compares keyed, order-insensitive content hashes and the
source's snapshot and as-of metadata, not raw-file checksums; (11) two kinds of tolerance are kept apart: an exact
accounting identity allows only a justified rounding amount, and the bandwidth applies to a measure compared with
an externally verified report.

### ARC-OP-32 — Should context cards conform to the Open Knowledge Format?
**⛔ STATE: OPEN**
Opened 2026-10-06, session 07, from an article the author asked to be assessed for relevance:
*How the Open Knowledge Format can improve data sharing*, Google Cloud blog, 12 June 2026, and the
specification it announces, read at version 0.2 (see [050](../docs/00_concept/050_prior-art.md)).

OKF is the same design as the context layer of [120](../docs/10_architecture/120_context-layer.md), arrived
at independently: markdown files with YAML front matter, one concept per file, links forming a graph, git
recommended as the carrier. Its version 0.2 goes further towards 120 than the announcement did — `generated`
and `verified` kept apart so that who wrote a concept is not who confirmed it, trust tiers of unverified,
machine-confirmed and human-reviewed, `status` and `stale_after`, sources with provenance, and an *Attested
Computation* type whose computation an agent may parameterise but not author, checked by deterministic code.

The differences that matter: OKF's identity is the file path, where 120 deliberately uses URNs with an alias
history so that an assertion made in 2026 still resolves in 2029; OKF's links are untyped, where 120 and
[ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md) type relationships as
assertions; and OKF keeps trust per concept, where 120 keeps it per assertion, with adjudication, retired
hypotheses and falsifiers that OKF has no place for.

Proposed by the model and **not ruled**: that cards adopt OKF's field names where they coincide — `type` for
the card kind, `title`, `description`, `resource`, `tags`, `generated`, `verified`, `status`, `stale_after`,
`sources` — and keep nsdn's own fields (URN, aliases, assertions) as permitted extensions, so that the context
layer is a conformant bundle at almost no cost and can be read by other tools and agents, while identity stays
by URN. Bears on `ARC-OP-26`, the human view of the same store, for which OKF's reference visualizer is a
ready candidate.

Open: whether to conform, by ADR; whether URN identity can be carried inside an OKF bundle without breaking its
path-as-identity rule; and whether OKF's Attested Computation is the right form for the metric definitions and
plausibility invariants of 160. OKF is at version 0.2 and changed incompatibly between 0.1 and 0.2, so nothing
should depend on it before it settles.

**Reviewed 2026-10-06, session 07, UNDETERMINED** by
[astra](../docs/30_research/notes/XREV_2026-10-06_okf-conformance_astra.md), which was not given the specification
itself and asks for its normative constraints. Its findings: card-level `verified` would tell an OKF consumer that
a whole card is human-reviewed when only some of its assertions were adjudicated — a metric whose definition is
ruled but whose implementation claim is only proposed; "the same design" overstates the match, since
[ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md) made assertions the core record
and cards views of them; a URN extension cannot make an ordinary OKF consumer recognise a moved file as the same
concept; nothing shows that card kinds are acceptable `type` values with the same meaning; and Attested
Computation is stricter than [ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md), which lets
models write code that deterministic machinery runs.

Recommended to the author on 2026-10-06, not ruled: (4) an OKF bundle, if adopted, is a publication-gated
projection generated from the assertion store, never the canonical record; (5) the projection writes `verified`
only when the recorded verification covers every claim the projected card makes, and otherwise omits it or
projects only the covered claims; (6) the card kind is kept in its own field beside `type` until the mapping has
been checked against the specification, and paths in the projection are kept stable, or a translation from URN to
path is published with it; (7) Attested Computation is used only for computations that meet its stricter rule
that an agent supplies parameters and never the computation. Any adoption waits for a second pass with the
specification supplied.

**Ruled 2026-10-06 by the author** on the four recommendations, numbered as they were put to him, where 4 to 7
are those above:

> 4. okay.
> 5. okay.
> 6. let's keep it the way we designed it, you have convinced me it is superior.
> 7. okay.

Accepted: an OKF bundle, if there is one, is a publication-gated projection generated from the assertion store
and never the canonical record (4); `verified` is written only when the recorded verification covers every claim
on the projected card (5); Attested Computation is used only for computations meeting its stricter rule (7). On
the sixth he chose to keep nsdn's design: identity stays by URN with alias history and card kinds stay as 120
and ADR-0011 define them, so it is the projection that adapts to nsdn, not the cards that adapt to OKF. The
earlier proposal in this row to adopt OKF's field names in the cards themselves is therefore not taken up; field
names are matched, where at all, in the projection. The row stays open on whether a projection is built, by
ADR, which waits for a second review pass with the specification supplied.

### ARC-OP-33 — Quality gates: which gates, where they sit, and which of them block
**⛔ STATE: OPEN**
Opened 2026-10-07, session 07, from the author's statement on the evening of 2026-10-06:

> We need quality gates. Partly we have them. But we might have to determine them more precisely. I know that this session cannot reach the PC, so just store it for now.

Some gates exist or are drafted, but no document lists them together.
[ADR-0011](../docs/20_decisions/0011-assertions-identity-plane-publication-gate.md) made the publication gate: a
failing join test stops publication. [162](../docs/10_architecture/162_test-framework.md) (draft) sorts the tests by
root cause, and [160](../docs/10_architecture/160_evaluation-and-regression.md) (draft) holds release regression and
plausibility (`ARC-OP-30`, `ARC-OP-31`). For this repository itself, `tools/check_repo.py` gates every commit. What is
not written anywhere is the whole set: which gates there are; at which point in the life of a change or a load each
one sits — commit, merge or deployment, each load, publication, the quarter turn of the frozen data; which of them
block and which only warn; and who may override a blocking gate, and how the override is recorded.

Proposed by the model and **not ruled**: one short gate catalogue, one entry per gate, naming its point, its checks
(by reference to 162, not restated), whether it blocks or warns, and who may override it. Two constraints follow
from what is already settled. Gates are deterministic and run without the agentic layer
([ADR-0004](../docs/20_decisions/0004-models-out-of-the-data-path.md), and the author's statement recorded in
[420](../docs/40_roadmap/420_next-sandbox-setup.md) §5). Plausibility checks are soft by his ruling in `ARC-OP-31`,
so they warn rather than block unless he rules otherwise. Changes made by agents pass the same gates as any other
change; that is what would make it safe to let the agent team of `ARC-OP-34` work without him watching.

Closes when the catalogue is written and adopted by ADR, with or after the adoption of 162.

**Reviewed 2026-10-07, session 07:** [sol](../docs/30_research/notes/XREV_2026-10-07_quality-gates_sol.md) FAILS — a switch from euros to cents only warns while a
mart 100 times too large is published; [astra](../docs/30_research/notes/XREV_2026-10-07_quality-gates_astra.md) HOLDS UNDER warnings being an accepted residual risk,
existing hard blockers staying hard, and passing gates not being taken as proof that unattended work is safe. Both
found the same gross case; they differ on whether to accept it. Sol also found a missing gate point: an assertion
being approved and starting to feed marts, which ADR-0011's publication pipeline implies. Both found that the row
overstated its footing: agent-independence of the gates is proposed in 420, not settled, and passing gates is
necessary for safe agent work but not sufficient.

Recommended to the author, not ruled:

1. Plausibility stays a warning in general, with one narrow exception: a deviation of an order of magnitude or more
   against like-for-like blocks publication until someone looks. (Alternative: accept the risk, as astra allows.)
2. Add *semantic admission* — an assertion becoming approved and eligible to feed marts — as a gate point.
3. Correct the row: agent-independent gates are proposed (420 §5), not settled; gates are necessary, not sufficient,
   for letting agents work unattended.
4. Keep it small: one change gate, one load-and-publication gate, semantic admission, and the author as the only
   override authority, with overrides recorded.

**Ruled 2026-10-07 by the author** on recommendations 1 to 4:

> 1. agree
> 2. agree
> 3. agree
> 4. agree

Accepted: plausibility warns, except that a deviation of an order of magnitude or more against like-for-like blocks
publication until someone looks (1); semantic admission is a gate point (2); agent-independent gates are proposed in
420, not settled, and passing gates is necessary but not sufficient for unattended agent work, which corrects the
row above (3); the catalogue stays small — a change gate, a load-and-publication gate, semantic admission, and the
author as the only override authority, with overrides recorded (4). The row stays open until the catalogue is written
and adopted by ADR.

**Change gate postponed in the sandbox, 2026-10-11, session 08.** On the author's ruling, "maybe postpone for now, just push all new SQL without gates", new SQL reaches the Wide World Importers warehouse without a change gate ([ADR-0015](../docs/20_decisions/0015-sandbox-warehouse-dbt-duckdb.md)). Read by the model, and confirmed by the author the same evening ("Correct."): the checks within a load and the runner's confinement to the warehouse stand. The row stays open; the gate returns before any use outside a sandbox.

### ARC-OP-34 — An agent team for the first build: roles, governing documents, and how agents confer and agree
**⛔ STATE: OPEN**
Opened 2026-10-07, session 07, from the author's question on the evening of 2026-10-06:

> Do you think we can work with an agent swarm when we first want to build the initial data warehouse? Which roles are there? Will it be self organizing under a mission, a vision, a constitution, a manifesto, a training program or something else? How do you envision the cooperation? The “overleg” and the making of “afspraken”?

The model's answer in that conversation, recorded here as a proposal and **not ruled**.

*A team, not a swarm.* A small set of roles with a lead, rather than a self-organising swarm. Agents left to organise
themselves tend to drift from the goal, duplicate work and agree with each other too easily, the more so when both
sides are the same model. Proposed roles: a lead who keeps the plan, hands out work, guards scope and keeps the
decision log; a source analyst who profiles sources, finds business keys, assesses historisation and writes metadata;
a modeller who proposes hubs, links and satellites from that; an engineer who writes the loads and marts as small
text files; a tester who builds the regression and plausibility tests and runs the gates of `ARC-OP-33`, preferably
on a different model, as [510](../docs/50_process/510_external-review.md) already does for review; and the author as
product owner, who rules on business meaning and on anything that changes the rules. Start with three or four roles
and split one only when it becomes a bottleneck.

*Governing documents in layers, not one.* A **constitution**: a handful of fixed principles that only the author
changes — for example models out of the data path (ADR-0004), text files in git (`ARC-OP-20`), no merge without
passing the gates, history never deleted. A **mission brief** per build: the sandbox, its scope, and what done means.
**Playbooks** per role: naming conventions, Data Vault patterns, test patterns, examples. The playbooks are the
training programme, because agents do not learn between sessions: what they know of the house rules is what is in
the repository. Agents may propose changes to them; the author accepts or not. A vision or manifesto serves people
more than agents and adds little beyond the mission brief.

*Overleg and afspraken.* Conferring happens in files, not in chat between agents: a proposal is written as a file,
the other roles comment on it, the lead decides or escalates. Agreements are decision records in git — what was
decided, why, what it replaces — binding until superseded, which is the release-note discipline of `ARC-OP-30`
applied to design. Mandate in three levels: within the conventions an agent decides alone; structural choices need a
second role's review; business meaning and changes to the constitution go to the author. Hand-offs are artefacts —
source profile, model proposal, code, tests — each consumed by the next role, so the chain stays traceable. Disputes
are settled by evidence first: a failing test outranks an argument, and only what evidence cannot settle reaches the
author.

This repository's own apparatus — [AGENTS.md](../AGENTS.md) as constitution, ADRs as agreements, this register, the
handovers, cross-model review — is already this pattern for design work, and is the obvious first draft of it for
build work.

Bears on `ARC-OP-8` (the unit of agent work), [070](../docs/00_concept/070_task-allocation.md) (the team would divide
its A column among roles), [130](../docs/10_architecture/130_agent-loop.md), `ARC-OP-20` (the constitution's
content) and `ARC-OP-33` (the gates). Open, and the model's addition rather than the author's: whether a team does
better than a single agent with the same playbooks on a build as small as the next sandbox. The first build could
be used to find out.

**Reviewed 2026-10-07, session 07:** [sol](../docs/30_research/notes/XREV_2026-10-07_agent-team_sol.md) FAILS — when the source analyst gets a key's grain wrong,
modeller, engineer and tester all build on the same false premise, every internally derived gate passes, and the
author finds it at review; [astra](../docs/30_research/notes/XREV_2026-10-07_agent-team_astra.md) HOLDS UNDER faculty mandates being preserved and acceptance being
bound to a revision, with the team's superiority unproved. Both found that *lead* collides with 070, where the lead is
whoever decides a task, often the author, and that a standing agent who "decides" exceeds the agentic layer's mandate;
and that the tester should design tests while deterministic machinery runs the gates. Astra added stale approval: a
test report for one model revision carried over to the next. Both judged that a single builder agent is likely as
good for one serial source, with independent review kept separate.

Recommended to the author, not ruled:

9. Rename *lead* to *coordinator*: it routes work and proposes; 070's allocation of who decides stands.
10. The tester designs and reviews tests; deterministic machinery runs the gates (`ARC-OP-33`).
11. Bind acceptance to a commit: a change in any input voids earlier approvals, and the gates rerun after integration.
12. Key and grain decisions are re-derived independently from the data by a second agent on another model before
    anything is built on them.
13. Start the first build with one builder agent plus independent cross-model review, and use the step log (ADR-0014)
    to see whether splitting roles would pay; add roles only on that evidence.

**Ruled 2026-10-07 by the author** on recommendations 9 to 13:

> 9. agree, maybe add orchestrator, planner
> 10. agree
> 11. agree
> 12. agree
> 13. agree

Accepted: *lead* becomes *coordinator*, which routes work and proposes, while 070's allocation of who decides stands
(9); the tester designs and reviews tests and deterministic machinery runs the gates (10); acceptance is bound to a
commit and voided by any change in its inputs (11); key and grain decisions are re-derived independently by a second
agent on another model before anything is built on them (12); the first build starts with one builder agent plus
independent cross-model review, and roles are added only when the step log shows it pays (13). On 9 he added
"maybe add orchestrator, planner". Read by the model, and confirmed below: *orchestrator* and *planner* are candidate
roles or names to consider when roles are added under 13 — a planner who breaks the build into steps, an
orchestrator who sequences and dispatches them, possibly the same function as the coordinator. Left open.
Confirmed by the author on 2026-10-07: "Your interpretation is correct."

### ARC-OP-35 — PARTLY RULED — BCBS 239 for banks in production; which of its consequences are adopted is open
**⛔ STATE: OPEN**
Opened 2026-10-15, session 08, on the author's instruction, verbatim:

> I’d like to make a note somewhere that the principles of BCBS 239 must be followed when working for a financial institution.

The principles, and what they would mean for the design, are in [152](../docs/10_architecture/152_bcbs-239.md).

**Ruled the same day**, in [ADR-0016](../docs/20_decisions/0016-regulatory-requirements-from-production.md): BCBS 239
binds banks and is a reference for other financial institutions; regulatory requirements are kept in mind from the
start, need not be met in a proof of concept or pilot, and apply in production (152 item 15); in an emergency a report
goes out despite a failed gate, *nood breekt wet*, released and recorded by a named person (152 item 16).

What is open:

1. **Which of the other consequences are adopted.** 152 §4 items 1 to 7 confirm the design. Items 8 to 14 would
   tighten it for in-scope data in production. After astra's review of 2026-10-21 each separates what BCBS 239 asks
   from a control proposed on top of it. Asked by the text: Tier 2's evidence route runs under institution-approved
   policies for authority, definitions and matching (ADR-0005); standing reconciliation; an inventory of validation
   rules; an inventory of manual procedures; consistency with the institution's dictionary; owner approval and
   reproducibility before retiring what fed a report. Proposed on top: the provisional lane closed where a claim's
   effect could be material (155); reconciliation thresholds and cadence; triage of plausibility warnings before a
   report goes out; a log of each manual adjustment. Those that change an accepted ADR need an ADR. Item 17 is a
   possible value area (ADR-0009).
2. ~~**What counts as production.**~~ Ruled 2026-10-21 (ADR-0016): from the moment a real decision or report relies
   on the system's output.
3. **Verification.** The ECB guide's expectation of attribute-level lineage is known only second-hand, from a vendor;
   it is to be checked against the guide. The BCBS text was read through a summarising fetch, not end to end.
4. ~~**Review.**~~ Done 2026-10-21: sol on §2 and §3
   ([XREV](../docs/30_research/notes/XREV_2026-10-21_bcbs239-facts_sol.md)), the table holding and §2 failing on three
   facts, and astra on §4 ([XREV](../docs/30_research/notes/XREV_2026-10-21_bcbs239-consequences_astra.md)), failing it
   on eight items that presented proposed controls as requirements. All findings applied; the amended text is
   unreviewed.

Bears on `CON-OP-2`: at a bank, review could take most of the human budget, depending on the policy of 152 item 9. Nothing here can be
exercised in the Wide World Importers sandbox (`EVI-OP-7`), which has no risk data.

### ARC-OP-36 — PARTLY RULED — Information analysis before building; how it is recorded is open
**⛔ STATE: OPEN**
Opened 2026-10-18, session 08, on the author's point, verbatim:

> So I was thinking, before anything gets built, there should be a business analysis phase, or rather an information
> analysis, to determine what's in the tables. Things to look out for are: granularity, meaning, temporal
> characteristics, relation to other tables. Can you store this somewhere? And also think of other things that should
> be inventoried before building anything? In terms of analysing the tables that are to be imported?

Recorded in [129](../docs/10_architecture/129_information-analysis.md): his four items and 22 further items proposed
by the model in reply.

**Ruled the same day** in [ADR-0017](../docs/20_decisions/0017-information-analysis-before-building.md): all 26 items
stay; the minimum (items 1, 3, 5, 6, 7, 19) with hard effort and no guessing, uncertainties stated clearly; the rest
best effort; a confidence level, reasoning and evidence where possible for every item; never a hard gate; the first
trial on the Wide World Importers sandbox as a proof of concept; review on sol and astra.

What is open:

1. **How it is recorded.** The author asked for a structure usable primarily by agents — folders, small text files,
   gitable, safe for several agents at once, searchable, predictable. Proposed in
   [`analysis/README.md`](../analysis/README.md): a folder per source and per table, a file per item and per column
   (not a folder per column, and no topic folders except for the four cross-table items), evidence as JSON
   aggregates, a confidence scale. Not ruled; unenforced by the checker until it is.
2. **The trial.** Round 1's minimum done on 2026-10-18 for all 48 WWI tables: 31 base tables with items 01, 03, 05,
   06, 07, 19 and 27, and the 17 history tables with item 05 (238 item files, 1,004 claims, 152 evidence files under
   [`analysis/wwi/tables/`](../analysis/wwi/tables/); scripts in [`prototypes/information_analysis/`](../prototypes/information_analysis/)).
   `Sales.Orders` was done by hand; the other tables by a generator that writes the mechanical claims from the
   evidence, with the agent's judgement claims per table. Findings that bear on a build include: the source masks
   supplier bank details, and the extract, made as owner, holds them in clear; the three transaction tables share one
   numbering; system-time columns record wall-clock edits (one row stamped 2022); `ColdRoomTemperatures` keeps only the
   latest reading, its history table holds 3.7 million readings; `VehicleTemperatures.FullSensorData` is malformed JSON
   in every row; tax on invoice lines is rounded per line, half up; head-office terms are copied onto branches in
   `Customers`. Reviewed by astra on three tables
   ([XREV](../docs/30_research/notes/XREV_2026-10-18_round1-dossiers_astra.md)): FAILS on an "exact" claim computed from
   rounded shares and four lesser defects, all fixed before commit; sol's pass on three other tables never wrote an
   answer and is owed again. Owed besides: the best-effort items, round 2, and what it cost.

   **Ruled 2026-10-18, 21:55** on the dossiers' questions for a person, verbatim: "Yes, this is a sandbox environment
   with test data." So in the WWI sandbox the sensitive columns (bank details, receiver names and positions, password
   hashes, employee terms) may be loaded as they are; the sensitivity claims stand as the classification a production
   implementation would need (ADR-0016). Not yet carried into the item files. The order-count and reporting-date
   questions he asked to have explained first; and he asked whether every column's business meaning is analysed, against
   which documentation, and in what structure (answered in conversation; awaiting his reaction).

   **Ruled 2026-10-18, 22:27**, in [ADR-0020](../docs/20_decisions/0020-analysis-describes-the-as-is.md): while in the
   analysis stage, the analysis describes the as-is and does not look ahead; the order-count and reporting-date
   questions belong to a later stage and were retracted from the dossiers, with design advice removed from their
   claims; that "order" means two things is recorded as a peculiarity of `Sales.Orders` (27, C12). He asked for the
   column meanings (item 2) for every column, and for sol's review to be tried again.

   **2026-10-19.** Sol's retried review, in two passes, returned **FAILS** on both
   ([A: Invoices, CustomerTransactions](../docs/30_research/notes/XREV_2026-10-18_round1-dossiers-a_sol.md);
   [B: ColdRoomTemperatures and its history](../docs/30_research/notes/XREV_2026-10-18_round1-dossiers-b_sol.md)): code
   labels, the contents of the delivery events and the history table's readings were asserted from evidence that does not
   observe them; uniqueness seen in one extract was rated high; one design statement remained. All eleven findings fixed,
   and their kind in every table: new evidence for code labels, delivery events and the cold-room history; uniqueness
   not declared is medium everywhere; README section 5 now separates a count over an extract (high) from a rule
   generalised from it (medium). **Column meanings** done: item 02 for all 368 columns of the 31 base tables, best-effort
   tier (21 at unknown, 312 medium, 35 high), cross-referenced with Microsoft's description of the business, which
   documents the business and not the columns ([`_source/18_documentation.md`](../analysis/wwi/_source/18_documentation.md)).
   Totals then: 606 item files, 2,383 claims, 178 evidence files. Reviewed the same day by sol (Sales.Invoices, Customers,
   Orders) and astra (SupplierTransactions, People, VehicleTemperatures, StockItems), both **FAILS**
   ([sol](../docs/30_research/notes/XREV_2026-10-19_column-meanings_sol.md),
   [astra](../docs/30_research/notes/XREV_2026-10-19_column-meanings_astra.md)): the audit-column templates asserted
   more than their evidence; LogonName's placeholder claim was contradicted by the profile; one Microsoft quotation was
   written from memory and is not in the evidence. All fixed in every table, with new evidence on editors, system time
   and logon names; Microsoft's text is now cited only as low-confidence context. Now 606 item files, 2,435 claims,
   209 evidence files; columns 34 high, 256 medium, 56 low, 22 unknown. New finding: two logon names are each shared by
   two people permitted to log on.

   **Round 2 begun 2026-10-19** (approved 22:01, "okay, go ahead."): the minimum (01, 02, 06, 07, 27) for all 100
   relations between the 31 base tables - the 98 declared foreign keys and two undeclared composite relations of stock
   movements to document lines - under [`analysis/wwi/across/`](../analysis/wwi/across/), with the generated
   [`candidates.md`](../analysis/wwi/across/candidates.md): 500 item files. No orphan in any relation; no undeclared
   ...ID column; 38 column names shared between tables, left as assumed. Findings: the customer ledger is booked on the
   bill-to customer on every invoice entry, while stock movements, orders and invoices' CustomerID name the customer
   delivered to, so "CustomerID" means two roles across tables; payments name no invoice, so which invoices a payment
   settles is not recorded by key, for customers and suppliers alike; each invoice line has exactly one stock issue,
   and a join on InvoiceID alone gives 847,672 rows instead of 228,432; several columns repeat a parent's value on
   every row (invoice contact, accounts person, salesperson, delivery method, package types); purchase-order lines count
   outer packages and sales lines unit packages; the purchase-order "contact" is a WWI salesperson, never the
   supplier's contact. Reviewed by sol and astra, both **FAILS**
   ([sol](../docs/30_research/notes/XREV_2026-10-19_relations_sol.md),
   [astra](../docs/30_research/notes/XREV_2026-10-19_relations_astra.md)); all findings fixed in every relation. Owed:
   item 03 (point-in-time) per relation, the reconciliations (invoice totals against lines, stock movements against
   holdings, quantities of lines against movements), processes, terms and entities.

   **2026-10-19, 23:11**, the author, verbatim in step S08-080: the orphan test is referential integrity and should be
   written down as a guideline (done: analysis/README.md section 9, "The tests per relation"); the two customer roles
   are "more for the next phase", where the two may be grouped if a relation is found and it adds value - parked here
   under ADR-0020. The data refines the roles: the order and the invoice's CustomerID name the customer delivered to,
   the ledger the customer billed (the head office where there is one), so who placed the order is the delivered-to
   customer. **Reconciliations** (item 16 across tables, six, best-effort tier, under
   [`across/reconciliations/`](../analysis/wwi/across/reconciliations/)): each stock issue equals its invoice line's
   quantity negated, on the invoice date, one to one; each ledger invoice entry equals the sum of its lines exactly;
   payment matching (afletteren) leaves no key, but in this extract each payment equals the bill-to customer's invoices
   finalized that day, a customer pays at most once a day, and no invoice is part paid or overpaid - every paid invoice
   was settled in full one day after its date, up to 47 invoices by one payment; the supplier side is the same with 0
   to 6 days' delay; supplier invoices equal their purchase orders at the expected price, tax 15% per line except on 5;
   stock holdings cannot be derived from the movements, neither in level nor in one day's change. So the one-to-one of
   lines and stock issues (goods) and the many-to-one of invoices and payments (money) do not contradict each other;
   instalments and overpayments do not occur in this test data, and how the source would record them is unknown.
   Reviewed by sol and astra, both **FAILS**
   ([sol](../docs/30_research/notes/XREV_2026-10-19_reconciliations_sol.md),
   [astra](../docs/30_research/notes/XREV_2026-10-19_reconciliations_astra.md)); all findings fixed.

   **2026-10-20** (approved 07:31, "Okay go ahead."): round 2 completed to best effort. **Point in time** (item 03) for
   98 relations: joined in the extract, a row gets its parent's current version; at their own dates, nearly all sales
   and purchase lines and stock movements named an earlier version of their stock item, which differs only in
   CustomFields and Tags, and 1,868 invoices an earlier customer version, differing in CreditLimit; orders, invoices and
   purchase orders are not versioned; no gaps between versions. **Processes** (item 24): order-to-cash (picked,
   invoiced and issued on one day, delivered and paid the next; backorders keep the original's date and are invoiced
   up to 1,116 days later), procure-to-pay (received in full 1 to 3 days after ordering, mostly 19 days before the
   expected date, invoiced on receipt, paid 0 to 6 days later), stocktake (quarterly, on the last day of January,
   April, July and October: the quarter ends of a financial year starting 1 November). **Terms** (item 25: order,
   customer, invoice, payment, transaction, quantity, contact person, finalized) and **entities** (item 26: customer,
   supplier, person, stock item, location), which link the claims that own each fact. Reviewed by sol and astra, both
   **FAILS** ([sol](../docs/30_research/notes/XREV_2026-10-20_point-in-time_sol.md),
   [astra](../docs/30_research/notes/XREV_2026-10-20_stocktake_astra.md)); all findings fixed. The record now holds
   1,226 item files. Open: the questions left unknown in the files (generated list: `grep -rl "confidence: unknown"
   analysis/`), a second extract to turn one-extract observations into rules, and the next phase.

   **Second extract, 2026-10-20** (asked 10:08, "allright, please continue with the second extract"): the agent advanced
   the sandbox one day through the request folder, with no act by the author; 2016-06-02 was simulated and extracted.
   [`_source/22_stability.md`](../analysis/wwi/_source/22_stability.md) records the recheck: no rule tested is
   contradicted - the same 13 tables change in both transitions in the same way, every candidate key is still unique,
   no relation has an orphan, the one-to-one relations stay one-to-one, the copies along two routes agree, the six
   reconciliations are exact again, the process timing is the same - so the medium claims stay medium, now observed on
   two days. Narrowed: almost all never-picked orders are backorders not yet supplied; the two open purchase orders were
   received in full the next day, one movement per line; the 56 open customer invoices were paid in full the next day.
   Still open: part payments and part receipts (none on either day), the 4 open supplier invoices, weekends and period
   ends. The other files keep describing 2016-06-01 and show as ageing. Reviewed by astra and sol, both **FAILS**
   ([astra](../docs/30_research/notes/XREV_2026-10-20_second-extract-readings_astra.md),
   [sol](../docs/30_research/notes/XREV_2026-10-20_second-extract-counts_sol.md)); all findings fixed.

   **Position in the schema, item 29, 2026-10-20** (asked 11:25; ruled 18:55 in
   [ADR-0021](../docs/20_decisions/0021-position-in-the-schema.md): a new item, the method recorded for reuse, the
   classification adopted in full, and "be cautious and sensitive to excluding attributes etc. that give a distorted
   picture of reality"). The method is [131](../docs/10_architecture/131_structural-position.md); the record is
   [`_source/29_position.md`](../analysis/wwi/_source/29_position.md) and a `29_position.md` for each of the 48 tables.
   Without the audit column `LastEditedBy` the hubs are StockItems, Suppliers, Customers and Cities, and People falls from
   rank 1 to 12, central through 12 roles rather than paths; the classes by rule agree with item 5's role on 27 of 31
   base tables (not on the three geography tables and SpecialDeals, whose readings stand beside the class). Reviewed by
   astra and sol, both **FAILS** ([astra](../docs/30_research/notes/XREV_2026-10-20_position-readings_astra.md),
   [sol](../docs/30_research/notes/XREV_2026-10-20_position-code_sol.md)); all findings fixed, among them that behaviour
   is now judged on business columns only, the distortion principle applied beyond links.

   **Measures, derived columns and arithmetic, items 8, 9 and 28, 2026-10-20** (asked 21:51, "Yes, do items 8,9 and 29
   before we close", 29 read as 28): `measures.py` profiled the numeric columns of the 17 tables that have any and tested
   the formulas and rounding they suggest; `08_measures.md` for 17 tables, `09_derived.md` for 8, `28_arithmetic.md` for 4.
   Among the findings, each on every row of the extract: tax per invoice line reproduced by rounding half up to cents;
   LineProfit = Quantity x (UnitPrice - the item's current LastCostPrice); RecommendedRetailPrice = UnitPrice x 1.3 x
   (1 + TaxRate / 100); ExpectedUnitPricePerOuter = LastCostPrice x QuantityPerOuter; an invoice's tax is the sum of its
   rounded line taxes, not 15% of its amount; no amount is stored on an order line; picking and receiving are all or
   nothing. Reviewed by astra and sol, both **FAILS**
   ([astra](../docs/30_research/notes/XREV_2026-10-20_measures-readings_astra.md),
   [sol](../docs/30_research/notes/XREV_2026-10-20_measures-code_sol.md)); all findings fixed.

   **Close of the analysis stage, 2026-10-20** ([ADR-0022](../docs/20_decisions/0022-the-analysis-stage-closes.md)).
   *Coverage* (counts from the record as committed): the minimum items and item 27 for all 31 base tables; role (item 5)
   and position (item 29) also for the 17 history tables; the meaning (item 2) of 368 columns; measures (item 8) for the
   17 tables with numeric columns, derived columns (item 9) for 8, arithmetic (item 28) for 4; across tables, 100
   relations with their five minimum items, 98 of them with point-in-time behaviour, 6 reconciliations, 3 processes, 8
   terms and 5 entities; documentation (18), stability against a second day (22) and position (29) for the source. In
   all 1,303 item files and 4,892 claims; 187 files have at least one claim of unknown confidence, the open questions of
   the record (`grep -rl "confidence: unknown" analysis/`). *Not covered*, with the reason: codes, formats, copies,
   hierarchies, quality, volume and per-table reconciliation (items 10 to 13, 15 to 17) as items of their own - parts of
   them sit in items 7, 27 and the column meanings - because they bear less on an integration layer and ADR-0017 makes
   them best effort; provenance, ownership and demand (14, 20, 21) because they need people the sandbox does not have;
   extraction (23) beyond what item 7 records of the extracting account. *As of*: the files describe the extract of
   2016-06-01; `_source/22_stability.md` rechecks them against 2016-06-02. *Parked for the next phase*: the two customer
   roles (above), and the warning that "orders" means two things (item 27). *Lessons*:
   [2026-10-20-information-analysis-trial-lessons](../docs/30_research/notes/2026-10-20-information-analysis-trial-lessons.md).
   This row stays open for the questions of unknown confidence and for what modelling adds to the record.
3. **Review.** Astra on the record layout (below, R1-R11, ruled in ADR-0018). Sol on 129's inventory: the first,
   large pass never wrote an answer; re-sent in two parts, both returned.
   [Gaps and minimum](../docs/30_research/notes/XREV_2026-10-18_information-analysis-inventory-gaps_sol.md):
   **FAILS** — two tables whose foreign key could point at either of two candidate keys pass the minimum, and the
   builder joins on the wrong one with a clean one-to-one result; and two things are uncovered, the source's arithmetic
   (precision, rounding mode, rounding at line or document) and what the extraction identity can actually see
   (row-level security, masking, tenant context).
   [Consistency and facts](../docs/30_research/notes/XREV_2026-10-18_information-analysis-consistency_sol.md):
   **FAILS** — 129 said its output was dataset and field cards only, leaving relationship findings no home, against
   128; **corrected in 129 the same day** as a plain inconsistency. Four of five WWI facts checked hold; the fifth
   (invoice header totals) was not cheaply checkable, since `Sales.Invoices` has no evidence files yet.
   **Recommendations to the author, not yet ruled:**
   - **R14. A minimum per join**, beside the minimum per table: before a build joins two tables, the relation's
     item 4 and the meaning (item 2) of its key columns are done with the minimum's hard effort. Sol's counterexample
     passes every per-table test.
   - **R15. Visibility of the extraction identity joins item 7 (population)**, so it is minimum: what row-level
     security, masking or tenant context hides from the account that extracts. Relevant to WWI, whose simulator
     applies row-level security (`Application.Configuration_ApplyRowLevelSecurity`); setup compared the customers seen
     by owner and reader once (663 each, `data/wwi/inventory/inventory.json`).
   - **R16. A new item 28, arithmetic policy**: precision, rounding mode, where rounding happens (line or document)
     and how residues are treated; best effort, since it decides whether recomputed values reconcile rather than what
     the grain is.

   **Ruled 2026-10-18, 14:38**, in [ADR-0019](../docs/20_decisions/0019-information-analysis-in-two-rounds.md): the
   analysis runs in two rounds, round 1 per table (the brief), round 2 across tables (how tables relate, warnings,
   the meaning of assumed or proven joins), R14 belonging to round 2; R16 accepted as item 28. **Ruled further at 14:59** ("R15: agreed. Round 2 structure looks good.
   Please proceed."): round 2's `across/` tree and its minimum, and R15 under item 7; recorded in ADR-0019 item 5. The
   two points as they stood before that ruling, superseded and kept for provenance:
   - **Round 2's folder structure**, proposed in [`analysis/README.md`](../analysis/README.md) section 9: an
     `across/` tree with a folder per relation holding item files 01, 02, 03, 06, 07 and 27, folders for processes,
     terms, entities and cross-table reconciliations, and a generated list of candidate relations; minimum per
     relation 01, 02, 06, 07, 27.
   - **R15, explained to the author on 2026-10-18 and awaiting his ruling.** A database can show different accounts
     different rows (row-level security) or blank out column values (dynamic data masking). An extract made through a
     restricted account can then look complete while it is not, and every count, total and orphan rate computed on it
     is quietly wrong. The check: does the table carry a security policy or masked columns, and do the extracting
     account and an unrestricted account see the same row count? In WWI, Microsoft's simulator applies row-level
     security to customers; setup compared the customers seen by owner and reader once (663 each). On 2026-10-18,
     queried as `nsdn_reader`, the catalogue showed no security policy at all — which either means there is none, or
     that the account cannot see them, and that ambiguity is the point of the check. Astra's verdict,
   [XREV_2026-10-18_information-analysis-record_astra](../docs/30_research/notes/XREV_2026-10-18_information-analysis-record_astra.md):
   **FAILS** — two agents following the rules can allocate the same evidence id. Its other findings: a column file
   is shared by every item about that column, so item ownership is not file ownership; source names break as file
   names (`/`, `AUX`, non-ASCII, and `Sales.EU` + `Orders` against `Sales` + `EU.Orders`); one status and one
   confidence per item bundle several claims, against ADR-0011's assertion and 120's lifecycle; evidence is not
   content-addressed and lacks its computation; "ruled by a person" wrongly counts as high confidence; set-level
   findings such as cross-table reconciliations have no home; and the example restates facts and drifts from the
   README in seven places. **Recommendations to the author, not yet ruled:**
   - **R1. A folder per column after all**, with one file per item inside it (`columns/<Column>/<nn>_<slug>.md`),
     created only when there is something to say. The author's instinct; it is what makes item ownership file
     ownership.
   - **R2. Schema and table as two folder levels** (`tables/<schema>/<table>/`), and names escaped reversibly: keep
     `A-Z a-z 0-9 _ -`, percent-encode every other byte of the UTF-8 name (`Unit%2FPrice`), encode the last letter
     of a reserved Windows name (`AU%58`); the checker flags names that differ only in case. Every path is then
     ASCII and constructible from the source name.
   - **R3. Evidence content-addressed**: named by the first 16 hex digits of the SHA-256 of the record without its
     write time, written once, never overwritten. No id is allocated, so no two agents can collide.
   - **R4. Each evidence record holds its computation** (query or code text) and its run time; catalogue evidence is
     pinned to the database and the simulation clock; catalogue metadata may be kept verbatim (aggregates-only applies
     to data rows); a fetched implementation is evidence too, with URL, date and the excerpt relied on.
   - **R5. One line per claim inside an item file** — id, claim type, lifecycle status (120's: proposed, accepted,
     contested, superseded, retracted), confidence, evidence, effective and observation time, recheck condition, text
     — so each claim is an assertion in ADR-0011's sense; the front matter becomes the item's summary; staleness is a
     separate flag. The uncertain part of a minimum item is its own claim with confidence `unknown`.
   - **R6. Confidence measures evidence, not authority**: a ruling sets status `accepted` and `ruled_by`; it does not
     raise confidence.
   - **R7. Each fact once**: other files link to the file that owns it.
   - **R8. A permanent id** per subject in the front matter, the path being only its current name (120's identity
     plane).
   - **R9. Homes for set-level findings**: `<source>/_source/` for source-wide ones, `<source>/reconciliations/` for
     item 16 across tables, `analysis/_landscape/` for findings spanning sources.
   - **R10. Say plainly** that "what must be rechecked if this changes" needs a generated dependency index, not grep.
   - **R11. Bring the example into line** with the revised README.

   **Added 2026-10-18, 14:07, on the author's two further points**, verbatim:

   > one more thing before we proceed, we should also test each table for peculiarities like multiple granularities
   > in one table (a table containing both customer data and contract data apart from keys, or events/transactions and
   > balances), I'm sure you can come up with more. Also, in every file we should probably record who wrote it, when
   > it was written, maybe also other meta data. That we we can see if claims are stale or fresh.

   The first is recorded as item 27 of [129](../docs/10_architecture/129_information-analysis.md), eighteen tests
   with WWI cases where observed (header totals that equal line counts on every invoice; invoice and payment events
   with a balance in one table; three kinds of stock movement and eight kinds of person under one key each).
   - **R12. Provenance and freshness in every file**, in the front matter: `written_by` (agent or person, as named in
     `records/vocabulary.json`), `written_at` (UTC), `step` (the step-log id, which says who asked and why),
     `method` (tool or script and its git commit), `inputs` (source, extract date, manifest hash, and a hash of the
     table's catalogue columns, so a schema change is visible), `last_checked_at`, `last_checked_by` and
     `last_checked_against` (when a claim was re-verified unchanged on a newer extract without being rewritten),
     `reviewed_by`/`reviewed_at`, `ruled_by`/`ruled_at`, `supersedes`/`superseded_by`, and `recheck_when` (the
     invalidation predicate of 120). Each claim line carries its own `as_of` and `checked_at`, since claims in one
     file age separately. Freshness is computed by a tool from these fields — **fresh** when last checked against the
     newest extract with no recheck condition met, **ageing** when checked only against an older one, **stale** when
     a recheck condition is met or new evidence disagrees — not set by hand. Git cannot carry this: every commit in
     the repository is under the author's git identity whichever agent wrote it, and a commit records when it was
     made, not when the analysis was done or which data it read.
   - **R13. The item-27 tests that bear on grain** (tests 1 to 9 and 11 to 13) are done with the minimum's hard
     effort as part of item 1; the rest best effort. Would amend ADR-0017.
4. **The citations** of 129's prior-art paragraph.

Related to `EVI-OP-4` (the minimum profiling pass), `ARC-OP-24` (the task allocation it follows) and `ARC-OP-34` (the
builder agent, for which this would be the input).

The list of open questions as opened, superseded by the ruling of 2026-10-18 and kept for provenance:

1. **The list.** Which of items 5 to 26 the author keeps, and what is missing.
2. **Phase or minimum.** Whether every table is fully analysed before the first build, or a minimum dossier (129
   proposes items 1, 3, 5, 6, 7 and 19) is required per table with the rest completed as the build reaches it; and
   whether that minimum is a quality gate, and blocking (`ARC-OP-33`).
3. **The record.** The sections of the `dataset` and `field` cards that hold the findings; shares the owed front
   matter of `ARC-OP-27`.
4. **A first trial.** Whether the agent's first work on the Wide World Importers extracts (`EVI-OP-7`) is this
   inventory, which needs no act of the author's on the Windows side and would test whether the list is complete.
5. **Review.** 129 is unreviewed; review on sol and astra per [510](../docs/50_process/510_external-review.md),
   against the standard of whether it covers what an experienced information analyst would inventory before a build,
   and whether it duplicates or contradicts 127 and 128. The prior-art paragraph owes citations.

### ARC-OP-37 — PARTLY RULED — The integration layer: raw vault, business vault, calculation engines and marts
**⛔ STATE: OPEN**
Opened 2026-10-26, session 09, from the author's questions of 25 and 26 October while the design of the generic
integration layer for Wide World Importers began (handover 09). Drafted in
[144](../docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md), which quotes the questions
verbatim; at the author's request, verbatim: "Please store all the above information and decisions in an appropriate
place in the repository."

**Ruled 2026-10-26, 08:58**, in [ADR-0024](../docs/20_decisions/0024-calculation-engines-are-a-versioned-source.md):
business rules and calculations beyond basic arithmetic run in calculation engines, versioned software with unit tests
and inline documentation; every result is stored with its engine version; the engines' output is a separate source;
the boundary between SQL and engine as proposed; on a new version everything is recomputed when compute and storage
allow, and a new version is new data even when the values are the same; corrected inputs are rerun, using
bitemporality.

**Ruled 2026-10-26, 09:12**, verbatim: "3: engine results go in the raw vault. Open fall back: if there is not enough
compute, first let's try it from a cut-off date. If still not enough, only do going forward. It always requires human
adjudication." Recorded in [ADR-0025](../docs/20_decisions/0025-engine-results-in-the-raw-vault.md), which closes
items 3 and 5 below; 030 corrected. On marts, the same message, recorded in
[ADR-0026](../docs/20_decisions/0026-conformed-dimensions-and-fact-table-changes.md): dimensions are conformed and
shared; design is mainly about fact tables; a new question that only partly fits a fact table gets an analysis of how
much the table would change and how far it drifts from its original intent, decided formally where the questions can
be formalised and by a person otherwise; extending a fact table is a fundamental decision and not a continuous
process. The considerations he asked for are drafted in
[146](../docs/10_architecture/146_fact-tables-and-new-questions.md).

Open, each proposed by the model and not yet ruled (items 3 and 5 ruled, kept for the record):

1. **The raw/business line** (144 §2): the raw vault as memory, holding what a system delivered, insert-only,
   generated, with only loss-free technical transformations; the business vault as understanding, holding
   interpretation, rebuildable, each object citing its decision; the boundary is provenance (*was this delivered by a
   system?*, our engines included), the second test of the first version having been withdrawn after review; and
   satellites grouped by source and assertion, split only for a stated reason. Note 030 §2 item 4 still says "split by
   source and rate of change" and is to be brought in line once this item is ruled.
2. **Several sources for the same entities** (144 §3): one raw vault; satellites always per source; a hub key shared
   only when the identifier has the same meaning across sources, otherwise qualified by a key-space code; links shared
   by issuer namespace rather than by system; links defined by keys, meaning and grain; matching across key spaces in
   the business vault with proposal, decision and publication kept apart (ADR-0011); delivered crosswalks loaded as raw
   with the relationship the source states.
3. **Where engine results land.** *Ruled 2026-10-26: the raw vault (ADR-0025).* The model proposed the raw vault, under the engine's own source code; the
   financial-services note [030](../docs/60_domain-knowledge/financial-services/030_bird-as-data-vault-foundation.md)
   §2 item 5 places calculated values in the business vault. One of the two is to be ruled, and the other document
   corrected.
4. **Conditions on engines** (144 §4, items 2 to 8): a version is code plus locked dependencies; each result records
   engine, version, run and the as-of of its inputs; versions side by side, so a release's impact is the difference of
   two versions on the same inputs (`ARC-OP-30`); money never in binary floating point; a fixed pipeline order without
   cycles; the source's computed columns as test oracles; results keyed at full calculation grain, and possibly run
   hubs. Extended after review (144 §4 items 2, 3 and 9 to 11): a version identifies code and execution environment by
   digest; every run stores an input manifest and a run record; only completed runs are published; every fallback
   leaves a policy record; results carry knowledge time as well as valid time.
9. **Reruns with unchanged results** (144 §4 item 10): whether a rerun after corrected inputs is recorded as new even
   when value and version are unchanged, extending the author's ruling that a new version is new data. Raised by
   review. *Ruled 2026-10-26, 11:29 (ADR-0024 decision 6), verbatim: "7. If it is rerun, with corrected input, under the same version, and the outcome is the same, then it should probably be a new row, because the new version means it's new. Otherwise we get into trouble if e.g. we want to do a regression analysis between versions, with the datawarehouse as the origin."*
5. **Recomputation when compute or storage do not allow everything.** *Ruled 2026-10-26 (ADR-0025): a cut-off date
   first, then going forward only, each step adjudicated by a person.*
6. **The grey zones** (144 §6): whether the raw vault allows tidying beyond loss-free conversion; and values that
   cannot be rebuilt later because their inputs are not versioned in the source, such as `LineProfit` against the
   cost price in `Warehouse.StockItemHoldings`.
7. **The two decisions and the route of handover 09.** Decision 2 (derived measures) is largely answered by ADR-0024;
   decision 1, whether the integration layer as a whole is bitemporal, is not yet put formally, though the author's
   answers rest on a bitemporal structure. *Decision 1 ruled 2026-10-26, 12:03, in
   [ADR-0027](../docs/20_decisions/0027-bitemporal-integration-layer.md): bitemporal on evidence (valid time only from
   source evidence, otherwise unknown), source system time kept as a labelled third timestamp, "as of" views in marts;
   the agent proposes each table's business time from the analysis record and the author rules only where evidence is
   weak. That per-table proposal is owed before the first load.* The route proposed on 2026-10-21 (concepts and keys, relationships,
   descriptive sets, time, derived values, writing it down) awaits his answer.
8. **Marts.** The author asked on 2026-10-26, verbatim: "do we derive datamarts from the raw and business vault? I
   think we should build dimensional models for every distinct use case. What are your thoughts?" The model's answer
   the same day, not ruled: marts are built from the business vault, including stored engine results, and reach the
   raw vault only through point-in-time and bridge structures, never calculating; a dimensional model per distinct
   use case, with conformed dimensions shared across marts and generated once, so that "customer" means one thing
   everywhere; each mart cites the use case or decision it serves ([140](../docs/10_architecture/140_data-vault-automation.md))
   and is retired when its consumers are gone ([145](../docs/10_architecture/145_entropy-and-pruning.md)); dimensional
   as the default shape, with other shapes where a consumer needs them (a regulatory extract at a fixed grain, a
   feature table, agents' access). Open with it: what counts as a distinct use case. *Partly ruled 2026-10-26
   (ADR-0026, above).* Still open: where marts take their data from; the considerations, the four-way
   classification and the case base of 146. *Ruled 2026-10-26, 09:20 (ADR-0026 decision 6), verbatim: "20. No
   adjudication needed. And if they cause any unforeseen problems, the unit tests, data tests and plausibility tests
   should catch them."* A minor extension needs no adjudication; it depends on tests not yet built (`ARC-OP-31`,
   `ARC-OP-33`).

**Step A proposed 2026-10-26, session 10** (handover 10), not ruled: [147](../docs/10_architecture/147_wwi-concepts-keys-and-business-time.md) proposes twenty-two hubs for the 31 base tables of WWI, keyed on the source's record identifiers in the key space `wwi` of their issuer (declared-unique names are renamed in eight tables, `06_keys.md#C5`) and on ISO 3166-1 for country; code lists as hubs only where they take part in a relationship, six as reference tables; lines as hubs on their own identifiers; and the business time of every table under ADR-0027 decision 4, with existence dated by the event date and each milestone a fact of its own. Reviewed on sol in two passes, both FAILS on the first version, all findings applied or partly applied ([keys](../docs/30_research/notes/XREV_2026-10-26_147-keys_sol.md), [business time](../docs/30_research/notes/XREV_2026-10-26_147-business-time_sol.md)); the revised text is unreviewed. Three cases are put to the author: the ISO key for country, how milestones enter valid time (recommendation (c)), and the two undescribed sensor tables. *Ruled 2026-10-28, 10:23, in [ADR-0028](../docs/20_decisions/0028-wwi-country-key-milestones-and-sensors.md), verbatim: "1. Okay. 2. Sounds good. In Kimball terms, this would be an accumulating fact table, but we should indeed separate them out, make separate rows of it. So are they also satellites? I'll leave it up to you. 3. Okay." The country is keyed on ISO 3166-1; option (c), each milestone a satellite of its own (the model's choice under his delegation), the accumulating snapshot in the marts; the sensor tables as proposed. The rest of 147 remains proposed.* *Ruled as a whole 2026-10-28, 10:31, in [ADR-0029](../docs/20_decisions/0029-wwi-step-a-concepts-and-keys.md), verbatim: "Agreed with all point, but there is one thing." The one thing was a question on synthetic hub keys; still open: how a hub's primary key is formed from its business key (hash, sequence or concatenated natural key; 142 and 144 §2 assume a hash).* *Ruled 2026-10-28, 11:01, in [ADR-0030](../docs/20_decisions/0030-hub-and-link-keys-are-hash-keys.md): hash keys, verbatim: "Okay, let's do hash keys then."* **Step B proposed 2026-10-28, session 10**, not ruled and unreviewed: [148](../docs/10_architecture/148_wwi-relationships.md) proposes forty-nine binary links between the twenty-two hubs, one per relationship and role, loading copies along a second route as the source's own assertions, no link for empty columns, reference codes or the audit column, effectivity for the masters' links and the picker link dated by its milestone, and four relationships derived in the business vault. Raised by review and owed with step C: milestone corrections supersede over their whole claimed validity at the later knowledge time, so ADR-0027's "valid to from the next row" applies within one knowledge-time slice.

Review: **done 2026-10-26 on sol in four passes, all FAILS on the first version, all findings applied** (dispositions
in [line](../docs/30_research/notes/XREV_2026-10-26_144-raw-business-line_sol.md),
[sources](../docs/30_research/notes/XREV_2026-10-26_144-multiple-sources_sol.md),
[engines](../docs/30_research/notes/XREV_2026-10-26_calculation-engines_sol.md),
[fact tables](../docs/30_research/notes/XREV_2026-10-26_146-fact-tables_sol.md)); astra was assigned two of the passes
twice and wrote nothing. The revised texts are unreviewed. The review as first planned, superseded by the above:
144, 146 and ADR-0024 to ADR-0026 unreviewed; review on sol and astra per
[510](../docs/50_process/510_external-review.md), against the standard of whether a Data Vault practitioner would
accept the raw/business line and the multi-source rules, and whether the engine design gives reproducible, auditable
figures. Related to `ARC-OP-29` (the data model), `ARC-OP-27` (temporal behaviour), `ARC-OP-30` (release regression),
`ARC-OP-31` (plausibility), `ARC-OP-35` (BCBS 239) and `ARC-OP-36` (the analysis record, which the design cites).

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

**2026-09-20, session 02.** `ARC-OP-18` argues the sample must be built to **span rules**
rather than to be a random sample of entities, or it measures performance on whichever
conventions it happened to include — which is `ARC-OP-17` arriving in the instrument rather
than in the system. That must be settled before the sample is frozen, and
[410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md) requires the
freeze to happen before development begins.

### EVI-OP-2 — Candidate public dataset survey
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 3)*

Sources must be independently built, must genuinely share entities, and must permit
identity to be established by hand for a sample. Dutch public registers are the leading
candidate on structural grounds. The survey needs no code and is the natural first
substantive task of Mode 1.

**Extended 2026-09-25, session 05.** A second requirement follows from `CON-OP-16`: the sources should
let a landscape grow one source at a time, with sources that change over time, so that maintenance
effort per stable unit of landscape — with burden indicators held steady — can be measured as the
landscape grows. Per [ADR-0012](../docs/20_decisions/0012-generic-framework-lean-start.md), the people
in such a sandbox are simulated and results must say so.

**Re-themed 2026-09-25, session 06, by the author.** The sandbox is to be a landscape of businesses in
the Netherlands, if needed restricted to the wider Utrecht region, serving a question he actually has.
In his words:

> I've always been interested in exploring the types of business there are and their turnover and
> revenue. It's kind of dual purpose. If I find large enough businesses in underserved
> BI/Analytics/AI markets, I might have an interesting proposal. [...] Also I am interested in Dutch
> businesses that are for sale. Interested in their earnings potential, but also in what gains they
> could have by properly implementing the aforementioned. Maybe throw in e-commerce opportunities for
> existing businesses in the mix.

He accepted the proposed "Utrecht business landscape" ("15: yes"), ruled out spending on it ("I don't
want to spend money on this use case"), set no size floor ("I don't really have a floor"), and endorsed
detecting web-shop and analytics technology from company websites ("is a good one!"). The paid KVK API
is therefore out; names come from free sources matched on address, name and domain, which is itself the
matching the falsifiable core is about. Candidate and rejected sources are recorded in
[`../records/sources.jsonl`](../records/sources.jsonl). The province's jobs register (PAR) is the
intended backbone and is blocked until downloaded by hand; whether its open file names establishments
is unsettled.

Two guards were proposed by the model and are **not yet ruled**: never match anonymised business-for-sale
listings to named register entries; and name no individuals — prospect lists name only legal entities
or establishments with at least two jobs. Also noted: turnover is largely not public for small and
medium companies, so it is estimated from headcount and sector ratios and labelled as an estimate; the
legal basis for that statement is from the model's knowledge and unverified.

**PAR acquired 2026-09-25, session 06**, by the author's hand download; recorded as `SRC-012` and assets
`ASSET-001`–`003` in [`../records/`](../records/README.md). It settles the contradiction: the open file is
establishment-level but **anonymous** — a point location, size-class code, SBI hierarchy, start date,
municipality, business-park code and, for 2,554 establishments, the parent company's country, with no
name, KVK number or address. It is titled 2024 but reconciles to the **1 April 2022** register (174,766
rows against the province's 174,770). The size-class codes are undocumented; two mappings fit the
reported job total. Consequence: every name must come from another source, matched on location and
sector, which makes the first join spatial rather than on keys.

**OpenStreetMap acquired 2026-09-25, session 06** (`SRC-014`, epoch 2): 17,279 named business features in
the province, 70% with a website and 85% with postcode and house number, but only 3 with a KvK tag, so
OSM supplies names and web presence without an answer key. It covers about a tenth as many places as PAR
has establishments.

**First measurement of the falsifiable core, 2026-09-26, session 06** (step S06-108 in the log). A blind
answer key of 12 OSM businesses, filled by the author from the free KvK search and translated into PAR
sector classes before the proposals were read, against proposals made from location (30 m) and sector:
unique proposals 3 of 3 correct, ambiguous 1 of 4, abstentions 5 of 5 correct. Only 5 of the 12 have an
acceptable PAR establishment within 30 m at all, most plausibly because the register is from 2022 and
OSM from 2026. Indicative only at n = 12, and none of it yet tests what a model adds beyond distance and
rule tables — the class rules are model-written, but applied deterministically.

**Utrecht business landscape parked, 2026-09-26, session 07, by the author:** "I think we'll leave it at
this for now for this use case. The problem is that it's not representative of a companies internal data.
We ran into a lot of issues, because this is an atypical use case, this is more about data scraping. There
are no regularly updating records, or a regular creation of new records." Its results stand in the
[session 06 post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md) and the data stays
on disk. The next sandbox is `EVI-OP-7`.

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

### EVI-OP-5 — Within-landscape transfer as the falsifier for locally-general rules
**⛔ STATE: OPEN**
Opened 2026-09-20, session 02, as the falsifier for `CON-OP-11`.

If specific generalisations are real and are being captured, they must **transfer within a
landscape**: precision on the seventh source should be measurably better than on the first,
because the conventions learned from the first six apply. If precision is flat across the
ingestion order, the rules are decorative — either none are being formed, or none are being
reused, or there were none to find, and in every case `CON-OP-11` is a story rather than a
mechanism.

The measurement is cheap and belongs in
[410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md)'s list
alongside precision, adjudication burden, evidence value and cost. It requires only that
ingestion order be recorded and that precision be scored per source rather than in
aggregate.

Two confounds must be controlled before the number means anything. Later sources may be
easier for reasons unrelated to transfer, which argues for randomising ingestion order or
for reporting per-source difficulty separately. And the cheap structural signals improve
with landscape coverage on their own, since sketch overlap has more to overlap with — the
same confound that document already guards against by reporting the structural baseline
separately, and the same guard applies here.

The slice as currently scoped uses two sources and cannot measure transfer at all. Either
the slice widens or this row waits for the source after it. Widening the slice to test this
would violate the slice's own discipline and should not be done casually.

**Second arm added 2026-09-20, session 03, from external review.** The pass recorded in
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md)
names a test adjacent to this one and not identical to it, and the difference is the
useful part. This row asks whether precision improves along the ingestion order. The
second arm asks whether examples improve semantic inference over a **context-only
baseline**, on held-out columns within a landscape and on held-out landscapes. The first
measures reuse; the second discriminates learnable local regularity from case-by-case
guessing, which is the thing actually in dispute once `CON-OP-4`(ii) has failed and
`CON-OP-11`'s axis with it. The second arm is also cheaper, since it does not require a
seventh source — only that some columns be withheld — so it can run inside the slice as
scoped while the transfer measurement waits.

### EVI-OP-6 — Does join elimination survive at anchor scale on a current engine?
**⛔ STATE: OPEN**
Opened 2026-09-20, session 04, from [2026-09-20-canon-survey](../docs/30_research/notes/2026-09-20-canon-survey.md) §1.4 and `ARC-OP-22`.

The literature does not answer this. The Anchor paper's own experiment compared one table
against "up to 25 tables in the anchor database" on Microsoft SQL Server 2008, and says so
as a limitation. A four-thousand-table anchor model on a current columnar engine is not
measured anywhere this survey found, and the whole re-evaluation programme of
[190_machine-authored-design-canon.md](../docs/10_architecture/190_machine-authored-design-canon.md)
assumes the answer.

The measurement is cheap and does not wait on the argument. Generate a synthetic anchor-style
schema at two or three decomposition levels, declare the constraints with `RELY` or
`NOT ENFORCED`, run a fixed query set that touches a small subset of attributes, and report
elapsed time and bytes scanned against a denormalised equivalent — with and without the
constraint declarations, because the difference between those two is the size of the
dependency `ARC-OP-22` names. Doing it on one engine is enough to be informative and not
enough to generalise; say which engine in the result.

Per [XREV_2026-09-20_canon-survey-interaction_sol](../docs/30_research/notes/XREV_2026-09-20_canon-survey-interaction_sol.md) Q2 the measurement must include the alternatives, or it will attribute to
join elimination what pruning, clustering and projection pushdown were doing: report the
denormalised baseline, the decomposed schema without declarations, and the decomposed schema
with them, and state the workload shape, since a workload touching few narrow relations does
not exercise the question at all.

This is the first row in the register that requires running something rather than reading
or arguing. Under [ADR-0006](../docs/20_decisions/0006-project-mode.md) that is Mode 2 work,
and it is scoped small enough to argue for an exception rather than a phase change.

**Demoted 2026-09-21.** Under the author's architecture (`ARC-OP-22`) the vault is never
queried interactively, so join elimination at anchor scale answers a question the design
does not ask. If run at all it should measure the mart layer. Not a candidate for the next
session.

---

### EVI-OP-7 — A simulated internal system for the next sandbox
**⛔ STATE: OPEN**
Opened 2026-09-26, session 07, by the author:

> A next use case should have a simple financial administration with regular updates at its core, or a
> very simple ERP system, with regular inserts and updates. I think we need to find a dataset that we can
> simulate this with.

What the Utrecht sandbox lacked, and what the framework's claims need: records created and changed on a
regular rhythm inside one organisation's system, so that capture, historisation, business keys across
modules, refresh and maintenance (`CON-OP-16`) are exercised as they would be in a client's landscape. Two
lessons of session 06 become requirements: the source must be reachable from the working environment
without the author's hands (GitHub and PyPI are; Dutch data portals, 4TU, Kaggle and Microsoft's sites are
not), and it should not be simulated by the same model that will be tested on it, since a landscape
designed by the tested party flatters it ([410](../docs/40_roadmap/410_first-vertical-slice.md)). Candidates
are in [`../records/sources.jsonl`](../records/sources.jsonl) from `SRC-018`.

**Preferred, tentatively, 2026-09-26, session 07, by the author:** "I think the Wide World is a good case. I'd have to install
the free SQL server instance, which is no problem." Wide World Importers (`SRC-018`) on SQL Server Developer
edition on his machine. Not to be ported: porting would mean the model rewriting the simulator, which is
the property the choice rests on. Access is the open question: the model's shell on his computer is an
isolated Linux environment that cannot reach services on the Windows host, so the proposed route is a
scheduled export on his side — advance the simulation, write changed rows into `data/` — to be tested once
the server is installed.

**Qualified the same day by the author:** "let's not move too quickly here with installing SQL server and
first think through the entire setup. I want to avoid manual work from my side as much as possible, this is
the goal of the entire excercise. With regards to point 4, updates are not a hard requirement. If it's
insert only that is also fine. Don't jump to conclusions, just because I said something, everything
tentative still, always keep in mind the big picture and the small steps to get there." Wide World
Importers is a preference, not a decision. Insert-only is acceptable. The criterion that now leads is the
author's manual work: the whole setup is to be designed before anything is installed, and judged by how
often it needs his hands.

**Setup drafted 2026-10-06, session 07, at the author's request:** [420](../docs/40_roadmap/420_next-sandbox-setup.md),
unreviewed. Checked the same day: the backups are reachable from GitHub; the simulator advances on any date range,
inserts, updates and keeps its own history; neither working environment can run SQL Server, so Wide World
Importers would run on his Windows machine and export into the repository folder on a schedule. Four decisions
are put to him there: route, pace, extract shape, and who repairs the Windows side.

**Ruled 2026-10-07, session 07, by the author:** route A (Wide World Importers on SQL Server Developer edition on his
machine), "if you can access a local database"; the simulation advanced "one day at a mouseclick … advance a day,
analyse what happened, then next day"; repairs on the Windows side by him. The agent's access is a request folder
watched by a fixed-action Windows job, the extract full to start; both proposed by the model and confirmed by him
("Yes"). Details in [420](../docs/40_roadmap/420_next-sandbox-setup.md) §11. Next: he installs SQL Server; the model
writes the setup script, reviewed before he runs it.

**Installed and scripted 2026-10-07:** SQL Server 2025 Developer edition installed by the author; the setup script and
the request-folder job are in [`prototypes/wwi_sandbox/`](../prototypes/wwi_sandbox/README.md), reviewed by sol and
astra (420 §11). Not yet run.

**Loads, scheduling and change capture ruled 2026-10-11, session 08:** a DuckDB warehouse transformed with dbt-core and dbt-duckdb, run by a pinned runner under Task Scheduler that polls for new extracts; change capture by comparing each full extract with the vault; no change gate in the sandbox; the retention problem and the frozen copy postponed, so the agent advances one day at a time. Proposal and rulings in [420 §12](../docs/40_roadmap/420_next-sandbox-setup.md); adoption in [ADR-0015](../docs/20_decisions/0015-sandbox-warehouse-dbt-duckdb.md). Nothing built yet.

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

**Second pass, assigned 2026-09-20, session 02, at the author's request.** The object is
the set of rows opened in session 02 — `CON-OP-11` above all, with `CON-OP-12`,
`ARC-OP-17`, `ARC-OP-19` and `CON-OP-14`. Those rows were drafted by the model that will
set the assignment, from a distinction supplied by the author, inside a single exchange and
with no interval for second thoughts; they are unreviewed by construction in exactly the
sense this row exists to record, and the objection in the paragraph above — that the
assignment is set by the drafter and the question selection is therefore unreviewed —
applies to this pass as it did to the first. It is stated in the note rather than left to
be noticed.

Note what this pass is *not*. The falsifiable core — that business keys are
machine-proposable at adjudication-worthy precision — remains unreviewed, and
[510_external-review.md](../docs/50_process/510_external-review.md) still ranks it first.
Reviewing this session's own output ahead of it is the comfortable choice, and it is taken
knowingly because `CON-OP-11` is a candidate spine for the §III rewrite that is owed next.

**Second pass run 2026-09-20, session 03:**
[XREV_2026-09-20_amortisation-threshold_sol](../docs/30_research/notes/XREV_2026-09-20_amortisation-threshold_sol.md)
— `CON-OP-11` chained to `CON-OP-8` and `CON-OP-4` on gpt-5.6-sol, adversarial, three
determinate questions, word-capped. `CON-OP-11` FAILS on its own counterexample from
§190; `CON-OP-8` resolves to two independent theses; `CON-OP-4`(ii) FAILS and (i) is
found to be Boisot's prior art. Dispositions narrowed `CON-OP-11`, `CON-OP-8`, `CON-OP-4`
and `EVI-OP-5`; no row was opened. The candidate spine did not survive, which is the
result this row's assignment was written to obtain and the reason the pass was worth
taking ahead of the falsifiable core.

The assignment was again set by the model that drafted the object, and this time it went
further: two of the three questions supplied the argument the reviewer was asked to rule
on rather than merely asking a question. That material is unreviewed by construction in
the strongest sense yet recorded here, and it is stated in the note as well as here.

Still unreviewed after two passes: the falsifiable core, which
[510_external-review.md](../docs/50_process/510_external-review.md) ranks first and which
both passes have now stepped around; and `CON-OP-12`, `ARC-OP-17`, `ARC-OP-19` and
`CON-OP-14`, which the second-pass assignment above named and the pass did not reach.

**Third pass run 2026-09-20, session 03:** [XREV_2026-09-20_faculty-inventory_sol](../docs/30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md)
— the faculty inventory on gpt-5.6-sol, adversarial, three chained questions. FAILS on all
three: one dimension cut, three added, the allocation rule replaced, and the proposed
interaction between `CON-OP-8`'s two theses refuted. Narrowed `CON-OP-8`, `CON-OP-2` and
`CON-OP-14`; opened `ARC-OP-21`, the only row opened in session 03.

**Two process findings from this pass, both worth more than the individual dispositions.**
The first is a transport lesson: supplying the apparatus does not require the reviewer to
*read* the apparatus, and stating it inline keeps a pass inside the bridge's sixty-second
ceiling. [510_external-review.md](../docs/50_process/510_external-review.md) should say so.
The second is a pattern rather than an incident — the allocation rule failed for the same
reason `CON-OP-11` failed the day before, by collapsing a multi-term expected-value
calculation onto one convenient axis, and both were drafted by the same model. That is now
twice in two days and is a standing defect in the drafter rather than bad luck.

The assignment problem also worsened rather than improved: Q3 named the attack it expected
to be fatal, and the reviewer agreed with it. A reviewer told which attack is decisive is a
weaker instrument than one that finds it, and the agreement is discounted in the note
accordingly.

**Fourth pass run 2026-09-20, session 03:** [XREV_2026-09-20_mission-statement_sol](../docs/30_research/notes/XREV_2026-09-20_mission-statement_sol.md)
— a candidate mission statement on gpt-5.6-sol, two chained questions. FAILS: the
reframing universalises adjudication without establishing it, and its success measure
rewards legible abundance. Q2 required the reviewer to produce repaired wording, which is
generative rather than critical and is unusual for a pass here; the result is version 0.3
in [002_mission-statement.md](../docs/00_concept/002_mission-statement.md). Narrowed
`CON-OP-15`.

**This is the third instance of the same drafting defect in two days**, and the mechanism
was new. The drafter guarded explicitly against asserting a causal link between
`CON-OP-8`'s two theses, and then asserted the governance pattern of one thesis over both
— in a clause written for cadence rather than for content. The lesson is that the guard has
to be applied clause by clause and not to an argument's headline, and that rhetorically
strong lines are where it fails.

**The falsifiable core is now unreviewed after four passes.** Each pass has reviewed the
argument rather than the claim everything rests on. That is a pattern and not a choice, and
it is the thing this row should be read as saying.

### PRC-OP-2 — Keep the apparatus proportionate to the work
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01, and held. **Resumed 2026-09-20, session 02, on its own
stated condition:** the register now carries forty-five live rows, past the roughly forty
at which this row said to resume. The condition was written before anyone knew what would
trip it, and what tripped it was a single conversation that added eleven rows.

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

**On resuming, 2026-09-20, session 02.** The honest reading is mixed and both halves should
be stated. Session 02 added no documents and no conventions, which is what
[HANDOVER_01](../handovers/HANDOVER_01_2026-09-19_repository-established.md) asked for, and
one ADR recording a ruling the author actually took. Against that, the register grew by a
third in one conversation without a single row closing, `PRC-OP-5`'s triage moved from
cheap to overdue, and the project still has no code, no data and no verified fact. A
register that only grows is a different failure from a bureaucracy that only grows, and it
is the one now in evidence.

The response this row prescribes is vigilance rather than action, and the specific
vigilance owed is this: the next session should close rows or execute residuals, and should
treat opening a new one as a cost. The §III rewrite is the natural instrument, because it
closes five at once.

**The author, 2026-09-25, session 06**, on the step log and the maintenance baseline: "let's not make it
too serious yet, we're still putting our feelers out. [...] And keep in mind, this whole system also
suffers from the same things described in Generative Structures, so let's not make it too large." The
apparatus is itself a growing stack whose upkeep draws on the same budget as the work; its overhead share
is measured in the step log (`work_class` overhead) and is this row's evidence from now on.

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

**Session 02 evidence, 2026-09-20.** The ratio inverted. The author supplied one
distinction — broad versus specific generalisation — and one refinement — sensing versus
memory — and asked what the model thought. The model's response was adversarial rather than
elaborative: it agreed with the distinction, found the consequence the author had not
stated, supplied the prior art that narrows it, and refused the author's own conclusion
about the human faculty's mandate. The author accepted all of it. The session then produced
eleven register rows, one ADR and no new design documents.

That is evidence for the row's hypothesis but not the evidence it asked for, and the
difference matters. Session 02 was a conversation, not a drafting session; there was no
document being produced to attack as it was produced, which is the specific practice the
row proposes making standard. What session 02 does establish is narrower and worth keeping:
**the author's material improves under attack and he asks for the attack**, which removes
the usual objection to the practice — that it is socially expensive — and leaves only the
question of when in a drafting session it is applied. Decide from a session that actually
drafts.

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

**2026-09-20, session 02.** No longer cheap. The register carries forty-five live rows,
eleven of them opened in one conversation, and the dependency structure grew faster than
the row count: `CON-OP-11` feeds `CON-OP-12`, `ARC-OP-16`, `ARC-OP-17`, `ARC-OP-18` and
`EVI-OP-5`; `ARC-OP-17` and `ARC-OP-18` must be worked together and jointly reshape
`ARC-OP-5`, `ARC-OP-6` and `EVI-OP-1`; `ARC-OP-19`, `ARC-OP-20` and `ARC-OP-15` form a
third cluster; and the §III rewrite now closes or rules on seven rows rather than five.
Those relationships are stated in prose inside the rows, which is exactly the condition
this row was opened to complain about, now at a third again the scale. `PRC-OP-2` resumed
on the same evidence.

### PRC-OP-3 — Cross-model review is unwired
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 15)*

Codex is registered as a local MCP server and reachable from these sessions, so the
transport exists. What does not exist is the convention for *this* repository: which
objects get reviewed, on what cadence, and how disagreement is recorded.
[510_external-review.md](../docs/50_process/510_external-review.md) adapts the
compendium's XREV convention; it has not been exercised once.

---

### PRC-OP-6 — Is the step log sound, and how are the author's minutes to be recorded?
**⛔ STATE: OPEN**
Opened 2026-09-25, session 06, with [ADR-0014](../docs/20_decisions/0014-step-log.md).

The step log of [520_record-keeping.md](../docs/50_process/520_record-keeping.md) was designed and built by
the model in one pass at the author's request and is unreviewed by construction. Owed: an external
review of the classification — whether the A/D line (who determined the content of the result), the
five work classes and the step grain will support the post-mortem the author asked for, and what they
will fail to capture.

Second question: the deciding number of [155](../docs/10_architecture/155_adjudication-economy.md) and
`CON-OP-16` is human minutes, and the log cannot observe them. Whether the author states his time per
step, per session, or not at all is his to decide; until then the log records elapsed upper bounds and
marks human effort `unknown`.

**Second question ruled 2026-09-25, session 06, by the author:** "Don't record mytime, just the number of
answers. If anything, answer length is a good indicator. Another one is maybe the type of activity.
Answering is Small. If I have to download stuff, or am otherwise your hands in the real world, it's a
size large." Implemented in [520](../docs/50_process/520_record-keeping.md) as `human_effort`. The first
question, external review, remains open.

**Reviewed 2026-09-25, session 06**, at commit b4003c6: sol,
[XREV_2026-09-25_step-log_sol](../docs/30_research/notes/XREV_2026-09-25_step-log_sol.md), FAILS with ten
findings on practice; astra,
[XREV_2026-09-25_step-log_astra](../docs/30_research/notes/XREV_2026-09-25_step-log_astra.md), FAILS on all
three hypotheses and on self-grading. **The author accepted the recommended dispositions** ("I'll go with
the recommendations"); integrated the same evening into 520 and the checker, with deferrals recorded in
both notes. Still owed: a review of the amendments themselves, and the parked design question whether
human attention is the binding constraint rather than merely in demand — a comparison to be fixed before
the post-mortem, not a field.

**First blind audit, 2026-09-26, session 06** (`AUD-S06-1` in [`../records/audits.jsonl`](../records/audits.jsonl)):
gpt-6-astra reclassified 15 random steps without the recorder's labels. Agreement: actor 15/15, outcome
15/15, role 14/15, tier 12/15, **work class 7/15, task type 5/15**. The two fields the post-mortem most needs
are the unreliable ones. Owed before the log is used for `CON-OP-16`: task type split into activity and
subject (sol's finding 8 on the step log, declined on 2026-09-25, now supported by evidence), a work-class
rule for coordination steps, and a second audit. See
[2026-09-26-session-06-post-mortem](../docs/30_research/notes/2026-09-26-session-06-post-mortem.md).

**Classification fix ruled 2026-09-26, session 07:** the author accepted the recommendation ("I'll go along
with the recommendation on 2"). Task type is now the subject and a new field, activity, what was done;
coordination takes the work class of what it coordinates. In [520](../docs/50_process/520_record-keeping.md),
enforced from S07 where mechanical. A second audit is still owed.

### PRC-OP-7 — A review assignment states the standard the object is meant to meet
**⛔ STATE: OPEN**
Opened 2026-10-06, session 07, by the model, from the author's remark on the plausibility reviews:

> The reviewers are applying insanely strict expectations, on plausibility checks, which should be more like back
> of the envelope sanity checks

[510](../docs/50_process/510_external-review.md) asks for adversarial framing — *assume the claim is wrong and try to
show it* — and it has paid off. But on 2026-10-06 the model's assignments for the first plausibility draft told the
reviewer to assume "a real double count or other implausible published number" would reach users. That set a
correctness standard for something meant as a quick sanity check, and two rounds of findings and recommendations
followed that the author then rejected as over-engineering (`ARC-OP-31`). Part of the cause was the draft itself,
which had claimed more than a sanity check should; the assignment then tested that claim faithfully. When the third
assignment stated the author's standard, the findings were proportionate and he accepted all four.

Proposed by the model and **not ruled**: add to 510's *Assignment design* that an assignment states the standard
the object is meant to meet — what it is for and what it is explicitly not for — and asks the reviewer to refute it
against that standard, not against completeness. Closes when the author rules and 510 is amended or the proposal is
declined.

### PRC-OP-8 — The procedures of the work are not yet skills
**⚠ STATE: HELD**
Opened 2026-10-20, session 08, on the author's instruction, verbatim:

> That's a good point, about the skills. Maybe we should distill all the analytical work we have done into skills. I
> think we should record that somewhere in the open points register. It goes for all activities. Having said that,
> it's not something I want to do immediately.

The point arose from item 29, whose method was written to be reused
([131](../docs/10_architecture/131_structural-position.md)) and which the model offered to turn into a skill: a packaged
set of instructions that an agent loads when a task of that kind comes up, so that the next source or project starts
from the procedure rather than from the conversation that produced it. The author widened it to all activities. So far
the procedures live in documents and scripts (129, 131, `analysis/README.md`, `prototypes/information_analysis/`,
[510](../docs/50_process/510_external-review.md), [520](../docs/50_process/520_record-keeping.md), the step log and this
register's conventions) and in the agent's working practice, which is not written down anywhere.

Which activities become skills, how a skill relates to the document that describes the same method, and where skills are
kept are **not decided**. **Held** until the author asks to resume it.

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
