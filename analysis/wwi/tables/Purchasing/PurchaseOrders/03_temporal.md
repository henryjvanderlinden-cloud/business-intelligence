---
id: wwi:object:1026102696
subject: wwi/tables/Purchasing/PurchaseOrders
item: 03
topic: temporal
tier: minimum
summary: Not versioned; orders are inserted and later updated in place once, when finalized; expected delivery dates run into the future.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: adb80ef2e4b8c472bfbd6569b8b3340fe525f86fe4769f74faa03e1e6624864a
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=the temporal type changes | text: The table is not system-versioned, so the source keeps no history of its own.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=5873eb9d909da99b | recheck=every new extract | text: Between the extracts of 31 May and 1 June 2016: 2 inserted, 0 deleted, 2 updated; columns updated: IsOrderFinalized (2), LastEditedBy (2), LastEditedWhen (2).
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=a column type changes | text: Date columns: OrderDate, ExpectedDeliveryDate; date-and-time columns without a time zone: LastEditedWhen.
- C4 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a time zone is found in documentation | text: The time zone of LastEditedWhen is not established; the catalogue states none.
- C5 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=5873eb9d909da99b | recheck=a second transition | text: Lifecycle seen in one day: 2 orders inserted, 2 earlier orders set to finalized (IsOrderFinalized, LastEditedBy, LastEditedWhen); 2 orders are not finalized.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=6883f497d8b4086d | recheck=every new extract, or a schema change | text: ExpectedDeliveryDate runs to 2016-06-21, after the extract date: future dates are normal here.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
