# XREV 2026-09-19 — manifesto §III (statability) — sol

```yaml
object:        docs/00_concept/005_manifesto.md, section III, with sections I, II, IV
               and VII as apparatus. At commit 9ac2f3e.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, cwd
               C:\Git\business-intelligence, sandbox read-only, thread
               01a0b9fd-c6db-7573-bb9b-cfbe3031ee0d
assignment:    three determinate questions, adversarial framing, general assessment
               explicitly forbidden. Out of scope: prose, structure, the rest of the
               repository, whether the project is a good idea.
second reader: assignment set by Claude Opus 5 — the same model that drafted the object.
               The question selection is therefore unreviewed by construction and may
               have steered the pass away from defects it did not think to ask about.
verdict:       FAILS on all three questions.
```

This is the first external review pass on this repository. It partially discharges
`PRC-OP-1`.

## Transport note

The first attempt sent the whole assignment in one prompt and exceeded the device
bridge's sixty-second ceiling, orphaning the session. The pass was re-run as a chained
thread — one question per turn, word-capped — which is precisely the discipline
[510_external-review.md](../../50_process/510_external-review.md) §"One object per pass"
inherited from the compendium. The convention predicted its own transport constraint and
was ignored on the first try.

## Q1 — are the three conditions necessary and jointly sufficient?

> **VERDICT: FAILS + effective-dated reference data and unavailable historical facts**
>
> Stability is not individually necessary. Warehouses successfully encode changing tax
> rates, organisational hierarchies, customer classifications, and code meanings through
> effective-dated reference tables and Type 2 dimensions. The fact changes; deterministic
> execution remains correct because transaction time selects the applicable version. Nor
> are the three conditions jointly sufficient. "Attribute each sale to the customer's
> principal place of business at transaction time" is articulable, general, and stable,
> yet cannot execute correctly when historical location was never captured. A fourth
> condition is OBSERVABILITY: every fact required to evaluate the rule must be available,
> identifiable, and sufficiently reliable at execution time. The existing three
> characterize the proposition; observability connects it to usable evidence.

**Disposition.** Both halves are accepted. The necessity half exposes a level confusion
in the object: §III does not distinguish the stability of the *fact* from the stability
of the *rule*, and Type 2 dimensions are precisely the discipline's general rule for
absorbing unstable facts. What actually resists encoding is change that is itself
*ungoverned* — unheralded, with no general form — which is a generality failure about
the change process rather than a third condition. Opened as `CON-OP-5`.

The sufficiency half is a genuine omission and not merely a repair. Observability also
connects directly to the original brief's bullet on data gaps and to the enrichment
phase, neither of which §III accounts for. Opened as `CON-OP-6`.

## Q2 — do data semantics fail generality rather than articulability?

> **VERDICT (a): FAILS** — expert entity resolution and anomaly recognition are central,
> genuinely inarticulable competencies.
> **VERDICT (b): COLLAPSES OPERATIONALLY** — distributed, elicited knowledge is
> functionally tacit even if its eventual conclusion is sayable.
>
> [...] The manifesto equivocates between articulating a conclusion — "these records are
> the same customer" — and articulating the knowledge that warrants or produces it. The
> former is easy; the latter may remain tacit.
>
> The distinction weakens further when semantics emerge only through prolonged
> elicitation across operations, finance, legal, and system owners. No participant
> possesses the whole proposition [...] If articulability means merely that a conclusion
> can eventually be written, nearly every judgement qualifies. If it means that
> knowledgeable people can state what they know without reconstruction, much warehouse
> knowledge fails it. The boundary therefore becomes a gradient of elicitation and
> reconstruction cost, not a categorical separation capable of locating the third
> component exactly.

**Disposition.** The equivocation is real and is the sharpest finding of the pass. §III
argues from the sayability of a *conclusion* and then claims a property of the
*knowledge*. The steward who knows two records are the same customer can state the
conclusion and frequently cannot state the cue-weighting that produced it — which is
Polanyi's condition, in the middle of the case §III uses to escape Polanyi.

The distributed-elicitation half also lands, and it damages more than the definition. §VII
argues that adjudication is viable *because* someone can always state the particular once
asked. If the proposition is held by nobody whole and exists only as a negotiated
synthesis across four departments, there is no single adjudicator to ask, and the
architecture's adjudication mechanism is weaker than
[170_human-interfaces.md](../../10_architecture/170_human-interfaces.md) assumes.
`ARC-OP-3` — disagreement between adjudicators — moves from a detail to a load-bearing
component. Opened as `CON-OP-7`, sub-items (a) and (b).

Not conceded: the counterexamples are *recognition* competencies, and the pass does not
establish what share of warehouse-building work they constitute. §III concedes
inarticulable recognition exists and calls the residue small; the pass asserts it is
central without evidence. That disagreement is recorded in `CON-OP-7(a)` and is
empirically settleable.

## Q3 — can learning from examples address a generality failure?

> **VERDICT: FAILS AS STATED** — learning can generalise over how to infer particulars
> without learning a universal rule for each particular.
>
> [...] The learned general rule is not "KLANTNR always means legal entity"; it is "given
> evidence shaped like this, infer the most likely local meaning." Particular outputs
> therefore do not imply absence of a general inference function.
>
> "Situated inference" is not yet shown to be distinct from pattern learning over a
> context window. Both map observed context to a proposition using regularities learned
> across prior examples. A real distinction would require a different mechanism or
> empirical signature, not merely a different level of description.

**Disposition.** Accepted. §III's argument against Autor conflates the object level with
the meta level: there is no general rule about *KLANTNR*, but there is a perfectly
general and learnable rule about *how to infer what a column like KLANTNR means*, and
schema-matching research has been learning exactly that for two decades. The claimed
distinction from Autor 2014 does not survive at the level of mechanism.

What may survive is empirical rather than conceptual, and it is weaker: cross-organisation
schema matching has existed for twenty years without dissolving this problem in practice,
which suggests the general inference function was correct in principle and inadequate in
performance until recently. That is a claim about capability thresholds, not about kinds,
and it is a considerably more modest thing to assert. Folded into `CON-OP-4`.

## Weakest link, as named by the reviewer

> **WEAKEST LINK:** The three-condition necessity-and-sufficiency claim; test one
> effective-dated business mapping on unseen records spanning rule changes to determine
> whether unstable knowledge can execute deterministically.

## What this pass did not do

It did not examine sections IV, V, VI, VIII or IX; the architecture documents; or the
falsifiable core (machine-proposable business keys), which
[510_external-review.md](../../50_process/510_external-review.md) ranks first and which
remains unreviewed. `PRC-OP-1` stays open.
