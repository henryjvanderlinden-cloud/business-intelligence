# XREV 2026-09-25 — the step log, as a test of the project's hypotheses — astra

```yaml
object:        docs/50_process/520_record-keeping.md at commit b4003c6 (ADR-0014; register row PRC-OP-6).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, reasoning effort medium,
               thread 01a0d9dc-2dc2-75d0-808f-40e8d2e9d951. Read 520 only; the three hypotheses were
               stated inline.
assignment:    adversarial ("assume the log cannot test these hypotheses"): for (a) allocation per the
               task table, (b) maintenance effort per stable unit with burden steady, and (c) human
               attention as the binding constraint, proxied by answers, words and activity size — can
               the test be computed from 520's fields; if not, the minimal addition. Then the minimal
               check against self-flattering classification by a recorder grading its own work.
               300 words; praise, assessment and summary forbidden. Declared out of scope: 520's
               admitted gaps. Practice went to sol in parallel.
second reader: assignment set by Claude Opus 5.5, which wrote the object; the three hypotheses as stated
               in the prompt are the drafter's paraphrase of 070, CON-OP-16 and 155. Dispositions by the author, below.
verdict:       FAILS — missing allocation baselines, maintenance denominators and burden rules, and a
               bottleneck test.
```

Astra's answer, verbatim:

1. **(a) Allocation: partly computable.** `task_row`, `role` and `actor` describe observed assignments, but do not identify the applicable version of the expected allocation. Nor does a task-row grouping distinguish separate task instances or expose omitted roles. Add `task_instance_id` and `allocation_version`, referencing a frozen table of expected faculties per role. Require each completed instance to account for every required role, with a step reference or explicit `missing`/`not_applicable` disposition. This makes deviations and omissions countable.

2. **(b) Maintenance: not computable.** Source acquisition status supplies no stable denominator of supported sources, governed products or dependencies. Add dated inventories with persistent component IDs and support status; fix reporting windows and denominator rules before comparison. Record backlog opening/closure dates, defect severity and fixed severity weights. Define numerical tolerances for “hold steady.” Add `rework_of_step_id` and a rule charging rework to the originating build or maintenance work; define overhead treatment. Compute maintenance effort per landscape unit separately for each effort measure, comparing successive source additions. Missing effort values must remain unknown, not become zero.

3. **(c) Scarce attention: proxy totals are partly computable; binding constraint is not.** Splitting one human message across steps can inflate answers and words. Add a unique `human_response_id`, require its verbatim text, and count each response once under a fixed word-count rule; count distinct real-world activities separately. These totals measure demand, not scarcity. Add task-level blocking-faculty and unblock-event references, plus completed-output counts. Predefine a comparison testing whether reducing required human interventions increases completions under comparable workload and machine capacity.

4. **Self-grading:** mechanically reconcile response IDs and action evidence with the transcript/tool trace. Independently classify a randomly selected sample against a frozen rubric, blinded to the recorder’s labels; retain disagreements and corrections.

VERDICT: FAILS + missing allocation baselines, maintenance denominators and burden rules, and a bottleneck test.

## Dispositions

The author, 2026-09-25, on the model's recommendation per finding: "I'll go with the recommendations."

1 accepted in part: `task_instance` and a frozen `allocation_version` now; role-by-role accounting at
instance close deferred to the first real instance. 2 deferred with a mechanical precondition: the asset
inventory starts with the first source, and `records/maintenance_baseline.json` — stable units,
denominator rules, window, burden weights, tolerances — must exist before a second source is acquired.
The rule that missing effort stays unknown is adopted now, unenforced. 3 accepted in part: one
`response_id` per message, words counted once, large acts counted apart; the bottleneck test is parked
as a post-mortem design question in `PRC-OP-6`. 4 accepted: a blind reclassification of a random sample
by a different model before a session is closed, in `audits.jsonl`, enforced by the checker. Integrated
into [520](../../50_process/520_record-keeping.md) and `tools/check_repo.py`.
