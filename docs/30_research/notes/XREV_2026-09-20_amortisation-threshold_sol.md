# XREV 2026-09-20 — CON-OP-11 (the amortisation threshold) — sol

```yaml
object:        registers/OPEN_POINTS.md `CON-OP-11`, chained to `CON-OP-8` and
               `CON-OP-4`, with docs/10_architecture/190_machine-authored-design-canon.md
               and XREV_2026-09-19_manifesto-statability_sol.md as apparatus.
               At commit 6a19361.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, cwd
               C:\Git\business-intelligence, sandbox read-only, thread
               01a0bdb6-329b-78b0-93ba-3f9bc8e0c9a6
assignment:    three chained determinate questions, adversarial framing, general
               assessment explicitly forbidden, each answer capped at 350 words and
               required to end in a verdict line. Out of scope: prose, structure, the
               rest of the repository, whether the project is a good idea.
second reader: assignment set by Claude Opus 5 — the same model that drafted
               `CON-OP-11`, `CON-OP-8`'s session-02 narrowing and `CON-OP-4`'s
               session-02 state. The question selection is unreviewed by construction.
               Q2 and Q3 went further than asking: they supplied the internal
               inconsistency between `CON-OP-11` and `CON-OP-4`(ii), and supplied the
               candidate prior-art list the reviewer then ruled on. Both are the
               assignment-setter's material and are unreviewed in exactly the sense
               `PRC-OP-1` exists to record.
verdict:       FAILS + Anchor-style 6NF — a discipline-wide domain the canon did not
               adopt — with (ii) of `CON-OP-4` failing on the same pass.
```

This is the second external review pass on this repository and discharges the second
pass assigned under `PRC-OP-1`. It reviews the rows session 02 produced, which is the
comfortable choice that row already flags; the falsifiable core remains unreviewed.

## Transport note

The chained discipline from the first pass was used deliberately rather than discovered
under duress: one question per turn in a single thread, each answer word-capped to hold
it inside the device bridge's ceiling. No reviewer output was lost. A harness failure
dropped the first tool call before it reached the bridge, and the pass was issued again
from the top; the reviewer saw one clean sequence of three prompts.

## Q1 — does domain size do any work that "inference got cheaper" does not?

> **VERDICT: FAILS + discipline-wide 6NF remained largely unadopted, while tiny
> high-frequency regulatory mappings are routinely authored**
>
> "Domain size" is not the operative variable. It is, at most, one multiplier in an
> expected-value calculation: expected reuse × value per correct application ×
> stability/confidence − discovery, validation, execution, and maintenance costs.
>
> Cardinality alone predicts neither authorship nor adoption. A convention spanning 400
> archival columns may remain uncodified because those columns are rarely queried, will
> soon be retired, vary in undocumented ways, or cannot justify validation. Conversely, a
> rule covering two status codes may be carefully authored because it executes on every
> transaction, drives regulatory reporting, and is stable. Large domain, no rule; tiny
> domain, rule.
>
> The repository supplies its own stronger counterexample. Anchor-style 6NF has a
> discipline-wide domain, yet §190 says it is "almost unused" because of object count and
> join complexity. Its domain could not be broader; adoption still depends on authoring,
> runtime, and comprehensibility costs. Machine authorship changes one cost term, not a
> domain-size threshold.
>
> Nor does domain size establish that canon cost and semantic inference are one claim. In
> the canon case, the generalisation is already known and the reduced cost concerns
> generating and maintaining deterministic machinery. In the semantic case, the rule must
> first be inferred from noisy local evidence, and validation may dominate generation.

**Disposition.** Accepted, and it lands on the row's own terms. `CON-OP-11` asserts that
the 400-column convention went unwritten "not because it is unstatable, but because
discovering, stating, testing and maintaining it never repaid a human at that domain
size." The reviewer concedes the second clause and denies that domain size is what
explains it: repayment is an expected-value quantity in which extension is one multiplier
among several, and the row promoted one benefit proxy into the governing axis.

