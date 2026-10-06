# 160 — Evaluation and regression

The brief asks for "a test framework that constantly monitors for regression." That
sentence contains three different guarantees, of sharply increasing difficulty, and they
need separating before anything can be built. A fourth guarantee, about the code rather than
the data, was added on 2026-09-28 and is set out under *Release regression* below. A fifth,
about whether the published output makes sense at all, was added on 2026-10-06 and is set out under
*Plausibility* below.

## Level 1 — Determinism

*Does the same input produce the same output?*

Mechanically straightforward and the least interesting, but non-negotiable, because it
is the property that the one law in [100_system-overview.md](100_system-overview.md)
exists to protect. Every transformation is deterministic code; re-running a period
reproduces that period exactly. A generated artifact is a pure function of its
declaration. If this ever fails, a model has got into the data path.

## Level 2 — Data quality contracts

*Does the data still look like what we said it looks like?*

Nullity, uniqueness, referential integrity, domain membership, row-count bounds,
freshness, distributional stability. Well served by existing open-source tooling, and
the interesting question is not how to check but **where the expectations come from**.
Here they are generated: profiling produced a characterisation, the characterisation
becomes an expectation, and the expectation is versioned alongside the card that
motivated it. Expectations therefore carry provenance like any other assertion.

The failure mode is alert fatigue, which is operationally identical to having no tests.
Two defences: expectations inherit the confidence of the profile that generated them, so
weak expectations produce weak signals rather than alarms; and a firing test is itself
evidence, which can retire the expectation rather than merely annoy someone.

## Level 3 — Semantic regression

*Does this still mean what it meant?*

The hard one, and the one that matters most for a system that publishes automated
analysis, because an analysis built on a metric whose definition quietly shifted is
worse than no analysis.

Three distinct things drift.

**Definitions.** A metric's definition changed. This is detectable only if definitions
are versioned artifacts — which is the argument for a semantic layer independent of any
other argument. Every published number should be traceable to a definition version.

**Assertions.** A previously adjudicated semantic fact has become false because a source
was re-platformed, a process changed, or a code list was extended. Nothing in the data
announces this. The defence is the **falsifier** recorded with each assertion: the
observation that would overturn it, monitored as a test. Where no falsifier can be
stated, the assertion needs a review date instead, and an assertion with neither is
technical debt.

**Populations.** The entity a table describes has silently changed — a new business line,
a migration, a merged subsidiary — without any schema change. Detectable as a
distributional break that no upstream change explains, which is weak evidence but
better than none, and should raise a question rather than an alert.

## Release regression — frozen data, moving code

*Added 2026-09-28, session 07, from the author's working practice, and open as `ARC-OP-30` in
the [register](../../registers/OPEN_POINTS.md). Reviewed the same day and failed by both
reviewers — [sol](../30_research/notes/XREV_2026-09-28_release-regression_sol.md) on the
method, [astra](../30_research/notes/XREV_2026-09-28_release-regression-adaptations_astra.md)
on the nsdn adaptations — on one common finding, that attribution is not acceptance. The
author ruled on the recommended changes on 2026-09-29; they are integrated under *Amended
after review* at the end of this section, and the text before it is as reviewed.*

The three levels above watch the data change while the code stands still. The opposite
question is just as necessary, and in most BI teams it is the one actually tested: when the
code changes, does the output change only where the change said it would? The author
described the method used at his current employer, and it is recorded here as the working
answer.

**The method as practised.** A fixed set of source data is used for a quarter at a time,
with one reference date per quarter standing in for *today*, so that the clock is frozen
along with the data. Every day a snapshot of all outputs is made with the codebase as it
stands that day, and it is compared with the previous day's snapshot. Because data and
clock are both held still, the only thing that can have changed between two snapshots is
the code. Every difference must therefore be attributed to one of the release notes for the
changes deployed since the previous snapshot; a difference that cannot be attributed is a
regression, and must be solved.

**Release notes are the expected side of the test.** A note says what was changed, why,
and what the intended impact is. Without it a diff is a list of differences with no way of
telling which were meant. For attribution to be mechanical rather than a matter of
goodwill, the intended impact would have to name what it touches — objects, columns or
measures, which rows, and the direction and rough size of the change — and a change meant
to leave the output untouched, such as a refactor, would say so explicitly. That last kind
is the strongest test there is, because any difference at all refutes it.

**Two checks, by two people.** In the author's words: "the developer checks that the
change has the intended consequence. The team's dedicated tester checks for regression (by
others)." The division matters. The developer confirms that the predicted differences
appeared, which catches a change that did not work. The tester examines everything else,
which catches a change that did more than it said, and the collisions between one
developer's change and another's that no single developer is placed to see. It is the same
separation that [520](../50_process/520_record-keeping.md) enforces for the step log:
whoever made the work does not validate it.

