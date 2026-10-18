---
id: wwi:object:510624862
subject: wwi/tables/Sales/InvoiceLines
item: 28
topic: arithmetic
tier: best-effort
summary: Tax is rounded per line, half up, to cents; totals are sums of rounded line values.
confidence: high
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: a450891eaeade41ce15c8097eee5390bcd9678fc811045b440235fd42c933f74
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=bb16c730135dd8e6 | recheck=a line breaks the rounding rule | text: Rounding half up to cents reproduces TaxAmount on all 228,432 lines; rounding half to even would miss 2,113; the largest difference between rounded and unrounded tax is 0.005.
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=bb16c730135dd8e6 | recheck=every new extract, or a schema change | text: As observed, tax computed on an invoice total rather than per line would differ from the sum of TaxAmount.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
