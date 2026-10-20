---
id: wwi:fk:FK_Sales_SpecialDeals_StockGroupID_Warehouse_StockGroups
subject: wwi/across/relations/Sales.SpecialDeals.StockGroupID__Warehouse.StockGroups.StockGroupID
item: 02
topic: meaning
tier: minimum
summary: ID of the stock group that the special pricing applies to (optional)
confidence: medium
claims: 2
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2 | recheck=the description changes | text: The source describes Sales.SpecialDeals.StockGroupID as "ID of the stock group that the special pricing applies to (optional)".
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=cb3e2847eb7ce9c2,93e85b830c7a77bb | recheck=every new extract, or a description changes | text: The stock group a deal applies to: USB Novelties for both deals.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
