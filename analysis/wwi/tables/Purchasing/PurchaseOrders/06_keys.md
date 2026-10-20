---
id: wwi:object:1026102696
subject: wwi/tables/Purchasing/PurchaseOrders
item: 06
topic: keys
tier: minimum
summary: PurchaseOrderID is the declared key, unique and gapless.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: adb80ef2e4b8c472bfbd6569b8b3340fe525f86fe4769f74faa03e1e6624864a
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=6883f497d8b4086d | recheck=the key range changes | text: The key runs from 1 to 2,076 with no gap.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=a foreign key changes | text: 4 declared foreign keies, all enabled and trusted: LastEditedBy -> Application.People.PersonID; ContactPersonID -> Application.People.PersonID; DeliveryMethodID -> Application.DeliveryMethods.DeliveryMethodID; SupplierID -> Purchasing.Suppliers.SupplierID.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ec7b7812547c43e1 | recheck=every new extract, or a schema change | text: Business key: PurchaseOrderID, the number WWI gives the order; SupplierReference is the supplier's reference for WWI, not for the order.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
