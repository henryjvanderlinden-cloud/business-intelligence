---
id: wwi:fk:FK_Sales_CustomerTransactions_PaymentMethodID_Application_PaymentMethods
subject: wwi/across/relations/Sales.CustomerTransactions.PaymentMethodID__Application.PaymentMethods.PaymentMethodID
item: 27
topic: peculiarities
tier: minimum
summary: Warnings: fan-out, chasm, current versions.
confidence: high
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 44fef738b353833eca086d59ebea46802593b4418a1a329198d32862bcc3bfcf
last_checked_at: 2026-10-19T20:31:00Z
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: Fan-out: joined from Application.PaymentMethods to Sales.CustomerTransactions, a Application.PaymentMethods row repeats up to 26,676 times (median 26,676), so a measure of Application.PaymentMethods summed after the join is counted once per referring row.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=every new extract | text: Chasm trap: Application.PaymentMethods also has other referring columns with several rows per parent (Purchasing.SupplierTransactions.PaymentMethodID (up to 2,440 per parent)); joining Sales.CustomerTransactions and one of these through Application.PaymentMethods pairs every row of one with every row of the other for the same parent.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=59ce7f1dd67ff9d6 | recheck=the temporal type changes | text: Application.PaymentMethods is system-versioned and the extract holds its current versions: joined in the extract, a row of Sales.CustomerTransactions that names a row of Application.PaymentMethods gets that row's attributes as they are on 2016-06-01, not as they were when the referring row was written; earlier versions are in the history table.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
