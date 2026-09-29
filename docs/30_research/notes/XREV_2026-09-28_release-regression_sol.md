# XREV 2026-09-28 — release regression on frozen data, the base method — sol

```yaml
object:        docs/10_architecture/160_evaluation-and-regression.md, section "Release regression — frozen
               data, moving code", at commit 11011a7 (register row ARC-OP-30), excluding its sub-part
               "What nsdn would add".
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), reasoning effort medium. A first attempt with a read-only sandbox
               timed out at the device bridge (60 s) with no answer returned; the second ran with
               workspace-write, was told to write its answer to the ignored scratch/ folder and modify
               nothing else, and the answer was retrieved from that file. Thread id not returned.
assignment:    one question, adversarial ("judge as a practitioner who has run regression testing on data
               warehouses and BI marts; assume the method, as written, will let real regressions through
               or will drown the tester in unattributable noise"): which concrete situations make it fail —
               a regression passing as attributed, a correct change flagged, a diff too large to attribute;
               minimal counterexample and minimal fix for each. Ranked, 300 words; praise, assessment and
               summary forbidden. Declared out of scope: the items the section lists under "Not decided",
               the nsdn adaptations (sent to astra in parallel), and that a frozen set cannot see new data.
second reader: assignment set by Claude Opus 5.5, which wrote the section from the author's description of
               his employer's practice. Dispositions owed to the author.
verdict:       FAILS — an unintended duplicate inside a declared impact footprint can pass as attributed.
```

Sol's answer, verbatim:

1. **Regression passes as attributed.** Minimal counterexample: a release note says a VAT change raises `net_revenue` for German rows by roughly 2%. The change correctly raises most such rows but a faulty join also duplicates one German invoice; the object, row population, direction and aggregate size all fit the note. Because the developer checks intended consequences and the tester checks “everything else,” the duplicate can disappear inside the attributed footprint. Minimal fix: attribution must not equal acceptance. For every declared footprint, require executable expected deltas or invariants (for example, unchanged invoice cardinality and an exact row-level formula), and have the tester check them independently.

2. **Diff too large or ambiguous to attribute.** Minimal counterexample: during one day, release A changes revenue eligibility and release B changes the exchange rate used by eligible rows. The combined delta is non-additive: neither note predicts the snapshot produced by both, so cells cannot be assigned uniquely, while reverting either changes the apparent impact of the other. Minimal fix: snapshot and diff each releasable change in a defined order before combining them; where changes cannot be isolated, require one joint expected-impact specification covering the interaction.

3. **Correct change is flagged as regression.** Minimal counterexample: correcting one customer’s segment in a conformed dimension legitimately changes that row plus every downstream mart, subtotal and percentage using the segment. A note that precisely states the root correction still leaves the transitive consequences unattributed; manually listing every derived cell is brittle and omissions look like regressions. Minimal fix: distinguish root impacts from mechanically derived impacts. Expand the declared footprint through versioned lineage, recompute the expected downstream closure, and flag only deltas outside it or deltas that violate reconciliation invariants.

VERDICT: FAILS + an unintended duplicate inside a declared impact footprint can pass as attributed.

## Dispositions

The author, 2026-09-29, on the recommendations recorded in `ARC-OP-30`: "1. agree, expected impact is usually in
the release notes (which entitities / tables etc) 2. maybe that is workable if CI/CD is properly implemented, and a
regression test can be run after every integration. For humans this is unworkable, but for an agentic layer this
might be an option. Maybe put this remark in, also. 3. okay"

1 accepted: the expected impact is stated as computable expected differences plus invariants that must not move,
checked by someone other than the change's author against the actual outputs. 2 accepted with his qualification:
snapshot after each change in a fixed order, or one joint expectation — workable only with proper CI/CD and a
regression run per integration, unworkable for people, possibly an option for an agentic layer. 3 accepted: a note
declares the root change and its downstream closure is derived through versioned column-level lineage. Integrated
into [160](../../10_architecture/160_evaluation-and-regression.md) under *Amended after review*.
