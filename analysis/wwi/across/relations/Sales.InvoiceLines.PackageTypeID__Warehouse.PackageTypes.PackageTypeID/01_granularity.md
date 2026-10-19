---
id: wwi:fk:FK_Sales_InvoiceLines_PackageTypeID_Warehouse_PackageTypes
subject: wwi/across/relations/Sales.InvoiceLines.PackageTypeID__Warehouse.PackageTypes.PackageTypeID
item: 01
topic: granularity
tier: minimum
summary: Many-to-one from Sales.InvoiceLines to Warehouse.PackageTypes; up to 217,959 rows of Sales.InvoiceLines per row of Warehouse.PackageTypes.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 940bd3cfc340d9c1959aa30e56159aa759298a180269b0a08c28d0bfa3e8b891
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=the foreign key changes | text: Declared foreign key FK_Sales_InvoiceLines_PackageTypeID_Warehouse_PackageTypes from Sales.InvoiceLines.PackageTypeID to Warehouse.PackageTypes.PackageTypeID, the primary key of Warehouse.PackageTypes: each row of Sales.InvoiceLines names at most one row of Warehouse.PackageTypes.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=every new extract | text: In this extract 228,432 of 228,432 rows of Sales.InvoiceLines name one of 4 referenced rows of Warehouse.PackageTypes (of 14); children per referenced parent: from 1,044 to 217,959, median 4,714.5; 0 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=10c56d380e53c456 | recheck=every new extract | text: Joined from Sales.InvoiceLines to Warehouse.PackageTypes, the result keeps the grain of Sales.InvoiceLines: one row per row of Sales.InvoiceLines. Joined the other way, each row of Warehouse.PackageTypes repeats once per row of Sales.InvoiceLines that names it (C2).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
