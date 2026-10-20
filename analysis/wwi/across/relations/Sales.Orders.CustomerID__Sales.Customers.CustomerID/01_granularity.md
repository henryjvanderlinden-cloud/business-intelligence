---
id: wwi:fk:FK_Sales_Orders_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Orders.CustomerID__Sales.Customers.CustomerID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Orders to Sales.Customers; up to 150 rows of Sales.Orders per row of Sales.Customers.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4ae9468fd714a10bd9058f3a93afbde9a91336c004feb980b503fc9dda81fbcb
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7efd7f9f14e41420 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Orders_CustomerID_Sales_Customers from Sales.Orders.CustomerID to Sales.Customers.CustomerID, the primary key of Sales.Customers: each row of Sales.Orders names at most one row of Sales.Customers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7efd7f9f14e41420 | recheck=every new extract | text: In this extract 73,653 of 73,653 rows of Sales.Orders name one of 663 referenced rows of Sales.Customers (of 663); children per referenced parent: from 4 to 150, median 114; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=7efd7f9f14e41420 | recheck=every new extract | text: Joined from Sales.Orders to Sales.Customers, the result keeps the grain of Sales.Orders: one row per row of Sales.Orders. Joined the other way, each row of Sales.Customers repeats once per row of Sales.Orders that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
