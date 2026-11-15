# 030 — Incremental capture: growth classes, watermarks with overlap, and two kinds of verification

**Status: proposed 2026-11-15, session 12, by Claude Opus 5.5 on the author's instruction; reviewed on sol, which failed
the first version ([XREV](../notes/XREV_2026-11-15_030-incremental-capture_sol.md)); this is the revised text, itself
unreviewed; nothing in it is ruled.** An answer-side file of the [equivalence investigation](README.md). It answers capability 2 (incremental
capture) of [010](010_capability-inventory.md) in part, and touches capability 4 (scale). It is step 1 and the start of
step 3 of the method of [ADR-0038](../../20_decisions/0038-etl-capability-equivalence-investigation.md); step 2, a
client's own requirements, is set out as questions in §6 and not answered.

**Where it comes from.** On 2026-11-06 the author asked, verbatim:

> Is there a certain pattern to discerned from the cold-room staging? Mind you, the WWI database is just an example. We
> want to generate generally applicable knowledge here, that is the main goal.

The model's answer proposed this note; on 2026-11-15 he replied "okay go ahead". The general assessment of 2026-11-14
makes the same point from the other side (its item 11: "Load time is a warning sign").

**Provenance.** WWI figures come from the sandbox's records (`runner.log`, dbt's `run_results.json`, the extracts'
manifests) and are reproducible from the repository. The statement about SQL Server's period columns rests on
Microsoft's documentation (§8). Everything else is the model's reasoning and is to be read as a proposal.

## 1. The finding: the load pays for what is delivered, not for what changed

1. Every day the WWI extract delivers the whole history of `Warehouse.ColdRoomTemperatures`, 3.7 million rows, of which
   about 22,000 are new (0.6 %). Until generator 0.3.0 every load re-read, re-hashed and re-checked all of them. On the
   author's machine that was about three of the 9.5 minutes of a day's rebuild after 0.2.1 (staging 69 s, its nothing-dropped
   test 74 s, the audit completeness test 36 s; S12-027).
2. The cost of a load therefore grew with the total history, while the useful work grows only with the day's change.
   The gap widens every day, in every table that keeps its past.
3. The cold room is only the first table where it shows, because it is the largest. Stock-item transactions, invoice
   lines, customer transactions and vehicle readings accumulate the same way, more slowly. At a client: ledgers, event
   logs, telemetry and audit trails.
4. **The general rule proposed: the cost of a load should be proportional to the change; anything proportional to the
   total history needs a reason.** "We verify the whole history" can be such a reason, but then it is a choice with a
   frequency (§4), not a side effect.

## 2. Growth classes: how a table behaves over time

The information-analysis phase can put every source table *provisionally* in one of these classes, from evidence:

| Class | Behaviour | Typical | Example in WWI |
|---|---|---|---|
| static | does not change between extracts | code lists, calendars | `Application.Countries` |
| slowly changing | few existing rows change, few are added | master data | `Sales.Customers`, `Application.People` |
| settling | rows are added, change for a while, then freeze | orders, invoices, cases | `Sales.Orders` (picking completed later) |
| accumulating | rows are added and never change once written or closed | ledgers, transactions, readings | `Warehouse.StockItemTransactions`, `Warehouse.VehicleTemperatures` |
| churning | a large share of existing rows changes every day | balances, stock levels, statuses | `Warehouse.StockItemHoldings` |

1. **The measures**, from two or more consecutive complete extracts: rows added per day; share of existing rows changed
   per day (by key and row hash); share removed; and, for a table with a history table, the ratio of history rows to
   current rows and the age at which rows stop changing. These are counts, computable by a generated query, with no
   knowledge of the business.
2. **A signature worth naming: an event stream kept as a versioned table.** `ColdRoomTemperatures` has 4 current rows
   (one per sensor) and 3.7 million history rows: every reading overwrites the previous one, and the history *is* the
   data. A tiny current table over a vast history, with every update closing the previous version, is detectable from
   the catalogue and a row count, and tells the loader that the history is an accumulating set.