The 6NF counterexample is the sharpest part of the finding because it is drawn from the
repository's own apparatus rather than from outside it.
[190_machine-authored-design-canon.md](../../10_architecture/190_machine-authored-design-canon.md)
§3 records Anchor modelling as near-unused on object-count and join-complexity grounds.
That is a maximal domain with no adoption, and it is fatal to a threshold stated in
domain size alone, whichever way the wider argument goes.

What survives is narrower and was already available: machine authorship lowers one cost
term. Restating that as a collapsed threshold on a size axis adds a mechanism the
evidence does not carry. To rescue the axis the row would have to show that, holding
frequency of use, stakes, stability, confidence and elicitation cost roughly constant,
adoption varies systematically with extension size. Nothing in the repository does that,
and `EVI-OP-5` as currently scoped does not measure it either.

The unification half falls with it, and on the ground `CON-OP-8` had already stated
against itself before the narrowing waved it away. Narrowed into `CON-OP-11`; the
dependents opened from it — `ARC-OP-16`, `ARC-OP-17` and `ARC-OP-18` — are not
automatically void, because each was argued from locally-general rules existing, not from
domain size being the axis that explains them. They need re-deriving, not withdrawing.

## Q2 — with the narrowing removed, which spine?

> **VERDICT: (c) + without a demonstrated interaction, the manifesto risks becoming a
> bundle of two adjacent technology claims rather than one explanatory thesis**
>
> Neither can serve honestly as evidence for the other. Canon examples such as
> bitemporality and exhaustive lineage demonstrate cheaper implementation, not improved
> semantic discovery. Schema interpretation demonstrates improved hypothesis generation,
> not that elaborate physical designs have become operationally affordable.
>
> Choosing (a) would make the manifesto sturdier only by amputating the premise on which
> much of the architecture depends [...] Choosing (b) would subordinate the
> better-supported claim to one already damaged by the articulability/generalisation
> objections and would misdescribe known-design automation as evidence about knowledge.
>
> The opening claim therefore becomes: **data infrastructure is changing under two
> concurrent shifts: machines can economically author and maintain deterministic designs
> that humans previously rejected as too costly, and models can propose local semantic
> interpretations that previously required unaffordable human investigation; humans remain
> responsible for validating and authorising both.**
>
> The manifesto loses a single causal mechanism [...] It must establish two capability
> changes, two cost curves, and two distinct failure regimes. Their conjunction may be
> historically important, but it is not conceptually necessary: either could occur without
> the other.

**Disposition.** Accepted as the reading the §III rewrite should carry, with one caveat
recorded below. The either/or `CON-OP-8` poses comes back live once the unification is
denied, and the reviewer answers it by refusing both single-spine options for reasons
that are not symmetrical and should not be compressed. Demoting semantic inference would
cost the architecture its premise; subordinating the canon argument would hitch the
better-supported claim to the one the first pass already damaged.

The caveat is that the reviewer's own closing objection is the live risk and is not
answered by adopting (c). Two adjacent capability claims with no demonstrated interaction
are a weaker object than one thesis, and the manifesto currently has no account of an
interaction. There may be one — the canon designs whose authoring cost collapsed are
disproportionately the ones that carry semantic annotation, and a landscape whose
deterministic machinery is cheap to regenerate is a landscape where a revised semantic
assertion is cheap to propagate — but that is an argument this repository has not made
and must not assume it can make. Stated as an obligation on the rewrite in `CON-OP-8`.

Note what (c) costs procedurally rather than rhetorically. `CON-OP-8`'s attraction was
that the canon argument "yields a research programme that can be executed without any
code." Under (c) that remains true of one thesis and false of the other, so the two
halves of the manifesto will not be evidenced at the same rate, and the repository should
expect the canon half to firm up while the semantic half waits on `EVI-OP-1`.

## Q3 — does the generality-not-articulability distinction hold, and is it novel?

