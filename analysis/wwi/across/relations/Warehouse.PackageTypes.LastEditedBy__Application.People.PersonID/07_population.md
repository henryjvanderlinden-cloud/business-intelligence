---
id: wwi:fk:FK_Warehouse_PackageTypes_Application_People
subject: wwi/across/relations/Warehouse.PackageTypes.LastEditedBy__Application.People.PersonID
item: 07
topic: population
tier: minimum
summary: No orphans; 0 empty; 1,110 of 1,111 Application.People rows unreferenced.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: e0a1b8350b5a388b0885cc7c72030f3af36458d80f5f5627453229ef5238d6e8
last_checked_at: 2026-10-20T05:51:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dc6218425c1c2677 | recheck=every new extract | text: Orphans: 0 rows of Warehouse.PackageTypes (0 distinct values) name no row of Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dc6218425c1c2677 | recheck=every new extract | text: LastEditedBy is filled on every row of Warehouse.PackageTypes.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dc6218425c1c2677 | recheck=every new extract | text: 1,110 of 1,111 rows of Application.People are named by no row of Warehouse.PackageTypes.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dc6218425c1c2677 | recheck=a security policy or a count difference appears | text: Extraction visibility: Application.People 1,111 rows for the owner, 1,111 for the extracting reader, 1,111 in the extract; Warehouse.PackageTypes 14 rows for the owner, 14 for the extracting reader, 14 in the extract; masked columns: none.
- C5 | type=declared | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=dc6218425c1c2677 | recheck=permission to read security policies is granted | text: Whether a row-level security policy filters either table is not established: the extracting reader sees no security policies and may lack the permission to see them; equal counts for owner and reader (as here) argue against a filter.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

Whether row-level security filters either table: the claim with confidence unknown.

## For a person

None.
