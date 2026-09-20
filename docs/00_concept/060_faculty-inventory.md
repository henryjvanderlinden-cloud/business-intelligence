# 060 — Faculty inventory

A comparison of the three faculties of
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md) on a common set of
dimensions, for the purpose of **allocation**: deciding which faculty should be given
which work, and what the handoff costs.

Drafted 2026-09-20, session 03, and revised the same session against an external pass
recorded in
[XREV_2026-09-20_faculty-inventory_sol](../30_research/notes/XREV_2026-09-20_faculty-inventory_sol.md).
The dimensions, the allocation rule and the interaction candidate below all changed as a
result; the note holds what they were and why they failed.

## Why a grid and not three lists of strengths

Three lists of strengths and weaknesses do not yield an allocation, because the entries
are not commensurable and the comparison stays intuitive. An allocation needs the same
dimensions scored for each faculty, so that giving a unit of work to one faculty rather
than another is a calculation rather than a preference.

The form of that calculation is the one the external pass of 2026-09-20 supplied when it
refuted `CON-OP-11`: not a single governing axis, but an expected-value quantity with
several terms. Allocation per unit of work is the same shape, and the reason to run it
properly here is that the project has already been burned once by collapsing such a
calculation onto one axis.

## Capability and entitlement are different columns

[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md) already holds this
distinction and this document inherits rather than proposes it: a mandate is what a
faculty is *entitled* to do, which does not follow from what it is *able* to do.
Dimensions 1 to 12 are capability. Dimension 13 is entitlement and is set by
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md), not by anything in the other
twelve. Keeping them apart matters because an argument that slides from *cannot* to *may
not* is refutable at the first counterexample, and the repository has an instance of
exactly that error on record.

## The test a dimension must pass

A dimension earns its place only if some allocation decision flips when it is added —
some unit of work goes to a different faculty with it than without it. The test is owed
to the external pass, which used it to cut one dimension and add three. A dimension that
sounds complete and flips nothing is decoration.

## Provenance

Per [`../../AGENTS.md`](../../AGENTS.md) rule 8: the cells describing the second
faculty's behaviour are stated from general knowledge and are hypotheses until measured
on this project's own data. The cells describing human performance are weaker still —
practitioner observation, not literature. No cell here is evidence. `CON-OP-2` records
that the economics have no number, and this grid does not supply one; it states which
number would settle which cell.

The second faculty is referred to by that name because it has none. `CON-OP-10` holds
the question and is blocking.

---

## 1 — Instruction cost

**Deterministic.** A complete specification in a formal language, paid once per rule. The
defining property is not that instructions must be explicit but that *whatever is unstated
is not detected* — an incomplete specification is executed as written rather than refused.

**Second faculty.** Examples and context. Low per attempt and paid repeatedly, because
nothing persists between sessions. Under-specification produces a plausible completion
rather than an error, which is the deterministic failure wearing better clothes.

**Human.** A stated intent: cheap to utter, expensive to transfer, because the recipient
must already hold the background it assumes. The distinguishing property of this faculty
across the whole grid appears here — **it is the only one that interrogates an
underspecified instruction rather than executing it** — and the architecture cannot obtain
that behaviour from either other faculty.

## 2 — Marginal cost and latency

**Deterministic.** Effectively zero marginal cost; latency from microseconds to hours. The
cost is compute, which is procurable.

**Second faculty.** Small but non-zero per unit, seconds of latency. Unlike deterministic
execution, cost scales with volume rather than amortising against it.

**Human.** Expensive, minutes to weeks. The cost is *attention*, the scarce resource this
project is organised around and the only one of the three that cannot be bought at scale.

## 3 — Variance

**Deterministic.** Zero by construction — the definition rather than a feature.

**Second faculty.** Non-zero and irreducible. Bounded by sampling, never eliminated.

