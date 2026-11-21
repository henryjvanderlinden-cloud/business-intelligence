# Wide World Importers sandbox

**Question.** Can a simulated ERP be advanced, extracted and queried by the agent, one simulated day at a time,
with no act from the author per day? (`EVI-OP-7`; route A of
[420](../../docs/40_roadmap/420_next-sandbox-setup.md), ruled 2026-10-07.)

**Answer, first evidence (2026-10-07).** Yes for one day: after setup (three runs by the author, two defects fixed), the agent advanced 2016-06-01 and received its full extract with no act by him. Whether it holds over many days is not yet known.

**Second day (2026-10-20).** The agent requested `advance` for one day at 08:09 UTC; the job simulated 2016-06-02 (a Thursday, 115 new orders) in 86 seconds and wrote its full extract by 08:17, with no act by the author. The newest three extracts (2016-05-31 to 2016-06-02) are all kept.

## The pieces

`setup.ps1` is run once by the author, as administrator. It restores Microsoft's `WideWorldImporters-Full.bak` into the
SQL Server on his machine, adds a simulation clock (`nsdn.SimulationClock`) and a read-only database user
(`nsdn_reader`), writes an inventory of what it restored to `data/wwi/inventory/`, installs pinned copies of the two
scripts below in `C:\ProgramData\nsdn-wwi\`, registers the task `nsdn-wwi-job`, puts a shortcut on his desktop, and
tests the path end to end. It can be run again; it keeps an existing database unless given `-Reset`.

`job.ps1` runs every minute as the author, without a window. It handles request files in `data/wwi/requests/` and
answers in `data/wwi/responses/`. It knows seven actions and no others; the last three, and the generation after
every export, were added for the second source (see *The customer system* below):

| request | does |
|---|---|
| `{"action":"status"}` | simulated date, row counts, database file sizes, free disk space |
| `{"action":"advance","days":1}` | runs Microsoft's simulator for the next simulated day (1 to 7 days), then a full extract of each day |
| `{"action":"export"}` | a full extract of the current simulated day |
| `{"action":"query","sql":"SELECT …"}` | runs the SQL as `nsdn_reader` (`EXECUTE AS … WITH NO REVERT`), result as CSV beside the response, at most 100 000 rows or 200 MB, each text or binary value cut at 100 000 characters or bytes; spatial columns must be selected as `col.ToString()` |

| `{"action":"generate","date":"YYYY-MM-DD"}` | the customer system's extract for a date whose WWI extract is present; also run after every export |
| `{"action":"freeze","experiment":"E1","date":"YYYY-MM-DD"}` | freezes an experiment: both extracts copied into `data/frozen/E1/`, with the development list |
| `{"action":"score","experiment":"E1","part":"development","proposals":"data/proposals/…csv"}` | figures only, never a verdict per record; `part` `holdback` takes both methods' files and cutoffs, once |

`request.ps1` only writes a request file; the desktop shortcut uses it to request `advance`.

## The agent's side

Write the request as `<id>.json.tmp` in `data/wwi/requests/`, then rename it to `<id>.json`; the job never reads a
`.tmp`. Read `data/wwi/responses/<id>.json` (and `<id>.csv` for a query). The job moves each request to
`data/wwi/processed/` before acting on it, so a request never runs twice. `data/wwi/heartbeat.json` is rewritten on
every run; `data/wwi/job.log` keeps a line per request.

An extract is `data/raw/wwi/<simulated date>/`: one `<schema>.<table>.csv.gz` per table, all tables outside the
simulator's own schema, ordered by primary key, and a `manifest.json` with rows, bytes and SHA-256 per file. CSV is RFC
4180 in UTF-8; every value is quoted, and NULL is an empty unquoted field. Spatial columns are given as WKT text. The
folder appears complete or not at all. The newest three dated folders are kept; `data/frozen/` is never touched.

## The customer system (added 2026-11, ADR-0043, ADR-0044)

A second, messy source for the falsifiable core of [410](../../docs/40_roadmap/410_first-vertical-slice.md): WWI's
customers as an independently built customer system would hold them, designed in
[430](../../docs/40_roadmap/430_second-source-and-answer-key.md). Its generator, freeze and scorer are written by sol
and live in `C:\nsdn-holdout\`, outside this repository, with the answer key; `setup.ps1` copies the scripts into the
pinned folder's `holdout\`. The model that proposes matches never reads that folder.

After every export the job runs the generator on the new extract. Its extract is `data/raw/crm/<date>/`, published
atomically after the key and a readiness record are written in the hidden folder; it is deleted when the WWI extract of
the same date is. A failed generation leaves the export standing, is reported with a fixed code and no detail, and is
repeated with `generate`. Proposals for scoring go in `data/proposals/`, which, like all of `data/`, is not in git.

## Limits, known in advance

The job can only do what it was installed with. A change to `job.ps1` reaches the machine only when the author runs
`setup.ps1` again, which is the price of the agent not being able to run arbitrary code on Windows.

The procedures in the 2016 backup may differ from those on GitHub (finding 6 of 420). The job passes only the
parameters the restored procedure declares, and if `Configuration_ApplyDataLoadSimulationProcedures` exists it calls it
before each day and `…Remove…` after it, as the released database requires; the inventory keeps both procedure texts
so this can be checked before the first `advance`.

The people, customers and suppliers in the data are Microsoft's fictitious sample records.

## The warehouse runner (added 2026-10-11, ADR-0015)

`runner.py` is the second scheduled task, `nsdn-wwi-runner`, every minute as the author, from a pinned copy with its own
Python environment in `C:\ProgramData\nsdn-wwi\` (Python 3.12.15 installed by uv 0.13.0; dbt-core 1.12.5, dbt-duckdb
1.11.0 and DuckDB 1.5.6 from `requirements.txt`, which carries hashes). Nothing goes on the PATH or into the registry.

Each run it looks for complete extracts newer than the last date loaded. For each, oldest first, it checks that the
date is the next one expected and that every file matches the manifest (SHA-256 and row count), lands the files as
text into the schema `landing` of `data/warehouse/wwi.duckdb` (one table per source table, `schema__table` in lower
case, with `_nsdn_load_date`), and runs `dbt build` on the project in `dbt/` **as it stands in the repository**. Every
attempt goes into `nsdn_meta.load_log`. After a successful load it copies the warehouse to
`data/warehouse/published/wwi.duckdb`, which is the copy to read. If the dbt project changes and no new extract is
waiting, it rebuilds the latest date with the new project, so new SQL goes live within a minute.

It writes `data/warehouse/status.json` on every run and `data/warehouse/alerts/<time>-<kind>.json` on every failure.
A failed date is retried only when the dbt project or the extract changes, and a later date is never loaded past a
failed or missing one ("expected 2016-06-02 next, found 2016-06-03").

**Confinement.** Only the runner's landing step reads files. dbt connects through the pinned `profiles/profiles.yml`,
which opens DuckDB with file-system access off and the configuration locked, so the project's SQL can read and write
only tables in the warehouse: `read_csv`, `COPY`, `ATTACH`, `INSTALL` and switching the setting back all fail (tested
2026-10-11). The runner refuses a project containing any `.py` file, `packages.yml`, `dependencies.yml` or
`profiles.yml`, because those would run code or change the connection outside that confinement. There is no change
gate (the author's ruling of 2026-10-11).

**Tested 2026-10-11** in the agent's Linux shell on copies of the two real extracts, under Python 3.12: both days
loaded (4.7 million rows landed per day, about 30 to 45 seconds each, warehouse about 390 MB), and the idle run, the
rebuild after a project change, a broken model, a model reading a file, a Python model and a missing day each behaved
as described. Not yet run on Windows.

**Disk.** The environment takes about 0.5 GB and each warehouse copy about 0.4 GB, about 1.3 GB in all; setup refuses
to install it with less than 3.5 GB free, so that the job's 2 GB floor for extracts still holds afterwards.

**Known limit, postponed by the author (420 §12, G).** The job keeps only the newest three extracts. Advance one day at
a time, so that no extract is pruned before the runner has loaded it.

## When a day fails

Before it runs a day the job writes `data/wwi/advance-in-flight.txt`, and it removes the file only once the day has
run and the clock has moved. If the file is still there, a day started and did not finish: the simulator may have
committed part of it, and it switches system-versioning off on the temporal tables while it runs, so it may also have
left those switched off. Running the same date again could double it, so every further `advance` is refused while the
file exists. The agent reports it; the repair is the author's, by `setup.ps1 -Reset`, which restores the database
afresh and loses the simulated days.

If the day ran but its export failed, the clock has moved and the response says so; an `export` request repeats the
extract for that date. Nothing is lost.
