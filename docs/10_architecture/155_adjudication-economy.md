# 155 — The adjudication economy: spending scarce human attention where it counts

Drafted 2026-09-25, session 04, from a question the author put, verbatim:

> Next question, how do we keep the human review queue to a responsible minimum? Human
> adjudication will become the bottleneck. Only things that absolutely need adjudication should
> end up there. At the same time we want to minimze the risk of faulty assumptions. Is this a
> real field of tension? Do we need to do something about it? How do we postulate this problem?
> How do we operationalize it?

and his addition when asking for this document: "We should also keep a structured record in an
implementation I think + workflows to monitor."

Revised the same day after external review — GPT-6 Astra on the model, gpt-5.6-sol on whether it
works in a real organisation — recorded in
[XREV_2026-09-25_adjudication-economy_astra](../30_research/notes/XREV_2026-09-25_adjudication-economy_astra.md)
and
[XREV_2026-09-25_adjudication-economy_sol](../30_research/notes/XREV_2026-09-25_adjudication-economy_sol.md).
The author accepted all eleven findings, ruled that seeded checks stay in blinded form and are
excluded from the estimates, and placed the reviewers' disagreement about rigour versus a lean
start where it belongs: "A lean start is about implementation. Every implementation must start
lean." That principle is [ADR-0012](../20_decisions/0012-generic-framework-lean-start.md), and this
document is written accordingly: it describes the full design, and its last sections say how an
implementation grows into it.

Nothing here is built; everything is stated as what the system should do.

This document ties together pieces that were scattered: the allocation rule in
[060_faculty-inventory.md](../00_concept/060_faculty-inventory.md), stratified adjudication
(`ARC-OP-18`), correlated error (`ARC-OP-17`), the adjudication surface (`ARC-OP-15`), ranking
bias (`ARC-OP-6`), queue control in [124_context-write-back.md](124_context-write-back.md), and
value-weighted coverage (`CON-OP-15`).

## Why it matters

Human adjudication is the scarce, specialised, non-fungible resource the whole design is
organised around (060, dimension 2). The agentic layer can propose far more than people can rule
on, and "ten times the proposals is ten times the adjudication" (060, dimension 11). If the queue
cannot be kept small, the cost advantage of the approach disappears however cheap generation
becomes. This is the other half of the economics in `CON-OP-2`: next to the cost per proposal,
the number that decides the case is **human minutes of adjudication per week**.

## Is the tension real?

Yes, locally: every claim that is not reviewed is a risk accepted. But it is not a simple
trade-off, for three reasons.

**Human review is not error-free.** People reviewing a long queue drift into approving what they
are shown; error clusters at the end of long repetitive runs (060, dimension 4). A flooded queue is
reviewed badly. So beyond some volume, *more* review produces *more* risk, not less. There is an
optimum, not a slider.

**Review is only one defence.** Tests, reconciliation, the publication gate of
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md), monitoring and
quarantine ([126](126_context-gardening.md)) also catch faulty assumptions. Where they catch an
error quickly and its effect can be undone, reviewing it beforehand adds little.

**Many claims do not need deciding yet.** A claim nothing depends on can wait until a prioritised
deliverable needs it. Adjudicate on demand, not in advance.

## The problem, stated

*Spend a fixed budget of human attention where it prevents the most expected damage, subject to a
few hard rules.*

The quantity that matters for a candidate claim is **the loss averted by reviewing it**: the
expected loss if it is *not* reviewed, minus the expected loss if it *is*. Both sides count
everything, not only the claim being wrong:

- **without review** — the chance the claim is wrong, times the loss it causes before anything else
  catches it, including damage already done by the time tests or monitoring detect it;
- **with review** — the loss that remains when the reviewer misses the error, plus the **cost of the
  delay** while the claim waits, plus **errors reviewers introduce** themselves.

The loss averted, divided by the minutes of the right person's time the review costs, gives **loss
averted per human minute**. With a fixed weekly budget per reviewer role, candidates are ranked by
that, and the budget is filled from the top.

Three cautions about the terms:

