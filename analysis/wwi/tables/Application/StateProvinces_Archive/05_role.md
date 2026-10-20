---
id: wwi:object:386100416
subject: wwi/tables/Application/StateProvinces_Archive
item: 05
topic: role
tier: minimum
summary: History of Application.StateProvinces (earlier row versions), not a separate entity.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: b85fd6a1b65683d407663a7b52ebc7c96f376f8345323ada5a5fc81b70edef97
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0eae049d69c4899e | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0eae049d69c4899e | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0eae049d69c4899e | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0eae049d69c4899e,099252e01207a6c2 | recheck=every new extract, or a schema change | text: History table of Application.StateProvinces: one row per earlier version of a Application.StateProvinces row, current from ValidFrom to ValidTo; 104 rows for 52 distinct StateProvinceID values; versions ended between 2013-01-01 and 2015-07-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0eae049d69c4899e | recheck=every new extract, or a schema change | text: Role: not a separate entity; it holds the earlier versions of Application.StateProvinces and never the current one.

## Reasoning

The catalogue declares the table a history table of Application.StateProvinces; the period columns bound each version.

## Uncertainties

None.

## For a person

None.
