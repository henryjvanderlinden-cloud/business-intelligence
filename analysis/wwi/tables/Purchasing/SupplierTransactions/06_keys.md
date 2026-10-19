---
id: wwi:object:1682105033
subject: wwi/tables/Purchasing/SupplierTransactions
item: 06
topic: keys
tier: minimum
summary: SupplierTransactionID is the declared key, unique; its numbers come from a numbering shared with customer and stock transactions.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T09:21:00Z
step: S08-072
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
last_checked_at: 2026-10-19T09:21:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the key range changes | text: The key runs from 134 to 336,263 with 333,690 unused numbers.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=8516b26c8ecea17f | recheck=a foreign key changes | text: 5 declared foreign keies, all enabled and trusted: LastEditedBy -> Application.People.PersonID; PaymentMethodID -> Application.PaymentMethods.PaymentMethodID; PurchaseOrderID -> Purchasing.PurchaseOrders.PurchaseOrderID; SupplierID -> Purchasing.Suppliers.SupplierID; TransactionTypeID -> Application.TransactionTypes.TransactionTypeID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e92a9afe4dfc7700 | recheck=a transaction table gets its own numbering | text: The key's 333,690 unused numbers are explained: SupplierTransactionID, CustomerTransactionID and StockItemTransactionID partition one range, 1 to 336,525, with no overlap and no gap, so the id is unique across all three tables. What that means between the tables is round 2.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
