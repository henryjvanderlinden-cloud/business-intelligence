# XREV 2026-10-26 — the calculation-engine design: ADR-0024, ADR-0025, 144 section 4 — sol

```yaml
object:        docs/20_decisions/0024-calculation-engines-are-a-versioned-source.md, docs/20_decisions/0025-engine-results-in-the-raw-vault.md
               and 144 §4, as committed in ad64b5b/68090d3.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch.
assignment:    assume the design fails to guarantee that every stored engine result can be reproduced exactly and audited,
               including after a new version, the fallback and reruns; up to six failure scenarios with minimal text
               additions; contradictions; technical errors of fact; the author's rulings not to be argued as preferences.
               First assigned to gpt-6-astra twice (09:30 and 09:40); astra wrote nothing in either attempt, and the pass
               was re-sent to sol at 09:52.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 09 on 2026-10-26; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [a same-version rerun after corrected inputs can leave no new row when the output is unchanged]. Resolved in
               the revised 144 §4 as proposals; the item touching the author's ruling (10) is put to him.
```

## sol's answer, verbatim

# External review — calculation-engine reproducibility and auditability

## Finding 1 — An engine version does not identify the executable environment

**Quote:** “A version is the code and its locked dependencies.” (144 §4 item 2.) “Engines are deterministic code.” (ADR-0024, Consequences.)

**What is wrong:** A dependency lock does not by itself identify the interpreter, platform, native libraries, DuckDB build, locale, timezone, environment variables, or deterministic settings. It may also contain platform markers whose resolution differs by host. Code is not made deterministic merely by calling it deterministic: parallel reductions, unordered iteration, random generators, current-time reads and native numerical libraries can vary a result. ADR-0024 requires only an engine-version label on the result, so the stronger proposal in 144 does not close the gap either.

**Scenario:** Engine `tax-allocation` version `1.4` and lock `L17` run on 2026-03-31 on Python 3.12/x86-64 with OpenBLAS and again on 2027-04-01 on Python 3.13/ARM64 with a different BLAS. Both runs read input snapshot `S88`. A parallel sum lies on a half-cent boundary: the first execution produces EUR 10,000.00 and the second EUR 10,000.01. Both stored rows say engine `1.4`; the claimed version cannot select which executable produced the first value.

**Correction:** Replace the version definition with: “An engine version is an immutable, content-addressed source revision plus the digest of a fully resolved execution artifact recording the interpreter, all direct and transitive Python and native dependencies, DuckDB version, OS/architecture, locale/timezone, deterministic settings and random seeds; every result stores both digests.”

**Confidence:** High.

## Finding 2 — An input “as-of” does not identify the input rows used

**Quote:** “Every result row records what it was computed from: the engine and its version, a run identifier, and the as-of of its inputs (which load, or which point in time). Without the as-of, a version does not reproduce a figure.” (144 §4 item 3.)

**What is wrong:** A date or point in time is not an immutable input manifest. It does not identify the tables, row revisions, selection query, or transaction-time cutoff. After late arrival or correction, rerunning a current query “as of” the same business date can select different rows. The sentence states a necessary condition as though it were sufficient, and ADR-0024 requires none of these input identifiers.

**Scenario:** Version `margin-2.0`, run `R100`, is executed on 2026-02-01 “as of 2026-01-31” from order revision `O7a` and cost revision `C4a`, producing 12.40. On 2026-02-10, a late cost revision `C4b` is loaded with the same valid date. In 2027, the same version is rerun “as of 2026-01-31”; the warehouse now selects `C4b` and produces 11.90. The stored as-of does not recover `C4a` or prove which rows `R100` read.

**Correction:** Add: “Each run stores an immutable input manifest (or content-addressed snapshot) naming every input relation and row revision, the input transaction/knowledge-time cutoff, and the version or digest of the selection query; an as-of date alone is not input identity.”

**Confidence:** High.

## Finding 3 — Run identity is optional where the audit claim needs it to be mandatory

**Quote:** “Results are keyed at their full calculation grain, and a run may deserve identity of its own.” (144 §4 item 8.) “Whether WWI needs run hubs is open.” (same item.) “Every result is stored with the version of the engine that produced it.” (ADR-0024 decision 2.)

