# Information analysis — first trial

**Question.** Does the inventory of [129](../../docs/10_architecture/129_information-analysis.md), recorded in the
layout proposed in [`analysis/README.md`](../../analysis/README.md), work on one real table, and what does it cost?

Under [ADR-0017](../../docs/20_decisions/0017-information-analysis-before-building.md), which ruled the Wide World
Importers sandbox the first trial. Started 2026-10-18 on `Sales.Orders`, minimum items only.

`evidence_orders.py` writes the evidence files of `analysis/wwi/tables/Sales.Orders/evidence/`: it profiles the
table in the extracts under `data/raw/wwi/` and copies in the catalogue queries answered through the sandbox's request
folder. Run from the repository root with Python 3 and no dependencies:

```
python prototypes/information_analysis/evidence_orders.py
```

It writes aggregates only, never rows. **Answer:** not yet.

A defect of the sandbox met on the way: three catalogue queries through the request folder (`sys.indexes`, and
foreign keys *referencing* `Sales.Orders`, by catalogue view and by `INFORMATION_SCHEMA`) failed with "the session is
in the kill state" and left a `.csv.tmp` in `data/wwi/responses/`. Simpler queries on `sys.foreign_keys` and
`INFORMATION_SCHEMA` succeeded. Not investigated.
