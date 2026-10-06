# XREV 2026-10-06 — plausibility testing, the amendment after review — sol

```yaml
object:        docs/10_architecture/160_evaluation-and-regression.md, section "Plausibility — does the output
               still make sense?", sub-part "Amended after review", at commit 2e11d12 (register row ARC-OP-31).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning
               effort medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call
               timed out at the device bridge (60 s); the answer was retrieved from the file. Thread id not
               returned. The same reviewer had failed the section before amendment.
assignment:    adversarial: for each of its own three earlier counterexamples, does the amended text now catch or
               prevent it, yes or no and why; and does the amendment open a new way for an implausible number to
               reach users or for alarms to drown the author — with attention to verified reports being periodic,
               not daily. Minimal counterexample and fix for each; 300 words; praise, assessment and summary
               forbidden. Out of scope: adoption by ADR, unset bandwidths, nothing built, the "Not decided" list.
second reader: assignment set by Claude Opus 5.5, which wrote the amendment from the author's rulings of 2026-10-06.
               One sentence of the amendment is the model's extension rather than the author's words: that every
               hard check's tolerance is a bandwidth "in line with the first change". Dispositions owed to the
               author.
verdict:       FAILS — a differently identified duplicate publishes daily before the periodic verified report
               exists.
```

Sol's answer, verbatim:

1. **Cross-system duplicate: NO.** An approved P&L or external report is periodic and arrives after daily publication. On 3 October, both ERPs deliver the same invoice under different IDs; the October report does not yet exist, so daily revenue reaches users. “Tested population exclusivity” cannot solve this without identity independent of those IDs. **Minimal fix:** during overlap, gate publication on canonical business-event identity or an independent control total at the publication grain; otherwise quarantine the feeds until the periodic control exists.

2. **Soft-first rules create a new publication hole.** A new debit-equals-credit rule is soft; a one-sided €1m journal publishes with a question although the invariant is known by construction. **Minimal fix:** calibrate on replay data before live use; let established source invariants start hard, and withhold their scope until calibration finishes.

3. **Frozen mixed cut: YES.** Per-input effective cuts and high-water marks checked against one reference date, then reproduction under identical versions, reject 30-June facts with a 2-July dimension extraction. The checksum requirement can instead create alarms: identical dimension rows exported in another order change a raw checksum. **Minimal fix:** use keyed, order-insensitive content hashes and source snapshot/as-of metadata, not raw-file bytes.

4. **Routine hard-check failures: YES, if configured as required.** Stating the accounting state, adding tax/freight/rounding, and dating the late-posting exception remove both counterexamples. But a “bandwidth” admits conservation errors: a €999 imbalance passes a €1,000 band. **Minimal fix:** separate rounding tolerances from control-total bandwidths; exact accounting identities get only a justified rounding quantum.

VERDICT: FAILS + a differently identified duplicate publishes daily before the periodic verified report exists

## Dispositions

Owed to the author. Recommended to him on 2026-10-06, as recorded in `ARC-OP-31`.
