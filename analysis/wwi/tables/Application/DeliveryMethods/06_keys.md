---
id: wwi:object:1573580644
subject: wwi/tables/Application/DeliveryMethods
item: 06
topic: keys
tier: minimum
summary: Primary key unique and gapless; DeliveryMethodName is declared unique.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 169579607a2535747c02c42c767a59e970a169cbedd96dbb067dc3463de2fdc8
last_checked_at: 2026-10-20T05:44:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4d0a658d91d44a61 | recheck=a unique constraint changes | text: Declared unique besides the primary key: UQ_Application_DeliveryMethods_DeliveryMethodName (DeliveryMethodName).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=1eeacd7a9c1daa95 | recheck=the key range changes | text: The key runs from 1 to 10 with no gap.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4d0a658d91d44a61 | recheck=a foreign key changes | text: 1 declared foreign key, all enabled and trusted: LastEditedBy -> Application.People.PersonID.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=4d0a658d91d44a61 | recheck=every new extract, or a schema change | text: Business key candidate: the unique name (DeliveryMethodName is declared unique); the numeric key is the source's surrogate.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
