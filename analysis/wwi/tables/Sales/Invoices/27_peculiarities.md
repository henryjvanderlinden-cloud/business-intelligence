---
id: wwi:object:2018106230
subject: wwi/tables/Sales/Invoices
item: 27
topic: peculiarities
tier: minimum
summary: A list of delivery events inside a JSON column, with two of its values copied into columns; customer attributes copied onto the invoice; driver totals on the header; an unused credit-note flag.
confidence: medium
claims: 12
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=the empty-column patterns change | text: Test 8: 2 distinct patterns of empty columns; the most common: 70,510 rows with CreditNoteReason, Comments, InternalComments, DeliveryRun, RunPosition empty; 56 rows with CreditNoteReason, Comments, InternalComments, DeliveryRun, RunPosition, ConfirmedDeliveryTime, ConfirmedReceivedBy empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=the pattern changes | text: Test 8, by SalespersonPersonID (partial): SalespersonPersonID=16 (7,191 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (7 empty), ConfirmedReceivedBy (7 empty) | SalespersonPersonID=2 (7,164 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (4 empty), ConfirmedReceivedBy (4 empty) | SalespersonPersonID=13 (7,083 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (4 empty), ConfirmedReceivedBy (4 empty) | SalespersonPersonID=15 (7,083 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (9 empty), ConfirmedReceivedBy (9 empty) | SalespersonPersonID=6 (7,081 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (8 empty), ConfirmedReceivedBy (8 empty) | SalespersonPersonID=20 (7,068 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (7 empty), ConfirmedReceivedBy (7 empty) | SalespersonPersonID=3 (6,990 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (2 empty), ConfirmedReceivedBy (2 empty) | SalespersonPersonID=14 (6,984 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (6 empty), ConfirmedReceivedBy (6 empty) | SalespersonPersonID=7 (6,964 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (5 empty), ConfirmedReceivedBy (5 empty) | SalespersonPersonID=8 (6,958 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (4 empty), ConfirmedReceivedBy (4 empty).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=the pattern changes | text: Test 8, by TotalChillerItems (partial): TotalChillerItems=0 (69,567 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (48 empty), ConfirmedReceivedBy (48 empty) | TotalChillerItems=1 (956 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (8 empty), ConfirmedReceivedBy (8 empty) | TotalChillerItems=2 (41 rows): empty -; filled ConfirmedDeliveryTime, ConfirmedReceivedBy | TotalChillerItems=3 (2 rows): empty -; filled ConfirmedDeliveryTime, ConfirmedReceivedBy.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=the pattern changes | text: Test 8, by TotalDryItems (partial): TotalDryItems=3 (17,195 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (16 empty), ConfirmedReceivedBy (16 empty) | TotalDryItems=2 (17,039 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (15 empty), ConfirmedReceivedBy (15 empty) | TotalDryItems=4 (16,895 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (12 empty), ConfirmedReceivedBy (12 empty) | TotalDryItems=5 (13,681 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (5 empty), ConfirmedReceivedBy (5 empty) | TotalDryItems=1 (5,740 rows): empty -; filled -; partly empty ConfirmedDeliveryTime (8 empty), ConfirmedReceivedBy (8 empty) | TotalDryItems=0 (16 rows): empty -; filled ConfirmedDeliveryTime, ConfirmedReceivedBy.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=a row breaks a dependency | text: Test 1: 18 functional dependencies between non-key columns over the whole extract (7 involving audit columns, a batch-edit signature, not listed): CustomerID -> BillToCustomerID; CustomerID -> ContactPersonID; CustomerID -> AccountsPersonID; CustomerID -> DeliveryInstructions; BillToCustomerID -> AccountsPersonID; ContactPersonID -> CustomerID; ContactPersonID -> BillToCustomerID; ContactPersonID -> AccountsPersonID; ContactPersonID -> DeliveryInstructions; AccountsPersonID -> BillToCustomerID; and 8 more in the evidence.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=the structured columns change | text: Test 6: ReturnedDeliveryData holds JSON in 70,566 rows, 70,566 of which parse.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract, or a schema change | text: Test 6: ReturnedDeliveryData holds an event list (a grain of its own: delivery events) and, once delivered, DeliveredWhen and ReceivedBy; a check constraint requires valid JSON.
- C9 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=every new extract, or a schema change | text: Test 9: ConfirmedDeliveryTime and ConfirmedReceivedBy are described as promoted from the JSON: derived copies that can disagree with their source.
- C10 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract, or a schema change | text: Test 1: CustomerID determines BillToCustomerID, ContactPersonID, AccountsPersonID and DeliveryInstructions: customer attributes copied onto the invoice.
- C11 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=round 2 compares them with the lines | text: Test 3 candidate: TotalDryItems and TotalChillerItems are described as package totals for the driver; whether they equal anything summed from the lines is a cross-table test for round 2.
- C12 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract, or a schema change | text: Test 10: IsCreditNote exists but no credit note is present; a build must still treat it as a sign switch.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
