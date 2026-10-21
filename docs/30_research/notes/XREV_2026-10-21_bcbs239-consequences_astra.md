# XREV 2026-10-21 — BCBS 239 consequences for the design (152 §4) — astra

```yaml
object:        docs/10_architecture/152_bcbs-239.md §4, items 1 to 14 and 17, as committed in b975c97 (items 15 and 16
               ruled by the author in ADR-0016 and out of scope).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder with apply_patch; the call timed out at the device
               bridge and the answer was retrieved from the file. Two earlier attempts (2026-10-15 and earlier on
               2026-10-21) wrote nothing.
assignment:    assume each item is wrong; report misdescriptions of cited design elements, consequences that do not
               follow from the cited principle or paragraph (good practice dressed as BCBS 239), and omitted
               consequences that would change an accepted ADR. Admitted weaknesses excluded; praise and general
               assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted 152 on 2026-10-15.
verdict:       FAILS [an institution-approved, independently validated identity-matching rule can generate semantic
               assertions automatically without the per-claim owner rulings item 8 presents as a BCBS 239 consequence]
```

Astra's answer, verbatim:

1. Item 6; kind (b), architectural choice presented as a regulatory consequence. Quotation: "every in-scope load, test and report runs without the agentic layer". [BCBS 239](https://www.bis.org/publications/201301-guidelines-principles-effective-risk-data-aggregation-and-risk-reporting.pdf), Principle 2 and paragraph 32, require continuity, not a particular execution architecture. Counterexample: redundant, independently hosted model services with tested failover could meet the reporting deadline; an entirely deterministic pipeline with one unavailable database could miss it. The existing ruling can stand, but does not follow from the principle. Minimal fix: describe agent-independent operation as the repository's chosen means of supporting continuity, whose effectiveness still needs demonstrating.

2. Item 8; kind (b), ownership confused with individual adjudication. Quotation: "For in-scope data that would not be allowed" and "Those would be ruled by the owner". Paragraphs 34, 36(d) and 37 do not prohibit automated semantic assertions. Counterexample: an owner approves a matching policy, evidence thresholds and exception handling; independently validated machinery applies that policy to new identifiers without asking the owner about each match. An identifier match remains a semantic assertion under ADR-0005, even when it is produced under that policy. Minimal fix: require institution-approved authority, definitions and matching controls; reserve individual adjudication for cases those controls cannot resolve. Label any blanket removal of ADR-0005's evidence route as an additional institutional policy.

3. Item 9; kind (b), downstream use treated as proof of an unbounded consequence. Quotation: "A claim that reaches a risk report has neither" reversibility nor limited reach. Counterexample: a provisional classification affects a bounded, immaterial exposure; even reversing every uncertain classification would leave the report's decisions unchanged. Publication does not by itself establish irreversible harm from that claim. Paragraphs 54-56 recognise approximations and institution-defined accuracy and materiality requirements. Minimal fix: require an assessment of the claim's possible effect on decisions, including aggregate exposure and correlated errors. Attribute the blanket provisional-lane ban to a proposed policy, not to BCBS 239, and make the predicted increase in human review conditional on that policy.

4. Item 10; kind (b), reconciliation turned into an unconditional publication veto. Quotation: "an unexplained difference would block publication rather than warn". Paragraph 36(c) requires reconciliation; it does not prescribe this zero-tolerance gate. Counterexample: a bounded residual below a justified accuracy threshold remains under investigation, with its possible effect assessed and disclosed through exception handling. Its unresolved cause alone does not establish that the report is unusable. Paragraphs 53(c) and 55-56 matter here. Minimal fix: distinguish performing reconciliation from satisfying its acceptance criteria; specify justified thresholds, escalation and exception handling. Likewise, identify "at least as often as the report" as the proposed control cadence, not wording supplied by paragraph 36(c).

5. Item 11; kind (b), additions attributed to the wrong paragraph. Quotation: "an owner for each, which [paragraph] 53b asks for". Paragraph 53(b) asks for a validation-rule inventory and explanations of its mathematical or logical conventions; it does not ask for an owner per rule. The item also equates every statistical warning with a data error requiring closure before release or inclusion in the report. A normal but unusual business day can trigger a warning without establishing an error. Minimal fix: retain rule ownership as an implementation proposal under governance, include the conventions actually specified, and distinguish warning triage from the confirmed errors or integrity weaknesses addressed by paragraph 53(c).

6. Item 12; kind (b), process documentation expanded into a mandated event ledger. Quotation: "every manual adjustment, override, top-side entry or repair ... recorded with who, when, why and its effect". Paragraph 39 addresses aggregation processes and the appropriateness, criticality and mitigation of manual workarounds. It does not specify those fields for every execution. Counterexample: documenting and controlling a recurring adjustment procedure is a different artifact from logging each adjustment's operator and effect. Minimal fix: separate the process inventory required by paragraph 39 from the proposed transaction-level audit trail, and justify the latter as an institutional control rather than a direct requirement of that paragraph.

7. Item 13; kind (b), semantic consistency turned into a prescribed publication topology. Quotation: "Its publication pipeline would feed the official one, or feed nothing." Paragraph 37 does not prescribe a catalogue product or write destination. Counterexample: a read-only local catalogue publishes a faithful, versioned projection of approved institutional definitions and links them to local fields, without writing back to the official glossary. It introduces no competing meaning. Minimal fix: require consistency, traceability and governed conflict resolution; allow faithful local projections. Also replace the assumption that every bank already has a satisfactory official dictionary with a prerequisite to verify.

8. Item 14; kind (a), existing retention described as a new restriction. Quotation: "Evidence that nobody uses a mart is enough to retire it" followed by the proposed requirement to "keep the declarations and context versions". Document 145 already defines staged retirement: flag to the owner, deprecate with consumer warnings, make dormant with the definition retained, then archive with the definition retained in git. Its context-pruning section also retains retired material. Minimal fix: describe those as existing safeguards. Identify only the additional requirement being proposed: owner approval and a demonstrated ability to reconstruct the reported result, including its retained data and dependencies, rather than merely retaining definitions.

verdict - FAILS + counterexample: an institution-approved, independently validated identity-matching rule can generate semantic assertions automatically without the per-claim owner rulings item 8 presents as a BCBS 239 consequence.

## Disposition

Applied by Claude Opus 5.5 on 2026-10-21, uncommitted at the time of filing and put to the author with the commit:
all eight findings are accepted. Items 6, 8, 9, 10, 11, 12, 13 and 14 of 152 were rewritten so that each separates
what the BCBS 239 text asks from a control proposed on top of it, and §4's introduction now says that a *proposed*
control is one the text permits, not one it requires. Item 14 now credits 145's staged retirement as existing.
