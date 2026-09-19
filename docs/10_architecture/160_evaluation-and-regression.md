# 160 — Evaluation and regression

The brief asks for "a test framework that constantly monitors for regression." That
sentence contains three different guarantees, of sharply increasing difficulty, and they
need separating before anything can be built.

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
