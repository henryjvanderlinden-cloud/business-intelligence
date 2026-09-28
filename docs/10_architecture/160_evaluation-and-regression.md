# 160 — Evaluation and regression

The brief asks for "a test framework that constantly monitors for regression." That
sentence contains three different guarantees, of sharply increasing difficulty, and they
need separating before anything can be built. A fourth guarantee, about the code rather than
the data, was added on 2026-09-28 and is set out under *Release regression* below.

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

*Added 2026-09-28, session 07, from the author's working practice. Unreviewed, and open as
`ARC-OP-30` in the [register](../../registers/OPEN_POINTS.md).*

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
for whether the movement is credible over that interval.

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

**Not decided.** The form and location of release notes: one per release, tied to a
commit, machine-readable so that attribution can be checked, and distinct from ADRs, which
record why a design was chosen, and from the step log, which records what work was done.
What counts as an output for the snapshot. How the diff is summarised so that its residue
is readable. And whether the method is adopted at all, which needs an ADR. All of this is
held in `ARC-OP-30`.

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
