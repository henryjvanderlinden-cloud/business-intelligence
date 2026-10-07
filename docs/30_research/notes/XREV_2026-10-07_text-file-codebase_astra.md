# XREV 2026-10-07 — the codebase as small text files in git — astra

```yaml
object:        the paragraph "The author's statement, 2026-10-06, session 07" at the end of register row ARC-OP-20 (codebase as small text files in git), as committed in c2adb83.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: record the author's wish faithfully and draw only consequences that follow, as a candidate principle, not a repository policy. Four questions: a necessary part of a warehouse codebase that cannot be a small text file; factually wrong tool examples; conflicts or costs of many small files; consequences not following from the author's words. 250 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + ordinary SSIS packages are XML text; readable diffs and release-note attribution do not follow automatically.
```

Astra's answer, verbatim (characters the transport replaced with "?" are left as received):

1. No necessary authored warehouse source requires binaries. DuckDB databases, Parquet data and compiled dependencies are runtime artefacts, not counterexamples about source. Minimal clarification: apply the preference to maintained source; permit UTF-8 text. Literal ASCII makes non-English identifiers and test literals needlessly escaped.

2. The SSIS example is wrong: ordinary .dtsx packages are XML text, although encryption and embedded script binaries can obscure parts. Text does not ensure pleasant diffs. From general knowledge, high confidence; not independently verified here. The .pbix versus dbt SQL/YAML distinction is sound on that basis. PBIP/TMDL supports text definitions; exact current coverage and version limitations remain unchecked.

3. No direct conflict with 142, 180 or an ADR follows from preferring small source files. Splitting one cohesive transformation across numerous fragments increases retrieval and cross-file reasoning; arbitrary fragmentation could defeat 142's three-load retrieval target. Keep one coherent concept per file, rather than minimise size. ADR-0011's separate stores need not become git files. Also, small files are 180's third property, not fourth.

4. The quotation does not endorse stable identity, prohibit all binary artefacts, or guarantee that every diff is readable. These are additions to a preference. Release-note attribution also needs an explicit mapping and output evidence: ARC-OP-30 concerns output changes, whose causes cannot be established merely from source diffs. Replace the guarantee with ?supports source review?; label the stronger filter and attribution connection as proposals.

VERDICT: FAILS + ordinary SSIS packages are XML text; readable diffs and release-note attribution do not follow automatically.

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