3. **A history table kept by the database engine is accumulating by construction**, whatever the class of its current
   table. SQL Server writes a version into the history table when it is closed; while system versioning is on, no
   user can change or delete history rows, whatever their permissions (§8). This needs no profiling: it follows from
   the declarations `system_time` and `history` in the source file. **The condition matters**: with versioning
   switched off, anyone with the rights can edit or delete history, and a retention policy deletes old history on its
   own (§8). A deletion of old history costs the vault nothing (it keeps what it has); an edit made with versioning off
   is seen only by the full reread of §4 item 4, where the rewritten-version test (143 §10 item 4: the whole-row hash of
   each staged version against the one stored in the audit satellite) fails the build.
4. **A class observed is a hypothesis, not a guarantee** (review, finding 5). Two or ten extracts show what happened in
   those intervals, not that a row will never change. A table that looked accumulating can be corrected in place
   tomorrow, without its timestamp moving, and a watermarked read would never see it; recomputing the measures does not
   help, because seeing an old row change means reading the old rows. So the class is recorded with confidence and
   reasoning, like every item of the analysis record, and **a watermark that skips old rows needs a guarantee from the
   source**, not only observed behaviour: the database engine's (§2 item 3), a documented contract of the application,
   or an explicit change feed. Without one, the table is read in full, or reread in full often enough (§4 item 4) that a
   miss is found within an interval the client accepts.

## 3. The pattern for each class

1. **Static and slowly changing: read in full.** They are small; a full comparison is the simplest correct method.
2. **Accumulating, with a guarantee (§2 item 4): read from a watermark, with an overlap.** Read only what lies beyond the highest point already
   loaded, less a margin. The vault's rule "insert only what is not yet there" (143 §5) makes re-reading the margin
   harmless, so the overlap costs time but never correctness.
3. **Settling: watermark on the edit time, with an overlap**, only if the source guarantees that every change moves the
   edit time (`LastEditedWhen` in WWI is set by the application, so that is a claim about the application to be
   confirmed, not a fact about the database); otherwise read in full, or ask the source for a change feed.
