# XREV 2026-09-20 — mission statement — sol

```yaml
object:        a candidate mission statement drafted to replace the author's, with
               docs/00_concept/001_mission.md as the only file read. At commit 05e54f2.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, cwd
               C:\Git\business-intelligence, sandbox read-only, thread
               01a0befd-71fb-7ef0-a332-173b5206526e
assignment:    two chained determinate questions, adversarial framing, general assessment
               forbidden. Q2 required the reviewer to produce wording, which is a
               generative rather than critical task and is unusual for a pass here.
second reader: assignment set by Claude Opus 5, which drafted the object. The object was
               the assignment-setter's own reframing of the author's mission, so this
               pass reviews the drafter's proposal rather than the author's.
verdict:       FAILS — the reframing universalises adjudication without establishing it,
               and its success metric rewards legible abundance.
```

Fourth external pass; partly discharges `PRC-OP-1`. The falsifiable core remains
unreviewed after four.

## Q1 — does the adjudication reframing hold?

The candidate reframed the binding constraint from development speed to the adjudication
capacity of people holding both systems and business, and claimed that the two theses of
`CON-OP-8` are responses to a single scarcity — a **common purpose** rather than the causal
interaction that review had already refused.

> **VERDICT: REFRAMING FAILS — it unprovenly universalises adjudication as the bottleneck
> and rewards low-value coverage**
>
> "Common purpose, not interaction" is logically honest, but this draft has not earned it.
> [...] "machines propose, people rule" recasts T1 as though expressing an already-known
> deterministic design were another semantic proposal awaiting adjudication. That collapses
> specification/authoring labour into adjudication labour and quietly makes T2's governance
> pattern universal.
>
> The distinguishing test is intervention and cost accounting: deploy T1 and T2 separately,
> classify the human work each displaces and creates, and measure their effects while
> holding adjudication capacity fixed. If each independently increases valuable, warranted
> coverage, with no dependence or cross-term, they merely share a purpose. [...] The
> mission currently asserts that bottleneck rather than establishing it.
>
> "Coverage gained per unit of human adjudication" is gameable because coverage is not
> value-weighted and "a unit of adjudication" is undefined. A system can maximise the ratio
> by modelling thousands of easy, low-value, stable tables; attaching technically
> sufficient provenance; and obtaining one coarse bulk approval. [...] The organisation
> becomes worse off even if every counted artifact is individually competent.
>
> "Meaningful and trustworthy" does not cure this unless admission to the numerator
> requires claim-level validation tied to organisational consequence. But deciding
> consequence is precisely what the system may not do under ADR-0005.

**Disposition.** Both accepted, and the first is the more important because of *how* the
unification re-entered. The drafter guarded against asserting a causal link between the two
theses and then asserted the governance pattern of one over both, in a clause written for
cadence rather than for content. **The distinction between common purpose and interaction
is real, and the guard has to be applied to every clause rather than to the argument's
headline.** That the reviewer had to point this out one day after the same drafter's
previous unification was refuted is the third instance of the pattern `PRC-OP-1` now
records.

The gameable-metric finding is independently useful and generalises past the mission:
any coverage-shaped measure this project adopts, including in
[410_first-vertical-slice.md](../../40_roadmap/410_first-vertical-slice.md), inherits it.
The bind is the interesting part — the repair is value-weighting, and
[ADR-0005](../../20_decisions/0005-three-autonomy-tiers.md) forbids the system from
deciding consequence, so the weighting must come from people and the mission therefore
depends on the decision register that `ARC-OP-12` says may never be supplied. That
dependency is now stated in [002_mission-statement.md](../../00_concept/002_mission-statement.md)
rather than left implicit.

## Q2 — the repaired wording

The reviewer was required to repair both findings rather than argue them away, to stay
under ninety words, and to be explicit about what is unestablished.

> nsdn exists to help organisations extend reliable understanding of their data landscapes.
> It uses machines to express and maintain human-specified deterministic designs more
> cheaply, and separately to propose contextual semantic hypotheses for human judgment.
> People determine which outcomes and parts of the landscape matter, and every accepted
> claim remains traceable to evidence or an accountable person. Success means improving
> human-prioritised coverage and maintenance efficiency without a defect rate worse than
> competent human practice or disproportionate validation cost. Whether the capabilities
> interact or adjudication is the binding constraint remains unestablished.
>
> This concedes the orders-of-magnitude claim, any single measure of "quality," and any
> assertion that speed and quality arise from one mechanism. [...] Its strongest objection
> is that human priorities may be incomplete, political, or unstable; optimising against
> them may merely relocate the value problem from the system to its governors.
>
> **VERDICT: human-prioritised coverage**

