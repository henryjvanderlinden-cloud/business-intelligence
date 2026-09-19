# nsdn Open Points Register v1.0

**Status: authoritative.** Cut 2026-09-19, session 01. This file is the single
authoritative answer to *what is open?* for this project.
[`docs/00_concept/040_open-questions.md`](../docs/00_concept/040_open-questions.md) is
superseded as of this cut and retained for provenance; its numbering is preserved in the
`from` line of each migrated row.

Conventions — state tokens, supersession, identifiers, archiving — are in
[README.md](README.md). Enforcement is `python tools/check_repo.py`.

---

## §1 — Concept and argument (`CON`)

### CON-OP-1 — Is the three-tier autonomy claim original?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The structural / semantic / teleological tiering in
[ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) is the load-bearing
intellectual contribution of this project so far, and it has not been checked against
anybody else's work. The schema-matching and data-governance literatures have been
thinking about the structural-versus-semantic boundary for thirty years, and the
teleological layer resembles arguments from the decision-support tradition. If the
tiering is already standard, the contribution is the *mandate policy* built on it rather
than the distinction itself, and the framing should change accordingly.

Closes when [050_prior-art.md](../docs/00_concept/050_prior-art.md) carries a verdict on
this specific claim.

### CON-OP-2 — The economics have no number
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The argument rests on an unquantified premise: that per-token reasoning cost has fallen
far enough to make per-column, per-hypothesis machine reasoning affordable, while the
cost of a human doing the same has not moved. Nothing in this repository puts a figure
on it.

A back-of-envelope is cheap and should be done early, because the whole thesis is softer
than it sounds if the ratio is not dramatic: cost to profile one column, cost to
generate and evidence one hypothesis, cost per adjudicated assertion, against a
contractor day rate. Compute it against real token prices and a plausible landscape
size, and state the break-even in columns.

If the number is unflattering, that is a finding and belongs in the argument rather than
outside it.

### CON-OP-3 — What is the acceptance test for an automated analysis?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 11)*

"Interesting" is not measurable. "Changed a decision" is, but only retrospectively and
rarely. Without an acceptance test, Phase 3 cannot be evaluated and its failure mode —
statistically true irrelevance — will be invisible from inside the system.

---

## §2 — Architecture (`ARC`)

### ARC-OP-1 — How is a source discovered rather than registered?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 4)*

The crawler image is the most evocative element of the original brief and the most
legally fraught. [150_trust-and-blast-radius.md](../docs/10_architecture/150_trust-and-blast-radius.md)
proposes inventory-driven discovery with inferred-source *proposals*, but does not
settle whether active discovery is in scope at all.

### ARC-OP-2 — What evidence promotes a joinability hypothesis to a business-key assertion?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 7)*

A stated threshold is needed or the system floods the adjudication queue or silently
asserts nonsense. [ADR-0005](../docs/20_decisions/0005-three-autonomy-tiers.md) rules
that thresholds are set from measured precision against a held-out adjudication set
rather than from judgement, which makes this row dependent on `EVI-OP-1`.

### ARC-OP-3 — How is disagreement between two adjudicators represented?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 8)*

Semantics are contested in real organisations. A model admitting only one answer records
whichever arrived last, and silently discards the more interesting finding — that two
named people believe different things about the same column.

### ARC-OP-4 — How does an assertion age?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 9)*

A confirmed fact about a system re-platformed two years later is no longer true and
nothing in the data says so. Falsifiers and review dates are proposed in
[120_context-layer.md](../docs/10_architecture/120_context-layer.md); the decay policy
itself is unspecified.

### ARC-OP-5 — Per-source reliability is not modelled
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The design calibrates autonomy globally — one precision figure per job type per model.
It should almost certainly be calibrated *per source*: how often were our inferences
about this system subsequently overturned? Sources differ enormously in how well their
structure predicts their semantics, and a source with a poor record should generate
hypotheses that are ranked lower and adjudicated earlier, not the same ones with the
same confidence.

This is a genuine addition to the architecture rather than a question about it, and it
costs almost nothing once the held-out adjudication set exists, because the labels are
already being produced.

### ARC-OP-6 — Information-gain ranking is biased toward what is already understood
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The adjudication queue in [170_human-interfaces.md](../docs/10_architecture/170_human-interfaces.md)
ranks questions by how many downstream hypotheses they unblock. High-degree entities —
customer, product, order — unblock the most, and are precisely the entities an
organisation already understands well. The adjudications that carry real information may
be low-degree: the obscure code list, the one table nobody remembers.

Pure information gain will systematically under-ask exactly where the system is most
ignorant. Some counterweight is needed — expected surprise, or uncertainty-weighted
gain — and the naive formulation should not be implemented without one.

### ARC-OP-7 — Context layer: files, graph, or both?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 12)*

[120_context-layer.md](../docs/10_architecture/120_context-layer.md) argues for markdown
cards in git with a derived, disposable graph index, and states the honest objections —
git discomfort past roughly a hundred thousand files, and history thrashing from
high-frequency profile updates. The most consequential unmade decision in the
architecture; it should be settled by an ADR and not by drift.

### ARC-OP-8 — What is the unit of agent work?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 13)*

[130_agent-loop.md](../docs/10_architecture/130_agent-loop.md) argues for many short,
idempotent, independently retryable jobs over a long-running loop. Almost certainly
right; unratified, and with unexamined implications for how state passes between jobs.

