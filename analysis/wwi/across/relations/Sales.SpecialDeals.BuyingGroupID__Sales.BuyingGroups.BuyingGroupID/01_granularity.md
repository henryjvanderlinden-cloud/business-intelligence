---
id: wwi:fk:FK_Sales_SpecialDeals_BuyingGroupID_Sales_BuyingGroups
subject: wwi/across/relations/Sales.SpecialDeals.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID
item: 01
topic: granularity
tier: minimum
summary: Sales.SpecialDeals to Sales.BuyingGroups; at most one row of Sales.SpecialDeals per row of Sales.BuyingGroups in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 3fcad77aea87633fa0866f526af11b5d0979c9e1d2c695c438c97e3dd2c18b72
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a74b520f3b650fa2 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_SpecialDeals_BuyingGroupID_Sales_BuyingGroups from Sales.SpecialDeals.BuyingGroupID to Sales.BuyingGroups.BuyingGroupID, the primary key of Sales.BuyingGroups: each row of Sales.SpecialDeals names at most one row of Sales.BuyingGroups.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a74b520f3b650fa2 | recheck=every new extract | text: In this extract 2 of 2 rows of Sales.SpecialDeals name one of 2 referenced rows of Sales.BuyingGroups (of 2); children per referenced parent: from 1 to 1, median 1; 2 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a74b520f3b650fa2 | recheck=every new extract | text: Joined from Sales.SpecialDeals to Sales.BuyingGroups, the result keeps the grain of Sales.SpecialDeals: one row per row of Sales.SpecialDeals. Joined the other way, each row of Sales.BuyingGroups repeats once per row of Sales.SpecialDeals that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=a74b520f3b650fa2 | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Sales.BuyingGroups is named by more than one row of Sales.SpecialDeals. No unique constraint on BuyingGroupID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
