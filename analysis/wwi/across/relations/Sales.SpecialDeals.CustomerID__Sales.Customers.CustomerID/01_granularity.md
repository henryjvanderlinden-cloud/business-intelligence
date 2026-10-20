---
id: wwi:fk:FK_Sales_SpecialDeals_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.SpecialDeals.CustomerID__Sales.Customers.CustomerID
item: 01
topic: granularity
tier: minimum
summary: Declared from Sales.SpecialDeals to Sales.Customers, but no row refers in this extract.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5d9850da726a95eafd536d832acb7541297cfa1058050a7d73201078a70d31d4
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=39387fb48b059e45 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_SpecialDeals_CustomerID_Sales_Customers from Sales.SpecialDeals.CustomerID to Sales.Customers.CustomerID, the primary key of Sales.Customers: each row of Sales.SpecialDeals names at most one row of Sales.Customers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=39387fb48b059e45 | recheck=the column fills | text: In this extract no row of Sales.SpecialDeals names a row of Sales.Customers: CustomerID is empty in all 2 rows.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