**Human.** Non-zero and *not random*: correlated with time of day, workload, recency, and
what the person believes the answer is supposed to be. Two humans also disagree, which is
`ARC-OP-3` and is a variance term the architecture currently treats as an edge case.

## 4 — Error character

Error **character** rather than error **rate** drives allocation, because character sets
verification cost.

**Deterministic.** Systematic, reproducible and total within scope: wrong every time and in
the same way, findable by a single test and invisible to sampling where no test exists. It
also proceeds confidently on well-formed input that violates its assumptions, having no
representation of its own scope.

**Second faculty.** Individually plausible, which is what makes it expensive — a wrong
answer is shaped like a right one — and, where the inference is mediated by a learned local
rule, **correlated while appearing independent**: one bad convention yielding four hundred
assertions wrong in the same direction. That is `ARC-OP-17`, it survived the review that
killed `CON-OP-11`, and it is the most dangerous cell in this grid because it defeats the
sampling that would otherwise price the others. Fluency at the boundary of competence is
why it is dangerous rather than merely annoying.

**Human.** Fatigue-shaped, clustering at the end of long repetitive runs, and *socially
shaped*: error follows incentive and politics, not only attention. An inconvenient number
is checked harder than a convenient one. Humans usually know when they are out of their
depth and frequently do not say so, because admitting it carries a political cost.

## 5 — Verification cost

**The project's economic argument lives in this row.**

**Deterministic.** Cheap where a test exists. The test is the specification restated, so it
costs roughly what the specification cost — verification does not scale down, because
somebody must still decide what correct means.

**Second faculty.** Cheap for structural claims, which are recomputable; expensive for
semantic ones, because checking a claim about meaning requires the knowledge that producing
it required. This is the whole bet: **the architecture is viable only where verifying costs
materially less than producing.** Where the two converge, the second faculty is an
expensive way to generate work for a human.

**Human.** Verified socially — by a second human, or by an outcome arriving much later.
Both are slow and the second is often too late to attribute.

## 6 — Consequence containment and reversibility

Added by external review. Verification cost prices the check; it does not price the loss
when the check is skipped or fails, and irreversible actions have losses asymmetric to
their verification cost.

The repository holds an adjacent treatment and this dimension is not wholly new to it.
[150_trust-and-blast-radius.md](../10_architecture/150_trust-and-blast-radius.md) governs
the blast radius of **reading** — contracts, legal basis, permitted operations, budgets.
What it does not cover is the irreversibility of **acting**, which is what flips an
allocation here. The two should probably be one treatment and currently are not.

**Deterministic.** Consequence is exactly the scope of what it was authorised to execute,
and is knowable in advance. Reversibility is a property of the design — the non-destructive
vault of [140_data-vault-automation.md](../10_architecture/140_data-vault-automation.md) is
precisely a decision to keep consequences containable.

**Second faculty.** Proposals are inherently contained; the consequence arrives only on
assertion or execution, which is why
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) draws the mandate line there
rather than at capability.

**Human.** The only faculty that can be held accountable after the fact, which is a
containment mechanism of a different kind and is part of why irreversible actions route
here.

*The flip:* drafting a proposed schema migration goes to the second faculty; approving an
irreversible production migration with destructive backfill goes to the human, even where
the second faculty's error would be cheap to verify.

## 7 — Context economics

**Deterministic.** No context; all state explicit in code and configuration. Simultaneously
its strongest property, because the state is auditable, and a real limitation, because
nothing implicit can be brought to bear.

**Second faculty.** Cheap to load, nothing retained. It starts cold every time, the
landscape must be re-supplied, and under pressure context degrades lossily rather than
announcing that it has. It does not natively distinguish, within that context, between what
was adjudicated and what it guessed — that distinction must be supplied by the
architecture, which is `ARC-OP-16`.

**Human.** Expensive to load, measured in years, durable once loaded, and retains what was
never written down. Decays slowly and **leaves entirely**: staff turnover is uncompensated
context loss, a cost this discipline absorbs without accounting for it.

