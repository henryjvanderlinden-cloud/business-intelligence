# XREV 2026-10-07 — the machinery without the agentic layer — astra

```yaml
object:        the paragraph "Added 2026-10-07: noticing must not depend on the agentic layer" in section 5 of docs/40_roadmap/420_next-sandbox-setup.md, as committed in c2adb83.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: a proportionate principle for the next sandbox as 420 describes it, aimed at minimising the author's manual work, not a production monitoring design. Three questions: a common failure where with no agent running no alert is raised or reaches the author; consistency of queued runtime agent work with ADR-0004; whether the escalation timer costs the author more than it saves. 250 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + Windows remains asleep past the escalation deadline, leaving local checks and notification unable to run.
```

Astra's answer, verbatim (characters the transport replaced with "?" are left as received; relative links re-based from scratch/ to this folder):

1. Yes. [420 §§3–5](../../40_roadmap/420_next-sandbox-setup.md) names Windows Task Scheduler for export but Claude for checks. If Claude never runs, deterministic check code alone changes nothing. Moving checks to Windows still leaves an ordinary counterexample: the computer stays asleep beyond the escalation deadline; neither checks nor local notification run. No watcher is specified. Minimal sandbox fix: schedule checks and escalation independently of Claude and export success, and explicitly allow catch-up notification after waking. If notification during machine downtime is required, one external missed-heartbeat notifier is needed. A repository file alone does not deliver an alert to the author.

2. Consistent for diagnosis, repair proposals and other work outside row processing. [ADR-0004, Decision](../../20_decisions/0004-models-out-of-the-data-path.md#decision) says “Deterministic engines execute”; model row processing requires a separate ADR and versioned, evaluated, materialised, attributed outputs treated as a source under its own contract. Queueing does not waive that contract: a load requiring enrichment cannot silently pretend that source arrived. Unaffected loads can continue. [162](../../10_architecture/162_test-framework.md) also explicitly makes plausibility warnings nonblocking.

3. Not inherently, but elapsed time alone can generate avoidable work: an expected overnight shutdown followed by successful catch-up could still escalate a stale alert. Recheck before notifying, coalesce repeats, and treat “dealt with” as resolved or explicitly dispositioned, not merely picked up. Under route A, agents cannot repair Windows faults anyway; waiting merely delays the author's unavoidable act. No evidence establishes that the timer's upkeep outweighs filtered interruptions.

VERDICT: FAILS + Windows remains asleep past the escalation deadline, leaving local checks and notification unable to run.

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
