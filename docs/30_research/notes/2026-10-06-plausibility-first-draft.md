# The first draft of plausibility testing, superseded — 2026-10-06

*Moved here verbatim from [160](../../10_architecture/160_evaluation-and-regression.md) on 2026-10-06, session 07,
when the author redefined plausibility as back-of-the-envelope sanity checks; only relative links were adjusted
to this file's location. Everything below is **superseded** and is kept for provenance: the first draft, its
review by sol, the author's rulings on that review, the amendment that integrated them, and the review of the
amendment. The current text is the section *Plausibility* in 160 and the overview in
[162](../../10_architecture/162_test-framework.md); the account of how it got there is in `ARC-OP-31` in the
[register](../../../registers/OPEN_POINTS.md).*

*Why it was superseded, in the author's words:* "The reviewers are applying insanely strict expectations, on
plausibility checks, which should be more like back of the envelope sanity checks". The draft had made
plausibility the end-to-end check of published outputs, with six hard check families, and its review
assignments asked the reviewer to assume a real double count would reach users; both held plausibility to a
standard of completeness it was never meant to meet. Of the rulings recorded below, the reconciliation against
a verified report within a bandwidth (1) and the scoped domain equations (3) moved to data tests in 162; the
admission check on a new frozen set (2) was dropped as over-engineering for now; and recommendations 8 to 11
lapsed unruled.

---

## Plausibility — does the output still make sense?

*Added 2026-10-06, session 07, at the author's request, and open as `ARC-OP-31` in the
[register](../../../registers/OPEN_POINTS.md). Nothing in this section has been ruled except the author's request
itself. Reviewed the same day and failed by [sol](XREV_2026-10-06_plausibility_sol.md): a
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
[128](../../10_architecture/128_join-knowledge.md) ask whether one relationship can be joined without fan-out; release regression
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
[128](../../10_architecture/128_join-knowledge.md) — row-count preservation, aggregate and per-fact reconciliation, multi-path
fan-out checks — which run on every load and block publication through the gate of
[ADR-0011](../../20_decisions/0011-assertions-identity-plane-publication-gate.md); the monitoring of the order of
time in [127](../../10_architecture/127_temporal-behaviour.md) — replays and duplicate deliveries, sequence gaps, closed periods
that change; row 23 of [070](../../00_concept/070_task-allocation.md), reconciliation across source, vault,
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
any other ([120](../../10_architecture/120_context-layer.md)). They are, moreover, the same invariants the author's ruling of
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
[ADR-0011](../../20_decisions/0011-assertions-identity-plane-publication-gate.md) from relationships to outputs;
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
and the bandwidths themselves are not set. *Reviewed the same day and failed by
[sol](XREV_2026-10-06_plausibility-amendment_sol.md): verified reports are periodic, so a
duplicate published daily is not caught until the report arrives; new rules starting soft let a known
accounting identity publish broken; raw-file checksums would reject a reordered export; and a bandwidth on an
exact accounting identity lets a real imbalance through. The last follows from a sentence above that extends
the author's ruling further than he said. Recommended changes await his ruling in `ARC-OP-31`; the text above
is as reviewed.*