## 8 — Signal access

**Deterministic.** Only what is in the data path.

**Second faculty.** Only what is rendered as tokens in its channel. It cannot attend the
meeting, read the room or notice the silence, and — the sharper limitation — cannot *seek*
signal outside the channel it was given, so absent evidence is indistinguishable to it from
absent phenomenon.

**Human.** The full sensorium, including political and unarticulated signal: the strongest
entry in this grid and the hardest to substitute. It carries the caveat established by
external review as `CON-OP-7(b)` — the knowledge may be held by nobody whole, existing only
as a negotiated synthesis across departments, in which case "ask the human" is an
idealisation and the real cost is elicitation.

## 9 — Negotiation and value-setting

Added by external review. Signal access says what inputs a faculty can receive; it does not
say whether the faculty can produce a *binding settlement* between parties with conflicting
legitimate interests.

**Deterministic.** None. It executes a settlement already reached.

**Second faculty.** Can surface the conflict, enumerate the positions and draft a candidate
reconciliation. It cannot bind anyone to one, and no amount of capability changes this,
because the barrier is standing rather than skill.

**Human.** The only faculty that can settle such a question, and specifically a human with
the authority to do so — which is not any human.

*The flip:* inferring a metric's likely meaning from documentation goes to the second
faculty; defining *net revenue* where Finance and Sales hold conflicting legitimate
interests goes to the human faculty. This dimension is the capability-side argument for
`CON-OP-14`'s candidate formulation that the human mandate includes elicitation and purpose
rather than adjudication alone.

## 10 — Inferential novelty and precedent

Added by external review. Instruction cost says what must be supplied; it does not say
whether the faculty can form a defensible interpretation where no precedent exists.

**Deterministic.** Requires the precedent to have been encoded already.

**Second faculty.** Strong where an adjudicated convention or a close analogue exists, and
this is where its throughput advantage is largest. Weak and confidently so where the
concept has no established analogue, because it will produce an interpretation shaped like
a precedented one.

**Human.** The only faculty that can defensibly interpret a genuinely novel concept, and
the one that pays the most for doing it.

*The flip:* mapping a source that follows an already-adjudicated vendor convention goes to
the second faculty or to deterministic machinery; interpreting a novel source whose
concepts have no analogue in the landscape goes to the human.

## 11 — Scaling behaviour

**Deterministic.** Scales with compute. Maintenance cost scales worse than linearly with
artifact count, which is what
[190_machine-authored-design-canon.md](../10_architecture/190_machine-authored-design-canon.md)
is built on and what `CON-OP-8`'s first thesis addresses.

**Second faculty.** Scales with money, and the consequence is the project's central
structural risk: **ten times the proposals is ten times the adjudication**, so scaling this
faculty scales the human bottleneck rather than relieving it. `ARC-OP-18` — stratify
adjudication by rule rather than sampling instances — is therefore not an optimisation but
a precondition for the architecture working at all.

**Human.** Does not scale. Adding people adds coordination cost and, past a threshold,
subtracts throughput.

## 12 — Drift under a changing world

**Deterministic.** Does not notice and does not stop, executing yesterday's specification
against today's world indefinitely.

**Second faculty.** Would notice if asked and shown the evidence, has no standing to act on
the observation, and does not remember having made it. Drift detection is available only as
a scheduled question, never a spontaneous one.

**Human.** Notices slowly and unevenly, and is the only faculty that revises its own
instructions in response.

## 13 — Mandate

Entitlement, not capability. Set by
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) and
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md).

**Deterministic.** Executes. Asserts nothing. Never the author of a claim.

**Second faculty.** Full autonomy on structural claims; propose-freely-assert-on-evidence on
semantic ones; machine-assisted only on teleological ones. Design claims are a fourth kind
the tiers do not classify, which is `ARC-OP-19`.

