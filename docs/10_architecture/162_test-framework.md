# 162 — The test framework, by root cause

*Drafted 2026-10-06, session 07, from the author's direction, and held in `ARC-OP-31` in the
[register](../../registers/OPEN_POINTS.md). Unreviewed. Nothing here is adopted; that needs an ADR.*

[160](160_evaluation-and-regression.md) describes the guarantees one at a time. This file is the overview
the author asked for: which kinds of test there are, what each is for, and which test is expected to catch
which root cause first. It exists because a first draft of plausibility testing tried to make one kind of
test carry the weight of all the others, and was then reviewed against a standard of completeness it was
never meant to meet. The author put the correction in these words:

> Plausibility means that by and large, the data is plausible. It doesn't state that it's 100% correct. It
> is a first line of defense against grave errors, load failures etcetera. It doesn't need to catch all
> errors. It is a quick survey of what comes in, and how it is transformed, to do a sanity check to catch a
> wide range of (unexpected) errors. Let's not over engineer this. We also have unit tests (not sure if
> that's already in the documentation) that should cover design flaws. So let's take if from the root
> causes, some examples: A data load has not arrived: should be covered by the plausibility tests. A batch
> was loaded twice: plausibility test. Debit equals credit is a different type of test, not a plausibility
> test, although it should be in the test framework and it is a very simple sanity check. Okay, so maybe
> part of ongoing plausibility testing. Uniqueness issues, also part of plausibility, but more of the
> "regular" test framework. Let's work from the angle of plausibility tests, unit tests, whatever other
> tests there are, and root causes, such as loading issues, modelling issues, unexpected edge cases, data
> quality issues. The reviewers are applying insanely strict expectations, on plausibility checks, which
> should be more like back of the envelope sanity checks, to quickly and regularly check for issues on those
> parts of the data where a 'hard' check is difficult (like changing daily amounts).

The principle that follows: **each kind of test has one job, and no kind of test is expected to catch
everything.** Defence comes from the layers together.

## The kinds of test

**Unit tests** check transformation logic on small, fixed inputs whose expected output is known by
construction: a handful of rows, the result written down beforehand. They catch flaws in design and
modelling — a wrong join, a wrong grain, a mishandled null, a known edge case — and they run on every code
change, before anything reaches real data. When an edge case is found in production, it becomes a unit test,
so that it is caught at design time from then on. Until now this repository did not mention them; row 22 of
[070](../00_concept/070_task-allocation.md), *write tests and a regression suite*, is where they are
allocated, and [`tests/`](../../tests/README.md) is where tests of the system's own code would live.

**Data tests** are the regular framework: hard checks that hold or fail, on every load. Uniqueness of keys,
nullity, referential integrity, accepted values, freshness — Level 2 of 160 — and the query-level join tests
of [128](128_join-knowledge.md). Simple domain rules belong here too: debits equal credits, invoice lines sum
to the header, within a stated rounding. So does reconciliation of a financial measure against a verified
report — external reporting, an approved balance sheet or profit and loss statement — within a stated
bandwidth, whenever such a report exists; the author ruled on that on 2026-10-06, and it is a periodic data
test, not a daily one.

**Plausibility checks** are back-of-the-envelope sanity checks on what comes in and how it is transformed:
quick, cheap, run on every load, and soft — they warn and ask, they do not block. They are for the parts of
the data where a hard check is difficult, such as amounts that change every day. 160 describes them under
*Plausibility*.

**Release regression** tests the code on frozen data: every difference between two daily snapshots is
attributed to a release note and accepted against its stated expectation, or treated as a regression. 160,
*Release regression*.

**Semantic regression and the evaluation of the agents** test whether meaning has drifted and whether the
system's own judgement is good enough for the autonomy it has. 160, Level 3 and *Evaluating the agents
themselves*.

## Root causes, and what catches them first

| Root cause | First line | Also likely to notice it |
|---|---|---|
| A load did not arrive, or arrived partly | plausibility: volume far below normal | data test: freshness |
| A batch was loaded twice | plausibility: volume about double | data test: uniqueness |
| A load arrived late or out of order | data test: freshness; [127](127_temporal-behaviour.md)'s monitoring of the order of time | plausibility |
| Modelling flaw: wrong join, wrong grain, fan-out | unit tests; the join tests of 128 | plausibility: ratios between layers shift |
| Unexpected edge case | plausibility, if it is large enough to move a total | a unit test, once the case is known |
| Data quality at the source | data tests | plausibility, for gross shifts |
| A code change does more than it said | release regression | plausibility |
| A definition or assertion changes meaning | semantic regression (160, Level 3) | release regression, which attributes the change |
| Figures disagree with the books | data test against a verified report, when one exists | plausibility, for gross gaps |

The table is a starting point. A root cause that turns up in practice and is caught by none of these is
the signal to add a test where it would have been cheapest to catch it.

## Not decided

The tooling for unit and data tests — [180](180_technology-posture.md) names dbt tests, Great Expectations and
Soda Core as candidates; where each kind of test is declared; and whether the framework is adopted, by ADR.
All held in `ARC-OP-31`.
