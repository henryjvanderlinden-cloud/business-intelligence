# Wide World Importers sandbox

**Question.** Can a simulated ERP be advanced, extracted and queried by the agent, one simulated day at a time,
with no act from the author per day? (`EVI-OP-7`; route A of
[420](../../docs/40_roadmap/420_next-sandbox-setup.md), ruled 2026-10-07.)

**Answer, first evidence (2026-10-07).** Yes for one day: after setup (three runs by the author, two defects fixed), the agent advanced 2016-06-01 and received its full extract with no act by him. Whether it holds over many days is not yet known.

## The pieces

`setup.ps1` is run once by the author, as administrator. It restores Microsoft's `WideWorldImporters-Full.bak` into the
SQL Server on his machine, adds a simulation clock (`nsdn.SimulationClock`) and a read-only database user
(`nsdn_reader`), writes an inventory of what it restored to `data/wwi/inventory/`, installs pinned copies of the two
scripts below in `C:\ProgramData\nsdn-wwi\`, registers the task `nsdn-wwi-job`, puts a shortcut on his desktop, and
tests the path end to end. It can be run again; it keeps an existing database unless given `-Reset`.

`job.ps1` runs every minute as the author, without a window. It handles request files in `data/wwi/requests/` and
answers in `data/wwi/responses/`. It knows four actions and no others:

| request | does |
|---|---|
| `{"action":"status"}` | simulated date, row counts, database file sizes, free disk space |
| `{"action":"advance","days":1}` | runs Microsoft's simulator for the next simulated day (1 to 7 days), then a full extract of each day |
| `{"action":"export"}` | a full extract of the current simulated day |
| `{"action":"query","sql":"SELECT …"}` | runs the SQL as `nsdn_reader` (`EXECUTE AS … WITH NO REVERT`), result as CSV beside the response, at most 100 000 rows or 200 MB, each text or binary value cut at 100 000 characters or bytes; spatial columns must be selected as `col.ToString()` |

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

## Limits, known in advance

The job can only do what it was installed with. A change to `job.ps1` reaches the machine only when the author runs
`setup.ps1` again, which is the price of the agent not being able to run arbitrary code on Windows.

The procedures in the 2016 backup may differ from those on GitHub (finding 6 of 420). The job passes only the
parameters the restored procedure declares, and if `Configuration_ApplyDataLoadSimulationProcedures` exists it calls it
before each day and `…Remove…` after it, as the released database requires; the inventory keeps both procedure texts
so this can be checked before the first `advance`.

The people, customers and suppliers in the data are Microsoft's fictitious sample records.

## When a day fails

Before it runs a day the job writes `data/wwi/advance-in-flight.txt`, and it removes the file only once the day has
run and the clock has moved. If the file is still there, a day started and did not finish: the simulator may have
committed part of it, and it switches system-versioning off on the temporal tables while it runs, so it may also have
left those switched off. Running the same date again could double it, so every further `advance` is refused while the
file exists. The agent reports it; the repair is the author's, by `setup.ps1 -Reset`, which restores the database
afresh and loses the simulated days.

If the day ran but its export failed, the clock has moved and the response says so; an `export` request repeats the
extract for that date. Nothing is lost.