**What is wrong:** The documents require an engine version but make the calculation run optional. Version, result grain and computation time do not identify an execution or its completeness. Without a mandatory run record, an auditor cannot distinguish a retry from a separate authorized rerun, determine whether all rows belong to one atomic execution, or attach logs and failures to the stored results.

**Scenario:** Version `allocation-3.1` reads snapshot `S9`. Run `R20` starts on 2026-05-01 01:00 and writes 600 of 1,000 rows before failing. A retry at 02:00 writes all 1,000. The result key is account, month and engine version; 600 rows can now be attributed to either execution, and there is no stored run object from which to prove that the published set came entirely from the successful retry.

**Correction:** Replace “may deserve identity” with: “Every execution has a globally unique run identifier. A run record stores engine-artifact digests, input-manifest digest, parameters, start and finish times, status, row counts, logs and the identity of every result row; only a completed run may be selected for publication.”

**Confidence:** High.

## Finding 4 — A corrected-input rerun can disappear when its output is unchanged

**Quote:** “Corrected inputs are handled by rerunning, using the same bitemporality.” (ADR-0024 decision 5.) “Change detection on engine results includes the engine version, so a new version that reproduces the old values is still recorded as new.” (ADR-0024, Consequences.)

**What is wrong:** The special change-detection rule covers a new engine version, not a new input revision or run under the same version. If corrected inputs produce the same value, ordinary value-plus-version change detection sees no change and can omit the rerun. Even when the value changes, there is no required link from the replacement result to the corrected input and prior result.

**Scenario:** Run `R30` of `risk-score-5.0` on 2026-06-01 reads income 50,000 and stores band `B`. On 2026-06-05 the income is corrected to 51,000 and run `R31` still produces band `B`. Version and value are unchanged, so the described change detection emits no new result. Later the warehouse can show `B`, but cannot prove whether the correction was rerun, which input revision was assessed, or what was known on either date.

**Correction:** Add: “Input-manifest identity and run identity are part of result identity and change detection. Every correction-triggered rerun is recorded even when the value and engine version are unchanged, and it links to the superseded result and the correction event.”

**Confidence:** High.

## Finding 5 — The fallback boundary is not defined on the temporal axes it must govern

**Quote:** “Where the fallback is used, the history before the cut-off, or before the release, keeps the earlier version's results. A mart that spans the boundary mixes versions, and must show which version applies to which period.” (ADR-0025, Consequences.)

**What is wrong:** “Cut-off,” “release” and “period” do not say whether the boundary applies to business valid time, source knowledge/load time, run time, or some combination. The human adjudication itself has no required durable record or version-selection mapping. Consequently a later correction whose valid date and knowledge date fall on opposite sides of the boundary has no specified engine version.

**Scenario:** Version `v2` is released on 2026-10-15 with a human-chosen cut-off of 2026-07-01. An invoice valid on 2026-06-30 arrives late on 2026-11-01, and an invoice valid on 2026-07-02 that was loaded in June is corrected on 2026-11-02. “From the cut-off onwards” can select `v1` or `v2` for each invoice depending on whether valid time or knowledge time controls. Two conforming reruns can therefore store different results and each claim to follow the adjudication.

**Correction:** Add: “Each fallback creates an immutable, identified policy record containing the adjudicator, decision time and reason; exact inclusive/exclusive boundaries on valid time and input transaction/knowledge time; release identifier; engine-version mapping; and the rule for late arrivals and corrections. Every affected run and result references that policy.”

**Confidence:** High.

## Finding 6 — “Time computed” is not knowledge time, and the pipeline order is internally incomplete

**Quote:** “Engine results are bitemporal: each has the period it describes and the time it was computed.” (ADR-0024, Consequences.) “An engine result has two times: the period it describes and when it was computed.” (144 §4, “Time.”) “A fixed order without cycles: load the raw vault, build the business vault, run the engines, load their results, build the marts.” (144 §4 item 6.)

**What is wrong:** Bitemporal history conventionally distinguishes valid time from transaction/system time. Computation time is an event timestamp, not necessarily the time the input facts became known or the time the result became recorded and query-visible. The fixed order also builds the business vault before loading current engine results even though 144 §2 says the business vault can be rebuilt from stored engine results; it does not specify a second business-vault phase or that only prior-run results may be consumed.

