# XREV 2026-09-25 — the maintenance baseline, in practice — sol

```yaml
object:        records/maintenance_baseline.json at commit 1d3396e (register row CON-OP-16), ruled
               provisionally by the author at S06-052.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, reasoning effort medium,
               thread 01a0da09-b15c-7790-ba8d-9bbf7badf462. Read the file only; the sandbox and the
               classification were described inline.
assignment:    one question, adversarial ("judge as a practitioner who has run BI teams; assume this
               baseline will yield a misleading verdict"): how the recording agent's classification, the
               epoch definition, the refresh rule, or the choice of stable units distort the result,
               towards a false pass or a false fail; the minimal mechanical fix for each. Ranked, 300
               words; praise, assessment and summary forbidden. Declared out of scope: the file's stated
               limits. The decision rules went to astra in parallel.
second reader: assignment set by Claude Opus 5.5, which drafted the object. Dispositions pending the author.
verdict:       FAILS — endogenous epochs, incomplete refresh exposure, and non-auditable attribution can
               manufacture flat maintenance per source.
```

Sol's answer, verbatim:

1. **False pass — self-classification.** The builder-recorder can classify integration failures, schema adaptations, and repairs to existing assets as `build` or `explore`, especially when bundled with onboarding a new source. The counterfactual is not mechanically testable, and later `rework_of` links can rewrite attribution. **Fix:** require `trigger`, `assets_touched`, and immutable `initial_work_class`; automatically classify any work triggered by refresh/check failure or modifying a pre-epoch supported asset as `maintain`. Reject mixed steps unless split.

2. **False pass — refresh exposure.** Refreshing once per source-acquisition epoch ignores releases occurring within long epochs. Daily OSM/GLEIF obligations therefore cost no more than annual PAR, while calendar days are merely reported. Growth pace controls measured maintenance. **Fix:** generate `refresh_due` events from cadence and timestamps; require one outcome per due event. Count missed events as failed service commitments and divide effort by due refresh cycles as well as sources.

3. **False pass or fail — acquisition-bounded epochs.** Work before the acquisition timestamp is charged to the smaller preceding landscape; work after it to the larger one. Delaying or advancing acquisition moves the numerator between denominators. The open final epoch also permits partial-cycle comparisons. **Fix:** use fixed-duration epochs, or assign work by `stock_served`; compare only closed epochs after every due refresh and check has completed.

4. **Usually false pass — stable units.** A source counts equally regardless of cadence, checks, transformations, dependency surface, or whether it has completed a full service cycle. Thin sources inflate the denominator; counting dependency edges would additionally reward coupling. **Fix:** define an eligible unit as a supported source that has passed a fixed acceptance suite and one complete refresh cycle; freeze that unit manifest per epoch. Treat dependencies only as burden, never denominator.

VERDICT: FAILS + endogenous epochs, incomplete refresh exposure, and non-auditable attribution can manufacture flat maintenance per source.

## Dispositions

Pending the author.
