# 420 — The next sandbox, end to end: options and the author's hands

*Drafted 2026-10-06, session 07, at the author's request, for `EVI-OP-7` in the
[register](../../registers/OPEN_POINTS.md). Nothing here is decided or installed. Unreviewed.*

The task, from [handover 07](../../handovers/HANDOVER_07_2026-09-26_first-sandbox-steps.md): think through the
whole setup for the next sandbox — source, simulation, capture, landing, the loads the agent runs, and every
point where the author would otherwise have to act — before anything is installed. The measure is the
author's own: "I want to avoid manual work from my side as much as possible, this is the goal of the entire
excercise." Wide World Importers (`SRC-018`) is his current preference, not a decision; this note says what
it would take, and what the alternatives would cost.

## 1. What was checked on 2026-10-06

The facts below were checked from both working environments on 2026-10-06, unless marked otherwise.

1. **The backups are reachable without the author.** The release `wide-world-importers-v1.0` on GitHub
   carries `WideWorldImporters-Full.bak` (and a DW counterpart); a ranged download from the cloud workspace
   succeeded through `release-assets.githubusercontent.com`. The GitHub API itself is blocked. The release page
   says the Full backups restore on "any edition except LocalDB" and need about 10 GB of disk and 1.5 GB of
   memory for both databases.
2. **The simulator lives inside the database.** It is a set of T-SQL procedures in the schema
   `DataLoadSimulation` (source: `wwi-ssdt/wwi-ssdt/DataLoadSimulation` in `microsoft/sql-server-samples`,
   read in full for the two driving procedures). `PopulateDataToCurrentDate` runs from the day after the last
   order to *yesterday by the server's clock*. Underneath it, `DailyProcessToCreateHistory` takes any start and
   end date and processes one transaction per day. So the simulation could run on its own calendar, one
   simulated day at a time, without being tied to today's date.
3. **It inserts and updates, and deletes a little.** Each simulated day it receives purchase orders, takes
   customer orders, picks stock, invoices picked orders, records deliveries, processes customer payments, pays
   suppliers on Mondays, takes stock at quarter ends, adds customers, stock items and special deals, changes
   passwords, and makes "temporal changes" to reference data (cities, provinces, countries, delivery and
   payment methods). That is more than `EVI-OP-7` asks: updates were welcome, not required.
4. **History is written in simulated time.** Before a load it switches system-versioning off on the temporal
   tables and writes their archive tables itself, then switches it back on. The source therefore carries its
   own history, dated by the simulation rather than by the wall clock — useful for testing historisation.
5. **The released data starts on 1 January 2013** and ends on the day the backup was generated (Microsoft
   Learn, *WideWorldImporters data generation*). That end date is believed to be mid-2016 but was not
   verified. Bringing it up to today would mean simulating about ten years. One published run took "more than
   35 minutes" for about four and a half months on a Windows VM (mytecbits.com), which would put ten years at
   the order of fifteen hours. Point 2 makes that unnecessary.
6. **The procedures on GitHub are newer than the backup.** The source on `master` defaults to a start of 31
   December 2019 and records cold-room temperatures from December 2021, which the 2016 backup cannot know
   about. The procedure inside the backup may therefore behave differently from the one read. Unverified
   until a restore.
