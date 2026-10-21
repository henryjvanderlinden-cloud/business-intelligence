# XREV 2026-10-21 — BCBS 239 and the ECB guide as stated in 152 §2 and §3 — sol

```yaml
object:        docs/10_architecture/152_bcbs-239.md as committed in b975c97: §3, the table of the fourteen principles
               (pass 1), and §2, what BCBS 239 and the ECB guide are (pass 2).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, told to answer from its own knowledge without browsing; each answer written to the ignored
               scratch/ folder with apply_patch, the calls having timed out at the device bridge. Three earlier, broader
               attempts covering §2 and §3 together (2026-10-15 and 2026-10-21) wrote nothing; the object was then split
               in two, per handover 09's note that a narrower brief to sol writes where a broad one does not.
assignment:    list only factual errors: wrong dates or scope, a principle paraphrased so that its meaning changes, a
               paragraph number attached to the wrong content; the section's admissions about second-hand sources
               excluded; praise and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted 152 on 2026-10-15.
verdict:       pass 1 (§3): HOLDS UNDER [concise, non-exhaustive paraphrase and citations scoped to the immediately
               preceding content]. Pass 2 (§2): FAILS [the ECB guide's seven named areas are reported incorrectly].
```

## Pass 1 — §3, the table — sol's answer, verbatim

verdict - HOLDS UNDER concise, non-exhaustive paraphrase and citations scoped to the immediately preceding content

## Pass 2 — §2 — sol's answer, verbatim

1. Quoted sentence: "The principles apply at group and at solo level, and also to the data used in a bank's key internal risk models."

   What is wrong: The final clause misstates the stated scope. BCBS 239 says that the principles also apply to key internal risk management models; it does not formulate that extension merely as applying to the data used in those models.

   Correction: "The principles apply at group and solo levels, and also to a bank's key internal risk management models."

   Confidence: High.

2. Quoted sentence: "Risk data aggregation is defined there as defining, gathering and processing risk data according to the bank's risk reporting requirements, so that the bank can measure its performance against its risk tolerance or appetite; it includes sorting, merging and breaking down sets of data."

   What is wrong: The last conjunction changes the definition. BCBS 239 says that risk data aggregation includes "sorting, merging or breaking down sets of data," not that it necessarily includes all three operations.

   Correction: Replace "sorting, merging and breaking down" with "sorting, merging or breaking down."

   Confidence: High.

3. Quoted sentence: "It names seven areas: the management body's responsibility, the scope of application of the data governance framework, key roles and responsibilities, a group-wide integrated data architecture, the effectiveness of data quality controls, the timeliness of internal risk reporting, and implementation programmes."

   What is wrong: This is not the ECB Guide's named seven-area list. In particular, its third area is an "effective data governance framework," not "key roles and responsibilities," and its fifth is "group-wide data quality management and standards," not merely the effectiveness of data quality controls. The second and fourth headings are also misstated by redistributing "data governance framework" and "group-wide" into them.

   Correction: The seven areas are: responsibility of the management body; sufficient scope of application; effective data governance framework; integrated data architecture; group-wide data quality management and standards; timeliness of internal risk reporting; and effective implementation programmes.

   Confidence: High.

Verdict - FAILS + the ECB Guide's seven named areas are reported incorrectly.

## Disposition

Applied by Claude Opus 5.5 on 2026-10-21. All three findings of pass 2 accepted. Finding 3 was checked against a second
summary of the guide, Management Solutions' technical note, which names the same seven areas as sol; the first summary
used in 152, Regulation Tomorrow's, had paraphrased them. 152 §2 now says the principles apply to key internal risk
management models (finding 1), that aggregation includes sorting, merging *or* breaking down (finding 2), and names the
seven areas as the guide does, citing the second summary (finding 3). The guide itself has still not been read.
