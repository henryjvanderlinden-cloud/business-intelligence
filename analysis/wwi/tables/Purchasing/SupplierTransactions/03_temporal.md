---
id: wwi:object:1682105033
subject: wwi/tables/Purchasing/SupplierTransactions
item: 03
topic: temporal
tier: minimum
summary: Not versioned; rows are inserted and, for invoices, settled later (balance, finalization); none updated in the transition.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=the temporal type changes | text: The table is not system-versioned, so the source keeps no history of its own.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a2d046c1f3fab478 | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 2 inserted, 0 deleted, 0 updated; columns updated: none.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=a column type changes | text: Date columns: TransactionDate, FinalizationDate; date-and-time columns without a time zone: LastEditedWhen.
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a time zone is found in documentation | text: The time zone of LastEditedWhen is not established; the catalogue states none.
- C5 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a2d046c1f3fab478 | recheck=a second transition | text: In one day 2 rows were inserted and none updated; settlement updates were not seen in this window.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=every new extract, or a schema change | text: 4 transactions are not finalized and are the only rows with an OutstandingBalance above zero; FinalizationDate is empty exactly for them.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
