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
