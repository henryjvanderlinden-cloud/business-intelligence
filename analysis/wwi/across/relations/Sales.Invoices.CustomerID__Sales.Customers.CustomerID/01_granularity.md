---
id: wwi:fk:FK_Sales_Invoices_CustomerID_Sales_Customers
subject: wwi/across/relations/Sales.Invoices.CustomerID__Sales.Customers.CustomerID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.Invoices to Sales.Customers; up to 144 rows of Sales.Invoices per row of Sales.Customers.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2ce83d3e97200a06f4d8df60b09a4948373b555ba7aa8f288282685f535571a5
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_Invoices_CustomerID_Sales_Customers from Sales.Invoices.CustomerID to Sales.Customers.CustomerID, the primary key of Sales.Customers: each row of Sales.Invoices names at most one row of Sales.Customers.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=every new extract | text: In this extract 70,566 of 70,566 rows of Sales.Invoices name one of 663 referenced rows of Sales.Customers (of 663); children per referenced parent: from 4 to 144, median 109; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=1ccae8b1dee94657 | recheck=every new extract | text: Joined from Sales.Invoices to Sales.Customers, the result keeps the grain of Sales.Invoices: one row per row of Sales.Invoices. Joined the other way, each row of Sales.Customers repeats once per row of Sales.Invoices that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
