# XREV 2026-10-07 — the Wide World Importers sandbox scripts — sol

```yaml
object:        prototypes/wwi_sandbox/ (README.md, setup.ps1, job.ps1, request.ps1), drafted 2026-10-07 for route A of 420 §11.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answers written to the ignored scratch/ folder. Four calls; the first never wrote its answer, so
               round 1 below is the second call. Rounds 1 to 3 are on successive revisions.
assignment:    framed by PRC-OP-7: a throwaway sandbox prototype on the author's own PC, run once by him: first-run success or a clear stop; no damage to his machine or other data; requests cannot escape the four fixed actions (no arbitrary code execution or write access for the file-writing agent through 'query'); no per-day acts by him. From round 2, stated proportion: a runaway query stopped by the timeout and output caps, tempdb pressure on his own server, and halting advances with the repair left to the author are acceptable. 300 words (later rounds 150-200); numbered findings with file, line and fix; praise and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the scripts. Static review only; nothing was run.
verdict:       round 1 FAILS; round 2 FAILS; round 3 PASS.
```

## Round 1, verbatim

1. `setup.ps1:73-75,103-106` treats any existing database named `WideWorldImporters` as this sandbox, mutates it, and with `-Reset` destroys it. Fail unless an existing database carries a sandbox ownership marker created by this setup; permit reset only for a marked database.

2. `setup.ps1:234-238` queues the first export but declares success without waiting for or checking its response. A first-run export failure therefore appears as successful setup and may require later diagnosis. Wait for `<id>.json`, validate `status = ok`, and stop with the returned error on failure.

3. `job.ps1:290-295` deletes the in-flight marker before the `finally` block restores the simulator procedures/temporal configuration. If `Configuration_RemoveDataLoadSimulationProcedures` fails, the clock has advanced, the marker is gone, and later advances are allowed against damaged temporal state. Remove the marker only after cleanup succeeds; also verify expected temporal tables have system versioning enabled before clearing it.

4. `job.ps1:129-142,315-320` does not enforce the advertised 200 MB cap: it tests the accumulated character count before formatting and writing the next row. One huge value (or row) can consume gigabytes of memory and disk; UTF-16 character count is not UTF-8 byte count. Count encoded bytes and refuse/truncate a row before writing it, with a per-field/row bound. No route was found for query SQL to persist database writes, execute OS code, or read outside the database under the stated permissions.

VERDICT: FAILS — setup can damage an unrelated same-named database, and cleanup and output-limit failures violate unattended safe operation.

## Round 2, verbatim

1. RESOLVED — `setup.ps1:73-79` refuses an existing same-named database unless it carries the setup-created `nsdn.SimulationClock` marker, including under `-Reset`.

2. PARTLY — `setup.ps1:247-253` treats a 30-minute first-export timeout as background continuation and still prints `DONE`; first-run success is therefore unproved without a clear stop. Fail on timeout (the author can rerun setup).

3. PARTLY — `job.ps1:305-336` compares only the number of temporal tables, not their identities, and writes the in-flight marker only at line 324, after Apply and procedure inspection at lines 307-310. Snapshot and compare the temporal table identities, and create the marker before Apply so every configuration-changing failure halts advances.

4. RESOLVED — `job.ps1:130-175,349-361` reads text/binary cells incrementally, cuts each cell, counts UTF-8 bytes before writing a row, and enforces the timeout, row cap and 200 MB budget.

NEW: `job.ps1:172-184` encodes truncation as `-rows`; if the first row exceeds the budget, `-0` is `0`, so the response falsely says `truncated=false`. Return truncation separately (or use a sentinel distinguishable at zero).

VERDICT: FAILS — setup can claim completion without a verified extract, and advance safety plus zero-row truncation reporting remain unsound.

## Round 3, verbatim

2. RESOLVED — `setup.ps1:253-254` now calls `Fail` when the first export exceeds thirty minutes, so setup exits without printing `DONE`.

3. RESOLVED — `job.ps1:313-345` snapshots and compares the temporal-table identities, writes the in-flight marker before Apply, and clears it only after cleanup and verification.

Prior NEW. RESOLVED — `job.ps1:165-192` returns truncation through a separate `out bool truncated`, including when zero rows fit the byte budget.

NEW: none.

VERDICT: PASS

## Dispositions

By the model, within the author's instruction to write and review the script before he runs it; none changes a ruling.
Round 1: (1) accepted — setup touches an existing database of the same name only if it carries `nsdn.SimulationClock`;
(2) accepted — setup waits for the first extract; (3) accepted — the in-flight marker is cleared only after cleanup and a
check of the system-versioned tables; (4) accepted, together with astra's finding 2. Round 2: all three accepted as
stated. Round 3 passes.
