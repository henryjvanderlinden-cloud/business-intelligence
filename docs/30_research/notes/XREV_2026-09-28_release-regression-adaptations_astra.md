# XREV 2026-09-28 — release regression on frozen data, the nsdn adaptations — astra

```yaml
object:        docs/10_architecture/160_evaluation-and-regression.md, section "Release regression — frozen
               data, moving code", sub-part "What nsdn would add", at commit 11011a7 (register row
               ARC-OP-30), read with the rest of the section, Level 3 of 160, ADR-0004 and ARC-OP-13.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), reasoning effort medium. A first attempt with a read-only sandbox
               timed out at the device bridge (60 s) with no answer returned; the second ran with
               workspace-write, was told to write its answer to the ignored scratch/ folder and modify
               nothing else, and the answer was retrieved from that file. Thread id not returned.
assignment:    one question, adversarial ("assume both adaptations are wrong: that context changes as a
               second attribution source open a channel through which regressions get explained away, and
               that the agent-run loop removes the independence that made the original method work"): does
               each preserve the guarantee that every output difference is either intended or caught; if
               not, minimal counterexample and minimal restoring condition. Ranked, 300 words; praise,
               assessment and summary forbidden. Declared out of scope: the items the section lists under
               "Not decided", and weaknesses of the base method (sent to sol in parallel).
second reader: assignment set by Claude Opus 5.5, which proposed both adaptations; they are unruled by the
               author. Dispositions owed to the author.
verdict:       FAILS — a shared attribution error hides an unintended change to a second customer; a valid
               definition change hides an unintended extra exclusion.
```

Astra's answer, verbatim:

1. **(b) A different agent does not establish independent validation.** A release note authorises a £10 increase for customer A only. The implementation also increases customer B by £10. The matcher wrongly includes B; the reviewing agent accepts the attribution using the same mistaken customer mapping as the author. No residue reaches the human. This defeats the proposed replacement for the tester: the second agent's identity provides no protection against a shared erroneous premise. ADR-0004 makes execution reproducible; it does not make attribution correct.

   **Minimum repair:** require an independently established acceptance criterion and validate every attributed difference against it, including exclusions, using the actual before/after outputs. The reviewer must check the matcher's accepted set, not merely endorse its explanation. Where that validation cannot establish conformance, the difference must remain residue for independent adjudication. A second model or agent alone is insufficient; the quarterly plausibility check cannot recover a silently accepted daily regression.

2. **(a) Context provenance is not an intended-impact specification.** An adjudicated definition changes revenue to exclude tax. A faulty implementation also excludes shipping. The resulting revenue decrease is attributed to the logged definition change, whose authority and timing are genuine, although the shipping exclusion was unintended. A legitimate cause of some movement has explained away excess movement.

   **Minimum repair:** context changes must meet the same prospective intended-impact requirements as code changes. Attribution must establish that the observed difference conforms to that authorised impact, not merely that a relevant context event occurred. Pin both snapshots to their actual context versions so later adjudications cannot retrospectively authorise the difference. Joint code/context effects must satisfy the combined authorised expectation or remain residue; resolving ARC-OP-13's temporal representation is unnecessary for this requirement.

VERDICT: FAILS + shared attribution error hides customer B's change; a valid tax-definition change hides unintended shipping exclusion.

## Dispositions

The author, 2026-09-29, on the recommendations recorded in `ARC-OP-30`, numbered as put to him in the conversation:
"4. yes 5. yes"

1 accepted (his 4): the reviewing agent validates each attributed difference against the stated expectation and the
actual outputs, not the change author's explanation; what it cannot confirm stays residue for a person. 2 accepted
(his 5): a context change carries the same executable expectation as a code release, and each snapshot records the
context version it ran with. Integrated into [160](../../10_architecture/160_evaluation-and-regression.md) under
*Amended after review*. The adaptations themselves remain unadopted until an ADR adopts the method.
