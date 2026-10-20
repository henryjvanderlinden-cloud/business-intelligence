---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 27
topic: peculiarities
tier: minimum
summary: Item attributes copied onto the line, but the price is the price at the time; tax and extended price derived and rounded per line; quantities in mixed package units.
confidence: high
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a450891eaeade41ce15c8097eee5390bcd9678fc811045b440235fd42c933f74
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c830515726d3ad77 | recheck=the empty-column patterns change | text: Test 8: 1 distinct pattern of empty columns; the most common: 228,432 rows with none empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c830515726d3ad77 | recheck=a row breaks a dependency | text: Test 1: 10 functional dependencies between non-key columns over the whole extract (3 involving audit columns, a batch-edit signature, not listed): StockItemID -> Description; StockItemID -> PackageTypeID; StockItemID -> TaxRate; Description -> StockItemID; Description -> PackageTypeID; Description -> TaxRate; PackageTypeID -> TaxRate; UnitPrice -> TaxRate; ExtendedPrice -> TaxRate; ExtendedPrice -> TaxAmount.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c830515726d3ad77 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c830515726d3ad77 | recheck=every new extract, or a schema change | text: Test 1: StockItemID determines Description, PackageTypeID and TaxRate, but not UnitPrice: the price on the line is the price at the time of sale, not a copy of the item's current price.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=bb16c730135dd8e6 | recheck=every new extract, or a schema change | text: Test 9: TaxAmount and ExtendedPrice are derived from Quantity, UnitPrice and TaxRate on every line (09_derived.md).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c830515726d3ad77,21777813c14f1502,28e741112736c678 | recheck=every new extract, or a schema change | text: Test 17: Quantity counts packages of the line's PackageTypeID (each, packet, pair or bag), so a sum across items adds unlike units.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
