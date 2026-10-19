---
id: wwi:fk:FK_Warehouse_StockItems_OuterPackageID_Warehouse_PackageTypes
subject: wwi/across/relations/Warehouse.StockItems.OuterPackageID__Warehouse.PackageTypes.PackageTypeID
item: 07
topic: population
tier: minimum
summary: No orphans; 0 empty; 11 of 14 Warehouse.PackageTypes rows unreferenced.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 9a090c85fa6cc4c111163aea7274c174e4b3f701c4e4219649dddeafc9c848a2
last_checked_at: 2026-10-19T20:31:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0405540c22176c22 | recheck=every new extract | text: Orphans: 0 rows of Warehouse.StockItems (0 distinct values) name no row of Warehouse.PackageTypes.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0405540c22176c22 | recheck=every new extract | text: OuterPackageID is filled on every row of Warehouse.StockItems.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0405540c22176c22 | recheck=every new extract | text: 11 of 14 rows of Warehouse.PackageTypes are named by no row of Warehouse.StockItems.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0405540c22176c22 | recheck=a security policy or a count difference appears | text: Extraction visibility: Warehouse.PackageTypes 14 rows for the owner, 14 for the extracting reader, 14 in the extract; Warehouse.StockItems 227 rows for the owner, 227 for the extracting reader, 227 in the extract; masked columns: none.
- C5 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=0405540c22176c22 | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