| Term | Caution |
|---|---|
| **The chance a reviewer catches it** | Must be recorded, not assumed. It is not independent of the machine checks: reviewers tend to miss precisely what the machines miss, so the two are estimated together, not multiplied |
| **Detection by other defences** | Detection is not prevention: an error caught three weeks later may already have reached a board pack |
| **Estimates** | Expressed as numeric ranges, not as low/medium/high labels, which cannot be multiplied. Wide ranges are honest at the start; the control loop narrows them |

**The hard rules sit outside the optimisation.** Some claims go to a person by mandate, not by risk:
meaning, KPI definitions, priorities and purpose (060, dimension 13; the teleological tier of
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md)); anything irreversible; anything
regulatory — for a financial institution, BCBS 239, whose effect on the lanes is set out in
[152](152_bcbs-239.md) item 9. **Whether a hard rule applies is itself checked independently**, not left to the triage
that benefits from answering no. This is the allocation rule already proposed in 060 — minimise
expected lifecycle cost *subject to explicit limits on irreversible downside* — applied to the queue.

## Four lanes

| Lane | What goes there | What happens |
|---|---|---|
| **Auto-accept** | Verified by machine on exactly what was tested ([124](124_context-write-back.md)), low consequence, reversible, monitored | Accepted; sampled for audit |
| **Accept provisionally** | Plausible, reversible, limited in reach | Used within an enforced scope; flagged; sampled; promoted only through a gate (below) |
| **Human** | Hard-rule items; wide reach; low confidence together with high consequence; anything contradicting an authorised claim | Enters the adjudication queue with a decision owner, a deadline and a default (below) |
| **Park** | Nothing depends on it yet | Stays a candidate, visibly, with an expiry date; re-triaged when a prioritised deliverable needs it |

Parking is also where value-weighting enters: `CON-OP-15` records that coverage must be coverage of
*what people have prioritised*, and the park lane is how the queue honours that.

**The lanes need enforceable tests, or they will be gamed.** "Reversible", "limited reach" and "has
held up" are not tests anyone can run, and a provisional claim can "survive" simply because nobody
used it, while internal use already shapes decisions. So:

- **promotion from provisional needs evidence and has exposure limits**: the claim must have been
  exercised enough to be tested, not merely left alone, and its use is bounded until then;
- **provisional scope is enforced**: dependency tracking shows where a provisional claim is used, and
  use beyond its scope — an extract, copied logic, a deadline exception — triggers automatic
  quarantine;
- **every lane is re-triaged when a claim's dependencies or use change**, so a claim cannot keep a
  cheap lane after it has become consequential;
- **parked claims are visible debt**, each with an expiry date and a count of what is waiting on it,
  not a place things disappear.

## Who decides, and by when

Routing an item to "the person who knows" fails in practice, because knowledge and decision rights
rarely sit with the same person, named owners do not reserve time, delegates lack authority, and
contested definitions get postponed while urgent delivery goes around the queue. So every item in the
human lane carries:

- an **accountable decision owner** — the person entitled to decide, who may consult whoever knows;
- a **named delegate** with the authority to decide in the owner's absence;
- a **response deadline**;
- an **explicit default** that applies when the deadline passes — for example *remains provisional
  within its scope*, or *stays parked* — so that silence has a defined, safe outcome;
- **cost attribution**: unresolved items are charged to the deliverable that needs them, so the
  sponsor feels the delay.

## Service classes and capacity

A fixed budget turns overload into ageing and parking, and service classes invite every sponsor to
claim the top one. So:

- each class — for example regulatory, consequential, routine — has **objective entry criteria**, a
  **maximum age**, an **escalation path** and a **capacity owner**;
- **capacity is reserved** for mandatory reviews and for the monitoring itself — audits and seeded
  checks draw on the same people and must not be crowded out;
- **demand, capacity and the work displaced** are published, so that trade-offs are visible rather
  than settled quietly.

## Levers that shrink the queue

Each lever acts on one part of the loss averted, and together they move the whole frontier rather
than rationing along it.

- **Better evidence before asking.** The agentic layer gathers independent evidence before proposing.
  Beware correlated error (`ARC-OP-17`): several signals that all derive from one flawed rule are not
  independent evidence.
- **More detection, sooner.** Every test, gate and monitor that catches an error quickly reduces what
  needs review up front. **Reversibility plus fast detection substitute for review.**
- **Less exposure.** Staged use: a claim is used within a bounded scope first and reaches published
  outputs only after it has been exercised and survived.
