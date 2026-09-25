# 155 — The adjudication economy: spending scarce human attention where it counts

Drafted 2026-09-25, session 04, from a question the author put, verbatim:

> Next question, how do we keep the human review queue to a responsible minimum? Human
> adjudication will become the bottleneck. Only things that absolutely need adjudication should
> end up there. At the same time we want to minimze the risk of faulty assumptions. Is this a
> real field of tension? Do we need to do something about it? How do we postulate this problem?
> How do we operationalize it?

and his addition when asking for this document: "We should also keep a structured record in an
implementation I think + workflows to monitor." Nothing here is built; everything is stated as
what the system should do. Not yet externally reviewed.

This document ties together pieces that were scattered: the allocation rule in
[060_faculty-inventory.md](../00_concept/060_faculty-inventory.md), stratified adjudication
(`ARC-OP-18`), correlated error (`ARC-OP-17`), the adjudication surface (`ARC-OP-15`), ranking
bias (`ARC-OP-6`), queue control in [124_context-write-back.md](124_context-write-back.md), and
value-weighted coverage (`CON-OP-15`).

## Why it matters

Human adjudication is the scarce, specialised, non-fungible resource the whole design is
organised around (060, dimension 2). The agentic layer can propose far more than people can rule
on, and "ten times the proposals is ten times the adjudication" (060, dimension 11). If the queue
cannot be kept small, the cost advantage of the project disappears however cheap generation
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

For each candidate claim:

| Term | Meaning |
|---|---|
| **p** | the probability the claim is wrong |
| **L** | the loss if it is wrong and slips through: reach × severity × how hard it is to undo |
| **d** | the probability something else catches it in time: tests, the publication gate, monitoring |
| **r** | the probability the reviewer actually catches it |
| **h** | the cost of reviewing it, in minutes of the right person's time |

The expected loss a review averts is **p × L × (1 − d) × r**. A claim is worth a person's time when
that exceeds **h**. With a fixed weekly budget per reviewer role, candidates are ranked by
**expected loss averted per human minute** and the budget is filled from the top.

**The hard rules sit outside the optimisation.** Some claims go to a person by mandate, not by risk:
meaning, KPI definitions, priorities and purpose (060, dimension 13; the teleological tier of
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md)); anything irreversible; anything
regulatory. This is the allocation rule already proposed in 060 — minimise expected lifecycle cost
*subject to explicit limits on irreversible downside* — applied to the queue.

**Numbers are not needed to start.** Low, medium and high bands for p, L and d are enough; the
control loop below calibrates them against what actually happens.

## Four lanes

| Lane | What goes there | What happens |
|---|---|---|
| **Auto-accept** | Verified by machine on exactly what was tested ([124](124_context-write-back.md)), low consequence, reversible, monitored | Accepted; sampled for audit |
| **Accept provisionally** | Plausible, reversible, limited in reach | Used in internal and staging work only, flagged, sampled; promoted to published use after it has held up for a set period |
| **Human** | Hard-rule items; wide reach; low confidence together with high consequence; anything contradicting an authorised claim | Enters the adjudication queue of [124](124_context-write-back.md), with its service class |
| **Park** | Nothing depends on it yet | Stays a candidate; re-triaged when a prioritised deliverable needs it |

Parking is also where value-weighting enters: `CON-OP-15` records that coverage must be coverage of
*what people have prioritised*, and the park lane is how the queue honours that.

## Levers that shrink the queue

Each lever acts on one term, and together they move the whole frontier rather than rationing along
it.

- **Lower p before asking.** The agentic layer gathers independent evidence before proposing. Beware
  correlated error (`ARC-OP-17`): several signals that all derive from one flawed rule are not
  independent evidence.
- **Raise d.** Every test, gate and monitor that catches an error quickly reduces what needs review
  up front. **Reversibility plus detectability substitute for review.**
- **Lower L.** Staged exposure: a claim is used internally first and reaches published outputs only
  after it has survived.
- **Lower h.** Make each review cheap and far-reaching:
  - rule on **patterns, not instances**, so that one ruling covers four hundred columns
    (`ARC-OP-18`);
  - present pre-drafted options with their evidence, and only what changed;
  - route each item to the person who actually knows;
  - keep the adjudication surface comprehensible (`ARC-OP-15`).
- **Precedent — the largest multiplier.** A ruling on a pattern becomes an accepted rule ([124](124_context-write-back.md)),
  and later cases matching it are auto-accepted under it, monitored and sampled. The queue shrinks
  as the system learns the organisation.