4. **Churning: a change feed from the source** (the database's change tracking or log-based capture), or a full read.
   A watermark does not help when any old row can change.
5. **Deletions** remain visible only where the source shows them: as absence from a complete extract (`127`), as the
   closing time of a version in an engine-kept history (143 §13 item 7), or as an explicit event in a change feed. A
   watermarked read of an accumulating history still sees deletions, because a deleted row's last version is closed,
   and so written to the history, at the time of the deletion.

## 4. When a watermark is safe

1. **The watermark column must not run behind the moment a row becomes visible.** It often does. SQL Server stamps
   both period columns with the *begin* time of the transaction, not its commit time (§8). A transaction that started
   before an extract and committed after it writes rows with times earlier than rows the extract already held. A strict
   watermark would miss them forever. The same holds for application columns such as "last modified".
2. **Hence an overlap**: read again everything within a margin behind the watermark. The margin must exceed the
   longest transaction (or, for an application column, the longest delay between stamping and committing). It is a
   property of the source, to be stated with evidence, not a constant of the loader.
3. **Hence a tripwire**: the late-arrival test (143 §10 item 5) already reports any version older than the latest
   loaded; a row that arrives inside the overlap is caught and loaded normally.
4. **Hence a backstop**: at a fixed interval the whole set is read anyway, and anything the watermark missed is loaded
   then, as a late arrival with its own knowledge time. The interval bounds how long a miss can stay unseen **only if
   the missed row is still in the source at the next full reread** (review, finding 4). A retention policy or a purge
   that removes history before then can remove a missed row unseen. So the reread interval must be shorter than any
   retention or purge period of the source, and that is a requirement to check per source (§6).
5. **The watermark is taken from the warehouse, not from the extract**: from the model that keeps every version of the
   table, counting only rows written by successful runs (143 §13 item 5). So a failed load does not move it.
6. **A watermark must not split a group of versions that share a source time.** Where versions with the same key and
   the same source time are told apart by their position (`source_seq`, 143 §6 item 2), the numbering depends on which
   members of the group are read. Leave out an old zero-length version and its successor, still current, moves from
   number 2 to number 1: to the vault that is the same version with different content. The first trial run showed
   exactly that on the second day (§7 item 4). The rule: read, besides the rows beyond the watermark, every other row
   with the same key and source time as one of them. In general: **anything that identifies a version by its position
   among others must see the whole group, so a partial read is safe only along boundaries no such group crosses.**

## 5. Two kinds of verification

1. **Daily, on the increment**: did every row delivered since the watermark arrive, exactly once? The nothing-dropped
   test compares delivered and staged rows by control totals over the whole-row hash and period end: a count and two
   independent 64-bit hash sums, so one row twice and another missing changes them. The first version compared only
   counts, which that case passes (review, finding 3); the second compared the rows as multisets, which needed 3.6 GB
   on a whole-history day and failed on the author's machine with the operating system out of memory (§7 item 7).
   Control totals stream in one pass (379 MB peak for the same data). The completeness test then checks every staged
   version against the audit satellite. **Memory is a constraint of the general rule too**: in the sandbox DuckDB
   cannot spill to disk (external access is off), so a check over the whole history must stream.
2. **Periodic, on the whole**: the full reread of §4 item 4, with the same tests over everything. Cheaper alternatives
   for very large sets, not built: control totals (count and hash sum per day or per partition), compared each day,
   with only the partitions whose totals moved read in full.
3. Proving the entire history again every night, as nsdn did until 0.3.0, is the expensive end of a range, and a
   legitimate choice for a small or regulated source. It should be chosen, with its frequency, not inherited.

## 6. Step 2 of the method: what a client's environment decides

Questions for each client and source, to be answered there, not here:

1. Which classes do its tables fall into, and how large are the accumulating ones?
2. Does the source offer a change feed (change tracking, log-based capture, an outbox, an API with "changed since")?
   Who may enable it, and at what cost to the source system?
3. Which timestamps exist, who sets them, and is there evidence of how far they can run behind commit?
4. What reread interval is acceptable, given how long a missed row may stay unseen (a question of risk, and for a
   bank of BCBS 239)?
5. **Is the extract one consistent snapshot?** Where the current table and its history are copied one after the other,
   a transaction that commits in between leaves a group of versions that share a start time incomplete in that extract,
   and its numbering (`source_seq`) changes the next day (review, finding 1). This holds for full reads as much as for
   watermarks; the rewritten-version test then fails the build. The extract must read all tables of a source in one
   snapshot (snapshot isolation, or a database snapshot). In the WWI sandbox the database is written to only by the
   sandbox job itself, which runs one request at a time and exports after it has simulated, so its extracts are
   consistent; at a client this is a requirement. The deeper weakness is that `source_seq`
   identifies a version by its position; an identity that does not depend on which other rows are present would remove
   the risk, and is not designed yet (§8).
6. **What the extract itself should deliver.** The cheapest fix is often upstream: an extract that carries only the
   history rows closed since the previous extract, plus the full current tables, instead of copies of growing history
   tables. This belongs in an extract specification nsdn can hand to every client, with the overlap, the reread
   interval and the snapshot requirement as stated parameters.

## 7. The trial on WWI (generator 0.3.0)

What was built, as a first test of §3 item 2 and §4 on the one place in WWI where the rule follows from the
declarations alone (§2 item 3):

1. For each system-versioned table, staging reads all current rows, the history rows whose period end (`ValidTo`)
   lies after the latest source time already loaded for that table less an overlap of one day, and every other history
   row with the same key and start time as one of those (§4 item 6). The latest
   source time is read from the audit satellite (or, for a reference table, the reference table), counting only rows of
   successful runs.
2. The whole history is read on the first load, every Sunday (the backstop, §4 item 4), and when the dbt variable
   `full_history` is set. The bound used is kept in the staging table (`_history_from`), and the nothing-dropped test
   counts against the same bound.
3. Tables without an engine-kept history are read in full as before; their classes (§2) are not yet recorded, so no
   watermark is used for them.

4. **First run, without the rule of §4 item 6: failed on its second day, loudly.** The rewritten-version test reported
   3 versions in `Application.StateProvinces` and 1 in `Sales.Customers`, the tables with zero-length versions: the
   watermark had left out old zero-length rows and renumbered the current rows that share their start time. Nothing
   wrong reached a published vault, because the build failed.

5. **Second run, with the rule: passed.** Five days, 2016-05-31 to 06-04, in the cloud workspace, with the runner's
   landing code and versions:

   | Day | Load | Cold-room rows staged | Bound used |
   |---|---|---|---|
   | 2016-05-31 | 157 s | 3,654,740 | none (first load, whole history) |
   | 2016-06-01 | 105 s | 44,544 | 2016-05-30T23:59:24 |
   | 2016-06-02 | 107 s | 44,540 | 2016-05-31T23:59:29 |
   | 2016-06-03 | 101 s | 45,148 | 2016-06-01T23:59:20 |
   | 2016-06-04 | 101 s | 44,676 | 2016-06-02T23:59:28 |

   The same days took 317 and 330 seconds each with generator 0.2.1 in the same workspace. All 777 tests passed every
   day. **The resulting vault is identical, in all 216 tables, to the one built by reading every history in full**
   (content fingerprints without `load_run`). About 44,500 rows are staged a day for 22,000 new: the one-day overlap
   reads the previous day again.
6. **After sol's review, on the final code:** the cloud suite's eight checks pass over the five extracts and two
   constructed days, one a Sunday (whole history) and one a Monday (watermark): loading twice changes nothing; a
   failed batch, and a failed rebuild of a date that had succeeded, leave nothing; a late arrival is restated; a
   closing time is kept; an empty table is dated. Its five-day clean load is again identical, in all 216 tables, to
   the full-read vault of 0.2.1. The reconstruction check covers the versions staged on the last day (1,705,797
   here); the whole history is covered on Sundays.
7. **On the author's machine:** the rebuild of 2016-06-04 with 0.3.0 took 326 seconds (with 0.2.1, 572). The first
   Sunday, 2016-06-05, failed: the multiset version of the nothing-dropped test ran out of memory on the whole history
   (the operating system refused the allocation; nothing was published, the runner stopped). Replaced by control totals
   (item 1 of §5); peak memory for that test 3.6 GB before, 379 MB after, in the cloud workspace.
8. **The retry failed again, in two models** (the cold-room audit and reading satellites, also out of memory),
   although the same models had read the whole history every day on 2026-11-04 without trouble. The machine had less
   free memory than then. The runner's DuckDB had no memory budget, so it assumed 80 % of physical memory and failed
   when Windows refused an allocation. With a budget it spills to disk instead: in the cloud workspace the whole
   cold-room chain loads on a whole-history day with 300 MB and file-system access off. The pinned profile now sets
   2 GB. **General rule: a load must run within an explicit memory budget, never the engine's default share of a
   machine it shares with the source database and everything else.**
9. **With the budget in place** (the author re-ran `setup.ps1`, which re-pinned the profile, on 2026-11-15): the
   Sunday 2016-06-05, whole history, loaded in 425 seconds and the Monday 2016-06-06, watermark, in 318, all 777
   tests passing on both; 0.2.1 had taken 893 to 1,330 seconds a day on the same machine. On the Monday no single item
   dominates any more: the largest are the nothing-dropped test of the cold room (14 s) and the staging of other
   accumulating tables (order lines, stock-item transactions, invoice lines, 8 to 10 s each), the next candidates of
   §3 item 2, which first need a guarantee from the source (§2 item 4). These two days were not compared with a
   full-read vault (their extracts are only on the author's machine).

## 8. Not decided here

The overlap per source and the reread interval (§6 items 3 and 4); a version identity that does not depend on position
(§6 item 5); recording growth classes in the analysis record and
computing the measures of §2 item 1 on every load; watermarks for settling and accumulating tables other than
engine-kept histories; control totals; change feeds; the extract specification of §6 item 5. And whether the overlap
of one day and the Sunday reread used in the trial are right for WWI: they are guesses, stated as such.

Sources: [Temporal tables — SQL Server, Microsoft Learn](https://learn.microsoft.com/sql/relational-databases/tables/temporal-tables)
(period columns set to the begin time of the transaction);
[Temporal table security](https://learn.microsoft.com/nb-no/SQL/relational-databases/tables/temporal-table-security?view=sql-server-2017)
(history cannot be altered while system versioning is on);
[Stopping system-versioning](https://docs.microsoft.com/en-us/sql/relational-databases/tables/stopping-system-versioning-on-a-system-versioned-temporal-table)
(with it off, history can be modified or deleted);
[Introduction to SQL Server temporal tables, MSSQLTips](https://www.mssqltips.com/sqlservertip/3680/introduction-to-sql-server-temporal-tables/)
(retention policy since SQL Server 2017). All read as search extracts on 2026-11-15.
