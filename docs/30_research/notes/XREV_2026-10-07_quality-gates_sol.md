# XREV 2026-10-07 — quality gates — sol

```yaml
object:        register row ARC-OP-33 in registers/OPEN_POINTS.md (quality gates), as committed in c2adb83.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: a proportionate first framing of the gate question for a one-source sandbox and an author minimising his manual work, not a complete gate design. Four questions: an omitted gate point where a gross error passes; a contradiction with anything ruled; whether warn-only plausibility leaves a gross common failure published; over-engineering. 250 words; praise, summary, general assessment and demands for exhaustive coverage forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + a euros-to-cents shift warns while a 100× mart is published
```

Sol's answer, verbatim (characters the transport replaced with "?" are left as received):

1. The omitted point is semantic admission: an assertion becoming approved/certified, entering the catalogue, or becoming eligible to generate a mart. ADR-0011 requires an explicit catalogue publication pipeline; ARC-OP-33 names only change, load, artifact-publication and quarter-turn points. In WWI, an agent could assign revenue to `BillToCustomerID` rather than `CustomerID`. Both keys join, totals reconcile, volumes look normal, and deterministic gates pass, while users receive grossly wrong customer revenue.

2. “Deterministic and agent-independent” does not contradict ADR-0004, but is not entailed by it: ADR-0004 permits models to emit assertions and requires deterministic row execution. The stronger rule in 420 §5 is proposed, not ruled. “Plausibility warns” conflicts with ADR-0011’s rejection of “detection without consequence” and requirement that tests pass before publication, unless plausibility is explicitly a non-test signal outside that gate.

3. Yes. ARC-OP-31 and 162 themselves name a source switching from euros to cents: values remain valid-looking, structural data tests pass, and plausibility is the first line. A 100× total raises only a warning, so publication continues. This is gross, common, and needs a narrow escalation rule, not harder plausibility generally.

4. A catalogue is proportionate; separate commit, merge, deployment and quarter-turn gates plus override offices are not. One change gate, one load/publication gate, semantic admission, and the author as recorded exception authority suffice.

VERDICT: FAILS + a euros-to-cents shift warns while a 100× mart is published

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
