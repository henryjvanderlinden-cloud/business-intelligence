---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 09
topic: derived
tier: best-effort
summary: TaxAmount = round(Quantity x UnitPrice x TaxRate / 100) per line; ExtendedPrice = Quantity x UnitPrice + TaxAmount; LineProfit derived from a cost not on the line.
confidence: unknown
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-18T13:20:00Z
step: S08-054
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a450891eaeade41ce15c8097eee5390bcd9678fc811045b440235fd42c933f74
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=bb16c730135dd8e6 | recheck=a line breaks the formula | text: ExtendedPrice equals Quantity x UnitPrice + TaxAmount on all 228,432 lines.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=bb16c730135dd8e6 | recheck=a line breaks the formula | text: TaxAmount equals Quantity x UnitPrice x TaxRate / 100 rounded to cents on all lines (exactly, without rounding, on 220,700).
- C3 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the cost basis is found | text: LineProfit is described as profit at current cost price; the cost is not on the line, so its formula is not established.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

LineProfit's cost basis: Warehouse.StockItemHoldings.LastCostPrice is the obvious candidate, a cross-table test for round 2.

## For a person

None.
