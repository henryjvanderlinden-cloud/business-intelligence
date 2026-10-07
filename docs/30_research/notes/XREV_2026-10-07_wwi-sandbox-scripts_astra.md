# XREV 2026-10-07 — the Wide World Importers sandbox scripts — astra

```yaml
object:        prototypes/wwi_sandbox/ (README.md, setup.ps1, job.ps1, request.ps1), drafted 2026-10-07 for route A of 420 §11.
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answers written to the ignored scratch/ folder. Five calls; the second read files that had not been
               replaced on disk (a stale copy from the file bridge) and is set aside as STALE, not reproduced.
assignment:    framed by PRC-OP-7: a throwaway sandbox prototype on the author's own PC, run once by him: first-run success or a clear stop; no damage to his machine or other data; requests cannot escape the four fixed actions (no arbitrary code execution or write access for the file-writing agent through 'query'); no per-day acts by him. From round 2, stated proportion: a runaway query stopped by the timeout and output caps, tempdb pressure on his own server, and halting advances with the repair left to the author are acceptable. 300 words (later rounds 150-200); numbered findings with file, line and fix; praise and summary forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the scripts. Static review only; nothing was run.
verdict:       rounds 1 to 4 FAILS; the one remaining item of round 4 was fixed and not re-reviewed.
```

## Round 1, verbatim

1. prototypes/wwi_sandbox/job.ps1:255-275: Procedure discovery precedes Configuration_ApplyDataLoadSimulationProcedures. In the released backup's apply/remove lifecycle, DailyProcessToCreateHistory is created by apply and removed by cleanup; advance therefore stops at "not found" before reaching apply. Fix: detect the wrapper first, apply it before inspecting parameters, and put discovery and execution inside its cleanup-protected scope. Verify this lifecycle against the restored definitions during setup.

2. prototypes/wwi_sandbox/job.ps1:294-298: Impersonation does not bound resource consumption. A permitted SELECT returning repeated large varchar(max) values can exhaust memory or C: through the CSV writer, despite the row cap; read-only joins/sorts can also exhaust tempdb. There is no query byte budget or free-space guard. Fix: impose per-cell and total-output limits with streaming reads, a disk reserve, query resource limits and an independently enforced deadline. Arbitrary OS-code execution or author-privilege recovery through request SQL: none identified by static inspection.

3. prototypes/wwi_sandbox/job.ps1:276-283: The simulator commits before cleanup and the separate clock INSERT. A crash or cleanup failure in between leaves committed data with yesterday's clock; the next advance repeats that date. Moving the request first does not prevent this. An export failure instead leaves the clock advanced, while the response merely says error. Fix: durably journal request/day phases, reconcile unfinished advances before accepting another, and resume failed exports without advancing again; make the database commit and clock update atomic where the restored procedure permits it.

4. prototypes/wwi_sandbox/job.ps1:297-298: Query results bypass export's spatial conversion at line 204. SELECT * FROM Application.Cities can require the missing Microsoft.SqlServer.Types assembly. Fix: supply the matching client assembly or expose/query projections that convert CLR columns server-side, and document that restriction.

VERDICT: FAILS - Advancement lifecycle, resource limits and recovery need correction before unattended use.

## Round 2, verbatim

1. RESOLVED. Apply precedes parameter discovery; discovery and execution are inside cleanup's protected scope. Setup records the applied definitions.

2. PARTLY. prototypes/wwi_sandbox/job.ps1:135-141 checks the budget before materializing an entire row, counts characters rather than UTF-8 bytes, and writes the whole row even if it exceeds the remaining budget. A single large varchar(max) value can still cause huge allocations through GetValues, escaping and joining, or overshoot the disk reserve; the SQL timeout does not bound these client allocations. Fix: use SequentialAccess with bounded field reads and enforce an encoded-byte budget while escaping/writing, before allocating or writing oversized values.

3. RESOLVED. The in-flight marker blocks subsequent advances after an interrupted simulator/clock update; fresh restore clears it. The clock now precedes cleanup, preventing cleanup failure from repeating a committed day. Export failures explicitly identify the advanced date and retry action.

4. RESOLVED. README.md:25 documents server-side spatial conversion for query requests.

NEW defects: none.

VERDICT: FAILS - The query output cap still permits unbounded per-row client allocations and writes beyond its stated limit.

## Round 3, verbatim

2. PARTLY. prototypes/wwi_sandbox/job.ps1:168-172 enforces UTF-8 output bytes and bounds individual cells, but still allocates every escaped cell and joins the entire row before checking its budget. Thousands of 100,000-character columns can consume gigabytes. Fix: enforce the remaining encoded-byte budget incrementally while reading/escaping, with bounded row staging.

NEW defects:
- prototypes/wwi_sandbox/job.ps1:172,183-184: rejecting an oversized first row returns negative zero, so the response incorrectly reports truncated=false. Fix: return truncation separately from the row count.
- prototypes/wwi_sandbox/setup.ps1:77-78: interruption after restore but before SimulationClock creation leaves a database that subsequent runs, including -Reset, refuse as foreign. Fix: persist restore ownership before restoration, tied to the target, and support recovery without weakening refusal for unrelated databases.

VERDICT: FAILS - Per-row allocation remains excessive, and the revision introduces incorrect truncation reporting and an interrupted-setup recovery failure.

## Round 4, verbatim

2. RESOLVED. Incremental cell checks bound row staging by the remaining output budget plus one bounded cell, acceptable at the stated sandbox standard.

Zero-row truncation: RESOLVED. The separate boolean survives a rejected first row.

Interrupted setup recovery: PARTLY. prototypes/wwi_sandbox/setup.ps1:38,80,113: the ownership note identifies only the database name, not the server, and recovery checks only its existence. After an interrupted restore on one instance, rerunning with another -Server can overwrite an unrelated same-named database. Fix: persist and validate the server/instance and database identity before accepting recovery ownership.

NEW defects: none.

VERDICT: FAILS - Recovery ownership is still insufficiently tied to the restore target.

## Dispositions

By the model. Round 1: (1) accepted — `Configuration_ApplyDataLoadSimulationProcedures` is called before the simulator's
parameters are inspected, inside the cleanup scope, and setup records the procedures as applied; (2) accepted in
proportion — a 200 MB output budget, a 100 000-character cut per value read in chunks, and a disk check; (3) accepted in
proportion — an in-flight marker halts advancing after any unfinished day, the repair being a fresh restore by the
author, who has ruled Windows-side repairs his; a failed export after an advance is repeated by an `export` request;
(4) accepted — the README says spatial columns are queried as `col.ToString()`. Round 2: accepted, the budget now checked
cell by cell. Round 3: both new defects accepted (truncation reported separately; a restore begun and interrupted is
recognised by a note written before it). Round 4: accepted — the note now names server and database; fixed after the
round, parse-checked, not re-reviewed.
