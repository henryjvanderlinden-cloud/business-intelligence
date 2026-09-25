# XREV 2026-09-25 — the maintenance baseline, as a test of the claim — astra

```yaml
object:        records/maintenance_baseline.json at commit 1d3396e (register row CON-OP-16), ruled
               provisionally by the author at S06-052.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, reasoning effort medium,
               thread 01a0da0a-399e-7aa3-952e-f60ccadf1dd9. Read the file only; the claim and the
               sandbox were described inline.
assignment:    adversarial ("assume the decision rules cannot discriminate a maintainable landscape from
               an unmaintainable one at this scale"), three determinate questions: whether comparing
               later epochs with epoch two per source tests burden growing faster than the landscape;
               what heterogeneous sources do to a per-source denominator; whether the hard-fail rule is a
               valid collapse signal or a step-counting artefact. Minimal repair for each. 300 words;
               praise, assessment and summary forbidden. Practice went to sol in parallel.
second reader: assignment set by Claude Opus 5.5, which drafted the object; the claim as stated in the
               prompt is the drafter's paraphrase of CON-OP-16 and the Generative Structures mapping.
               Dispositions by the author, below.
verdict:       UNDETERMINED — owed comparable maintenance exposures, composition-adjusted workload, and
               evidence of sustained capacity failure.
```

Astra's answer, verbatim:

1. No. The epoch-two comparison tests a bounded departure from one reference value, not whether maintenance grows faster than landscape size. A rising ratio can remain inside +10%; an initial jump followed by flat costs can fail it. Minimally restate the claim as: “Across comparable maintenance windows, maintenance effort grows no faster than maintained workload, while burden remains steady.” Assess successive effort-to-workload ratios; retain the epoch-two threshold only as a separate acceptance rule. Normalize maintenance opportunities, and count the stock actually maintained: the newly acquired source contributes to the denominator before undergoing subsequent upkeep.

2. A per-source denominator treats an annual register and a large, frequently changing feed as equivalent units. Adding cheap sources can dilute expensive upkeep; adding demanding sources can raise the ratio without worsening maintainability. Source order therefore confounds scaling with composition. Minimally record effort by source against predetermined workload descriptors—maintained volume, refreshes, and changes processed—and compare matched maintenance exposures within sources. Report shared maintenance separately. Any aggregate needs fixed workload weights; source count alone cannot identify the claimed relationship.

3. The hard-fail rule is not a valid collapse signal. Splitting maintenance into more steps, batching build work, or simply reducing construction can trigger it without increased maintenance demand. Rising burden warrants investigation but does not make the step-count crossover causal evidence. Minimally remove its automatic failure status. Require persistent burden deterioration alongside maintenance demand exceeding a predefined resource budget under comparable service obligations, using consistently measured effort independent of step fragmentation. Treat the existing conjunction as a diagnostic trigger.

VERDICT: UNDETERMINED + owed comparable maintenance exposures, composition-adjusted workload, and evidence of sustained capacity failure; the stipulated decision rules cannot establish maintainability or collapse.

## Dispositions

The author, 2026-09-25: "let's not make it too serious yet, we're still putting our feelers out. No budget
in 8. I'll go with 1-7." 1 accepted: the test restated as effort growing no faster than workload, the +10%
kept as a separate acceptance check. 2 accepted: workload descriptors per source and refresh. 3 accepted:
the hard-fail rule demoted to a trigger for investigation; the budget astra's repair requires was declined
by the author for now. Integrated into `records/maintenance_baseline.json`.
