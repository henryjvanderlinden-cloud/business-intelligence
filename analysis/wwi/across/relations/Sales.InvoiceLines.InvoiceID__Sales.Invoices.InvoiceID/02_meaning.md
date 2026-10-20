---
id: wwi:fk:FK_Sales_InvoiceLines_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Sales.InvoiceLines.InvoiceID__Sales.Invoices.InvoiceID
item: 02
topic: meaning
tier: minimum
summary: Invoice that this line is associated with
confidence: medium
claims: 2
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob 48ceba838b93a9eb864e3d0b8c559252980a0b6c) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4f13fc336406ec0bb1d1037173a280ae7a4db580eb0f1c2964eeec23dc885f19
last_checked_at: 2026-10-20T08:31:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of either table
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9ac2d6c6407f6bbc | recheck=the description changes | text: The source describes Sales.InvoiceLines.InvoiceID as "Invoice that this line is associated with".
- C2 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=9ac2d6c6407f6bbc | recheck=every new extract, or a description changes | text: Header and lines: an invoice line belongs to one invoice; every invoice has lines (07).

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
