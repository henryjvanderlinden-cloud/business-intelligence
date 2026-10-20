---
id: wwi:object:94623380
subject: wwi/tables/Sales/OrderLines
item: 27
topic: peculiarities
tier: minimum
summary: Picking time is order-level, repeated on lines; item attributes copied, price at the time; mixed package units.
confidence: high
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: c00930db9c641c1b31801c17473429ceaa1b6c45519761d89148dd23ed44a1e7
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=the empty-column patterns change | text: Test 8: 2 distinct patterns of empty columns; the most common: 228,432 rows with none empty; 3,149 rows with PickingCompletedWhen empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=the pattern changes | text: Test 8, by PackageTypeID (partial): PackageTypeID=7 (221,108 rows): empty -; filled -; partly empty PickingCompletedWhen (3,149 empty) | PackageTypeID=9 (5,215 rows): empty -; filled PickingCompletedWhen | PackageTypeID=10 (4,214 rows): empty -; filled PickingCompletedWhen | PackageTypeID=1 (1,044 rows): empty -; filled PickingCompletedWhen.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=the pattern changes | text: Test 8, by TaxRate (partial): TaxRate=15.000 (230,537 rows): empty -; filled -; partly empty PickingCompletedWhen (3,149 empty) | TaxRate=10.000 (1,044 rows): empty -; filled PickingCompletedWhen.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=a row breaks a dependency | text: Test 1: 9 functional dependencies between non-key columns over the whole extract (4 involving audit columns, a batch-edit signature, not listed): OrderID -> PickingCompletedWhen; StockItemID -> Description; StockItemID -> PackageTypeID; StockItemID -> TaxRate; Description -> StockItemID; Description -> PackageTypeID; Description -> TaxRate; PackageTypeID -> TaxRate; UnitPrice -> TaxRate.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=every new extract, or a schema change | text: Test 4: OrderID determines PickingCompletedWhen: all lines of an order are picked at one moment, so the value is order-level, repeated per line.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453 | recheck=every new extract, or a schema change | text: Test 1: StockItemID determines Description, PackageTypeID and TaxRate but not UnitPrice: the price is the price at the time.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cf49010c2c9f9453,10ba08f87c0c050b,b36a5d13889aff12 | recheck=every new extract, or a schema change | text: Test 17: Quantity and PickedQuantity count packages of the line's PackageTypeID (each, packet, pair or bag).

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
