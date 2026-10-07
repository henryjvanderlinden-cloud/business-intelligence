# XREV 2026-10-07 — quality gates — astra

```yaml
object:        register row ARC-OP-33 in registers/OPEN_POINTS.md (quality gates), as committed in c2adb83.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: a proportionate first framing of the gate question for a one-source sandbox and an author minimising his manual work, not a complete gate design. Four questions: an omitted gate point where a gross error passes; a contradiction with anything ruled; whether warn-only plausibility leaves a gross common failure published; over-engineering. 250 words; praise, summary, general assessment and demands for exhaustive coverage forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       HOLDS UNDER [warnings are an accepted residual risk, existing hard blockers remain hard, and passing gates is not sufficient evidence of safe unattended work]
```

Astra's answer, verbatim (characters the transport replaced with "?" are left as received; relative links re-based from scratch/ to this folder):

1. No omitted lifecycle point demonstrated: “each load” and “publication” cover the relevant boundaries. A failed check ignored at publication would be an enforcement failure at a listed point.

2. No necessary contradiction. [ADR-0011](../../20_decisions/0011-assertions-identity-plane-publication-gate.md) covers temporal checks as well as joins; the catalogue must preserve those blockers. [ARC-OP-31](../../../registers/OPEN_POINTS.md#arc-op-31--plausibility-as-back-of-the-envelope-checks-and-the-test-framework-by-root-cause) explicitly makes plausibility soft. Deterministic execution must not erase ARC-OP-30’s accepted independent review and human disposition of unresolved residue. Also, “already settled” overstates the provenance: [420 §5](../../40_roadmap/420_next-sandbox-setup.md#5-what-happens-when-it-breaks) labels agent-independent availability proposed, not ruled; ADR-0004 settles deterministic execution, not every gate’s availability policy.

3. Yes. Suppose a simulated source delivery switches monetary values to cents while consumers still interpret them as currency units. Keys, dates, delivery identity and counts remain valid; consistently scaled monetary components still reconcile. Frozen-data regression sees no code change, and no verified report need exist. Revenue publishes at 100 times its proper value with only a plausibility warning. [162](../../10_architecture/162_test-framework.md) explicitly identifies this failure class. This exposes the accepted warning-only tradeoff, rather than an omitted gate point; equal gates cannot alone justify the row’s claim of safe unattended agent work.

4. No inherent excess in a short catalogue. One author can be the override authority throughout; separate approval machinery per gate would exceed this sandbox’s needs.

VERDICT: HOLDS UNDER [warnings are an accepted residual risk, existing hard blockers remain hard, and passing gates is not sufficient evidence of safe unattended work]

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
