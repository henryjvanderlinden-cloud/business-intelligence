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
second reader: assignment set by Claude Opus 5.5, which drafted the object. The author accepted
               every finding except the sixth, ruled the first in ADR-0013, and accepted the fourth
               in the narrower form proposed below.
verdict:       FAILS — nine findings; eight integrated 2026-09-25, one rejected.
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

Integrated into [080](../../00_concept/080_overview-for-discussion.md) and its schematic on
2026-09-25, after the author's reaction.

1. **Accepted, ruled.** The author: Data Vault is the example, "but I'd be hard pressed to find
   another". Recorded as [ADR-0013](../../20_decisions/0013-data-vault-or-equivalent.md): Data Vault or
   a functionally equivalent layer, with a three-property test — all data, all history, integrated on
   business keys. Point 6 and the schematic say so.
2. **Accepted.** Point 3: humans set purpose and delegation policy and rule directly on meaning;
   everything else is decided within that policy.
3. **Accepted.** Point 5: *governed* work, stages automated where policy allows.
4. **Accepted in narrower form.** The design already sends irreversible items to a person by hard
   rule ([155](../../10_architecture/155_adjudication-economy.md)), so the substitution already excludes
   them; point 10 now adds "where the damage is bounded" rather than sol's full condition.
5. **Accepted.** Point 8: triage *aims* at loss averted per minute, a way of reasoning until audit
   history exists; defaults are safe, with an example.
6. **Rejected.** "Every claim" and "one set of identifiers" state the design of
   [ADR-0011](../../20_decisions/0011-assertions-identity-plane-publication-gate.md) faithfully; the
   overview summarises it rather than scoping it down.
7. **Accepted.** All twelve points are now phrased as what the framework would do, per rule 9 of
   [AGENTS.md](../../../AGENTS.md), under a line that calls them a proposed design.
8. **Accepted.** Point 9 names the current value areas again, as the 2026-09-24 draft did.
9. **Accepted.** Point 11: an implementation adopts each further stage only once it needs it and the
   prerequisites have been shown to work, as ADR-0012 says.

No second round: apart from ADR-0013, which records a ruling rather than new design, the changes are
wording.
