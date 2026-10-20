---
id: wwi:fk:FK_Purchasing_Suppliers_SupplierCategoryID_Purchasing_SupplierCategories
subject: wwi/across/relations/Purchasing.Suppliers.SupplierCategoryID__Purchasing.SupplierCategories.SupplierCategoryID
item: 03
topic: temporal
tier: best-effort
summary: Point in time: earlier parent version on 1 rows, differing in SupplierCategoryName.
confidence: medium
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7095eed2c5b53b68acacfebfd7dba9faed29c90ddae3ad76579ad1581e94d64a
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e697ea0947b13293 | recheck=the temporal type changes | text: Purchasing.SupplierCategories is system-versioned: the version of a row current at a given time is in Purchasing.SupplierCategories_Archive or the table itself, by ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e697ea0947b13293 | recheck=every new extract | text: As of the end of each row's date (ValidFrom), the row of Purchasing.SupplierCategories it names was: the current version on 12; an earlier version on 1.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e697ea0947b13293 | recheck=every new extract | text: On 1 of those earlier versions some attributes differ from the current version: SupplierCategoryName (1 rows). Joined in the extract, these rows get the current values of these columns, not the values of their date.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=e697ea0947b13293 | recheck=every new extract | text: No other attribute of Purchasing.SupplierCategories differs between the version current at a row's date and the current version (LastEditedBy, LastEditedWhen and the period columns are not compared).
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a ValidFrom far from simulated time appears | text: The comparison places business dates against system time (ValidFrom), which is the server's clock at the change; in WWI it follows the simulated dates except for one version of Application.Countries stamped 2022 (round 1), so it holds as far as the two clocks agree.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