**Disposition.** Adopted as version 0.3 in
[002_mission-statement.md](../../00_concept/002_mission-statement.md), rewritten for cadence
and shortened, with no substantive change: *maintenance efficiency* was folded into the
coverage clause, and the sentence order was altered so the statement opens on what the
project is for rather than on what it uses.

The self-nominated weak point — *human-prioritised* — is carried into the document as its
own section rather than buried, because it is simultaneously the defence against the
gameable metric and the statement's largest unanswered objection. Both facts belong next to
the wording.

## What this pass did not do

It did not test the statement against a reader outside the project, which is the audience
it is written for and the one this repository has never had. It did not review the
falsifiable core.

---

# Second sitting — 2026-09-20, same day, same object, same model

Thread 01a0bf09-de77-7383-a199-93ca0a001a3a. Appended rather than filed separately because
it is the same object, the same model and the same day; a near-duplicate note would add
apparatus without adding record, which `PRC-OP-2` exists to resist. The verdict shape is
preserved per [510_external-review.md](../../50_process/510_external-review.md).

**Occasion.** The author rejected version 0.3 for making the objective *understanding* the
data landscape, which he named as drift into an academic exercise. His correction: the
objective is to **build** a modelled, meaningful and trustworthy landscape at lower cost and
higher quality, with coverage an aspect of quality; to derive a methodology from a real
understanding of the new capabilities rather than applying models where they look
interesting; and to make best practices such as Data Vault — theoretically superior,
practically unattainable for ordinary teams — actually attainable. The rejection is upheld
and is not reviewed here; what was reviewed is the replacement.

## Q1 — does version 0.4 survive?

> **VERDICT: 0.4 HOLDS [only after restoring human-prioritised scope, narrowing the
> attainability test, and retaining the open hypotheses adjacently] / FAILS [a, b]**
>
> **(a) It hides the problem as written.** Coverage can coherently be an aspect of quality
> only if "quality" means quality of the landscape as a portfolio, not correctness of each
> modelled item. But then coverage must remain coverage of the human-prioritised scope.
> "People set priorities" merely assigns authority; it does not constrain the success
> measure. Consequently, 0.4 again rewards modelling abundant, easy, low-value material.
>
> **(b) The test is unsound.** Cheap authoring and maintenance can remove labour barriers;
> it cannot by itself remove inherent object count, join complexity, operational cost, or
> poor comprehensibility. The 6NF finding therefore defeats the general claim about designs
> "the canon rejected", though not a narrower claim about methods rejected principally
> because their specification and maintenance burden exceeded ordinary teams' capacity.
> [...] "Become ordinary" otherwise confounds technical attainability with adoption,
> training, tooling, and organisational fashion.
>
> **(c) Dropping the sentence is legitimate, conditionally** [...] honest if that section
> states plainly that the interaction between deterministic machinery and contextual
> inference, and the alleged adjudication bottleneck, remain unestablished.

**Disposition.** All three accepted; (a) and (b) as repairs, (c) as a condition now met.

The (a) finding is the same defect as version 0.2's, surviving a rewrite that was supposed
to fix it: the guard moved from the measure into a clause about authority, where it looks
like a guard and does no work. *People set priorities* is a mandate statement and
`ARC-OP-12`'s problem; it constrains nobody's scorecard. This is the fourth time in two days
that a protection has been lost by rewording, and it is worth recording that the loss was
invisible to the drafter each time.

The (b) finding is the more valuable, because it turns the author's Data Vault ambition
into something falsifiable without weakening it. Naming Data Vault was right; the error was
generalising from it to *designs the canon rejected*, which the repository's own 6NF
counterexample refutes. The narrowed form selects designs by the kind of obstacle rather
than by the fact of rejection, which is a sharper claim and is testable against
`ARC-OP-14`'s survey once it exists.

## Q2 — version 0.5

