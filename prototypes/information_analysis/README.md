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

**Answer:** not yet; one table is not a trial.

**A defect of the sandbox, diagnosed 2026-10-18.** In one run of the job, the first query succeeds and every later
request in the same run - a query or even `status` - fails with "Cannot continue the execution because the session
is in the kill state", leaving a `.csv.tmp` in `data/wwi/responses/`. The same request sent alone succeeds. The cause
is visible in `prototypes/wwi_sandbox/job.ps1`: `Do-Query` runs `EXECUTE AS USER ... WITH NO REVERT` on the
connection the whole run shares, so the connection cannot be used again. **Workaround:** one request per job run
(one a minute). **Fix, not yet made:** give each query its own connection with `Pooling=false` and close it after;
the pinned job only changes when the author reruns `setup.ps1`, so the fix waits for the next batch of job changes.
Separately, `nsdn_reader` cannot read procedure definitions (`OBJECT_DEFINITION` returns null).
