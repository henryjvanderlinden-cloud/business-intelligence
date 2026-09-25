# XREV 2026-09-25 — adjudication economy (155), the model — astra

```yaml
object:        docs/10_architecture/155_adjudication-economy.md, first draft, at commit 383bff1.
reviewer:      gpt-6-astra, reasoning effort medium, via the Codex MCP server on
               desktop-lv8udh0 (pinned Codex 0.153 in C:\Tools\codex-0153), sandbox read-only,
               thread 01a0d7f6-4237-7762-b60c-fbfcd8b572bf. Read the file itself.
assignment:    one question, adversarial, ranked, 300 words, praise, assessment and summary
               forbidden: attack the model — formula, hard rules, lanes, levers, control loop.
               The same document went to sol in parallel on organisational practice.
second reader: assignment set by Claude Opus 5.5, which drafted the object. The author accepted
               all findings; on the one point where the two reviewers conflicted he ruled that
               seeded checks stay, blinded and excluded from estimates, and that rigour versus a
               lean start is a question of implementation (ADR-0012).
verdict:       FAILS in part — five findings; all integrated 2026-09-25.
```

Astra's answer, verbatim:

1. **The objective misprices review.** Loss cannot be compared directly with minutes; ordinal bands cannot support multiplication. The product requires conditional probabilities: reviewers may miss precisely what machines miss. Detection may leave damage already incurred. **Minimal fix:** estimate loss without review minus loss with review, including delay, correction and reviewer-induced errors; rank that difference per minute. Use numerical ranges and record `r`, currently omitted.

2. **Automatic tightening can collapse capacity.** A failing precedent could send thousands of claims into a fixed human budget, crowding out mandatory reviews. Audits, seeds and automation approvals consume that same budget. Alerts cannot resolve infeasibility. **Minimal fix:** reserve mandatory and monitoring capacity; quarantine or throttle affected work when capacity runs out. Add hysteresis and explicit release criteria.

3. **The loop can certify its own blind spots.** Stratification complements random sampling; it does not replace it. Selective audits, correlated instances and incomplete downstream detection can produce reassuring confidence bounds while losses rise. Overall calibration can conceal dangerous subgroups. **Minimal fix:** randomise within strata, retain known inclusion probabilities and exploration samples, use cluster-aware uncertainty, and measure exposure and detection delay. Independently adjudicate audit labels.

4. **The lanes reward waiting and favourable classification.** Provisionals can “survive” because nobody exercises them; internal use can already influence decisions. Understated reach or regulatory relevance bypasses hard rules. **Minimal fix:** require evidence and exposure limits for promotion, independently check hard-rule applicability, and re-triage every lane when dependencies or use change.

5. **The levers and reviewer metrics invite false confidence.** Pattern reuse amplifies one mistaken ruling; cheaper, pre-drafted reviews can reduce reviewer sensitivity. Obvious seeds and low overrides can coexist with shared semantic errors. **Minimal fix:** bound precedents by validated applicability and expiry, measure total dependent exposure, and use blinded independent reviews with representative seeds excluded from production and calibration estimates.
