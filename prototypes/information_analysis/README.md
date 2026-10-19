# Information analysis - first trial

**Question.** Does the inventory of [129](../../docs/10_architecture/129_information-analysis.md), recorded in the
layout of [`analysis/README.md`](../../analysis/README.md), work on one real table, and what does it cost?

Under [ADR-0017](../../docs/20_decisions/0017-information-analysis-before-building.md), which ruled the Wide World
Importers sandbox the first trial, and [ADR-0018](../../docs/20_decisions/0018-information-analysis-record.md), which
ruled the layout. `Sales.Orders` was done first on 2026-10-18 in a first layout, reviewed by astra, and redone the
same day in the ruled one: the six minimum items, item 27 and two column files.

`evidence_orders.py` writes the evidence files of `analysis/wwi/tables/Sales/Orders/evidence/`: it profiles the
table in the extracts under `data/raw/wwi/` and copies in the catalogue queries answered through the sandbox's request
folder. Each evidence is one function whose source text is stored in the record; records are named by their content
hash and never overwritten. Run from the repository root with Python 3 and no dependencies:

```
python prototypes/information_analysis/evidence_orders.py
```

**Round 1's minimum for all 48 tables** (2026-10-18): `profile_tables.py` writes catalogue, profile and transition
evidence for every table; `evidence_shared.py` adds what one table's profile cannot show (a numbering shared by three
tables, candidate keys, invoice-line arithmetic); `write_dossiers.py` writes the item files, with mechanical claims
built from the evidence and judgement claims from a specification the agent writes per table (kept in the agent's
scratch folder; the item files are the record). Run in that order, from the repository root:

```
python prototypes/information_analysis/profile_tables.py
python prototypes/information_analysis/evidence_shared.py
python prototypes/information_analysis/evidence_shared.py candidates
python prototypes/information_analysis/evidence_shared.py arithmetic
python prototypes/information_analysis/evidence_shared.py documentation
python prototypes/information_analysis/evidence_shared.py more
python prototypes/information_analysis/write_dossiers.py <specification module>
python prototypes/information_analysis/write_column_meanings.py <notes module>
```

`documentation` records which published Microsoft documentation of WWI was read and what it says, as one evidence per
table; `more` adds the code labels per table (counts per code with the code table's name), the keys inside the
delivery events of Sales.Invoices and a profile of the cold-room history table, added after sol's review of
2026-10-18. **Column meanings** (2026-10-19): `write_column_meanings.py` writes item 02 for every column of every base
table, `columns/<column>/02_meaning.md`, best-effort tier: declared description, type and keys and the observed filling
and values mechanically, fixed readings for the audit and system-time columns, and the agent's reading per column from
a notes module, each with its confidence; a column the source and the documentation leave unexplained says so.

**Answer, first part:** the inventory works on a real source. The catalogue took 7 queries (one per job run), the
profiles about two minutes of machine time for 48 tables and 5.4 million rows, and the author's hands not at all; the
judgement claims took the agent most of the effort. Unanswered: whether a different agent would reach the same
judgements (review owed) and what round 2 costs.

**Changes waiting for the next run of `setup.ps1`** (the job is pinned, so these take effect only then):
1. a connection per query with `Pooling=false`, so several requests in one run no longer fail (below);
2. the `status` action to list security policies and masked columns as owner, which would settle the open R15
   question (`07_population.md`, "whether a row-level security policy exists") for every table.

**A defect of the sandbox, diagnosed 2026-10-18.** In one run of the job, the first query succeeds and every later
request in the same run - a query or even `status` - fails with "Cannot continue the execution because the session
is in the kill state", leaving a `.csv.tmp` in `data/wwi/responses/`. The same request sent alone succeeds. The cause
is visible in `prototypes/wwi_sandbox/job.ps1`: `Do-Query` runs `EXECUTE AS USER ... WITH NO REVERT` on the
connection the whole run shares, so the connection cannot be used again. **Workaround:** one request per job run
(one a minute). **Fix, not yet made:** give each query its own connection with `Pooling=false` and close it after;
the pinned job only changes when the author reruns `setup.ps1`, so the fix waits for the next batch of job changes.
Separately, `nsdn_reader` cannot read procedure definitions (`OBJECT_DEFINITION` returns null).