**The quarter turn.** When the frozen data set is replaced, the reference date moves with
it, and no code change is deployed that day, so that the new baseline is produced by code
already verified against the old one. The differences between the two reference dates,
usually a quarter apart, are then expected to be large and cannot be attributed row by row.
Instead a plausibility check is made between them: volumes, totals and distributions judged
for whether the movement is credible over that interval. *(Added 2026-10-06: what that check contains, and the
rule that the new frozen set must first pass the plausibility suite on its own, are under
*Plausibility* below.)*

**Preconditions here.** The method depends on determinism. If the same code on the same
data could produce different output, the daily diff would be noise; that is Level 1 above,
and it is why [ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md), which keeps
models out of the data path, is a precondition for this method rather than merely
compatible with it. It also depends on every output being regenerable from versioned
definitions, which [150](150_trust-and-blast-radius.md) already requires.

**What nsdn would add.** Two adaptations, proposed on 2026-09-28 and not yet ruled by the
author.

*Code is not the only thing that changes the output.* In this system a newly adjudicated
assertion — a business-key ruling, say — a new rule version or a changed metric definition
would change the marts as surely as a code release, and none of them is code. Attribution
would therefore have two legitimate sources: release notes for code, and the logged history
of context changes, which already carries who, when and on whose authority
([120](120_context-layer.md), and *Assertions* under Level 3 above). Whatever neither
explains is a regression. Whether rule versions form their own time axis is `ARC-OP-13`,
and the answer bears on how attribution would be computed.

*Most of the loop need not be human.* The agentic layer would write the change and its
release note; deterministic machinery would take the snapshot, compute the diff and match
differences against the declared impacts; a different agent from the author of the change
would review the attribution, as the tester does; and the author would see only the residue
that nothing explains, together with the quarterly plausibility check. That is the shape the
author's aim of minimal manual work asks for (`EVI-OP-7`).

**Relation to the levels above.** A frozen data set cannot show what new data would do,
which is why Levels 2 and 3 run on the live feed. The two regimes are complementary:
release regression on frozen data tests the code, and the levels above, on live data, test
the landscape. A simulated source of the kind sought under `EVI-OP-7` could supply both —
its live feed for the one, and a frozen copy, replaced each quarter, for the other.

**Amended after review.** Both reviews found the same hole: a difference that falls inside
what a release note or a context change declared can still be wrong, and nothing above
catches it. A duplicated invoice inside a declared revenue change, an extra exclusion inside
a genuine definition change, and a second customer accepted by a reviewer that shares the
author's mistaken premise all pass as attributed. The author ruled on the five recommended
changes on 2026-09-29, and they apply as follows.

*The expected impact is executable, and checked by someone else.* A release note states,
beside the entities and tables it touches — which, in the author's words, is what release
notes "usually" already give — the expected differences in a form that can be computed, and
the invariants that must not move: row counts, key cardinality, reconciliation totals. The
check compares the actual before and after outputs against both, and is made by someone
other than the author of the change. Matching a difference to a note is attribution;
confirming it against the stated expectation is acceptance, and only acceptance clears it.

*Changes deployed together are tested one at a time.* When two changes land in the same
interval, their effects can interact so that neither note predicts the combined result.
The remedy is to snapshot after each change in a fixed order, or, where changes cannot be
separated, to state one joint expectation. The author's remark on it, verbatim: "maybe that
is workable if CI/CD is properly implemented, and a regression test can be run after every
integration. For humans this is unworkable, but for an agentic layer this might be an
option." A daily cycle, as practised, bundles a day's changes; a snapshot after every
integration is only affordable when snapshot, diff and check cost nobody's time, which is the
condition an agentic layer would have to meet.

*A note declares the root; the consequences are derived.* Correcting one customer's segment
legitimately changes every mart, subtotal and percentage built on it, and listing all of them
by hand is brittle. The note declares the root change; its downstream closure is derived
through versioned column-level lineage ([190](190_machine-authored-design-canon.md)), and
only differences outside that closure, or breaking an invariant within it, are flagged.

*The reviewing agent checks outputs, not explanations.* In the agent-run loop, the reviewer
validates each attributed difference against the stated expectation and the actual outputs,
not against the change author's account of it. A second agent that shares the author's
premise adds nothing; what it cannot confirm stays residue, for a person.

*Context changes carry the same expectation as code.* An adjudicated assertion, a rule
version or a metric definition that changes output states its expected impact executably,
exactly as a release note does, and each snapshot records the context version it ran with, so
that a later adjudication cannot retrospectively explain an earlier difference.

These rulings settle how the method would work. Whether it is adopted — and with it the two
nsdn adaptations above — still waits for an ADR.