### ARC-OP-9 — Model routing policy
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 14)*

Which model, at which tier, for which job, and who decides. Dependent on `CON-OP-2`,
since routing is an economic question before it is a capability question.

### ARC-OP-10 — What does the human interface actually look like?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 16)*

Pull requests, a web application, a chat surface, or a weekly digest. Determines whether
adjudication happens at all, which makes it the highest-stakes interface question and
the one most likely to be answered by default.

### ARC-OP-11 — SQL dialect normalisation
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 6)*

`sqlglot` is the candidate in
[180_technology-posture.md](../docs/10_architecture/180_technology-posture.md),
unevaluated. Blocks `EVI-OP-3`.

### ARC-OP-12 — Who maintains the decision register?
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 10)*

The teleological anchor is a hard dependency for everything at Tier 3, and it is
maintained by people who have no immediate incentive to maintain it. If there is no
answer to this, Phase 3 has no foundation and the honest move is to say so early.

---

## §3 — Evidence and measurement (`EVI`)

### EVI-OP-1 — Ground truth for the falsifiable core
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 2, residual after
[ADR-0006](../docs/20_decisions/0006-project-mode.md))*

Public practice data supplies genuine messiness but no answer key for cross-source
entity identity, and the project's central claim is a precision figure. The resolution
proposed in [410_first-vertical-slice.md](../docs/40_roadmap/410_first-vertical-slice.md)
is a hand-built sample of a few hundred entities, frozen before development and partly
held back.

Closes when a candidate source pair is selected and the sample exists.

### EVI-OP-2 — Candidate public dataset survey
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 3)*

Sources must be independently built, must genuinely share entities, and must permit
identity to be established by hand for a sample. Dutch public registers are the leading
candidate on structural grounds. The survey needs no code and is the natural first
substantive task of Mode 1.

### EVI-OP-3 — Query logs as evidence
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

Query logs record joins that humans already believed were valid. They are usually
available, cheap to parse, and — the hypothesis — may carry more key evidence than
profiling does, at a fraction of the cost.

If that is true it partially undercuts the project's own thesis in an interesting way:
the most valuable semantic evidence would not be model-generated at all, but merely
model-*interpreted*. Worth knowing early, and it is a prototype rather than a debate. In
a public-data setting there are no query logs, which is a limitation of the Mode 2
environment worth stating alongside the result.

### EVI-OP-4 — Minimum viable profiling pass
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 5)*

How much joinability evidence do sketch-based methods yield across two schemas, at what
cost, without moving data? Determines whether profiling is affordable at landscape scale
and whether it is *permissible*, which matters more.

---

## §4 — Process (`PRC`)

### PRC-OP-1 — Nothing in this repository has been externally reviewed
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

Every document here was drafted by one model in one session, which by the model-switch
rule in [500_working-method.md](../docs/50_process/500_working-method.md) makes the
whole repository unreviewed by construction. The argument currently has exactly one
reader and that reader wrote it.

The first external pass should attack the two claims everything else rests on: the
three-tier distinction (`CON-OP-1`) and the assertion that business keys are
machine-proposable at useful precision. Adversarial framing, one object per pass, per
[510_external-review.md](../docs/50_process/510_external-review.md).

### PRC-OP-2 — Keep the apparatus proportionate to the work
**⚠ STATE: HELD**
Opened 2026-09-19, session 01. Resume when the register exceeds roughly forty live rows
or the first archive cut is contemplated.

This repository has acquired a register, a handover series, a process convention and a
checker while containing no code and one week of thinking. The apparatus is justified
here because it was inherited whole from a project where it was learned expensively, and
because it costs almost nothing at this size — but ceremony that exceeds the work is a
real failure mode, and a project that spends its Mode 1 perfecting its own bureaucracy
has found a comfortable way to avoid testing its thesis.

Held rather than open because the correct response is vigilance, not action.

### PRC-OP-3 — Cross-model review is unwired
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01. *(from open question 15)*

Codex is registered as a local MCP server and reachable from these sessions, so the
transport exists. What does not exist is the convention for *this* repository: which
objects get reviewed, on what cadence, and how disagreement is recorded.
[510_external-review.md](../docs/50_process/510_external-review.md) adapts the
compendium's XREV convention; it has not been exercised once.

---

## §5 — Commercial premises (`BIZ`)

### BIZ-OP-1 — The adjudication hedge may not be priced
**⛔ STATE: OPEN**
Opened 2026-09-19, session 01.

The project's strategic premise, stated by the author: work is getting scarce, rates are
under pressure, and the response is to move to where the remaining human contribution
is — adjudication, the judgement that the data cannot supply.

The uncomfortable version, recorded here rather than left in conversation because it is
the premise most likely to be wrong: *if* rates are under pressure because capability is
being commoditised, then adjudication capacity may be commoditised on the same schedule,
merely later. The hedge assumes the market can identify and will pay for judgement that
is hard to demonstrate in advance and only visible when it is absent. That assumption is
not obviously true, and it has not been examined anywhere in this repository.

The falsifier is observable and worth watching deliberately: whether engagements
increasingly buy *review and assurance* of machine-built data work as a distinct,
separately priced service, or whether that work is absorbed into delivery at the old
rate. Evidence either way belongs in this row.

Recording it does not make the strategy wrong. A hedge with a stated failure condition
is a better hedge than one without.
