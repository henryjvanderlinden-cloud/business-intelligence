# XREV 2026-10-06 — plausibility testing on published outputs — sol

```yaml
object:        docs/10_architecture/160_evaluation-and-regression.md, section "Plausibility — does the output
               still make sense?", uncommitted in the working tree on 2026-10-06 (register row ARC-OP-31).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning
               effort medium, workspace-write sandbox, told to write its answer to the ignored scratch/ folder
               and modify nothing else. The call timed out at the device bridge (60 s) before replying; the
               answer was retrieved from the file. Thread id not returned.
assignment:    one question, adversarial ("judge as a practitioner who has run production data warehouses for
               finance and ERP data; assume the section will still let a real double count or other implausible
               number reach users, or will fire so often that it is ignored"): which concrete situations make it
               fail — an implausible output passing all seven check families, a broken new frozen set passing the
               two-step baseline procedure, a check design that drowns the author in false alarms; minimal
               counterexample and minimal fix for each. Ranked, 350 words; praise, assessment and summary
               forbidden. Declared out of scope: the section's "Not decided" list, unset thresholds, that nothing
               is built.
second reader: assignment set by Claude Opus 5.5, which drafted the section the same day from the author's
               request. Dispositions owed to the author.
verdict:       FAILS — a cross-system duplicate with new document IDs passes every check.
```

Sol's answer, verbatim:

1. **A duplicated business event can pass all seven families.** Minimal counterexample: during an ERP migration, one week's invoices arrive from both legacy and replacement systems, with new document IDs in the replacement. Rows are unique at the declared technical grain; both feeds reconcile to their source extracts; complete invoices preserve header/line and debit/credit conservation; every output uses the same facts; no partition is missing; the period is open; and a 3% uplift remains inside the historical band. Delivery-duplicate monitoring passes because identifiers differ. Users receive overstated revenue. **Minimal fix:** for every additive financial measure, require an independently sourced control total at business-population and period grain, plus a tested cross-source population-exclusivity assertion or canonical business-event identity. Reconciliation through the duplicated chain is not independent evidence.

2. **A broken frozen set can pass both baseline steps.** Minimal counterexample: the quarter copy contains facts through 30 June but dimensions extracted on 2 July. Facts reconcile, keys are unique, accounting totals conserve, outputs agree, and quarter movement looks credible. Frozen tests then evaluate June facts using future hierarchy assignments: the baseline never existed at one cut. **Minimal fix:** admission must verify every input's source version, high-water mark, effective cut, row count and checksum against the production run at the declared cut, then reproduce that run under identical code and assertion versions. Plausibility is not proof of baseline integrity.

3. **Domain equations treated as universally hard will stop routine loads.** Minimal counterexample: an invoice header includes tax, freight and rounding while lines contain net merchandise; legitimate late postings amend a finance-closed but not legally locked period. Both hard checks fail routinely, publication blocks, and operators learn to accept discrepancies mechanically. **Minimal fix:** scope hard checks to an adjudicated accounting state and an explicit equation containing reconciling components and tolerances. Expected late-posting classes need effective-dated exceptions, an owner and expiry; other rules remain soft until observed false-positive rates justify promotion.

VERDICT: FAILS + a cross-system duplicate with new document IDs passes every check

## Dispositions

Owed to the author. Recommended to him on 2026-10-06, as recorded in `ARC-OP-31`.