**Scenario:** Input correction `C9` becomes known at 09:00 on 2026-08-04. Run `R40` starts at 10:00, finishes at 10:20, and its results commit to the raw vault at 11:00. A business-vault object built at 09:30 uses the preceding engine result. Recording only valid period 2026-07 and “computed at 10:20” cannot answer what the engine knew at 10:00, when the new result became visible, or whether the 09:30 business-vault state is the one to reproduce.

**Correction:** Replace the two-time statement with: “Each result records valid-from/to, the input knowledge-time cutoff, run start/finish and warehouse recorded-at/superseded-at. The pipeline declares whether the business vault consumes only a named prior completed engine run or is rebuilt in a second phase after current engine results load.”

**Confidence:** High.

## Contradictions

- ADR-0024 says, after recording ADR-0025's ruling in decision 4, “Full recomputation on every version costs compute and storage that grow with history; the fallback when they run short is not decided.” ADR-0025 decisions 2–3 do decide it: cut-off first, then going-forward only, with human adjudication. These are current statements with opposite status.
- 144 §4 item 4 presents insert-only, side-by-side versions as “Proposed with it, not yet ruled,” while ADR-0024 states as a consequence that engine results “are stored insert-only.” The documents disagree about whether insert-only storage has been decided.
- 144 §2 says the business vault can be rebuilt from stored engine results, while §4's fixed pipeline builds the business vault before running and loading engines. Both can hold only if “stored” means a named prior run or the business vault has a second build phase; neither qualification is written.

## Technical errors of fact or precision

- “Engines are deterministic code” is false without enforced restrictions and captured execution state; ordinary Python, NumPy and pandas programs can use nondeterministic inputs or execution paths.
- “A version is the code and its locked dependencies” is insufficient for exact reproduction. A lock does not necessarily freeze the interpreter, platform, native numerical stack, DuckDB build or runtime configuration, and environment-dependent lock entries can resolve differently.
- “pandas and numpy default to binary floats” is overbroad. NumPy infers integer dtype for integer input, and pandas supports integer, decimal-backed and other extension dtypes; non-integral numeric inference and many operations commonly use binary floating point, which is the narrower true claim.
- “Money is held as integer cents or as Python `Decimal`” does not by itself make the stated half-up calculation exact. Integer cents cannot represent pre-rounding fractional cents, and `Decimal` still needs an explicit precision, scale, rounding context and construction from decimal text or integers rather than a binary float.
- The floating-point core is otherwise correct: most decimal cent fractions are not exactly representable in binary floating point, and an unguarded half-up implementation can misround boundary cases.
- No DuckDB-specific factual claim in the scoped text is independently false. The documents describe a bitemporal table structure rather than expressly claiming that DuckDB supplies native temporal tables or database time travel; the reproducibility defect is that the required timestamps and snapshots are not specified.

VERDICT: FAILS [a same-version rerun after corrected inputs can leave no new row when the output is unchanged]

## Dispositions

1. **Accepted.** A version identifies code and the whole execution environment by digest (144 §4 item 2); ADR-0024's
   "deterministic" annotated as meaning no model in the data path.
2. **Accepted.** Every run stores an immutable input manifest (item 3).
3. **Accepted.** Every execution has a run record; only completed runs are published (item 9).
4. **Accepted as a proposal, to be put to the author** (item 10): reruns are recorded even when value and version are
   unchanged. It extends his ruling that a new version is new data.
5. **Accepted.** Every use of the fallback leaves a policy record with exact boundaries on both time axes (item 11).
6. **Accepted.** Knowledge time is distinguished from computation time; the pipeline gains a second business-vault phase
   and named runs (Time paragraph, item 6).
Contradictions: the stale "fallback not decided" in ADR-0024 annotated as ruled by ADR-0025; insert-only explained in
144 §4 item 4 as following from ADR-0025 and ADR-0013 rather than as a separate proposal; the §2/§4 rebuild order fixed
by item 6. Technical points: the floating-point sentence narrowed; Decimal with explicit context, built from text or
integers; integer cents only for rounded values.