> **VERDICT: (ii) FAILS + Boisot's independent codification/abstraction axes + the named
> primary readings and within-/cross-landscape holdout test are owed**
>
> A learner need not discover a universal rule mapping every column name to its meaning.
> It may learn either a landscape-local regularity or a general inference function that
> maps contextual evidence to probabilistic semantic hypotheses. Rejecting "domain size"
> as the governing economic axis does not deny that local regularities exist; it denies
> that their extension size explains codification. Where no object-level rule exists, the
> machine is still performing learned, fallible inference — not executing an unstated
> deterministic rule.
>
> (i) is defensible only as a non-novel and non-universal distinction. Boisot is the
> closest match: the I-Space separates codification from abstraction, allowing knowledge
> to be highly codified yet concrete and context-bound. That substantially anticipates
> "articulable but not general." Hayek supplies the adjacent account of dispersed
> knowledge of particular circumstances of time and place, though he does not consistently
> establish that such knowledge is readily articulable. Cowan, David, and Foray explain
> why potentially codifiable knowledge remains uncodified when constructing and
> maintaining the codebook does not repay its cost. Nonaka and Takeuchi are less exact
> [...]
>
> Accordingly, the manifesto cannot claim the distinction itself as its contribution. At
> most, its contribution becomes the architectural mandate policy.

**Disposition.** Accepted on both halves, and the first half matters more than the second.

(ii) fails without depending on Q1's result, which is worth stating plainly because the
two findings could otherwise look like one finding counted twice. The first pass already
established that there is a general and learnable rule about how to infer what a column
like *KLANTNR* means; `CON-OP-11` conceded that and rebuilt the claim on domain size;
this pass denies the axis and (ii) is left with no support from either direction. The
manifesto's residual formulation — "there is no rule to learn" — is now false as stated
whichever way `CON-OP-11` is resolved, and §III must say what the second faculty is
actually doing instead. The reviewer's formulation is usable: learned, fallible inference
from contextual evidence to probabilistic semantic hypotheses, which is a claim about
performance and calibration rather than about kinds of knowledge, and which is a
considerably more modest thing to assert.

Boisot is the significant external finding and the repository had not named him. If the
I-Space's separation of codification from abstraction anticipates articulable-but-not-
general, then the distinction §III leans on is prior art of roughly thirty years'
standing and the contribution reduces to the mandate policy — which `CON-OP-4` had
already conceded might be enough, and which
[ADR-0008](../../20_decisions/0008-faculties-substrate-mandate.md) has since made
load-bearing. Per [`../../../AGENTS.md`](../../../AGENTS.md) rule 8 this characterisation
of Boisot is the reviewer's, stated from general knowledge, and is a hypothesis until
somebody reads *Knowledge Assets*. It is recorded in `CON-OP-4` as such and not treated
as settled.

The holdout test the reviewer names — held-out columns within a landscape and held-out
landscapes, against a context-only baseline — is close to `EVI-OP-5`'s within-landscape
transfer measurement but is not the same instrument, and the difference is the useful
part. `EVI-OP-5` asks whether precision improves along the ingestion order; this asks
whether examples improve inference over a baseline that sees context alone. The second
discriminates learnable local regularity from case-by-case guessing, which is the thing
actually in dispute. Folded into `EVI-OP-5` as a second arm.

## What this pass did not do

It did not review `CON-OP-12`, `ARC-OP-17`, `ARC-OP-19` or `CON-OP-14`, all of which
`PRC-OP-1` named as part of this pass's object and all of which remain unreviewed. It did
not verify any of the prior art it names, including Boisot, which is now the most
consequential unverified claim in the repository because a disposition rests on it. It
did not examine the falsifiable core — that business keys are machine-proposable at
adjudication-worthy precision — which
[510_external-review.md](../../50_process/510_external-review.md) still ranks first and
which two passes have now stepped around. `PRC-OP-1` stays open.

No document was edited on the strength of this note, per
[510_external-review.md](../../50_process/510_external-review.md) §Discipline. No register
row was opened; every disposition narrowed a row that already existed.