**Not decided.** The form and location of release notes: one per release, tied to a
commit, machine-readable so that attribution can be checked, and distinct from ADRs, which
record why a design was chosen, and from the step log, which records what work was done.
What counts as an output for the snapshot. How the diff is summarised so that its residue
is readable. And whether the method is adopted at all, which needs an ADR. All of this is
held in `ARC-OP-30`.

## Plausibility — does the output still make sense?

*Added 2026-10-06, session 07, at the author's request, and open as `ARC-OP-31` in the
[register](../../registers/OPEN_POINTS.md). Nothing in this section has been ruled except the author's request
itself. Reviewed the same day and failed by [sol](../30_research/notes/XREV_2026-10-06_plausibility_sol.md): a
duplicate that arrives from two systems under different document numbers passes every check, a frozen set cut
inconsistently passes both baseline steps, and domain equations taken as universally hard would block routine
loads. Its recommended changes await the author's ruling in `ARC-OP-31`; the text below is as reviewed.*

The author asked for it in these words:

> next to regression testing we also need (constant) plausibility testing as a means of sanity checks,
> probably on production, where data can change daily, to make sure that we don’t get weird double
> counting, etc. Also for every transition of the fixed reference date / fixed data set, when the test data
> set is updated.

**What it is, and why the other levels do not already give it.** Each guarantee above looks at one part of
the system. Level 2 asks whether the data still looks like its own profile; the tests of
[128](128_join-knowledge.md) ask whether one relationship can be joined without fan-out; release regression
asks whether a code change did only what it said. None of them asks the question a business user asks of a
published number: *is this believable?* A mart can pass every profile expectation, be built from joins that
each passed their own tests, and differ from yesterday only where a release note said it would, and still
count an invoice twice — because two joins that are each safe combine into a chasm, because a delivery was
loaded twice upstream of every test, or because the frozen baseline itself was wrong. Plausibility testing is
the layer that checks the **published outputs themselves, end to end**, whatever has changed: data, code or
context. It is not a replacement for the levels above but the place where their partial views are made to
add up.

**What already exists.** Much of the machinery is designed already, scattered across four documents, and
this section collects it rather than duplicating it: the standing join tests of
[128](128_join-knowledge.md) — row-count preservation, aggregate and per-fact reconciliation, multi-path
fan-out checks — which run on every load and block publication through the gate of
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md); the monitoring of the order of
time in [127](127_temporal-behaviour.md) — replays and duplicate deliveries, sequence gaps, closed periods
that change; row 23 of [070](../00_concept/070_task-allocation.md), reconciliation across source, vault,
marts, Finance and legacy outputs, allocated to deterministic machinery with a person accepting
discrepancies; and Level 2 above. What is missing is the level at which a person would actually notice a
problem: the outputs.

**The checks.** Seven families would be enough to start, each of them deterministic:

1. **Reconciliation along the chain** — every published measure reconciles back through vault to source,
   in total and, for a set of named attribution cases, per originating fact, since totals can reconcile while
   attribution is wrong (128).
2. **Uniqueness at the declared grain** of every published output — the direct test for double counting,
   applied to the result rather than to each join that produced it.
3. **Conservation rules from the domain** — rules the business itself guarantees: debits equal credits;
   invoice lines sum to the invoice header; closing stock equals opening stock plus receipts minus issues.
   For the financial-administration or ERP sandbox sought under `EVI-OP-7` these are the strongest checks
   available, because they hold by construction in the source and any break is ours.
4. **Consistency across outputs** — the same metric, at the same definition version and the same cut,
   has the same value in every mart and report that publishes it.
5. **Completeness** — every expected partition is present: each day, each entity, each tenant or source.
   A missing day sums to a plausible-looking total.
6. **Closed periods stay closed** — a period that should no longer change does not (127).
7. **Movement within bands** — day-over-day and same-period-last-year changes of volumes, totals and
   distributions fall within bands derived from their own history, seasonality included.

The first six are **hard** checks: they hold or they do not. The seventh is **soft**: a movement outside
its band may be real, and it raises a question rather than an alarm, for the alert-fatigue reason given
under Level 2.

**Where the expectations come from.** Not from profiling alone. The conservation rules and the declared
grains are business claims, and they would be recorded as assertions with provenance and adjudicated like
any other ([120](120_context-layer.md)). They are, moreover, the same invariants the author's ruling of
2026-09-29 requires every release note to name — row counts, key cardinality, reconciliation totals — so
one definition would serve twice: as the invariant a release must not move, and as a standing check on
production. The bands of the seventh family are derived from history, inherit the confidence of that
history, and are versioned like Level 2's expectations.

**When it runs.** On three occasions, with the same suite each time.

*On every load in production*, after the load and before publication. This is the constant check the author
asked for, on the data that changes daily.

