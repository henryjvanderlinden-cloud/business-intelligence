# XREV 2026-10-07 — the codebase as small text files in git — sol

```yaml
object:        the paragraph "The author's statement, 2026-10-06, session 07" at the end of register row ARC-OP-20 (codebase as small text files in git), as committed in c2adb83.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop (pinned Codex 0.153), reasoning effort
               medium, workspace-write sandbox, answer written to the ignored scratch/ folder. The call timed out at
               the device bridge (60 s); the answer was retrieved from the file. Thread id not returned. Run in
               parallel with seven other passes, one object per pass.
assignment:    framed by PRC-OP-7: record the author's wish faithfully and draw only consequences that follow, as a candidate principle, not a repository policy. Four questions: a necessary part of a warehouse codebase that cannot be a small text file; factually wrong tool examples; conflicts or costs of many small files; consequences not following from the author's words. 250 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object the same day from the author's statements
               of 2026-10-06. Dispositions owed to the author.
verdict:       FAILS + SSIS `.dtsx` is text, and an atomic dependency lockfile need not be small
```

Sol's answer, verbatim (characters the transport replaced with "?" are left as received):

1. A reproducible-build lockfile is atomic and can be large; splitting it can break the package manager or fragment a resolution. Generated manifests such as dbt's `manifest.json` are similar. Amend the principle to prefer small text for hand-authored sources, while permitting atomic/generated files and unavoidable binary assets, with reproducible generation or a text projection where practicable.

2. “Classic SSIS packages” is wrong if it means `.dtsx`: they are XML text, although designer rewrites can produce noisy diffs. An `.ispac` deployment artifact is a ZIP container and should be generated. `.pbix` is effectively opaque to Git review. PBIP/TMDL is broadly a text-project alternative, but I am uncertain whether every current PBIP constituent is text or cleanly diffable.

3. There is no conflict: 180 proposes small files with stable identity, and 142 proposes one file per model object. No located ADR requires coarse files. Indiscriminate fragmentation nevertheless scatters a semantic change, increases retrieval calls, and complicates renames and cross-object invariants. It defeats the purpose below concept/object grain; 142's derived index and three-load contract partly constrain the cost.

4. Text does not ensure that “every change” has a readable diff: formatter churn, generated files, and unstable ordering can obscure it. Diffability also does not imply release-note attribution; ARC-OP-30 supplies that separate discipline and concerns output differences. “Inadmissible” converts the author's “rather” preference into a categorical tool ban, while “stable identity” was not stated.

VERDICT: FAILS + SSIS `.dtsx` is text, and an atomic dependency lockfile need not be small

## Dispositions

Owed to the author. The recommendations drawn from this pass and its parallel pass are numbered in the register row.
