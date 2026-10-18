---
id: wwi:object:1474104292
subject: wwi/tables/Warehouse/StockItemHoldings
item: 27
topic: peculiarities
tier: minimum
summary: Levels, not movements: semi-additive quantities; the stock item split over two tables.
confidence: high
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: bb1ea17573cd7d7073444df38e148e0a4fc7ac5b6c6bc1078e0bd538c0085e24
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a4dfbd2511423ab3 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 227 rows with none empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a4dfbd2511423ab3 | recheck=a row breaks a dependency | text: Test 1: 3 functional dependencies between non-key columns over the whole extract (2 involving audit columns, a batch-edit signature, not listed): LastStocktakeQuantity -> BinLocation; LastStocktakeQuantity -> ReorderLevel; LastStocktakeQuantity -> TargetStockLevel.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a4dfbd2511423ab3 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=a4dfbd2511423ab3 | recheck=every new extract, or a schema change | text: Test 2: QuantityOnHand, LastStocktakeQuantity, ReorderLevel and TargetStockLevel are levels: summable across items, never across time.
- C5 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=80a4585b8f062d77 | recheck=every new extract, or a schema change | text: Test 1 across tables: one entity (stock item) split over two tables by volatility; joined on the shared key in round 2.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
