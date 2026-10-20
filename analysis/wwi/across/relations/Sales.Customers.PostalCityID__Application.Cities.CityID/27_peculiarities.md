---
id: wwi:fk:FK_Sales_Customers_PostalCityID_Application_Cities
subject: wwi/across/relations/Sales.Customers.PostalCityID__Application.Cities.CityID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, roles, chasm, current versions.
confidence: high
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2d4f2f6640c040452432c763f82f4b44394989fd93369f746da7108654c9e720
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=df63a606f20e0cd2 | recheck=every new extract | text: Fan-out: joined from Application.Cities to Sales.Customers, a Application.Cities row repeats up to 2 times (median 1), so a measure of Application.Cities summed after the join is counted once per referring row.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=df63a606f20e0cd2 | recheck=a foreign key changes | text: Several paths between the same two tables: Sales.Customers also refers to Application.Cities through DeliveryCityID; a join of the two must say which role it means.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=df63a606f20e0cd2 | recheck=every new extract | text: Chasm trap: Application.Cities also has other referring columns with several rows per parent (Purchasing.Suppliers.DeliveryCityID (up to 2 per parent), Purchasing.Suppliers.PostalCityID (up to 2 per parent), Sales.Customers.DeliveryCityID (up to 2 per parent)); joining Sales.Customers and one of these through Application.Cities pairs every row of one with every row of the other for the same parent.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=df63a606f20e0cd2 | recheck=the temporal type changes | text: Application.Cities is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.Customers that names a row of Application.Cities gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
