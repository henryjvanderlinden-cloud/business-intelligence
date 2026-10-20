---
id: wwi:fk:FK_Sales_SpecialDeals_CustomerCategoryID_Sales_CustomerCategories
subject: wwi/across/relations/Sales.SpecialDeals.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID
item: 01
topic: granularity
tier: minimum
summary: Declared from Sales.SpecialDeals to Sales.CustomerCategories, but no row refers in this extract.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2f36f9a20dd086836a16de8d685fafe0dfabb7319607f9886b301f9bcae83a72
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=c8f54419407a8a6b | recheck=the foreign key changes | text: Declared foreign key FK_Sales_SpecialDeals_CustomerCategoryID_Sales_CustomerCategories from Sales.SpecialDeals.CustomerCategoryID to Sales.CustomerCategories.CustomerCategoryID, the primary key of Sales.CustomerCategories: each row of Sales.SpecialDeals names at most one row of Sales.CustomerCategories.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=c8f54419407a8a6b | recheck=the column fills | text: In this extract no row of Sales.SpecialDeals names a row of Sales.CustomerCategories: CustomerCategoryID is empty in all 2 rows.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
