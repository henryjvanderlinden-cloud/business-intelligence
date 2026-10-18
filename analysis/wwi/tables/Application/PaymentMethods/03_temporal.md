---
id: wwi:object:1669580986
subject: wwi/tables/Application/PaymentMethods
item: 03
topic: temporal
tier: minimum
summary: System-versioned reference data, changed rarely; no change in the transition observed.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 6ad07d5080cc67c9c57b9cf621509187e6f222d2624c74328488725ed956287d
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=the temporal type changes | text: The table is system-versioned: SQL Server keeps every earlier version of a row in Application.PaymentMethods_Archive, with the period columns ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d6a04c98c4a0cc7e | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 0 inserted, 0 deleted, 0 updated; columns updated: none.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=065bbf4844346cbb | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=d7ebcd1cb8412d2d,d6a04c98c4a0cc7e | recheck=every new extract, or a schema change | text: Changes are rare: ValidFrom shows the dates rows were last changed, and the one transition changed nothing.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
