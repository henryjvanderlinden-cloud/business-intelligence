---
id: wwi:object:638625318
subject: wwi/tables/Warehouse/StockItemTransactions
item: 27
topic: peculiarities
tier: minimum
summary: Three kinds of movement under one key, told apart by type, filled references and sign.
confidence: medium
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: aa0ff84050dc38732c7bd5472378de21f412a1f72bdf0c9aa4958b125c232331
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=the empty-column patterns change | text: Test 8: 3 distinct patterns of empty columns; the most common: 228,432 rows with SupplierID, PurchaseOrderID empty; 8,367 rows with CustomerID, InvoiceID empty; 44 rows with CustomerID, InvoiceID, SupplierID, PurchaseOrderID empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=the pattern changes | text: Test 8, by SupplierID (partial): SupplierID=(empty) (228,476 rows): empty PurchaseOrderID; filled -; partly empty CustomerID (44 empty), InvoiceID (44 empty) | SupplierID=4 (5,802 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=7 (2,477 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=5 (42 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=10 (18 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=12 (15 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=1 (10 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID | SupplierID=2 (3 rows): empty CustomerID, InvoiceID; filled PurchaseOrderID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=the pattern changes | text: Test 8, by TransactionTypeID (exact): TransactionTypeID=10 (228,432 rows): empty SupplierID, PurchaseOrderID; filled CustomerID, InvoiceID | TransactionTypeID=11 (8,367 rows): empty CustomerID, InvoiceID; filled SupplierID, PurchaseOrderID | TransactionTypeID=12 (44 rows): empty CustomerID, InvoiceID, SupplierID, PurchaseOrderID; filled -.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=a row breaks a dependency | text: Test 1: 3 functional dependencies between non-key columns over the whole extract (5 involving audit columns, a batch-edit signature, not listed): InvoiceID -> CustomerID; PurchaseOrderID -> SupplierID; TransactionOccurredWhen -> TransactionTypeID.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C6 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=every new extract, or a schema change | text: Reading of the split by type above: issues (customer and invoice filled), receipts (supplier and purchase order) and adjustments (neither) are three subtypes of movement, an exclusive arc of references (test 9).
- C7 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=02947584dba54bc6 | recheck=every new extract, or a schema change | text: Test 10: Quantity is positive for incoming and negative for outgoing stock, by description; issues are all negative, receipts all positive, adjustments either (or zero).
- C8 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=951d022fa77a5499 | recheck=every new extract, or a schema change | text: TransactionOccurredWhen determines the type: each kind of movement is booked at its own time of day, a sign of the simulator's batches.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
