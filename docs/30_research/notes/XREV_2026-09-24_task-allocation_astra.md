# XREV 2026-09-24 — task allocation (070) — astra

```yaml
object:        docs/00_concept/070_task-allocation.md at commit 1e7642c — the 39-row table
               and its "What the table shows so far" patterns, after revision by the sol pass.
reviewer:      gpt-6-astra, reasoning effort medium, via the Codex MCP server on
               desktop-lv8udh0, thread 01a0d520-5d6c-7b43-aa21-61afe8b489b5. Served by a
               pinned Codex 0.153 copy at C:\Tools\codex-0153, because Astra needs 0.153.1 or
               later and `codex mcp-server` was removed in 0.154.0. That copy cannot run
               commands (its command-runner helper is absent), so the reviewer could not read
               the file; the table and patterns were pasted into the prompt instead.
assignment:    two chained questions, adversarial framing, praise and general assessment
               forbidden, told the table had already been reviewed and not to repeat what it
               reflects. Q1: the most consequential remaining problems, ranked. Q2: test the
               four claimed patterns against the rows, and say which faculty a runbook is.
second reader: assignment set by Claude Opus 5.5; the table was drafted by Claude Opus 5 and
               revised against sol. The author asked for the review and afterwards accepted
               every finding.
verdict:       FAILS in part — one task missing, one check missing, one generation step given
               to the wrong faculty, one pattern overstated and one unestablished; two
               patterns hold. All accepted by the author, 2026-09-24.
```

Astra's answers are reproduced verbatim below.

## Q1 — the most consequential remaining problems, ranked

1. **Missing task: retention, erasure and controlled historical correction across layers.** Row 36 establishes authority and enforcement, but does not allocate identifying affected records, propagating deletion or correction through raw/Vault/marts, handling backups, and proving completion. Recovery and backfills do not establish which historical records should cease to exist or change. Allocate **H decides policy and exceptions; A proposes the implementation plan; D executes and verifies propagation; H checks policy compliance**. Deciding dimensions: **6 and 13**. This can directly constrain the historisation design.

2. **Row 34, checks: replace "—" with "D verifies dependency coverage; H validates affected business uses."** Lineage can establish recorded technical dependencies; it cannot establish that those records cover every consequential use. Exported spreadsheets, manually assembled reports and downstream decisions can escape the graph. A's interpretation therefore needs a check before its conclusions support production-change approval. Deciding dimension: **5**. Row 35's approval does not itself supply the missing evidence that the impact analysis is complete.

3. **Row 17, proposes: use D for generation covered by approved mappings and templates; A for unresolved transformation logic.** The allocation currently makes A the writer even where metadata plus established conventions completely specify the output—for example, repetitive Vault loading structures. That unnecessarily turns a reproducible generation problem into generated code requiring renewed scrutiny. **D** should instantiate those templates; **A** should propose extensions or logic the templates cannot express, with H approving their meaning. Deciding dimension: **1**, supported by **3**. This boundary matters because rows 16–17 sit on a potentially large volume of recurring implementation work.

## Q2 — the four claimed patterns

(a) holds

(b) holds

(c) **Overstates — rows 19, 31 and 33 permit decisions within previously authorised boundaries:** "H decides contested meaning, commitments and consequential exceptions; routine operational decisions may follow H-approved rules."

(d) **Not established, rather than contradicted — no row estimates costs:** "The rows identify faculty handoffs, but whether those handoffs dominate cost remains a hypothesis requiring their procedures, frequency and review effort to be described."

A **runbook is an artifact, not a faculty**. In row 31, the decision-maker is **D** if encoded conditions determine the action, **A** if an agent interprets the procedure and selects an action, or **H** if a person does so; the row must specify which.

This does **not break (b)** if A's discretion is confined to routine, uncontested cases, with consequential or contested cases escalated to H. It exposes **(c)'s overbreadth**: H's approval of a procedure is distinct from H deciding each case under it.

## How it was incorporated

In [070_task-allocation.md](../../00_concept/070_task-allocation.md): a new row 37 for
retention, erasure and correction (later rows renumbered); checks added to row 34; row 17
split between template instantiation (D) and what templates cannot express (A); rows 19, 31
and 33 reworded so routine decisions follow H-approved rules, with row 31 naming who applies
the runbook; pattern (c) replaced by the reviewer's wording and (d) restated as a hypothesis.
Two observations were added that the review prompted but did not make: that the agentic
layer's larger job may be writing the templates and rules D runs, and that erasure
obligations constrain the historisation design.