7. **SQL Server cannot run anywhere the agent controls today.** The cloud workspace has Docker and 7 GB of
   memory, but Docker Hub, Microsoft's container registry, GitHub's container registry and Microsoft's package
   server are all refused by its proxy, and the workspace is reclaimed overnight. The Linux shell on the
   author's computer is Ubuntu 22.04 with 2 GB of memory, no Docker, and the same refusals. Microsoft states
   2 GB as the minimum memory for SQL Server on Linux (from the model's knowledge; not checked today).
8. **Correction to handover 07.** The Linux shell on the author's computer now *does* reach GitHub and PyPI
   (Kaggle, 4TU and Microsoft's sites remain refused). It still cannot reach services on the Windows host:
   connecting to the host's gateway on port 1433 fails with "Network is unreachable".
9. **No independent port of the simulator was found.** One web search found no Postgres version of
   `DataLoadSimulation`; a port would have to be written by the model.

## 2. Where the source runs

Four routes, judged by the author's hands.

**A. SQL Server Developer edition on his Windows machine.** The simulator runs as Microsoft wrote it. The
author's hands would be needed once, to install the server; restoring the backup and creating the schedule
could be one script the model writes and he runs once as administrator. After that, nothing per refresh.
The price is that the agent cannot reach the server (finding 8), so everything it receives has to be put
into the repository folder by the Windows side (section 3), and anything that breaks on the Windows side
needs a hand that can reach it (section 5).

**B. A SQL Server the agent runs itself.** Not available in either environment (finding 7). It would remove
the author's hands entirely, so it is worth re-checking if the environments change, but it cannot be
designed on today.

**C. A port to Postgres or DuckDB.** Would run where the agent runs, with no hands at all. But the model
would be rewriting about four thousand lines of simulator (finding 9), and a landscape built by the party
being tested flatters it ([410](410_first-vertical-slice.md)). That is the property the choice of Wide
World Importers rests on.

**D. A different source that already runs where the agent runs.** The nearest is TPC-H in DuckDB
(`SRC-022`, on PyPI, with refresh functions for new and deleted orders). No hands at all, and not written by
the model; but it is a benchmark, not an ERP: uniform distributions, no reference-data changes, no own
history.

Route A is the only one that keeps both the simulator and the "not written by the model" property. Its cost
in hands is a few acts once, plus whatever breakage costs (section 5).

## 3. How new data would reach the agent (route A)

One scheduled job on Windows would do two things in sequence: advance the simulation (section 4), then
export what the database now holds into the repository's ignored data folder, for example
`data/raw/wwi/<simulated date>/`, one CSV file per table and a small manifest. The manifest would state the
simulated date, the row count and a hash per file. That gives the agent delivery identity and an arrival
schedule to check from the first day ([162](../10_architecture/162_test-framework.md)).

The Linux shell on his computer sees that folder, so the agent would read it there. Nothing would cross the
network.

The open choice is the shape of the extract:

- a **full extract every day** — simplest, and the agent works out what changed, as it would against a
  client's source without change capture; or
- **only the rows changed that day**, using the `LastEditedWhen` and validity columns the database carries
  (believed present on every table; not verified) — smaller, but it assumes the source tells the truth about
  its own changes.

## 4. Who advances the simulation

Windows Task Scheduler would run the job, set to run as soon as possible after a missed start, so a
computer that was off catches up when it comes back.

The open choice is the pace:

- **one simulated day per real day** looks most like a client's landscape but is slow;
- **several simulated days per run** gets to refreshes, quarter turns and maintenance (`CON-OP-16`) sooner.

On the agent's side, a scheduled task in Claude that is linked to his computer would run after the export:
check what arrived, load it, run the tests, and write a short report. Neither schedule needs him.

## 5. What happens when it breaks

The likely failures are these: the computer is off or asleep at the scheduled time (caught by catch-up, at
the cost of a late day); the SQL Server service is stopped; the simulator throws (it rolls back that day and
says so); or the export is partial.

All four would be noticed the same way. The manifest is missing, late, or does not match its files, and the
agent's arrival and delivery-identity checks say so. Noticing costs him nothing.

Repairing is the cost. Route A as drawn means every repair on the Windows side is one act by the author.
The alternative is to let the Codex server on his machine run `sqlcmd` with a sandbox wider than its present
read-only one. Then another model could diagnose and restart without him, at the price of giving an agent
write access on Windows. That is his decision; it is not needed on day one.

**Added 2026-10-07: noticing must not depend on the agentic layer.** On the evening of 2026-10-06 the author
asked whether "the entire machinery (data pipelines, data warehouse) should keep in working, even if the agentia
layer is down", and the model agreed. [ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md) already keeps
models out of the data path, for reproducibility; this adds availability. Read against this section, it would mean
that the arrival, delivery-identity and plausibility checks above are deterministic and run on the schedule whether
or not an agent runs, and that a failure raises a plain alert by itself — a file in the repository or a message —
which an agent picks up when it next runs, and which reaches the author only if no agent has dealt with it within an
agreed time. Where an agent does work at run time, the load does not wait for it: the work is queued and done when
the agent is back. Proposed, not ruled; the gates themselves are `ARC-OP-33`.

**Reviewed 2026-10-07:** [sol](../30_research/notes/XREV_2026-10-07_machinery-without-agents_sol.md) and [astra](../30_research/notes/XREV_2026-10-07_machinery-without-agents_astra.md) both FAIL the paragraph above. As 420 stands, the checks would
run when an agent runs, so with no agent nothing checks; and if the Windows scheduler stops or the computer stays
asleep, no job runs and no alert is raised, because a job that never started writes nothing. A timer that escalates to
the author would also turn ordinary overnight shutdowns into messages for him. Both found queued agent work consistent
with ADR-0004 as long as it is diagnosis and reporting; row processing still needs its own enrichment ADR. Recommended to
the author, not ruled, continuing the numbering in `ARC-OP-33`, `ARC-OP-20` and `ARC-OP-34`: (14) the checks run on
their own schedule, independent of agents and of the export, and catch up after the computer wakes; (15) either accept
that a machine that is off is noticed only when it wakes, or add one external missed-heartbeat notifier — his choice;
(16) no escalation timer in this sandbox: re-check before notifying, merge repeats, and tell him only of what is still
unresolved after the computer is back and an agent has run; (17) queued agent work is diagnosis and reporting, never
row processing.

**Ruled 2026-10-07 by the author** on recommendations 14 to 17:

> 14. agree
> 15. under normal circumstances, like a production environment, we would work with servers, which are always on except for maintenance windows.
> 16. okay
> 17. yes

Accepted: the checks run on their own schedule, independent of agents and of the export, and catch up after the
computer wakes (14); no escalation timer — re-check before notifying, merge repeats, report only what is still
unresolved (16); queued agent work is diagnosis and reporting, never row processing (17). On 15 he chose neither
option but set the frame: the target is a production environment on servers that are always on except for
maintenance windows. Read by the model, and confirmed below: an external heartbeat is not needed for the design, and in
this sandbox, which runs on his own computer, a machine that is off is noticed when it wakes — a limitation of the
sandbox, not of the design. Confirmed by the author on 2026-10-07: "Your interpretation is correct."

## 6. The frozen regression copy

The frozen copy for release regression (`ARC-OP-30`, [160](../10_architecture/160_evaluation-and-regression.md))
would come almost free. If extracts are kept per simulated date and never overwritten, the folders up to a
quarter's reference date *are* the frozen data set. A database backup at each quarter turn, taken by the
same job, would be a second copy if wanted. Nothing extra for him in either case.

## 7. The tests, kept small

The simulator's own parameters are a known truth that a client's data never offers: orders per working day,
the Saturday and Sunday shares, and seasonal and yearly variation within stated bands. The first plausibility
checks would therefore be back-of-the-envelope ones against those:

- daily order counts within the expected band;
- invoices following orders;
- payments following invoices;
- stock movements reconciling to stock take at quarter ends.

Delivery identity and the arrival schedule come from the manifest. Tooling would be whatever an ADR adopts
for [162](../10_architecture/162_test-framework.md); nothing is built before then.

## 8. Where the data model sits

The agent would declare the landed tables and its proposed vault in the text form drafted in
[142](../10_architecture/142_the-data-model.md), if `ARC-OP-29` is adopted. Wide World Importers offers
something the Utrecht sandbox lacked: Microsoft's own warehouse for it, `WideWorldImportersDW`, and the ETL
that loads it. That gives a reference to compare the agent's model and keys against, held back from the
agent as session 06 held back its answer key.

## 9. The author's hands, counted

| Route | Once | Per refresh | Per breakage |
|---|---|---|---|
| A, repairs by him | install SQL Server; run one setup script | none | one act |
| A, repairs by Codex | as above, plus widening Codex's sandbox | none | none, if Codex can fix it |
| B | — not available today — | | |
| C | none | none | none; but the simulator is the model's own |
| D | none | none | none; but not an ERP |

## 10. Decisions for the author

1. Which route (section 2). If A, nothing is installed until he says so.
2. The pace of the simulation (section 4).
3. The shape of the extract: full or changed rows (section 3).
4. Who repairs the Windows side: him, or Codex with a wider sandbox (section 5).

If he chooses A, the smallest next step would be for the model to write the one setup script, which would
restore the backup, create the export job and the schedule, and write the first extract. The script would be
reviewed before he runs it. The first extract would answer findings 5 and 6, which cannot be settled before
then.

## 11. Ruled 2026-10-07 by the author

On the four decisions of section 10, verbatim:

> Yes, let's do 420. I suspect that Route A would work best. I am for it, if you can access a local database. How
> fast the simulation advances, we don't need to put it on a timer, we can just advance one day at a mouseclick, if
> you know what i mean. We could advance the days at will, advance a day, analyse what happened, then next day. Not
> sure about c. With regards, I'll do d.

The model read "c" and "d" as decisions 3 and 4 and proposed what follows; he confirmed: "Yes."

1. **Route A**, on the condition that the agent can reach the local database. Checked the same morning: Codex on his
   Windows machine runs commands in its read-only sandbox (`hostname`, `where.exe`, `Test-NetConnection`); no SQL
   Server, no `sqlcmd`, nothing on port 1433 yet. The agent's own route is a **request folder**: a small Windows job
   watches a folder in the repository, runs only a fixed list of actions (advance one simulated day; export; run a
   query under a read-only login), and writes the result back. Codex with `sqlcmd` is a second, read-only route,
   unverified until a server exists.
2. **Pace: on demand, one simulated day per request**, not on a timer: advance a day, analyse what happened, then the
   next. The request is normally the agent's, so stepping does not need his hands; a desktop shortcut lets him step
   it himself. Section 4's Task Scheduler cadence is replaced by this; the checks of section 5 still run on their own
   schedule (recommendation 14).
3. **Extract: full every day to start**, measured after the first extract; changed rows only if the size calls for it.
4. **Repairs on the Windows side: by the author.** Codex's sandbox stays read-only.

**Next:** he installs SQL Server Developer edition and `sqlcmd` (an overview was given in the conversation); the model
writes the one setup script — restore the backup, a read-only login, the request-folder job, the first extract —
which goes to sol and astra before he runs it.

**Installed 2026-10-07 by the author; checked the same evening through Codex.** SQL Server 2025 runs as the default
instance `MSSQLSERVER` (automatic start), with the full-text launcher. `sqlcmd` is at `C:\Program Files\SqlCmd\` (go)
and in the ODBC 18 client tools, but not on the Codex server's `PATH`. Codex **cannot connect from its sandbox**: both
clients fail on Windows authentication ("AcquireCredentialsHandle failed 8009030e"; "Geen referenties beschikbaar in het
beveiligingspakket"), so the sandboxed process has no credentials to present. The second route of point 1 is therefore
closed while Codex stays sandboxed; the request-folder job, which runs as the author under Task Scheduler, is not
affected. Free space on C: was 9.8 GB, against the release page's 10 GB for both databases; only the OLTP database is
needed, but the margin is small.

## Sources

- Microsoft, `sql-server-samples`, `samples/databases/wide-world-importers/wwi-ssdt/wwi-ssdt/DataLoadSimulation`,
  GitHub, read 2026-10-06.
- Microsoft, release `wide-world-importers-v1.0`, GitHub, read 2026-10-06.
- Microsoft Learn, *WideWorldImporters data generation*,
  <https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-generate-data>, read 2026-10-06.
- My Tec Bits, *Generating more data in WideWorldImporters*,
  <https://www.mytecbits.com/microsoft/sql-server/generating-more-data-in-wideworldimporters>, read 2026-10-06.
