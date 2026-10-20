---
id: wwi:fk:FK_Sales_SpecialDeals_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Sales.SpecialDeals.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 07
topic: population
tier: minimum
summary: No orphans; 0 empty; 9 of 10 Warehouse.StockGroups rows unreferenced.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 94c41ddce1c1dbf18ebf8de5a6db886ab2b66d82f13749b0c9c0a9322728ad67
last_checked_at: 2026-10-20T08:31:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=every new extract | text: Orphans: 0 rows of Sales.SpecialDeals (0 distinct values) name no row of Warehouse.StockGroups.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=every new extract | text: StockGroupID is filled on every row of Sales.SpecialDeals.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=every new extract | text: 9 of 10 rows of Warehouse.StockGroups are named by no row of Sales.SpecialDeals.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=a security policy or a count difference appears | text: Extraction visibility: Sales.SpecialDeals 2 rows for the owner, 2 for the extracting reader, 2 in the extract; Warehouse.StockGroups 10 rows for the owner, 10 for the extracting reader, 10 in the extract; masked columns: none.
- C5 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
