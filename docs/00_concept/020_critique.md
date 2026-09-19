# 020 — Critique of the original brief

A structured response to [010_vision.md](010_vision.md): what holds up, what does not,
and what the brief omits. Written as a first pass; everything here is contestable and
nothing here is a decision. Decisions live in [`../20_decisions/`](../20_decisions/).

## 1. The load-bearing claim, and where it is only half true

The brief rests on one sentence: *"a properly instructed LLM with enough mandate and a
workflow can build a data infrastructure autonomously, because the analysis part can be
done independently."* The word doing the work is **independently**, and it is true of
some analysis and false of the rest.

It is worth separating three kinds of analysis that the brief treats as one.

**Structural analysis** — profiling, cardinality, type and format inference, nullity,
functional-dependency detection, candidate-key discovery, value-overlap between
columns, temporal behaviour of a table under repeated observation. This is genuinely
independent of the organisation. It is computable from the data and the catalogue, and
an agent can do it at scale without asking anyone anything. Everything in the brief's
first four bullets is mostly of this kind.

**Semantic analysis** — what a column *means*, whether two identifiers denote the same
real-world entity, which of six overlapping customer tables is authoritative, what the
status code `07` signified before the 2019 migration. This is not recoverable from the
data, because it was never in the data. It lives in people, in tribal memory, in a
decommissioned Confluence space, and occasionally in a comment field. An agent can
generate *hypotheses* here at superhuman rate, and that is a large gain, but it cannot
adjudicate them alone. Value overlap is evidence of joinability, never proof of
identity: two customer identifiers may share ninety percent of their values and denote
different populations, and two columns that mean exactly the same thing may share no
values at all.

**Teleological analysis** — which questions are worth answering, which insight is
actionable, what the organisation is actually trying to decide. This is not in the data
under any interpretation. An automated analysis layer with no model of the decisions
the organisation makes will reliably produce observations that are statistically true
and practically worthless. The brief's bullet on data marts, automated analyses and
storytelling is the bullet most likely to disappoint, and it will disappoint for this
reason rather than for any technical one.

The useful consequence is that **autonomy should not be uniform across the system.**
Near-full autonomy at the structural layer, assisted autonomy at the semantic layer,
human-anchored purpose at the teleological layer. This is elaborated in
[`../10_architecture/105_autonomy-tiers.md`](../10_architecture/105_autonomy-tiers.md)
and is, in my view, the most important reframing of the brief.

## 2. What the brief gets right

**The deterministic/contextual seam is the correct one.** It identifies precisely the
place where language models add value that existing automation does not: judgment under
ambiguity, subsequently compiled down into deterministic artifacts. This yields an
architectural law worth stating explicitly, because the brief implies it without saying
it: *the model is never in the data path.* The model writes code, configuration,
metadata and documentation; deterministic engines execute. Anything else forfeits
reproducibility, auditability and cost control at once.

**The context layer as first-class product.** The brief's insistence that context be
built, stored, indexed and made findable is right, and is right for a reason that
predates language models: the scarce asset in a data landscape has always been
semantics, not pipelines. The novelty is that a machine can now produce a first draft
of the semantics.

**Data Vault as the target model is a better fit for machine authorship than it is for
human authorship.** The usual objection to Data Vault — that it is mechanical, verbose
and generates far more objects than a human wants to maintain — becomes irrelevant when
the author is not human. More importantly, the raw vault is insert-only and
non-destructive, which means a wrong modelling decision is *recoverable* rather than
lossy. Under machine authorship, where the error rate is nonzero and the volume is
high, recoverability is worth more than elegance. Hub/link/satellite generation from a
declared set of business keys is close to a solved problem; the open problem is
declaring the keys, which is a semantic question, not a structural one.

**The context-window concern is the real engineering problem**, and the brief is right
that it is architectural rather than incidental. It is treated at length in
[`../10_architecture/120_context-layer.md`](../10_architecture/120_context-layer.md).

**The reluctance to place a decision-making unit on top** is sound, though for a subtler
reason than the brief gives. The reason to keep a human in that seat is not that the
model is too weak; it is that the value of an analytic layer lies in its being
*contestable*. A decision unit that consumes its own analyses closes the loop and
removes the last party capable of disagreeing with it. Keep a human in the contest role
even after they leave the build role.

## 3. Where the brief is weak

**The crawler analogy breaks at the point that matters.** A web crawler reads a public,
idempotent, effectively free surface, and the worst outcome of a bad crawl is a rate
limit. A crawler inside a corporate network reads *production*: it consumes warehouse
credits, takes locks, trips data-loss-prevention alerting, touches personal data under a
legal basis that must exist before the read rather than after it, and can be observed by
a security team that was not told it was coming. The phrase "of course with proper
security clearance etc" is carrying more weight than any other phrase in the brief, and
in practice it is where projects of this shape die. Access, legal basis and blast radius
are not an operational detail to be arranged later; they are a first-class component,
and they dictate the order of the crawl — metadata surfaces first, samples second, full
reads only under an explicit per-source contract. See
[`../10_architecture/150_trust-and-blast-radius.md`](../10_architecture/150_trust-and-blast-radius.md).