**Human.** Rules, and sets purpose. Whether the mandate also includes elicitation as a
first-class function is `CON-OP-14`, and dimension 9 is the capability-side argument that it
does.

---

## The allocation rule

The first draft of this document proposed *give a unit of work to the cheapest faculty
whose errors can be verified at acceptable cost*. External review found it wrong rather
than merely incomplete: it optimises production while treating verification as a
feasibility threshold, and so omits whether verification is mandatory, what it actually
costs, the chance it is skipped or fails, and the loss after an undetected error. An
irreversible action can satisfy that rule and still be irrational to allocate there.

The replacement, which is a candidate and not a ruling:

> Allocate each unit to the **entitled** faculty that minimises total expected lifecycle
> cost — instruction, execution, mandatory verification, remediation, and
> probability-weighted residual harm — **subject to explicit limits on irreversible
> downside.**

The explicit limit is not redundant with the probability-weighted term, because
probability-weighting disguises catastrophic outcomes behind uncertain small probabilities.
Retaining it is also what keeps the rule a decision rule rather than a counsel of caution:
low-consequence reversible work still goes to machinery rather than defaulting to a human.

**The objection to it is the reviewer's own and is not answered here.** The rule requires
probabilities and loss estimates that `CON-OP-2` says this project does not have. Its
present value is that it names which quantities would have to be estimated, which the
first version did not.

## What else falls out of the grid

**Error character dominates error rate**, because character sets verification cost and
verification cost is what allocation turns on. A faculty with a higher error rate and
cheaply detectable errors may be preferable to one with a lower rate and plausible ones.

**The correlated-error cell defeats the pricing of every other cell.** Sampling is how
verification cost would ordinarily be estimated, and `ARC-OP-17` says sampling misleads
exactly where the second faculty is most useful. Until `ARC-OP-18` exists, several cells
here cannot be priced even in principle.

**No faculty reliably announces that it is out of its depth**, and each fails to for a
different reason — deterministic machinery has no representation of its scope, the second
faculty is fluent at the boundary, and humans know but are penalised for saying. This was
drafted as a dimension and cut, because it flips no allocation: it applies to all three
equally. What survives is a requirement on the architecture rather than a property of a
faculty, and nothing in
[100_system-overview.md](../10_architecture/100_system-overview.md) currently provides it.
Recorded as `ARC-OP-21`.

**The interaction candidate failed.** This document first proposed that the deterministic
faculty's auditability is a precondition for verifying the second faculty's semantic
output, and that this was the interaction between `CON-OP-8`'s two theses that the §III
rewrite owes. External review refuted it: a materialised, queryable landscape does not
depend on *cheap machine* authorship, since conventional warehouses have supplied explicit
transformations, lineage and recomputation for decades, so the argument connects the second
thesis to materialisation in general rather than to the first thesis. Many semantic claims
are also validated against people or authoritative documentation rather than against data
at all, and auditability of machinery is not the same property as verifiability of an
interpretation.

What survives is narrower and conditional, and is not an interaction: *for semantic
hypotheses whose validation depends on recomputable structural evidence, cheaper authorship
and maintenance of evidence-producing artifacts may reduce validation cost or widen the
evidence economically available.* To become the interaction `CON-OP-8` requires, the
project would have to show that machine authorship changes the availability, coverage or
maintenance cost of validation evidence **relative to an otherwise equivalent
conventionally authored warehouse**. That is a stated and testable claim, and it is
recorded against `CON-OP-8` rather than asserted here.

## What this document does not do

It assigns no numbers, and `CON-OP-2` stays open. It does not settle `CON-OP-10`, though a
completed inventory is plausibly the instrument that would. It does not amend
[ADR-0005](../20_decisions/0005-three-autonomy-tiers.md) or
[ADR-0008](../20_decisions/0008-faculties-substrate-mandate.md), and nothing here should be
read as doing so.
