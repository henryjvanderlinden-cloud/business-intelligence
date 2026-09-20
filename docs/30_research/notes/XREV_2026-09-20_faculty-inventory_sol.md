# XREV 2026-09-20 — faculty inventory (060) — sol

```yaml
object:        docs/00_concept/060_faculty-inventory.md, first draft, uncommitted.
               At commit 28f00aa.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0, cwd
               C:\Git\business-intelligence, sandbox read-only, thread
               01a0bed4-6a24-7443-8585-c10f4c137241
assignment:    three chained determinate questions, adversarial framing, general
               assessment explicitly forbidden, 300-350 words per answer. Out of scope:
               prose, structure, the project's merit.
second reader: assignment set by Claude Opus 5, which drafted the object in the same
               session. Q3 named the attack it expected to be fatal, which steers the
               finding and is unreviewed by construction in the strongest form yet
               recorded. Q2 supplied its own counterexample from Q1's answer.
verdict:       FAILS on all three — one dimension cut, three added, the allocation rule
               replaced, and the proposed interaction between CON-OP-8's two theses
               refuted.
```

Third external pass; partly discharges `PRC-OP-1`. The falsifiable core remains
unreviewed.

## Transport note

The first attempt exceeded the device bridge's sixty-second ceiling because the opening
prompt asked the reviewer to read the object plus four apparatus documents. It was
re-issued with the apparatus stated inline and the reading reduced to the single object,
which fit. **The lesson generalises and is worth carrying:** supplying the apparatus, per
[510_external-review.md](../../50_process/510_external-review.md), does not require the
reviewer to *read* the apparatus. Summarising it in the prompt is cheaper and keeps the
pass inside the transport budget.

## A deviation from "a review note is not an edit", stated rather than taken quietly

[510_external-review.md](../../50_process/510_external-review.md) holds that a note's
dispositions become register rows and that documents change later, deliberately. Here the
object was a draft written in the same session and never committed, and the pass was
commissioned as part of drafting it rather than as a review of settled material. The
findings were therefore folded into the draft before its first commit, and this note
holds what the draft said beforehand so that nothing is lost by the fold. No committed
document was rewritten on the strength of a review note.

## Q1 — are these the right dimensions?

The test supplied: a dimension earns its place only if some allocation decision flips
when it is added.

> **VERDICT: MISSING [consequence containment and reversibility; negotiation or
> value-setting; inferential novelty] / REDUNDANT [behaviour at the edge of competence]**
>
> **Consequence containment and reversibility.** Drafting a proposed schema migration may
> go to the second faculty; approving an irreversible production migration with
> destructive backfill goes to the human faculty. Verification cost alone misses the
> asymmetric loss from a false approval.
>
> **Need for negotiation or value-setting.** Inferring a metric's likely meaning from
> documentation may go to the second faculty; defining "net revenue" where Finance and
> Sales have conflicting legitimate interests goes to the human faculty. Signal access
> identifies the inputs but not the faculty's ability to negotiate a binding settlement.
>
> **Inferential novelty / precedent availability.** Mapping another source that follows an
> adjudicated vendor convention may go to deterministic machinery or the second faculty;
> interpreting a novel source whose concepts have no established analogue goes to the
> human faculty.
>
> **Dimension 8, behaviour at the edge of competence, fails the stated test as written.**
> Its own conclusion is that none of the faculties can reliably perform out-of-depth
> detection and that this must be an architectural function. It therefore does not
> reallocate a work unit among faculties.

**Disposition.** All four accepted. The three additions are now dimensions 6, 9 and 10 and
each carries its flip case in the document, because a dimension that cannot state its flip
has not passed the test it was admitted under.

The cut is the sharper finding and it lands on the draft's own reasoning. The draft
flagged out-of-depth behaviour as "the finding this document would most want reviewed" and
then stated a conclusion — no faculty self-reports, so detection must be architectural —
that applies to all three faculties equally and therefore moves no work between them. It
was a requirement wearing a dimension's clothes. Its faculty-specific content is merged
into error character and verification cost; the requirement is promoted to `ARC-OP-21`,
which is the only row this pass opened.

Noted against the first addition and not conceded to it: the repository already holds
[150_trust-and-blast-radius.md](../../10_architecture/150_trust-and-blast-radius.md),
which governs the blast radius of reading. It does not govern the irreversibility of
acting, which is what flips the allocation, so the dimension stands — but it is adjacent
to existing material rather than absent from the repository, and the two treatments should
probably be one. Recorded in the document rather than as a new row.

