---
id: wwi:object:1941581955
subject: wwi/tables/Purchasing/SupplierCategories_Archive
item: 05
topic: role
tier: minimum
summary: History of Purchasing.SupplierCategories (earlier row versions), not a separate entity.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T07:26:00Z
step: S08-066
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 35cdfcd24713d6e9eb43784f7e3be5b8228ce8bb
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1419ef6b992982575960251d90234c9f5f46b72d6559f42f83b10ceb82e9e21f
last_checked_at: 2026-10-19T07:26:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=363a5d27d1d40451 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=363a5d27d1d40451 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=363a5d27d1d40451 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=363a5d27d1d40451,c8b54d4aeefef359 | recheck=every new extract, or a schema change | text: History table of Purchasing.SupplierCategories: one row per earlier version of a Purchasing.SupplierCategories row, current from ValidFrom to ValidTo; 1 rows for 1 distinct SupplierCategoryID values; versions ended between 2015-01-01 and 2015-01-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=363a5d27d1d40451 | recheck=every new extract, or a schema change | text: Role: not a separate entity; it holds the earlier versions of Purchasing.SupplierCategories and never the current one.

## Reasoning

The catalogue declares the table a history table of Purchasing.SupplierCategories; the period columns bound each version.

## Uncertainties

None.

## For a person

None.
