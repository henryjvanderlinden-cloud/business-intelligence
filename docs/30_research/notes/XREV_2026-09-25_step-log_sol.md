# XREV 2026-09-25 — the step log, as a basis for a build post-mortem — sol

```yaml
object:        docs/50_process/520_record-keeping.md and records/vocabulary.json at commit b4003c6
               (ADR-0014; register row PRC-OP-6).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, reasoning effort medium,
               thread 01a0d9db-9eb6-7123-b5cf-09089667bdd5. Read the two files only.
assignment:    one question, adversarial ("judge as a practitioner who has run BI teams and done project
               post-mortems; assume this step log will fail to support an honest post-mortem of a BI
               sandbox build"): which fields or rules will be misapplied, gamed or inconsistently applied
               by a model logging its own work; which distinctions are missing; which fields are dead
               weight; minimal fix for each. Ranked, 300 words; praise, assessment and summary forbidden.
               Declared out of scope: the admitted gaps in 520 (author's time by ruling, tokens,
               off-conversation work, reconstruction). The hypotheses went to astra in parallel.
second reader: assignment set by Claude Opus 5.5, which wrote the object. Dispositions by the author, below.
verdict:       FAILS — self-certified outcomes, unstable grain, and absent data-asset and validation
               lineage.
```

Sol's answer, verbatim:

1. `outcome=done` lets the producing model certify success. Split `completion_status` from `validation_status`; require `check_step`, acceptance criteria, and evidence before `validated`.

2. `role` is gameable: choices made while “executing” can escape `decide`. Rule: selecting among alternatives, defaults, mappings, thresholds, or exclusions is always a decision; require `decision_basis` and `decision_id`.

3. Step boundaries are subjective, making counts incomparable. Rule: one step has one observable state change or one validation result; require a parent `activity_id` for related steps and mechanically reject multi-output steps.

4. `work_class` conflates expected iteration with avoidable correction. Add `work_reason`: `first-pass`, `expected-iteration`, `defect-correction`, `scope-change`. Require every `rework` step to reference a defect; permit `introduced_by=unknown`.

5. Defects lack business consequence. Add `severity`, `affected_asset`, `detected_stage`, and `escaped_stage`; require closure evidence, not merely `fixed_by`.

6. A BI build cannot be reconstructed from generic inputs and outputs. Add `asset_id`, `asset_kind` (`source`, `table`, `model`, `report`, `control`), `environment`, `run_id`, and `data_as_of`. Mechanically require them for acquisition through analysis.

7. Checks do not record what was tested. Add `check_type` (`schema`, `row-count`, `reconciliation`, `freshness`, `uniqueness`, `referential`, `business-rule`, `visual`), expected result, observed result, and evidence reference.

8. `task_type` mixes activity and subject: modelling, documentation, review, and communication can describe the same step. Replace it with orthogonal `activity_type` and `subject_type`; prohibit catch-all communication when another activity applies.

9. `initiated_by` permits only one cause and hides dependencies. Replace it with `triggered_by[]`, `depends_on[]`, and `blocks[]`; check for resolved references and dependency cycles.

10. `human_size` is dead weight because activity determines it mechanically. Derive it. `instruments` also duplicates tool-call keys and executable `agent` entries; use one controlled `tool` vocabulary.

VERDICT: FAILS — self-certified outcomes, unstable grain, and absent data-asset and validation lineage prevent an honest build post-mortem.

## Dispositions

The author, 2026-09-25, on the model's recommendation per finding: "I'll go with the recommendations."

1 accepted: `outcome` is completion only; `validation` by a check step of a different agent. 2 accepted:
choosing is deciding, with `decision_basis`; hidden decisions are tested by the blind audit, since they
cannot be checked mechanically. 3 accepted as a grain rule and a `task_instance`; multi-output steps are not
mechanically rejected. 4 accepted: rework carries `rework_of` and `work_reason`. 5 accepted in part:
`severity` and `detected_stage` now; escaped stage deferred. 6 and 7 deferred to the first acquired
source, which arrived the same evening, so integrated then: `assets.jsonl` and `check` details. 8 declined
for now: the 070 row carries the subject. 9 parked. 10 declined: `size` is the author's term and the
checker enforces its mapping. Integrated into
[520](../../50_process/520_record-keeping.md) and `tools/check_repo.py`.
