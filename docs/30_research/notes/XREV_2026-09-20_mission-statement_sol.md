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
