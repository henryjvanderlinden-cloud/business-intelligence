---
id: wwi:object:402100473
subject: wwi/tables/Application/Cities
item: 03
topic: temporal
tier: minimum
summary: System-versioned; cities change about once a year in batches (1 July 2013, 2014, 2015, 16:00), each batch by one editor; nothing changed in the transition.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 0d0f05baf7f4ec7882708b350df17043db2080c16cc1aa96a19661956a6641b9
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b83a41fa256ce9db | recheck=the temporal type changes | text: The table is system-versioned: SQL Server keeps every earlier version of a row in Application.Cities_Archive, with the period columns ValidFrom and ValidTo.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b53f38ce5a091840 | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 0 inserted, 0 deleted, 0 updated; columns updated: none.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b83a41fa256ce9db | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: none; system-time period columns, datetime2 without a zone, set by SQL Server: ValidFrom, ValidTo.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=90dd2f59d12448a4 | recheck=every new extract, or a schema change | text: Row versions date from 2013-01-01 (37,912 rows) and from three batches on 1 July 2013, 2014 and 2015 at 16:00 (10, 5 and 13 rows), each by a single editor (persons 20, 8 and 15).
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the simulator's yearly procedure is read | text: What the yearly batches change (population, as the column name suggests) is not established from this table alone; the history table holds the earlier versions.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

Whether the yearly batches recur on 1 July 2016 in the simulation: watch the extract of 2016-07-01.

## For a person

None.
