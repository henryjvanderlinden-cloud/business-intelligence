---
id: wwi:object:1554104577
subject: wwi/tables/Purchasing/PurchaseOrderLines
item: 27
topic: peculiarities
tier: minimum
summary: Order-level values repeated on every line; item attributes copied onto lines; quantities counted in outer packages of varying type.
confidence: medium
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ff3afe91393905debcfd3922ce15e0214e6da79b9a15f2e41e4abf504040d77e
last_checked_at: 2026-10-18T20:32:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=the empty-column patterns change | text: Test 8: 2 distinct patterns of empty columns; the most common: 8,367 rows with none empty; 9 rows with LastReceiptDate empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=the pattern changes | text: Test 8, by IsOrderLineFinalized (exact): IsOrderLineFinalized=1 (8,367 rows): empty -; filled LastReceiptDate | IsOrderLineFinalized=0 (9 rows): empty LastReceiptDate; filled -.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=the pattern changes | text: Test 8, by PackageTypeID (partial): PackageTypeID=6 (5,779 rows): empty -; filled -; partly empty LastReceiptDate (6 empty) | PackageTypeID=7 (2,588 rows): empty -; filled -; partly empty LastReceiptDate (3 empty) | PackageTypeID=9 (9 rows): empty -; filled LastReceiptDate.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=a row breaks a dependency | text: Test 1: 10 functional dependencies between non-key columns over the whole extract (7 involving audit columns, a batch-edit signature, not listed): PurchaseOrderID -> LastReceiptDate; PurchaseOrderID -> IsOrderLineFinalized; StockItemID -> Description; StockItemID -> PackageTypeID; StockItemID -> ExpectedUnitPricePerOuter; Description -> StockItemID; Description -> PackageTypeID; Description -> ExpectedUnitPricePerOuter; ReceivedOuters -> IsOrderLineFinalized; LastReceiptDate -> IsOrderLineFinalized.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=every new extract, or a schema change | text: Test 4: PurchaseOrderID determines LastReceiptDate, IsOrderLineFinalized, LastEditedBy and LastEditedWhen - receipt happens per order, and its values are repeated on every line of the order.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060 | recheck=every new extract, or a schema change | text: Test 1: StockItemID determines Description, PackageTypeID and ExpectedUnitPricePerOuter: item attributes carried on the line.
- C8 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=cd3cf333fabc9060,9e1f3e773862db95 | recheck=every new extract, or a schema change | text: Test 17: OrderedOuters and ReceivedOuters count outer packages (PackageTypeID: carton, each or packet), not selling units; summed across items they add unlike units.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
