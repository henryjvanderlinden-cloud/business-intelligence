---
id: wwi:object:1365579903
subject: wwi/tables/Application/People_Archive
item: 05
topic: role
tier: minimum
summary: History of Application.People (earlier row versions), not a separate entity.
confidence: high
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2,678630c35fec4673 | recheck=every new extract, or a schema change | text: History table of Application.People: one row per earlier version of a Application.People row, current from ValidFrom to ValidTo; 962 rows for 182 distinct PersonID values; versions ended between 2013-01-01 and 2016-06-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2 | recheck=every new extract, or a schema change | text: Role: not a separate entity; it holds the earlier versions of Application.People and never the current one.
- C6 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=0bce2bfb915c4ce2 | recheck=every new extract, or a schema change | text: Sensitivity follows Application.People: its earlier versions hold the same personal data, including earlier password hashes.

## Reasoning

The catalogue declares the table a history table of Application.People; the period columns bound each version.

## Uncertainties

None.

## For a person

None.