*At every change of baseline* — the quarter turn described under *Release regression*, when the frozen data
set and its reference date are replaced. Two steps, in order. First the new frozen set, at its new reference
date, passes the full suite on its own: it is a copy of production at that date and should pass everything
production passes. A baseline that fails is not adopted; the old one stays in force until the failure is
fixed or a person accepts it, because a broken baseline would otherwise be frozen in for a quarter and every
daily diff measured against it. Only then the comparison between the two reference dates already described
under *The quarter turn*: volumes, totals and distributions judged for whether the movement is credible over
that interval.

*After a release*, on production as well as on the frozen set, since release regression on frozen data
cannot see what a change does to data it has not met.

**What happens when a check fails.** Proposed, not ruled: a hard failure blocks publication of the affected
outputs, extending the publication gate of
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md) from relationships to outputs;
a soft failure publishes with the output flagged and a question raised. Deterministic machinery runs the
checks; the agentic layer diagnoses a failure — which load, which source, which change — and proposes its
explanation; a person accepts a discrepancy, as row 23 of 070 already allocates. The author would see the
failures and the questions, never the passes, which is what his aim of minimal manual work asks of it
(`EVI-OP-7`).

**How the suite itself would be tested.** A plausibility suite that never fires is indistinguishable from
one that cannot. A simulated source of the kind sought under `EVI-OP-7` makes the obvious test cheap: inject
known defects — a delivery loaded twice, a day dropped, a duplicated customer, a correction to a closed
period — and record which checks caught which. The detection rate per defect type is the suite's own
evidence, and the defects it misses say where the next check belongs.

**Not decided.** Which outputs are in scope at first; the thresholds and how bands are derived; whether a
hard failure blocks only the affected outputs or the whole publication; who may accept a discrepancy, and
whether an accepted one expires; where the checks are declared, and in what format; and whether the method
is adopted at all, which needs an ADR. All of this is held in `ARC-OP-31`.

**Amended after review.** Sol's review found that reconciliation through the chain being tested is not
independent evidence, and gave three counterexamples, recorded in `ARC-OP-31`. The author ruled on the three
recommended changes on 2026-10-06, in these words:

> 1. agreed with the check on the additive financial measures. This can be done when there is a verified
> report, like external reporting or an approved balance sheet or profit and loss statement. We can then
> verify that it should be within a certain bandwith of this externally verified number. Agree with the
> overlap.
> 2. okay
> 3. yes, see also my remarks regarding rule 1.

They apply as follows.

*An independent figure for every additive financial measure.* Where a verified report exists — external
reporting, an approved balance sheet, an approved profit and loss statement — each additive financial measure
is checked against it, at the population and period that report covers, and must fall within a stated
bandwidth of that externally verified number. The figure comes from outside the chain being tested, which is
what makes it evidence: a week of invoices delivered by both an old and a new system under different document
numbers passes every check of the seven families, but not this one. Sources that could carry the same business
event also carry a tested assertion that their populations do not overlap, or a canonical identity for the
business event.

*A new frozen set is admitted on its integrity, not its plausibility.* Before the plausibility suite runs on a
new frozen set, every input is verified against the declared reference date — source version, high-water mark,
effective cut, row count and checksum — and the production run at that date is reproduced under the same code
and assertion versions. Only a set that passes this is tested for plausibility, and only then compared with the
previous reference date. A set whose facts were cut on 30 June and whose dimensions were extracted on 2 July
fails here, where it would have passed every plausibility check.

*Hard checks are scoped, and carry their tolerances.* A domain equation is hard only for a stated accounting
state, with its reconciling components — tax, freight, rounding — and its tolerance written into it; in line
with the first change, the tolerance is a bandwidth, not an exact equality. Expected exceptions, such as late
postings to a period closed in finance but not legally locked, are dated exceptions with an owner and an
expiry. Every new rule starts soft and is promoted to hard only once its observed false-alarm rate justifies
it.

These rulings settle how the checks would work. Whether plausibility testing is adopted still waits for an ADR,
and the bandwidths themselves are not set. The amendment is unreviewed.

## Evaluating the agents themselves

Distinct from evaluating the data, and equally necessary: the system's own semantic
judgment needs measurement, or its autonomy cannot be calibrated.

A **held-out adjudication set** is the natural instrument. Human rulings are recorded
continuously as a by-product of normal operation; a portion is withheld, the system's
hypotheses are scored against it, and the resulting precision figure — per job type, per
model — is what justifies or withdraws autonomy at Tier 2. This is the mechanism by
which thresholds get set from evidence rather than from optimism, and it costs almost
nothing to build because the labels are generated anyway.

Two supporting measures: **cross-model disagreement rate**, as an unsupervised proxy
available before enough rulings accumulate; and **adjudication burden** — questions
asked per useful assertion gained — which is the number that determines whether humans
keep participating.
