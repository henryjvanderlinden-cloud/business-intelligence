---
id: wwi:fk:FK_Sales_CustomerTransactions_InvoiceID_Sales_Invoices
subject: wwi/across/relations/Sales.CustomerTransactions.InvoiceID__Sales.Invoices.InvoiceID
item: 01
topic: granularity
tier: minimum
summary: Sales.CustomerTransactions to Sales.Invoices; at most one row of Sales.CustomerTransactions per row of Sales.Invoices in this extract.
confidence: medium
claims: 4
written_by: claude-opus-5-5
written_at: 2026-10-19T20:31:00Z
step: S08-079
method: mechanical claims by prototypes/information_analysis/write_relations.py (blob e1598587ca50051cb5e35244cfdae309e6e1c028) from the relation's evidence by relations.py; readings by claude-opus-5-5 from that evidence, the catalogue's column descriptions and round 1's files
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 2b4f18335a52663fe6cf5888eeea86b4017a10df501e0f58e111ff1148ff2e07
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=the foreign key changes | text: Declared foreign key FK_Sales_CustomerTransactions_InvoiceID_Sales_Invoices from Sales.CustomerTransactions.InvoiceID to Sales.Invoices.InvoiceID, the primary key of Sales.Invoices: each row of Sales.CustomerTransactions names at most one row of Sales.Invoices.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: In this extract 70,566 of 97,242 rows of Sales.CustomerTransactions name one of 70,566 referenced rows of Sales.Invoices (of 70,566); children per referenced parent: from 1 to 1, median 1; 70,566 parents have exactly one.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=every new extract | text: Joined from Sales.CustomerTransactions to Sales.Invoices, the result keeps the grain of Sales.CustomerTransactions: one row per row of Sales.CustomerTransactions (an inner join drops the 26,676 rows where InvoiceID is empty). Joined the other way, each row of Sales.Invoices repeats once per row of Sales.CustomerTransactions that names it (C2).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=32b2eaffd73eb69a | recheck=a second row refers to the same parent | text: One-to-one on the referenced side in this extract: no row of Sales.Invoices is named by more than one row of Sales.CustomerTransactions. No unique constraint on InvoiceID declares it.

## Reasoning

Mechanical claims from the relation's evidence (relations.py); readings, where present, are the writer's, with their confidence.

## Uncertainties

None.

## For a person

None.
