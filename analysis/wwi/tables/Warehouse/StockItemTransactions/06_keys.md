---
id: wwi:object:638625318
subject: wwi/tables/Warehouse/StockItemTransactions
item: 06
topic: keys
tier: minimum
summary: StockItemTransactionID is the declared key, unique; its numbers are shared with customer and supplier transactions.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: aa0ff84050dc38732c7bd5472378de21f412a1f72bdf0c9aa4958b125c232331
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=the key range changes | text: The key runs from 1 to 336,524 with 99,681 unused numbers.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=02947584dba54bc6 | recheck=a foreign key changes | text: 7 declared foreign keies, all enabled and trusted: LastEditedBy -> Application.People.PersonID; CustomerID -> Sales.Customers.CustomerID; InvoiceID -> Sales.Invoices.InvoiceID; PurchaseOrderID -> Purchasing.PurchaseOrders.PurchaseOrderID; StockItemID -> Warehouse.StockItems.StockItemID; SupplierID -> Purchasing.Suppliers.SupplierID; TransactionTypeID -> Application.TransactionTypes.TransactionTypeID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e92a9afe4dfc7700 | recheck=a transaction table gets its own numbering | text: The key's 99,681 unused numbers are explained: StockItemTransactionID, CustomerTransactionID and SupplierTransactionID partition one range, 1 to 336,525, with no overlap and no gap.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
