# XREV 2026-10-06 — conformance of context cards to the Open Knowledge Format — astra

```yaml
object:        registers/OPEN_POINTS.md row ARC-OP-32 and the OKF entry in docs/00_concept/050_prior-art.md, both
               uncommitted in the working tree on 2026-10-06, against 120_context-layer.md and ADR-0011.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning
               effort medium, workspace-write sandbox, told to write its answer to the ignored scratch/ folder
               and modify nothing else. Thread 01a1105c-a166-7852-b780-e5154587ae99. The assignment pointed to a
               copy of the OKF v0.2 specification in scratch/ "if present"; it was not present, so the reviewer
               relied on the row's account of OKF, which is why its verdict asks for the normative constraints.
assignment:    adversarial ("assume the proposal is wrong: that adopting OKF field names while keeping URN
               identity and per-assertion trust as extensions would break conformance, mislead an OKF consumer
               about trust, or damage the nsdn design"): does it hold; if not, the concrete counterexample and the
               minimal repair; and is any claimed correspondence between OKF and 120 false. Ranked, 300 words;
               praise, assessment and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the row and the entry the same day. The model's
               account of OKF v0.2 is its own reading of okf/SPEC.md at commit 85a2be8 and is unreviewed.
               Dispositions owed to the author.
verdict:       UNDETERMINED — normative OKF constraints and an explicit trust, type, identity and publication
               projection are owed.
```

Astra's answer, verbatim:

1. **Trust mapping needs a projection rule.** Consider `metrics/net-revenue.md`: its intended definition is human-approved, but its assertion that the warehouse implements that definition is merely proposed. Copying the definition's adjudication into card-level `verified` would let an OKF consumer present the whole concept as human-reviewed, including the implementation claim. Per-assertion extensions do not repair that interpretation for consumers that ignore them. Minimal repair: omit `verified` on mixed-review cards, or publish a projection containing only claims covered by the recorded verification. Adjudication of a scoped assertion is not verification of an entire concept. This counterexample defeats that mapping, not every possible OKF projection.

2. **“The same design” contradicts ADR-0011.** The cited “cards in git” passage no longer defines the canonical record: assertions do; cards are generated views, and assertion storage remains undecided. Making an OKF bundle the authoritative knowledge store would undo that decision. Minimal repair: propose OKF as an access-filtered, publication-gated projection, preserving canonical assertion identity and lifecycle separately.

3. **Identity and `type` correspondence are unproved.** A URN extension can coexist with path identity; it cannot make an ordinary OKF consumer recognise a moved file as the same concept. Preserve bundle paths or supply an explicit translation contract. The row does not establish whether OKF permits nsdn's card-kind values for `type`; shared field names establish neither vocabulary compatibility nor semantics. Retain `kind` separately until that mapping is checked.

4. **Attested Computation is not ADR-0004.** On the row's account, it prohibits agent authorship of the computation. ADR-0004 explicitly permits models to emit code and requires deterministic execution. Deterministic checking does not erase this difference; use the attested type only for computations meeting its stronger restriction.

VERDICT: UNDETERMINED + normative OKF constraints and an explicit trust, type, identity and publication projection are owed

## Dispositions

The author, 2026-10-06, on the four recommendations recorded in `ARC-OP-32`, numbered 4 to 7 there:

> 4. okay.
> 5. okay.
> 6. let's keep it the way we designed it, you have convinced me it is superior.
> 7. okay.

Accepted 4, 5 and 7. On 6 he kept nsdn's design: URN identity and card kinds unchanged, any OKF projection adapts to them. Recorded in `ARC-OP-32`; no design document changed.