The reviewer was required to bind all three repairs, to stay under 110 words, to read as a
statement of what the project builds rather than understands, and to keep Data Vault named
unless naming it was a mistake. It judged naming it correct.

The result is adopted verbatim as version 0.5 in
[002_mission-statement.md](../../00_concept/002_mission-statement.md) with one cadence
change and no substantive edit. Its self-nominated weak point — *whose principal obstacle
is modelling labour* — and the required honesty sentence are both carried into that
document as their own sections.

> **VERDICT: "whose principal obstacle is modelling labour"**

## What this sitting did not do

It did not test the statement on a reader outside the project. It did not establish that
modelling labour is in fact Data Vault's principal obstacle, which is now the statement's
load-bearing empirical assumption and belongs to `ARC-OP-14`.

---

# Third sitting — 2026-09-20, same day, same object, same model

Thread continued from the second sitting. **The reviewer's own Q1 finding was put back to
it and it conceded.** That is the first concession by a reviewer in this repository's
review history and is worth recording as such, because it is also the first pass where the
challenge originated with the author rather than with the model setting the assignment.

**The author's argument**, stated by him and reproduced rather than paraphrased into the
question: cognitive complexity is a subset of modelling labour rather than a separate
obstacle class; 6NF does not avoid labour but relocates it, out of modelling and into query
authoring and performance optimisation; and practitioners are perfectly capable of these
complex modelling challenges — what defeats them is the organisation's temporal and
budgetary constraints, not their capacity.

> **VERDICT: Q1 FINDING SURVIVES [only as a warning against displaced or unmeasured
> lifecycle cost] / CONCEDED [whose total lifecycle burden currently exceeds ordinary
> teams' time, budget and validation capacity]**
>
> My Q1 finding does not survive in its original form. I treated authoring, comprehension,
> querying and optimisation as separate obstacle classes when they are better understood as
> locations where lifecycle work accumulates. [...] Calling only the first category
> "modelling labour" arbitrarily privileges where the work occurs.
>
> What remains defensible is the warning against claiming success merely because model
> generation becomes cheap. The test must count displaced work across the whole lifecycle.
>
> (a) Runtime and compute cost are genuinely not labour, although both consume the same
> constrained budget. Columnar execution, cheap compute and join elimination have weakened
> the historical objection, but have not abolished it [...] Runtime feasibility therefore
> remains an empirical condition, not a settled reason to reject 6NF.
>
> (b) Adjudication capacity is labour, but it is scarce, specialised and non-fungible.
> Calling it labour does not imply that organisations can buy arbitrary quantities of it.
> Moreover, a representation that prevents a qualified person from reliably judging a claim
> fails the human mandate as a quality problem, not merely through expense. That does not
> condemn 6NF itself: tooling may present comprehensible semantic views while retaining a
> complex physical model. The test must assess the adjudication surface, not raw object
> count.

**Disposition.** The concession is accepted and version 0.6 adopts the replacement phrase.
Both carve-outs are accepted too and are carried into
[002_mission-statement.md](../../00_concept/002_mission-statement.md) as their own section,
because they are the reasons the statement does not claim that everything is labour.

Three consequences beyond the wording, in ascending order of value.

The surviving half of the finding — that success must not be claimed because generation
became cheap while the work reappears downstream — is now a clause inside the statement
rather than a caveat outside it.

`ARC-OP-14`'s canon survey is re-specified. It was to separate designs rejected for
authoring cost from those rejected for runtime cost; that distinction is the one this
sitting dissolved, so it should instead classify each design by where its lifecycle work
accumulates and report a distribution, keeping runtime cost and the adjudication surface as
separate accounts.

`ARC-OP-15` gains the sharpest instruction of the three: **assess the adjudication surface,
not the object count.** Every argument in this repository that reasons from table counts to
human comprehensibility is using a proxy, including §3 of the canon document — which is the
same §3 whose 6NF example refuted `CON-OP-11` this morning. The example survives as a case
of lifecycle burden; the inference from object count to incomprehensibility does not, and
that is a second finding against a document this repository has been leaning on all day.

## What this sitting did not do

It did not verify that modelling labour, or lifecycle burden of any kind, is in fact what
kept Data Vault from ordinary teams. That remains the statement's load-bearing empirical
assumption and belongs to `ARC-OP-14`.
