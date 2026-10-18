---
id: wwi:object:786101841
subject: wwi/tables/Purchasing/Suppliers_Archive
item: 05
topic: role
tier: minimum
summary: History of Purchasing.Suppliers (earlier row versions), not a separate entity.
confidence: medium
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 7bcb78223c92bb8418652485c9f8ee3acdcdaf5d5f711f56ade275cb0fd6aa98
last_checked_at: 2026-10-18T13:20:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4a1f5f6a946dcec6 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4a1f5f6a946dcec6 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4a1f5f6a946dcec6 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ebebcc1db7d5d404 | recheck=every new extract, or a schema change | text: History table of Purchasing.Suppliers: one row per earlier version of a Purchasing.Suppliers row, current from ValidFrom to ValidTo; 13 rows for 13 distinct SupplierID values; versions ended between 2013-01-01 and 2013-01-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4a1f5f6a946dcec6 | recheck=every new extract, or a schema change | text: Role: not a separate entity. Loaded, it supplies the earlier versions of Purchasing.Suppliers for its history in the warehouse; read alone, it never holds the current version.
- C6 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4a1f5f6a946dcec6 | recheck=every new extract, or a schema change | text: The same five bank columns are masked in this history table; the extract, made as owner, presumably holds them unmasked as in Purchasing.Suppliers (not checked here).

## Reasoning

The catalogue declares the table a history table of Purchasing.Suppliers; the period columns bound each version.

## Uncertainties

None.

## For a person

None.
