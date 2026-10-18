---
id: wwi:object:1474104292
subject: wwi/tables/Warehouse/StockItemHoldings
item: 03
topic: temporal
tier: minimum
summary: Not versioned and overwritten daily: every row changed on 2016-06-01; daily extracts see one state per day.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: bb1ea17573cd7d7073444df38e148e0a4fc7ac5b6c6bc1078e0bd538c0085e24
last_checked_at: 2026-10-18T20:32:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77 | recheck=the temporal type changes | text: The table is not system-versioned, so the source keeps no history of its own.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a9106224cd1f21d5 | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 0 inserted, 0 deleted, 227 updated; columns updated: LastEditedBy (227), LastEditedWhen (227), QuantityOnHand (226).
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77 | recheck=a column type changes | text: Date columns: none; date-and-time columns without a time zone: LastEditedWhen.
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a time zone is found in documentation | text: The time zone of LastEditedWhen is not established; the catalogue states none.
- C5 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a9106224cd1f21d5 | recheck=a second transition | text: All 227 rows were updated between the two extracts, QuantityOnHand on 226: a state overwritten in place every day.
- C6 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77,a9106224cd1f21d5 | recheck=every new extract, or a schema change | text: Capture: the source keeps no history of stock levels; daily extracts sample one state per day (sampled history in 127's sense), so intraday levels are not captured.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