## The control loop

Triage is only as good as its estimates, so the system checks them against outcomes:

- **Audit sampling.** A share of the auto-accepted and provisionally accepted claims goes to a person
  for audit, **stratified by rule or pattern** rather than drawn at random, because correlated error
  hides from random samples (`ARC-OP-17`).
- **Error rate per lane and per rule**, with confidence bounds, from the audits.
- **Escaped defects** — errors found downstream — traced back to the claim and the lane that let them
  through. This is the outcome measure that matters.
- **Reviewer override rate** — how often people reject or change what the agentic layer proposed.
  Near zero means either rubber-stamping or a class that could be automated; high means the
  proposals are poor.
- **Seeded checks.** Occasionally a known-wrong proposal is planted in the queue, to tell attentive
  approval from rubber-stamping. Reviewers are told that this happens.
- **Calibration** — the agentic layer's stated confidence against audited correctness. Only
  calibrated confidence may drive triage.
- **Queue health** — size against the budget, age, and response times per service class.

**Tightening is automatic; loosening needs a person.** When a lane's error rate or its escaped defects
cross a threshold, its class moves toward the human lane at once. Moving a class toward automation
requires a person to approve it, on the evidence of the audits.

## The adjudication record

In an implementation, all of this rests on a **structured record** of every candidate, kept as
workflow state and assertions under
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md). Without it none of
the measures above can be computed, and the triage cannot learn.

Per candidate:

| Field | Content |
|---|---|
| **Claim** | a reference to the assertion |
| **Estimates** | p, L, d and h, as bands, with the basis for each |
| **Lane** | the lane assigned, and the rule or hard rule that assigned it |
| **Service class** | for the human lane: regulatory, consequential or routine |
| **Queue times** | entered, presented, decided |
| **Reviewer** | who decided, in which role |
| **Effort** | time spent on the decision |
| **Decision** | accepted, rejected, amended or deferred, with the reason |
| **Precedent** | whether the decision created a rule, or was made under one |
| **Audit** | whether the claim was sampled for audit, and the result |
| **Seeded** | whether it was a planted check, and whether it was caught |
| **Downstream** | defects later traced back to this claim |

Aggregates per lane, per rule, per service class and per reviewer role are derived from it.

**A caution.** The record contains data about how individual people review, which is personal data
about them. It exists to calibrate the *system* — lanes, rules, confidence — and not to assess
people. Access is restricted accordingly, reports show roles rather than names where possible, and
the purpose is stated to the reviewers. The adjudication record falls under the data-location
register and retention rules of [126](126_context-gardening.md) like any other store.

## Monitoring workflows

The control loop runs as standing workflows on the agentic layer's heartbeat, with deterministic
machinery doing the counting:

| Workflow | When | What it does | Who acts on the result |
|---|---|---|---|
| **Triage** | each new candidate | estimate p, L, d, h; apply hard rules; assign a lane and service class; write the record | D and A, under approved rules |
| **Re-triage** | when a parked claim becomes needed, or its estimates change | re-assign the lane | D and A |
| **Audit sampling** | continuously, at a rate per lane | draw stratified samples and route them to people | H audits |
| **Lane calibration** | weekly | compute error rates with bounds per lane and rule; tighten automatically where a threshold is crossed; propose loosening where evidence supports it | D tightens; H approves loosening |
| **Escaped-defect tracing** | on each defect found downstream | trace it to the claim, lane and rule; count it against them | D and A; H for the consequence |
| **Calibration check** | monthly | compare stated confidence with audited correctness; flag drift | A reports; H decides |
| **Seeded checks** | periodically, at a low rate | plant known-wrong proposals; record whether they were caught | D |
| **Precedent review** | when a rule accumulates audit failures or escaped defects | suspend auto-acceptance under the rule; send the rule back to a person | D suspends; H rules |
| **Queue health** | continuously | queue size against budget, age, service-level breaches; alert on breaches | D alerts; H reallocates |
| **Budget report** | weekly | human minutes spent per role and lane, value averted, what was parked, what escaped — the number `CON-OP-2` needs | A drafts; H reads |

These are additions to the task allocation: row 44 of
[070_task-allocation.md](../00_concept/070_task-allocation.md).

## Open

`ARC-OP-28` holds what is open: how the estimates are made before any history exists; the initial
thresholds and sampling rates; who sets the weekly budget per role; and whether the record's data
about reviewers can be kept proportionate. The formula is a model to reason with, not a measured
result; nothing here has been tested.
