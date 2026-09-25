# XREV 2026-09-25 — adjudication economy (155), organisational practice — sol

```yaml
object:        docs/10_architecture/155_adjudication-economy.md, first draft, at commit 383bff1.
reviewer:      gpt-5.6-sol, via the Codex MCP server on desktop-lv8udh0 (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, thread
               01a0d7f6-b2b4-7d01-8b9b-24a1bea4c602. Read the file itself.
assignment:    one question, adversarial ("assume it will fail in a real organisation"), ranked,
               300 words, praise, assessment and summary forbidden: judge it as a practitioner who
               has run BI teams. The same document went to astra in parallel on the model.
second reader: assignment set by Claude Opus 5.5, which drafted the object. The author accepted
               all findings except that seeded checks are kept — blinded and excluded from
               estimates, per astra — rather than removed; and he placed the lean start in
               implementation rather than in the framework (ADR-0012).
verdict:       FAILS in part — six findings; all integrated 2026-09-25, finding 5 in part.
```

Sol's answer, verbatim:

1. **Business-owner and steward behaviour.** Named owners will not reserve time, delegates will lack authority, contentious definitions will be deferred, and urgent delivery will bypass the queue. “Route to the person who knows” fails because knowledge and decision rights rarely coincide. **Minimal fix:** require an accountable decision owner, named delegate, response deadline, and explicit default on expiry; charge unresolved items to the sponsoring deliverable.

2. **Budgets and service classes.** A fixed minutes budget converts overload into ageing and parking, while “regulatory/consequential/routine” invites every sponsor to claim priority. Reallocation by humans recreates portfolio politics. **Minimal fix:** give each class objective entry criteria, maximum age, escalation path, and capacity owner; publish demand, capacity, and work displaced.

3. **The four lanes.** “Reversible,” “limited reach,” “monitored,” and “held up for a set period” are not operational tests. Provisional claims will leak into production through extracts, copied logic, and deadline exceptions. Parked claims will become invisible debt. **Minimal fix:** define enforceable promotion gates, expiry dates, dependency tracking, and automatic quarantine when provisional use exceeds scope.

4. **Monitoring workflows.** Weekly calibration and defect tracing assume clean lineage, stable claim identifiers, reliable defect reporting, and staff who classify root causes. Real teams have none consistently; the workflow will emit precise-looking nonsense. **Minimal fix:** begin with queue age, decision latency, audit failures, and manually reviewed escaped defects; add calibration only after traceability is demonstrated.

5. **Reviewer controls.** Seeded wrong proposals will be experienced as covert employee testing despite disclosure. Override rate is confounded by case difficulty, local policy, and reviewer style; per-reviewer data will become performance evidence regardless of stated purpose. **Minimal fix:** remove individual metrics and seeded traps initially; measure cohorts and rules, using double-review samples to estimate reviewer disagreement.

6. **Adjudication record.** The schema demands estimates and reasons on every candidate, making record completion itself the bottleneck; fields will be guessed or backfilled. **Minimal fix:** require only claim, owner, lane, rule, timestamps, decision, and reason; capture richer evidence only for audited or consequential cases.
