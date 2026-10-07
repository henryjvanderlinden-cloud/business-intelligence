# XREV 2026-10-07 — the machinery without the agentic layer — sol

```yaml
object:        the paragraph "Added 2026-10-07: noticing must not depend on the agentic layer" in section 5 of docs/40_roadmap/420_next-sandbox-setup.md, as committed in c2adb83.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: a proportionate principle for the next sandbox as 420 describes it, aimed at minimising the author's manual work, not a production monitoring design. Three questions: a common failure where with no agent running no alert is raised or reaches the author; consistency of queued runtime agent work with ADR-0004; whether the escalation timer costs the author more than it saves. 250 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + a stopped Windows scheduler produces neither checks nor alerts, while timeout escalation turns expected offline periods into author work.
```

Sol's answer, verbatim (characters the transport replaced with "?" are left as received):

1. Yes. Windows Task Scheduler advances and exports; the paragraph names no independent check runner. If the PC remains asleep, the task is disabled, credentials expire, or Task Scheduler fails, neither load nor checks execute. Machinery that did not start creates no alert file or message. “On the schedule” does not watch the scheduler. The minimal fix is an external dead-man check: each successful job sends a heartbeat, and an independent service alerts after a long missed-heartbeat window. Otherwise exclude host/runner failure from the claim.

2. It is consistent if queued agent work means diagnosis, reporting, or artifact generation. ADR-0004 says models “emit code, configuration, assertions and prose” while “deterministic engines execute.” Model-based row processing must instead be an “explicit, versioned, separately evaluated enrichment step,” materialised and contracted as a source, under its own ADR. Queueing changes timing, not that boundary. If queued work produces rows, 420 cannot bypass this contract.

3. Yes. This private simulation has no downstream users or production SLA, and 420 already makes missed starts catch up. Escalation makes the author tune a timeout, receive alerts during ordinary offline periods, and perform the Windows-side repair section 5 assigns him. It saves work only where delay before the next agent run matters; 420 names no such case. Omit escalation here, or limit it to repeated misses after the host returns.

VERDICT: FAILS + a stopped Windows scheduler produces neither checks nor alerts, while timeout escalation turns expected offline periods into author work.

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
