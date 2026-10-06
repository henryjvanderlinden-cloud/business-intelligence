# XREV 2026-10-06 — the test framework by root cause, and plausibility redrafted — sol

```yaml
object:        docs/10_architecture/162_test-framework.md (new) and the section "Plausibility — back-of-the-envelope
               sanity checks" in docs/10_architecture/160_evaluation-and-regression.md (redrafted), uncommitted in
               the working tree on 2026-10-06 (register row ARC-OP-31).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned.
assignment:    framed by the author's redefinition: plausibility checks are rough, soft sanity checks against gross
               errors, not a completeness or correctness guarantee, and must not be judged as one. Four determinate
               questions: is any root cause assigned as first line to a test that structurally cannot catch a gross
               instance of it; is there a common gross root cause no kind of test catches; would the checks fire so
               often on a normal business calendar that they are ignored; is anything over-engineered. 250 words;
               praise, assessment, summary and demands for exhaustive coverage forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted both texts the same day from the author's direction.
               Dispositions owed to the author.
verdict:       FAILS — a plausible wrong-tenant file can pass every described kind of test.
```

Sol's answer, verbatim:

1. The row **“Data quality at the source”** assigns data tests first. Those tests check structural or declared-domain invariants; they cannot generally detect valid-looking bad values. A source switching amounts from euros to cents makes every amount 100 times too large while keys, nullity, accepted values, referential integrity, freshness, and debit/credit balance can pass. Plausibility, not those data tests, catches the gross movement first.

2. A common uncovered cause is **wrong-file or wrong-partition routing**: tenant A’s extract is loaded into tenant B’s partition, with the expected schema, similar volume, and valid shared-domain keys. Unit and release tests see no code defect; data tests can pass; totals and layer ratios can look normal. A data test should own delivery identity: source, tenant, business date, partition, and manifest/control totals.

3. Yes. Previous-load, previous-weekday, and recent-trend comparisons will predictably warn on public holidays, month-end/quarter-end, and post-holiday rebounds. Merely widening bands enough to absorb those events weakens the check. The simplest remedy is one business-calendar-aware peer set: compare like weekday and like holiday/month-end status, and encode expected no-load days in the arrival schedule.

4. Having the agentic layer diagnose every soft warning before display is over-engineered. Initially, show the observed value, reference range, delta, and affected load; invoke diagnosis only when someone opens it.

VERDICT: FAILS + a plausible wrong-tenant file can pass every described kind of test

## Dispositions

Owed to the author. Recommended to him on 2026-10-06, as recorded in `ARC-OP-31`.
