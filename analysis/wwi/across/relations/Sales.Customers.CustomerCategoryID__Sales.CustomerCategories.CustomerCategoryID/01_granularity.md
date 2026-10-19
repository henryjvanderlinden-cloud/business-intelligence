---
id: wwi:fk:FK_Sales_Customers_CustomerCategoryID_Sales_CustomerCategories
subject: wwi/across/relations/Sales.Customers.CustomerCategoryID__Sales.CustomerCategories.CustomerCategoryID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Customers to Sales.CustomerCategories; up to 459 rows of Sales.Customers per row of Sales.CustomerCategories.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 885a5617dc691872d83e1da579a1653654b1d66dc0b8de70e4feaec18d282284
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ed24711df6df724f | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Customers_CustomerCategoryID_Sales_CustomerCategories from Sales.Customers.CustomerCategoryID to Sales.CustomerCategories.CustomerCategoryID, the primary key of Sales.CustomerCategories: each row of Sales.Customers names at most one row of Sales.CustomerCategories.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ed24711df6df724f | recheck=every new extract | text: In this extract 663 of 663 rows of Sales.Customers name one of 5 referenced rows of Sales.CustomerCategories (of 8); children per referenced parent: from 47 to 459, median 51; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=ed24711df6df724f | recheck=every new extract | text: Joined from Sales.Customers to Sales.CustomerCategories, the result keeps the grain of Sales.Customers: one row per row of Sales.Customers. Joined the other way, each row of Sales.CustomerCategories repeats once per row of Sales.Customers that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