- **Cheaper, further-reaching review.**
  - rule on **patterns, not instances**, so that one ruling covers four hundred columns
    (`ARC-OP-18`);
  - present options with their evidence, and only what changed;
  - keep the adjudication surface comprehensible (`ARC-OP-15`).

  Pre-drafted options also make reviewers less alert, which is one reason the loop below measures
  reviewer detection rather than assuming it.
- **Precedent — the largest multiplier, and the largest risk.** A ruling on a pattern becomes an
  accepted rule ([124](124_context-write-back.md)), and later matching cases are auto-accepted under
  it. The queue shrinks as the system learns the organisation — and one wrong ruling spreads as far
  as its pattern reaches. So each precedent has a **validated scope** of applicability and an
  **expiry date**, and the **total exposure depending on it** is measured, so that a precedent's
  reach is known before it fails.

## The control loop

Triage is only as good as its estimates, so the system checks them against outcomes.

- **Audit sampling.** A share of auto-accepted and provisionally accepted claims goes to a person for
  audit. Sampling is **stratified by rule or pattern**, because correlated error hides from purely
  random samples (`ARC-OP-17`) — and **random within each stratum**, with **known inclusion
  probabilities** and a share of **exploration samples** outside the strata, because stratification
  alone only looks where the design already expects trouble.
- **Independent audit labels.** An audit's verdict is itself a claim; where the audit decides a
  lane's fate, a second, independent reviewer confirms it.
- **Error rates per lane and per rule**, with uncertainty computed in a way that accounts for
  clustering: four hundred columns under one rule are closer to one observation than to four hundred.
- **Escaped defects** — errors found downstream — traced back to the claim and the lane that let them
  through, together with **exposure** and **detection delay**: how far the error reached, and how
  long it took to find. Overall figures are broken down by risk class so that a reassuring average
  cannot hide a dangerous subgroup.
- **Reviewer disagreement**, estimated by having a sample of items reviewed twice, independently, and
  reported for **groups of reviewers and for rules, never for individuals**. Override rates are
  confounded by case difficulty, local policy and personal style, and per-person figures become
  performance evidence whatever their stated purpose.
- **Seeded checks, blinded.** Occasionally a known-wrong proposal, **representative** of real cases,
  is placed in the queue, **blinded** so that it cannot be told apart. Reviewers are told that this
  happens. Seeds measure whether the review catches what it is meant to catch; they are **excluded
  from production and from all calibration estimates**, and reported at group level only.
- **Calibration** — the agentic layer's stated confidence against audited correctness. Only
  calibrated confidence may drive triage.
- **Queue health** — size against the budget, age, and response times per service class.

**Tightening is automatic; loosening needs a person — within capacity.** When a lane's error rate or
its escaped defects cross a threshold, its class moves toward the human lane at once. But a failing
precedent can push thousands of claims into a fixed budget and crowd out mandatory reviews, and an
alert cannot make an infeasible queue feasible. So when tightening would exceed the reserved
capacity, the affected work is **quarantined or throttled** instead of queued. Moving back, in
either direction, follows **explicit release criteria** with **hysteresis**, so that a lane does not
oscillate. Loosening toward automation always requires a person's approval, on the evidence of the
audits.

## The adjudication record

In an implementation, all of this rests on a **structured record** of every candidate, kept as
workflow state and assertions under
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md). Without it, none of
the measures above can be computed and the triage cannot learn. But a record that demands estimates
and reasons for every candidate becomes a bottleneck itself, and fields get guessed or filled in
afterwards. So it has a small core and an extension.

**Core — every candidate:**

| Field | Content |
|---|---|
| **Claim** | a reference to the assertion |
| **Owner** | the accountable decision owner, and the delegate |
| **Lane** | the lane assigned, and the rule or hard rule that assigned it |
| **Times** | entered, presented, decided; the deadline and whether the default applied |
| **Decision** | accepted, rejected, amended, deferred or defaulted, with the reason |

**Extension — audited, consequential or human-lane candidates:**

