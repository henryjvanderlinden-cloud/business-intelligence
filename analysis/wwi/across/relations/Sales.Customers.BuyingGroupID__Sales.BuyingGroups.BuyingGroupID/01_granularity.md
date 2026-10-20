---
id: wwi:fk:FK_Sales_Customers_BuyingGroupID_Sales_BuyingGroups
subject: wwi/across/relations/Sales.Customers.BuyingGroupID__Sales.BuyingGroups.BuyingGroupID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Customers to Sales.BuyingGroups; up to 201 rows of Sales.Customers per row of Sales.BuyingGroups.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 40a894a1eed1f9f7c2412da918168035be054343ffd71bf2cce4a670ff720f30
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6b074e88d3798b05 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Customers_BuyingGroupID_Sales_BuyingGroups from Sales.Customers.BuyingGroupID to Sales.BuyingGroups.BuyingGroupID, the primary key of Sales.BuyingGroups: each row of Sales.Customers names at most one row of Sales.BuyingGroups.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6b074e88d3798b05 | recheck=every new extract | text: In this extract 402 of 663 rows of Sales.Customers name one of 2 referenced rows of Sales.BuyingGroups (of 2); children per referenced parent: from 201 to 201, median 201; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6b074e88d3798b05 | recheck=every new extract | text: Joined from Sales.Customers to Sales.BuyingGroups, the result keeps the grain of Sales.Customers: one row per row of Sales.Customers (an inner join drops the 261 rows where BuyingGroupID is empty). Joined the other way, each row of Sales.BuyingGroups repeats once per row of Sales.Customers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
