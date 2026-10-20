---
id: wwi:object:1749581271
subject: wwi/tables/Application/PaymentMethods_Archive
item: 05
topic: role
tier: minimum
summary: History of Application.PaymentMethods (earlier row versions), not a separate entity.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6ad07d5080cc67c9c57b9cf621509187e6f222d2624c74328488725ed956287d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3b644d5b13112c03 | recheck=a foreign key changes | text: It refers to no table and is referred to by no table.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3b644d5b13112c03 | recheck=the temporal type changes | text: This is a history table of system-versioning.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3b644d5b13112c03 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3b644d5b13112c03,1f029b97a2fc56e5 | recheck=every new extract, or a schema change | text: History table of Application.PaymentMethods: one row per earlier version of a Application.PaymentMethods row, current from ValidFrom to ValidTo; 1 rows for 1 distinct PaymentMethodID values; versions ended between 2016-01-01 and 2016-01-01.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3b644d5b13112c03 | recheck=every new extract, or a schema change | text: Role: not a separate entity; it holds the earlier versions of Application.PaymentMethods and never the current one.

## Reasoning

The catalogue declares the table a history table of Application.PaymentMethods; the period columns bound each version.

## Uncertainties

None.

## For a person

None.
