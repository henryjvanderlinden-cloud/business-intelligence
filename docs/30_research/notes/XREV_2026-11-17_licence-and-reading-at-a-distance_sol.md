# XREV 2026-11-17 — the licence and reading at a distance (ADR-0041, ADR-0042) — sol

```yaml
object:        ADR-0041 and ADR-0042 as committed in a44624b and e376493, with ADR-0035 and ADR-0036 as amended, the
               README's License and Third-party material sections, THIRD-PARTY-NOTICES.md, check_licence in
               tools/check_repo.py and register row PRC-OP-9; the author's source note (Dutch, e-mail header removed),
               the head and tail of LICENSE, .gitignore's data lines, SRC-014 and SRC-018, and the URLs cited by
               evidence of kind web source, as upstream facts. Bundled as scratch/REVIEW_s14_licence.txt.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; confined to the one file; answer written to the ignored scratch/ folder with
               apply_patch.
assignment:    assume the change is wrong and show it, as an open-source licensing counsel and repository auditor who
               rejects it: whether the README and notices meet each named third-party licence's conditions; whether a
               statement on the legal effect of CC0 or these licences is wrong or overstated; whether check_licence
               fails exactly when its conditions are broken; whether ADR-0035 or ADR-0036 still contradicts ADR-0042
               or lesson 2 was changed unstated; whether any file carries client material. Up to five findings; the
               choice of CC0 itself, wording, layout, general assessment and praise excluded.
second reader: assignment set by Claude Opus 5.5 in session 14, which also drafted the material. The dispositions are
               Opus's; the changes made in response are unreviewed.
limits:        the bundle did not reproduce the full CC BY 4.0 and CC BY-SA 4.0 legal texts nor the evidence files
               themselves, so finding 5 holds only for the material as described.
verdict:       FAILS [the checker accepts a host named only inside a longer host; ADR-0036 point 3 and ADR-0035's
               Consequences still require releases; ADR-0041 overstates what no licence forbids]. Disposition:
               2 applied (a host must stand as a whole name in the notices; README sections matched as headings,
               links as link targets; seen to reject notexample.org and sub.example.org and accept the exact host);
               3 applied (ADR-0036 point 3 and ADR-0035's Consequences annotated; ADR-0042 point 4 and its Amends line
               say that an accepted note is applied and tested on WWI and released only once a release exists, and
               that examples may be abstract); 4 applied (ADR-0041 now says no general permission, statutory
               exceptions and case-by-case permission aside); 5 holds. 1, client details in ADR-0035's context
               (unnamed, published since 2026-10-29, outside this change), put to the author, who ruled on
               2026-11-17 at 14:26 to leave it: "4 a let's leave it, it's very generic." Unreviewed.
```

## sol's answer, verbatim

1. **Client material — FAILS (question 5).** ADR-0035's Context describes an actual client's systems: PostgreSQL, approximately 100 tables, likely foreign keys, a production database, two further sources supplying daily extracts, and Claude subscriptions. Its decision 4 connects the PostgreSQL prototype to that first client. These are client system details even without a client name; the bundle does not establish that they identify a particular client. Nor does it establish that VDL-DIAA or Rick is a client. Minimal fix: remove the concrete client environment from material carried into the public repository and describe the generic catalogue-pass requirement instead. The note's own assertion that it contains no client material does not clear the other bundled files.

2. **Checker equivalence — FAILS (question 3).** Keep the correct LICENSE and README, put a web-source evidence JSON under `analysis/x/evidence/` with `{"kind":"web source","inputs":{"url":"https://example.org/page"}}`, and let the notices name only `https://notexample.org/`. The test `host not in notices` accepts `example.org` as a substring although that host has not been named. Conversely, a README beginning directly with `## License\n` fails the required `\n## License\n` search despite having the section. These are counterexamples derived from the supplied function, not executed tests. Minimal fix: compare normalized hostnames against explicitly declared notice hosts and recognize actual Markdown headings, including at the start of the file. The hash check validates the chosen CC0 template bytes after CRLF normalization; it is not a general test of legally equivalent text.

3. **Amendment consistency — FAILS; lesson preservation — HOLDS (question 4).** ADR-0036 decision 3 still requires every accepted upstream improvement to be “tested on WWI, and released.” Its amendment adds multiple lessons, reading-point patches and review, but does not qualify that release requirement. Counterexample: a client using only reading at a distance returns an accepted conceptual lesson before any client chooses a fixed release. ADR-0042 permits no release; ADR-0036 still requires one. The same point requires an example to be restated on WWI, whereas ADR-0042 expressly permits an abstract example. ADR-0035's Consequences also still say “nsdn now needs releases,” without limiting that claim to the fixed-release variant. Minimal fix: explicitly amend those requirements to make publication in a release conditional on that variant and allow abstract examples. The note's substantive lesson 2 is otherwise retained; using amendments instead of partial supersession and deferring the process document are changes expressly disclosed in ADR-0042.

4. **Legal-effect statements — FAILS (question 2).** ADR-0041's no-licence option says “no one, the author's own clients included, may lawfully copy the material.” Its own Context and the Dutch source note expressly preserve statutory exceptions. A copy permitted by such an exception is a concrete counterexample; the author can also grant individual permission. Minimal fix: say that absence of a licence supplies no general permission to copy, subject to statutory exceptions and separately granted permission. The README's third-party exception prevents reading its attribution-free promise as relicensing Microsoft's or Wikipedia contributors' material. The supplied CC0 extract does not contain the operative waiver and fallback provisions, so it supplies no basis for rejecting their description beyond the note's stated qualifications.

5. **Named third-party licence conditions — HOLDS on the material described in the bundle (question 1).** For WWI, the notices reproduce Microsoft's copyright and complete MIT permission notice, including the condition and disclaimer, and identify the database, simulation and generated data. Keeping that notice with the repository satisfies the quoted retention condition; MIT does not require a separate notice beside every occurrence. For the 14 Learn excerpts, the combined files identify Microsoft Corporation, retain a copyright notice, link CC BY 4.0, identify the source page and URL, and disclose the summarising fetch and possible wording changes. That disclosure indicates modification rather than representing verified verbatim quotations. No supplied fact establishes an additional upstream attribution or notice that was omitted. For the two Wikipedia items, the notices identify contributors, source pages and CC BY-SA 4.0; the bundle describes only ISO code lists, with no page prose. That does not establish an adaptation of protected Wikipedia expression requiring an adapter's share-alike licence. Merely extracting factual codes does not establish such an adaptation. No fix is demonstrated for these described items. This determination cannot certify unseen excerpts, protected selection or arrangement, or omitted upstream notices: the evidence files and the CC BY/CC BY-SA legal texts are not actually reproduced in the bundle.

VERDICT: FAILS — client system details, checker counterexamples, residual ADR conflicts and an overbroad copying prohibition remain.
