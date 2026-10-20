---
id: wwi:object:1682105033
subject: wwi/tables/Purchasing/SupplierTransactions
item: 27
topic: peculiarities
tier: minimum
summary: Two kinds of row under one key, told apart by type and filled columns; a balance on event rows; payments carry negative totals but zero net and tax amounts.
confidence: medium
claims: 10
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 10c8ac5e8c6792404fbdf9e86336cc8afb432c3106485f0c111b343ad363d85c
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the empty-column patterns change | text: Test 8: 3 distinct patterns of empty columns; the most common: 2,070 rows with none empty; 366 rows with PurchaseOrderID, SupplierInvoiceNumber empty; 4 rows with FinalizationDate empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the pattern changes | text: Test 8, by IsFinalized (partial): IsFinalized=1 (2,436 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (366 empty), SupplierInvoiceNumber (366 empty) | IsFinalized=0 (4 rows): empty FinalizationDate; filled PurchaseOrderID, SupplierInvoiceNumber.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the pattern changes | text: Test 8, by OutstandingBalance (partial): OutstandingBalance=0.00 (2,436 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (366 empty), SupplierInvoiceNumber (366 empty) | OutstandingBalance=1871894.10 (1 rows): empty FinalizationDate; filled PurchaseOrderID, SupplierInvoiceNumber | OutstandingBalance=849784.11 (1 rows): empty FinalizationDate; filled PurchaseOrderID, SupplierInvoiceNumber | OutstandingBalance=1875081.90 (1 rows): empty FinalizationDate; filled PurchaseOrderID, SupplierInvoiceNumber | OutstandingBalance=852596.89 (1 rows): empty FinalizationDate; filled PurchaseOrderID, SupplierInvoiceNumber.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the pattern changes | text: Test 8, by SupplierID (partial): SupplierID=4 (1,233 rows): empty -; filled -; partly empty PurchaseOrderID (178 empty), SupplierInvoiceNumber (178 empty), FinalizationDate (2 empty) | SupplierID=7 (1,161 rows): empty -; filled -; partly empty PurchaseOrderID (176 empty), SupplierInvoiceNumber (176 empty), FinalizationDate (2 empty) | SupplierID=5 (16 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (3 empty), SupplierInvoiceNumber (3 empty) | SupplierID=10 (14 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (4 empty), SupplierInvoiceNumber (4 empty) | SupplierID=12 (7 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (2 empty), SupplierInvoiceNumber (2 empty) | SupplierID=1 (7 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (2 empty), SupplierInvoiceNumber (2 empty) | SupplierID=2 (2 rows): empty -; filled FinalizationDate; partly empty PurchaseOrderID (1 empty), SupplierInvoiceNumber (1 empty).
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=the pattern changes | text: Test 8, by TransactionTypeID (partial): TransactionTypeID=5 (2,074 rows): empty -; filled PurchaseOrderID, SupplierInvoiceNumber; partly empty FinalizationDate (4 empty) | TransactionTypeID=7 (366 rows): empty PurchaseOrderID, SupplierInvoiceNumber; filled FinalizationDate.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=a row breaks a dependency | text: Test 1: 23 functional dependencies between non-key columns over the whole extract (5 involving audit columns, a batch-edit signature, not listed): PurchaseOrderID -> TransactionTypeID; PurchaseOrderID -> SupplierInvoiceNumber; PurchaseOrderID -> AmountExcludingTax; PurchaseOrderID -> TaxAmount; PurchaseOrderID -> OutstandingBalance; PurchaseOrderID -> IsFinalized; SupplierInvoiceNumber -> TransactionTypeID; TransactionDate -> FinalizationDate; TransactionDate -> IsFinalized; AmountExcludingTax -> TransactionTypeID; and 13 more in the evidence.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=every new extract, or a schema change | text: Test 10: payments (type 7) carry AmountExcludingTax and TaxAmount 0 and a negative TransactionAmount; invoices positive amounts and both references (the split by type is above).
- C9 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=every new extract, or a schema change | text: Test 2, events and states: OutstandingBalance is a state (what is still owed) carried on event rows; summing it over time double counts.
- C10 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=be40a492ac908708 | recheck=every new extract, or a schema change | text: A sum of TransactionAmount nets invoices against payments; a sum of AmountExcludingTax counts invoices only. Which one a measure means must be ruled per report.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
