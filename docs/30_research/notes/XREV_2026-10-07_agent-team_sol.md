# XREV 2026-10-07 — an agent team for the first build — sol

```yaml
object:        register row ARC-OP-34 in registers/OPEN_POINTS.md (an agent team for the first build), as committed in c2adb83.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: a proportionate first proposal for building the next sandbox's warehouse for an author minimising his manual work and wanting a small apparatus, not a complete multi-agent architecture. Three questions: collisions with anything ruled or defined (070's lead, the faculty names); an uncovered multi-role failure mode that lands on the author; the condition under which a single agent with the same playbooks is strictly better, and whether it holds. 250 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + a shared false grain assumption passes every internally derived gate and reaches the author
```

Sol's answer, verbatim (characters the transport replaced with "?" are left as received):

1. The fixed “lead” collides with 070: *lead* is whoever decides each task, commonly H, not a standing agent. “The lead decides” also exceeds ADR-0008: the agentic layer proposes; humans rule. “Tester … runs the gates” conflicts with 070 rows 22–24 and ARC-OP-33: A writes tests, D runs checks, H judges business reality. Minimal fix: rename the role *coordinator*, follow 070’s chain, and have the tester design/review tests while D runs gates. This preserves ADR-0010’s agent/unit-of-work distinction.

2. A source analyst misclassifies an order-line identifier as an order business key. The modeller creates a hub at line grain; the engineer implements it; the tester derives expectations from that profile. Every gate passes because code, tests and hand-offs share one false premise. “Evidence first” cannot settle evidence framed by that error; another model is independent only with independent evidence. The author discovers the error during business-reality review and must adjudicate downstream rework. Nothing requires adversarial re-derivation upstream.

3. One agent is strictly better when work is serial, role-agents share model and playbooks, and separation adds hand-off cost without independent evidence or fewer defects. The production chain meets that condition: one simulated source and a source→model→load→mart dependency leave little parallel work. It does not cover genuinely independent testing on another model; retain that as an external-review job, not a standing five-role team. ADR-0014 can test whether even that review repays its overhead.

VERDICT: FAILS + a shared false grain assumption passes every internally derived gate and reaches the author

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
