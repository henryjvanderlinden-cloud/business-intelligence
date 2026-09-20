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

### CON-OP-10 — What is the second faculty called, now that it designs as well as interprets?
**⛔ STATE: OPEN**
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