| Field | Content |
|---|---|
| **Estimates** | the ranges behind the loss averted, with the basis for each |
| **Service class** | and whether its entry criteria were met |
| **Effort** | time spent on the decision |
| **Precedent** | whether the decision created a rule, or was made under one; the rule's scope and expiry |
| **Audit** | whether sampled, the inclusion probability, the result, and the independent confirmation |
| **Seeded** | whether it was a blinded seed; excluded from all estimates |
| **Downstream** | defects later traced back to this claim, with exposure and detection delay |

Aggregates per lane, per rule, per service class and per reviewer group are derived from it.

**About the people in it.** The record holds data about how people review, which is personal data. It
exists to calibrate the *system* — lanes, rules, confidence — and not to assess people. Reports show
groups and rules, never individuals; access is restricted; the purpose is stated to reviewers; and
the record falls under the data-location register and retention rules of
[126](126_context-gardening.md) like any other store.

## Monitoring workflows

The control loop runs as standing workflows on the agentic layer's heartbeat, with deterministic
machinery doing the counting:

| Workflow | When | What it does | Who acts on the result |
|---|---|---|---|
| **Triage** | each new candidate | apply hard rules, with their independent check; estimate the loss averted; assign lane, class, owner, deadline and default; write the core record | D and A, under approved rules |
| **Re-triage** | when dependencies or use change, or a parked claim becomes needed | re-assign the lane | D and A |
| **Scope enforcement** | continuously | detect provisional claims used beyond their scope; quarantine | D |
| **Deadlines and defaults** | continuously | apply the default when a deadline passes; escalate per class | D; H by escalation |
| **Audit sampling** | continuously | draw stratified random and exploration samples, with known probabilities; route to people; obtain independent confirmation where it decides a lane | H audits |
| **Lane calibration** | weekly | error rates with cluster-aware uncertainty per lane and rule; tighten within capacity; quarantine or throttle beyond it; propose loosening | D tightens; H approves loosening |
| **Escaped-defect tracing** | on each defect found downstream | trace to claim, lane and rule; record exposure and detection delay | D and A; H for the consequence |
| **Precedent review** | when a rule accumulates failures, escapes, or reaches its expiry | suspend auto-acceptance under it; send it back to a person | D suspends; H rules |
| **Seeded checks** | periodically, at a low rate | place blinded representative seeds; record at group level; keep them out of all estimates | D |
| **Calibration check** | monthly | compare stated confidence with audited correctness, by risk class | A reports; H decides |
| **Queue health** | continuously | size against budget and reserved capacity, age, service-level breaches; alert | D alerts; H reallocates |
| **Budget report** | weekly | human minutes spent per role, class and lane; loss averted; work displaced; what was parked; what escaped — the number `CON-OP-2` needs | A drafts; H reads |

These are row 44 of [070_task-allocation.md](../00_concept/070_task-allocation.md).

## How an implementation grows into this

Per [ADR-0012](../20_decisions/0012-generic-framework-lean-start.md), this document describes the
framework, not a first implementation, and every implementation starts lean. The monitoring above
assumes stable claim identifiers, clean lineage and reliable defect reporting; an organisation that
does not yet have them would get precise-looking nonsense from it. So an implementation adds the
parts in stages, each stage only once the traceability it depends on has been shown to work:

| Stage | Adds | Requires first |
|---|---|---|
| **1 — Lean start** | Four lanes with hard rules; decision owners, deadlines and defaults; reserved capacity; the core record; queue age, decision time, audit failures, and escaped defects reviewed by hand | — |
| **2 — Measured** | Stratified random audits with independent confirmation; error rates per lane and rule; precedents with scope and expiry; scope enforcement; blinded seeded checks | Stable claim identifiers; dependable tracing of defects to claims |
| **3 — Calibrated** | Numeric estimates of loss averted; cluster-aware uncertainty; calibration of stated confidence; automatic tightening with release criteria; the extended record | Enough audit history to estimate from; lineage good enough to trace exposure |

The first implementations are planned as sandboxes on open data (ADR-0012), where stage 1 can be
exercised end to end and the prerequisites for stage 2 tested deliberately.

## Open

`ARC-OP-28` holds what is open: how the first estimates are made before any history exists; initial
thresholds, sampling rates and reserved-capacity shares; who sets the weekly budget per role; the
evidence required to promote a provisional claim; and how the model is exercised in a sandbox, where
the "business owners" are simulated. The formula is a model to reason with, not a measured result;
nothing here has been tested.
