# XREV 2026-09-25 — overview for discussion (080), updated main points — sol

```yaml
object:        docs/00_concept/080_overview-for-discussion.md, section "Updated main points and the
               schematic", the twelve points only, at commit a930af0.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153 in
               C:\Tools\codex-0153), sandbox read-only, thread
               01a0d8c3-4f20-7bc1-97de-5db42c48efb8. Read the file itself, no other files.
assignment:    one question, adversarial ("assume the points will mislead an experienced BI
               practitioner hearing them cold"): misreadings, overclaims against "nothing is
               built", contradictions, hidden caveats, load-bearing omissions; ranked, with minimal
               wording fixes, 300 words; praise, assessment and summary forbidden. Declared out of
               scope: density, and the items already listed as open. The schematic went to astra
               in parallel.
second reader: assignment set by Claude Opus 5.5, which drafted the object. Dispositions pending
               the author's reaction.
verdict:       FAILS — nine findings; the overview owes applicability boundaries, autonomy
               exclusions and a replaceable architecture profile.
```

Sol's answer, verbatim:

1. **Points 6/11:** A mandatory Data Vault architecture contradicts the claim of a generic framework. Minimal fix: call it one reference profile, with replaceable modelling patterns.

2. **Points 3/8:** “Humans rule on meaning” conflicts with auto-accept and unattended defaults. Minimal fix: humans define delegable policy and retain accountability; only specified decisions require direct human approval.

3. **Point 5:** “Every task” following one chain falsely implies uniform workflow and human decision-making. Minimal fix: “Governed changes use these roles, with stages automated or omitted according to policy.”

4. **Point 10:** Reversibility and detection do not substitute for review when harm is irreversible, externally visible, or detected late. Minimal fix: restrict substitution to bounded-blast-radius actions with proven detection and rollback times.

5. **Point 8:** “Prevents the most damage per minute” presents an unknowable prioritisation score as operational fact, while deadlines and defaults can silently authorise harm. Minimal fix: describe a risk-based heuristic and require explicitly bounded, fail-safe defaults.

6. **Point 7:** “Every claim” and “one set” overstate achievable coverage and conceal identifier lifecycle, conflicting sources, lineage, and derived-data access leakage. Minimal fix: scope assertions and identifiers, and require authorisation through retrieval, derivation, and publication.

7. **Points 1/4/6–8:** Present-tense architectural claims will be heard as demonstrated capabilities despite the final disclaimer. Minimal fix: introduce all twelve as “proposed design hypotheses”; use “would” throughout.

8. **Point 9:** Unnamed value areas make “separate” unverifiable and leave listeners unable to tell what outcomes the machinery serves. Minimal fix: name the current areas in the point while retaining that the set is extensible.

9. **Point 11:** “Every implementation grows into it” makes the full design inevitable rather than optional and evidence-driven. Minimal fix: implementations adopt only validated components needed for their context.

**FAILS — the overview owes explicit applicability boundaries, autonomy exclusions, and a replaceable architecture profile.**

## Dispositions

Pending the author's reaction.
