# XREV 2026-09-25 — the maintenance share as a success measure, organisational practice — sol

```yaml
object:        docs/30_research/notes/2026-09-25-generative-structures-mapping.md, §3, the proposal
               that the maintenance share is a success measure (register row CON-OP-16), at commit
               f432d62.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, thread 01a0d91e-eeb2-7bb2-ba98-d186e303159d.
               Read the note itself, no other files.
assignment:    one question, adversarial ("judge as a practitioner who has run BI teams: assume the
               maintenance share will fail as a measure in a real organisation"): gaming,
               misclassification, confounding; which break it outright and which need a guard; the
               minimal guard or companion measure for each. Ranked, 300 words; praise, assessment and
               summary forbidden. Declared out of scope: analogy status and the items CON-OP-16
               already lists as owed. The note went to astra in parallel on the model.
second reader: assignment set by Claude Opus 5.5, which wrote the object. Dispositions pending the
               author's reaction.
verdict:       FAILS — eight findings, four of them outright.
```

Sol's answer, verbatim:

1. **Outright — denominator gaming.** Sponsors classify migrations, rewrites, platform upgrades, and regulatory remediation as “new capability,” suppressing maintenance share without reducing burden. **Guard:** classify by counterfactual: would the work be required merely to preserve existing service? Independently audit a sample of tickets.

2. **Outright — rebuild reset.** Replacing a deteriorated warehouse becomes a new programme; its effort disappears from maintenance while accumulated burden is cosmetically reset. **Guard:** charge replacement effort and dual-running to lifecycle maintenance unless the rebuild delivers independently valued capabilities; report cumulative cost across predecessor systems.

3. **Outright — deferred maintenance.** Teams can improve the measure by tolerating fragility, extending incident queues, suppressing upgrades, and accepting manual workarounds. An unchanged observed defect rate does not capture exposure. **Guard:** pair the share with maintenance backlog age, unsupported-component count, control exceptions, recovery-test results, and estimated remediation effort.

4. **Outright — displaced effort.** Maintenance moves to analysts, source teams, vendors, or business users and vanishes from team logs. **Guard:** measure end-to-end effort by landscape, including shadow spreadsheets, reconciliations, vendor support, and upstream/downstream remediation.

5. **Guard needed — defect-rate denominator gaming.** Rapid growth can keep defects per asset flat while total incidents, user harm, and outage minutes rise materially. **Guard:** report absolute defects plus severity-weighted impact, downtime, data-correction volume, and affected users alongside normalized rates.

6. **Guard needed — agent-minute inflation or irrelevance.** Cheap, parallel agents may consume vast minutes while human bottlenecks shrink; alternatively, faster models make the share fall without architectural improvement. **Guard:** report human attention separately, monetary compute cost, elapsed recovery time, and agent retries/tool calls; never collapse them into one effort total.

7. **Guard needed — sponsor and portfolio selection.** Budget cuts raise the share by stopping builds; expansion funding lowers it by flooding the denominator with projects. Neither reflects maintainability. **Guard:** compare fixed-capacity cohorts and report maintenance effort per stable unit of stock as a companion trend.

8. **Guard needed — output fragmentation.** Teams can manufacture many trivial “capabilities,” making landscape growth look large. **Guard:** measure stock with stable operational units—supported sources, governed products, dependencies, users, and service commitments—not release or ticket counts.

**VERDICT: FAILS without lifecycle attribution, boundary-wide effort capture, latent-risk measures, and separate human, compute, impact, and stock-normalized trends.**

## Dispositions

Pending the author's reaction.