## Q2 — is the allocation rule wrong, incomplete, or vacuous?

> **VERDICT: (a) + the replacement requires probabilities and loss estimates that
> CON-OP-2 says the project does not yet possess**
>
> Replacement: *Allocate each unit to the entitled faculty that minimizes total expected
> lifecycle cost — instruction, execution, mandatory verification, remediation, and
> probability-weighted residual harm — subject to explicit limits on irreversible
> downside.*
>
> "Cheapest faculty" optimizes production while treating verification as a feasibility
> threshold. That omits whether verification is mandatory, its actual cost, the chance it
> fails or is skipped, and the loss after an undetected error. An irreversible action can
> therefore satisfy the original rule while remaining economically irrational to allocate
> there.
>
> The explicit downside limit is necessary because probability-weighted cost alone can
> disguise catastrophic outcomes behind uncertain small probabilities. It also preserves a
> real decision rule: low-consequence, reversible work can still go to deterministic
> machinery or the second faculty rather than defaulting to a human.

**Disposition.** Accepted, with the reviewer's self-objection carried into the document
unanswered. The replacement is not obviously better than the original in any way the
project can currently act on — it names five quantities where the first named two, and
`CON-OP-2` says none of them has a number. What it buys is that the quantities are now
named, which converts an unfalsifiable rule into an unmeasured one. That is a real but
modest gain and the document says so.

The structural point worth keeping is that the first rule failed for the same reason
`CON-OP-11` failed: it collapsed a multi-term expected-value calculation onto a single
convenient axis, this time verifiability instead of domain size. That is twice in two days,
by the same drafter, and it is the pattern this repository should watch for.

## Q3 — does the proposed interaction between the two theses survive?

The draft proposed that deterministic auditability is a precondition for verifying
semantic output, and that this discharges `CON-OP-8`'s obligation to demonstrate an
interaction. The question named attack 3 as the one expected to be fatal.

> **VERDICT: FAILS + attack 3**
>
> A materialised, queryable landscape may support validation, but its existence does not
> depend on cheap machine authorship. Conventional warehouses already provide explicit
> transformations, lineage, recomputation, and queryable evidence. The argument therefore
> connects T2 to materialisation generally, not specifically to T1.
>
> Attack 1 also defeats the claim that materialisation is a universal precondition. Many
> semantic claims — business definitions, intended policy, ownership, acceptable
> interpretation — are validated against people or authoritative source documentation.
>
> Attack 2 identifies a further equivocation. Deterministic auditability answers "what
> transformation ran, on which inputs, under which rules?" Semantic verifiability asks
> "does this interpretation correctly represent the relevant concept?" The former can
> supply evidence for the latter, but it neither entails nor guarantees it.
>
> The narrowest surviving proposition is only conditional: *for semantic hypotheses whose
> validation depends on recomputable structural evidence, cheaper authorship and
> maintenance of deterministic evidence-producing artifacts may reduce validation cost or
> broaden the evidence economically available.* [...] To connect it to T1, the project
> would need to show that machine authorship changes the availability, coverage, or
> maintenance cost of validation evidence relative to an otherwise equivalent
> conventionally authored warehouse.

**Disposition.** Accepted in full, and this is the most useful result of the pass because
it converts an obligation into a test. `CON-OP-8` said the §III rewrite owes either an
interaction argument or an admission that there is none. The first candidate is now
refuted, with the reason named: it links the second thesis to materialisation, which the
discipline has had for decades, rather than to the first thesis.

The surviving conditional is recorded against `CON-OP-8` as the thing that would have to be
shown, stated as a comparison against an otherwise equivalent conventionally authored
warehouse. That comparison is concrete enough to run once the canon survey (`ARC-OP-14`)
exists, which is a second reason that survey has been promoted.

Against the pass, and it is not small: the question named attack 3 as expected to be fatal
and the reviewer agreed with it. A reviewer told which attack is decisive is a weaker
instrument than one that finds it, and the agreement should be discounted accordingly. The
independent value is in the narrow surviving form and the test, which were not supplied by
the question.

## What this pass did not do

It did not examine dimensions 1 to 5 or 11 to 13 cell by cell; only the dimension set, the
rule and the interaction candidate were tested, so an individual cell being wrong would not
have been caught. It did not price anything, and `CON-OP-2` is untouched. It did not review
the falsifiable core, which
[510_external-review.md](../../50_process/510_external-review.md) still ranks first and
which three passes have now stepped around.
