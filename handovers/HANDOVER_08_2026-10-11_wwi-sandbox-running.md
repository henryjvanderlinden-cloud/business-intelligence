# nsdn — Handover 08: the Wide World Importers sandbox runs, and the agent advances it without the author
## Written 2026-10-11 at the close of session 07

> **STATUS: HISTORICAL (superseded 2026-10-21)** by
> [HANDOVER_09_2026-10-21_analysis-closed-generic-layer-next.md](HANDOVER_09_2026-10-21_analysis-closed-generic-layer-next.md).

---

## First actions

1. `git status`, then `git log --oneline -15`. Expect HEAD at the commit that closed S07 (message begins "Close session
   07"). The author pushes himself; if `origin/main` is behind, ask, do not push.
2. `python tools/check_repo.py` — must pass. **Run it on its own, never piped** (`| tail` hides the exit status; it
   happened again in S07, commit `35c9e99`, corrected in `7be6f50`). Expect 7 sessions, S07 closed with `AUD-S07-1`.
3. Read [420 §11](../docs/40_roadmap/420_next-sandbox-setup.md) and the sandbox's
   [README](../prototypes/wwi_sandbox/README.md). Together they are the whole operating manual.
4. Ask the job for its status before anything else (see *Driving the sandbox*). Expect simulated date 2016-06-01 and
   about 4 GB free, unless the author has changed something since.
5. Open session S08 in `records/sessions.jsonl` and log from S08-001.

## Where we stand

**Route A is built and running** (`EVI-OP-7`). Wide World Importers runs on SQL Server 2025 Enterprise Developer
(default instance, Windows authentication) on the author's Windows machine. Setup restored Microsoft's 2016 backup
(data 2013-01-01 to 2016-05-31, 3.1 GB), added `nsdn.SimulationClock` and the read-only user `nsdn_reader`, and
installed a request-folder job that the scheduled task `nsdn-wwi-job` runs every minute as the author, with no window
and no stored password. **On 2026-10-07 the agent advanced the first simulated day, 2016-06-01, alone, by a request
file**: 58 new orders, 50 seconds, and a full extract written. Between the 31 May and 1 June extracts, 15 of 48
tables changed, by inserts and updates. Nothing else has been advanced since.

**The author can look at the data himself** in SSMS 22 (`localhost`, Windows authentication, *Trust Server
Certificate* ticked). He was asked not to edit rows or run the simulator's procedures by hand: the clock and the
extracts assume only the job changes the database.

**What it cost him**, for the post-mortem: installing SQL Server and `sqlcmd`, three runs of `setup.ps1` (two script
defects, below), installing SSMS, and freeing disk space twice. From the first advance onwards the cost per
simulated day is nil.

## Task for the next session, in one sentence

Advance the simulation and, with the author, decide what the agent builds first on the daily extracts.

Do not jump ahead: everything about the build is unruled. Put the choices to him as decisions. Candidates already in
the repository: landing the extracts and the first loads (410, ADR-0004), the plausibility checks on every load and
the release regression (160, 162; adoption needs ADRs), the data model as text declarations (142, `ARC-OP-29`), the
agent team for the first build (`ARC-OP-34`), and quality gates (`ARC-OP-33`). The quarter turn on 2016-06-30 is the
first natural point for a frozen regression copy (`ARC-OP-30`).

## Driving the sandbox

Write `{"action":"…"}` to `data/wwi/requests/<id>.json.tmp`, then rename it to `.json`; read
`data/wwi/responses/<id>.json` within a minute or two. Four actions only: `status`, `advance` (`"days"`, 1 to 7, each
day exported), `export`, and `query` (`"sql"`, run as `nsdn_reader`, capped). An extract is
`data/raw/wwi/<simulated date>/`, 48 gzipped CSV files with a `manifest.json` (rows, bytes, SHA-256); the newest three
are kept. `data/wwi/heartbeat.json` shows the job is alive. Details and failure handling are in the README.

**The job is a pinned copy** in `C:\ProgramData\nsdn-wwi\`, writable only by administrators. Editing
`prototypes/wwi_sandbox/job.ps1` changes nothing until the author runs `setup.ps1` again (it keeps the database). That
is deliberate: it is what stops the agent from running arbitrary code on Windows. Batch changes to the job so that he
reruns setup rarely.

**If `data/wwi/advance-in-flight.txt` exists, advancing is halted**: a day started and did not finish. Report it; the
repair is his (`setup.ps1 -Reset`, which loses the simulated days). He ruled on 2026-10-07 that Windows-side repairs
are his and that Codex's sandbox stays read-only.

## Outstanding actions for the author, not the model

**Push** (he said on 2026-10-10 that he pushes himself).

**Rule the two guards** from session 06 if they are to stand: no de-anonymising business-for-sale listings; no named
individuals. Still open since handover 07.

## How to work with the author

As in handover 07: plain English, numbered; propose, let him react, write what he settles; quote him verbatim;
external review on sol and astra in parallel, framed against the standard the object must meet (`PRC-OP-7`). Keep
the apparatus small. **Minimising his manual work is the goal of the exercise**, not a convenience: count every act
you ask of him, and say before asking what it saves him. Do not jump to conclusions from what he says; everything is
tentative until he rules it. He will say when a session is long.

## Traps and warnings

**A reviewed script is not a tested one.** Sol and astra reviewed `setup.ps1` over several rounds; it still failed
twice on its first real run, on things a static review cannot see: `icacls /T` applied folder inheritance flags to
files and left them unreadable, and `Measure-Object -Property` cannot sum hashtable keys in PowerShell 5.1. Prefer a
cheap real run (Codex can execute read-only PowerShell, e.g. parsing, compiling, an in-memory test) over another
review round.

**Disk is tight.** C: had 4.16 GB free on 2026-10-11. The job refuses an extract below 2 GB, and a day advanced while
extracts are refused leaves its export to be repeated. Each extract is about 61 MB; the database grows with every
day. Check `free_gb` in each response and warn him early.

**The device file bridge can serve a stale copy.** `device_commit_files` once wrote an earlier version of a staged
file. After committing files to the computer, compare SHA-256 on the device before relying on them; stage each new
version under a new path.

**Codex cannot log in to SQL Server** from its sandbox ("no credentials available in the security package"), with
either `sqlcmd`. The request folder is the agent's only route to the database. Codex calls through the bridge time out
after 60 seconds while the run continues: have it write to `scratch/` and read the file.

**The checker shapes the labels.** `AUD-S07-1` (astra, 20 steps) agreed on actor 20, role 19, activity 15, outcome
17, work class 11, task type 7, tier 5. For the setup steps the recorder chose `repo-maintenance` because the checker
demands registered assets for `source-acquisition`; the auditor chose `source-acquisition`, which is what they were.
And the recorder writes tier `none` where the auditor sees semantic or structural claims. Register the WWI database
and its extracts as assets (`SRC-018`) before the first load, so data steps can carry their true type. Whether the
tier field earns its keep is a question for the author, not a fix to make silently.

**Another conversation may be writing to the repository at the same time.** It happened twice in S07 (the
overview schematic of 8 to 10 October, steps S07-134 to S07-140). Check `git log` and the last step id before
writing.

**The cloud workspace is reclaimed overnight**; the scripts' working copies there are gone. The repository holds
everything.

## What session 07 did

Session 07 ran from 26 September to 11 October across several conversations. It parked the Utrecht sandbox
(`EVI-OP-2`) and opened `EVI-OP-7`; recorded release regression (160, `ARC-OP-30`), the test framework and
plausibility (162, `ARC-OP-31`), the OKF assessment (`ARC-OP-32`), the data model note (142, `ARC-OP-29`), and the
author's points on quality gates, a text-only codebase, the machinery without agents and an agent team (`ARC-OP-33`,
`ARC-OP-20`, `ARC-OP-34`), with his rulings on seventeen review recommendations. It designed the next sandbox end to
end in 420, got the author's rulings on route, pace, extract shape and repairs, built and ran it, and advanced the
first day. In parallel it brought the overview schematic up to date and made an A4 print version for a potential
client (080). It closed with the blind audit `AUD-S07-1`.

## Do not reopen

Everything in handovers 06 and 07, plus:

- Route A: Wide World Importers on SQL Server on the author's machine, not a port and not TPC-H (420 §11).
- The simulation advances on request, one day at a time, not on a timer; the request is normally the agent's.
- Full extract every day to start; changed rows only if the size calls for it, measured first.
- Windows-side repairs are the author's; Codex's sandbox stays read-only.
- Everything stays on C:; a database on removable storage was declined.
- The machinery's checks run on their own schedule, independent of agents; no escalation timer; queued agent work is
  diagnosis and reporting, never row processing (rulings of 2026-10-07, 420 §5).

## What was not done

Only one day has been simulated. No load, model, test or plausibility check has been built on the extracts. The WWI
database and extracts are not yet registered as assets. Nothing was measured for `CON-OP-16`.
