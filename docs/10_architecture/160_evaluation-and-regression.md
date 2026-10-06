# 160 — Evaluation and regression

The brief asks for "a test framework that constantly monitors for regression." That
sentence contains three different guarantees, of sharply increasing difficulty, and they
need separating before anything can be built. A fourth guarantee, about the code rather than
the data, was added on 2026-09-28 and is set out under *Release regression* below. A fifth,
a quick sanity check on whether the data is plausible at all, was added on 2026-10-06 and is set out under
*Plausibility* below. How these and the other kinds of test — unit tests and data tests among them — fit
together, and which root cause each is meant to catch first, is in [162](162_test-framework.md).

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
for whether the movement is credible over that interval. *(Added 2026-10-06: see *Plausibility* below. A rule
proposed the same day, that a new frozen set first pass checks of its own before it becomes the baseline, was
dropped by the author as over-engineering for now.)*

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

## Plausibility — back-of-the-envelope sanity checks

*Redrafted 2026-10-06, session 07, after the author redefined plausibility; open as `ARC-OP-31` in the
[register](../../registers/OPEN_POINTS.md). Unreviewed. The first draft of the same day, its review, the
author's rulings on it and their review are superseded and kept, verbatim, in
[2026-10-06-plausibility-first-draft](../30_research/notes/2026-10-06-plausibility-first-draft.md). Where the
other kinds of test sit, and which root cause each is meant to catch, is in
[162](162_test-framework.md).* *Amended 2026-10-06 after [sol's review](../30_research/notes/XREV_2026-10-06_test-framework_sol.md), on the author's ruling (`ARC-OP-31`, recommendations 12 to 15); the amendment is unreviewed.*

The author's request:

> next to regression testing we also need (constant) plausibility testing as a means of sanity checks,
> probably on production, where data can change daily, to make sure that we don’t get weird double
> counting, etc. Also for every transition of the fixed reference date / fixed data set, when the test data
> set is updated.

and, the same day, what it is and is not: "a first line of defense against grave errors, load failures
etcetera. It doesn't need to catch all errors. It is a quick survey of what comes in, and how it is
transformed" — "back of the envelope sanity checks, to quickly and regularly check for issues on those parts
of the data where a 'hard' check is difficult (like changing daily amounts)." The full text is in
[162](162_test-framework.md).

**What it checks.** Each load is compared with what is usual for it. Did every expected load arrive? Are its
row count and its main totals roughly in line with the previous load, the same weekday last week, or the
recent trend? And does roughly the expected volume pass through each layer — source, staging, vault, marts —
so that a sudden change in the ratio between two layers shows where something went wrong in the
transformation? These are the questions an experienced analyst asks of a morning's figures before trusting
them, written down so that they are asked every time. "Usual" is judged like with like on a business
calendar — the same weekday, and the same holiday or month-end status — and the arrival schedule lists the days
on which no load is expected, so that a public holiday or a month-end does not raise a warning by itself.

**What it catches.** Gross errors, and above all unexpected ones: a load that did not arrive or arrived
partly, a batch loaded twice, a join that suddenly multiplies rows, a source that changed what it sends.
It is not expected to catch a single wrong invoice or a small double count; those belong to unit tests and
data tests ([162](162_test-framework.md)).

**How it reports.** Softly. A figure outside its usual range raises a warning and a question; it does not
block publication. "Usual" is deliberately rough — a band around recent history, wide enough that a normal
day does not fire — because a check that fires every day is ignored, which is the alert-fatigue argument of
Level 2 above. A warning shows the observed value, the usual range, the difference and the load concerned;
the agentic layer is asked to diagnose it only when someone opens it. The author sees the warnings, never the
passes.

**When it runs.** On every load, in production. And at the quarter turn, when the frozen data set and its
reference date are replaced: the plausibility check between the two reference dates already described under
*The quarter turn* — volumes, totals and distributions judged for whether the movement is credible over a
quarter.

**Not decided.** Which loads and totals are watched first; how wide the bands are and how they are derived;
and whether the method is adopted, which needs an ADR. Held in `ARC-OP-31`.

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
