---
id: wwi:object:366624349
subject: wwi/tables/Sales/CustomerTransactions
item: 27
topic: peculiarities
tier: minimum
summary: Invoices and payments under one key, told apart by type and filled columns; payments negative with zero net and tax; a balance on event rows.
confidence: medium
claims: 10
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 8e272ee961a192b88ad69f58e01cf2ccba809358d2e23ff34de608bfd295c067
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=the empty-column patterns change | text: Test 8: 3 distinct patterns of empty columns; the most common: 70,510 rows with PaymentMethodID empty; 26,676 rows with InvoiceID empty; 56 rows with PaymentMethodID, FinalizationDate empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=the pattern changes | text: Test 8, by IsFinalized (partial): IsFinalized=1 (97,186 rows): empty -; filled FinalizationDate; partly empty InvoiceID (26,676 empty), PaymentMethodID (70,510 empty) | IsFinalized=0 (56 rows): empty PaymentMethodID, FinalizationDate; filled InvoiceID.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=the pattern changes | text: Test 8, by PaymentMethodID (partial): PaymentMethodID=(empty) (70,566 rows): empty -; filled InvoiceID; partly empty FinalizationDate (56 empty) | PaymentMethodID=4 (26,676 rows): empty InvoiceID; filled FinalizationDate.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=the pattern changes | text: Test 8, by TransactionTypeID (partial): TransactionTypeID=1 (70,566 rows): empty PaymentMethodID; filled InvoiceID; partly empty FinalizationDate (56 empty) | TransactionTypeID=3 (26,676 rows): empty InvoiceID; filled PaymentMethodID, FinalizationDate.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=a row breaks a dependency | text: Test 1: 16 functional dependencies between non-key columns over the whole extract (5 involving audit columns, a batch-edit signature, not listed): TransactionTypeID -> PaymentMethodID; InvoiceID -> TransactionTypeID; InvoiceID -> PaymentMethodID; InvoiceID -> AmountExcludingTax; InvoiceID -> TaxAmount; InvoiceID -> OutstandingBalance; InvoiceID -> IsFinalized; PaymentMethodID -> TransactionTypeID; AmountExcludingTax -> TransactionTypeID; AmountExcludingTax -> PaymentMethodID; and 6 more in the evidence.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C7 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=every new extract, or a schema change | text: Reading of the split by type above: invoices and payments are two subtypes of ledger entry; the filled reference shows which, and so does the type code.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=every new extract, or a schema change | text: Test 10: payments carry a negative TransactionAmount and zero AmountExcludingTax and TaxAmount; invoices positive amounts.
- C9 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1,34c668954c133c3d | recheck=every new extract, or a schema change | text: Test 2: OutstandingBalance is a state carried on event rows and updated in place (84 rows in the transition, with FinalizationDate and IsFinalized); a sum of it over rows of different dates adds states, not movements.
- C10 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=62d71a286e682cb1 | recheck=every new extract, or a schema change | text: A sum of TransactionAmount nets invoices against payments; a sum of AmountExcludingTax counts invoices only.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