**There is no pruning.** The brief describes a system that proposes, builds, enriches
and extends, continuously, with no countervailing force. Such a system accretes. Within
a year it holds four thousand tables that nobody asked for, three hundred marts with no
consumers, and a catalogue whose signal-to-noise ratio is worse than the landscape it
was built to explain. Autonomous construction requires autonomous *garbage collection*,
and this is not a caveat — it is a missing component of equal rank to the builder. The
brief's own metaphor supplies the vocabulary, and supplies it better than the brief
realises: synaptic pruning is not a failure mode of neural development, it is the
mechanism. Every generated artifact should carry a demand justification — a question it
answers, a named consumer, a usage signal — and an expiry. See
[`../10_architecture/145_entropy-and-pruning.md`](../10_architecture/145_entropy-and-pruning.md).

**"Regression testing" conflates three different guarantees.** Pipeline determinism
(same input, same output) is straightforward. Data-quality contracts (nullity,
cardinality, referential integrity, distributional stability) are largely solved by
existing open-source tooling. *Semantic* regression — has the meaning of this metric
drifted? — is neither, and it is the one that matters for a system that publishes
automated analyses. It requires metric definitions to be versioned artifacts and drift
to be detected against the definitions, not only against the data. See
[`../10_architecture/160_evaluation-and-regression.md`](../10_architecture/160_evaluation-and-regression.md).

**"Ask humans for context" underspecifies the scarcest resource in the entire design.**
Human attention is the binding constraint. A system that asks questions
opportunistically will burn its welcome in a fortnight. Questions must be batched,
deduplicated, addressed to the right person, and — the part that makes this
interesting — *ranked by expected information gain*: which unanswered question, if
answered, unlocks the most downstream inference? That is a computable quantity over the
hypothesis graph, and turning the human interface into a ranked adjudication queue is
one of the more tractable novel components in the design.

**No metadata claim is marked with how it is known.** A catalogue that mixes
machine inference, human assertion and documented fact without distinguishing them
becomes a corpus of confident lies within a year, and its decay is invisible because
every entry looks identical. Every assertion in the context layer needs provenance
(inferred / asserted-by / documented-in), a timestamp, a confidence, and — ideally — a
falsifier: the observation that would overturn it.

**Cost has no ceiling.** A continuously crawling, continuously proposing agent system is
a recurring expense with no natural stopping point. The economics that make the idea
plausible now — per-token reasoning cost has collapsed while the cost of an analyst
performing the same reasoning has not — also make unbounded loops expensive in a way
that is easy not to notice until the invoice. Budget belongs in the architecture: cost
per crawl, per hypothesis, per artifact, attributed and visible.

## 4. What I would add to the brief's list

**A source contract per data source.** Owner, legal basis, personal-data
classification, read budget, permitted operations, freshness expectation. The crawler
obeys contracts; it does not discover its own permissions.

**A decision register.** An explicit, human-maintained record of the decisions the
organisation actually makes — recurring and one-off, with their cadence, their owner,
and the evidence that currently informs them. This is the anchor that makes automated
analysis actionable rather than merely true, and it is the only proposed input that
addresses the teleological layer directly. It is also, conveniently, a document an
experienced business analyst can produce in a week.

**An adjudication queue** ranked by information gain, as above.

**A pruning process** with the same mandate and cadence as the building process.

**Cost accounting** as a first-class signal, not an operational report.

## 5. On the metaphor

The organism analogy earns its place in three spots and misleads in one.

It earns it for *sensing* (heterogeneous, noisy, partial inputs that must be integrated
rather than merely collected), for *local connection-forming* (the dendritic image is
genuinely apt: cheap local hypotheses, reinforced by use, most of them discarded), and
for *pruning* (as above — the metaphor supplies the missing component). Graceful
degradation is a fourth, weaker case.

It misleads in that organisms have no accountability requirement. No organism must
explain to a regulator why it retained a record, nor produce an audit trail, nor
attribute a cost. Corporate data infrastructure is in large part a *bureaucratic*
artifact, and the bureaucratic layer — provenance, authorisation, attribution,
reversibility — is not decoration on the biological core; it is much of what makes the
thing usable in an organisation at all. A design led by the metaphor will
systematically underweight it.

A separate and more practical objection: "neural" will be read as "neural network" by
every technical reader, and the system is not one. The instinct in the brief — *"just a
bunch of fancy words I threw together to evoke a kind of feeling"* — is the correct
instinct and worth trusting. Keep the metaphor as a private heuristic and give the
project a boring external name. `nsdn` is used throughout this repository as a neutral
handle; see [ADR-0003](../20_decisions/0003-codename-nsdn.md).

## 6. Sequencing

The characteristic failure of ambitious data projects is to build the ontology first and
discover, two years in, that nothing consumes it. The counter-discipline is a narrow
vertical slice: two sources, one business question, driven end to end — crawl, card, key
hypothesis, adjudication, vault, mart, analysis, test — before widening anything.

There is a happy accident available here. The read-only half of the system — crawler,
catalogue, profiling, hypothesis generation, adjudication queue — is independently
valuable, ships on its own, and is by far the easiest thing to obtain organisational
permission for, because it writes nothing. It is also the part that de-risks everything
downstream, since the quality of every later stage is bounded by the quality of the
context layer. Build that first and treat the vault, the marts and the analyses as
phases that must earn their way in. See
[`../40_roadmap/400_phasing.md`](../40_roadmap/400_phasing.md).
