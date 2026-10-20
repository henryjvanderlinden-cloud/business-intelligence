---
id: wwi:object:1826105546
subject: wwi/tables/Sales/SpecialDeals
item: 27
topic: peculiarities
tier: minimum
summary: Exclusive arcs: scope by any of five optional columns, price by exactly one of three; two rows exercise only one combination.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-20T05:44:00Z
step: S08-088
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 1fab0ac0c38feadfe9bfe300ae286a471a51b393aaa88d88466a89d9b333f329
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e851aae8274c22e9 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 2 rows with StockItemID, CustomerID, CustomerCategoryID, DiscountAmount, UnitPrice empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e851aae8274c22e9 | recheck=a row breaks a dependency | text: Test 1: 0 functional dependencies between non-key columns over the whole extract (0 involving audit columns, a batch-edit signature, not listed).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=e851aae8274c22e9 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C4 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=da3666690fc688ae | recheck=every new extract, or a schema change | text: Test 9: the scope columns (StockItemID, CustomerID, BuyingGroupID, CustomerCategoryID, StockGroupID) are optional, and by its name a check requires exactly one of the pricing columns (DiscountAmount, DiscountPercentage, UnitPrice).
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=more deals appear | text: How deals combine when several apply to one sale is not established from two rows.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
