---
id: wwi:source:documentation
subject: wwi/_source
item: 18
topic: documentation
tier: best-effort
summary: The only published documentation found is Microsoft's description of the WWI business and its workflows; it documents no table or column. It gives the financial year (starting 1 November) and the business processes behind the tables.
confidence: unknown
claims: 5
written_by: claude-opus-5-5
written_at: 2026-10-19T07:35:00Z
step: S08-067
method: web search and a summarising fetch of Microsoft Learn (evidence 0f9e0d3eb9dd8048); column descriptions come from the catalogue (extended properties), recorded per table
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-19T07:35:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: Microsoft's description changes, or other documentation is found
---

## Claims

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-19 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: Microsoft Learn's "What is Wide World Importers" describes the business and its workflows (customers, orders, backorders, invoicing, payments, purchasing, stocking, stocktakes, deliveries, credit notes, chilled stock and sensors); it contains no schema, table or column documentation.
- C2 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-19 | evidence=0f9e0d3eb9dd8048 | recheck=Microsoft's description changes | text: The company's financial year starts on 1 November.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-19 | evidence=none | recheck=a column description changes | text: The column-level documentation is the source's own description per column (extended properties in the catalogue); it is recorded in each column's 02_meaning.md and was not checked against Microsoft's text, which has none.
- C4 | type=observed | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-19 | evidence=0f9e0d3eb9dd8048 | recheck=the excerpts are checked against the page | text: The excerpts were returned as verbatim quotations by a summarising fetch and were not compared with the page by hand; a quotation could be paraphrased.
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-19 | checked=2026-10-19 | evidence=none | recheck=other documentation is found | text: Whether other documentation exists (the sample's generation scripts, its data dictionary, a description of the daily simulation's procedures) is not established; nsdn_reader cannot read procedure definitions.

## Reasoning

Item 18 asks what documentation exists and what it covers. The one source found describes the business, not the data, so it supports readings of what a table is for, cited per column as "doc" claims at medium; it never settles what a column holds. The financial year is recorded because it is a fact of the as-is business, not as a reporting choice (ADR-0020).

## Uncertainties

C4: the quotations depend on a summarising fetch. C5: other documentation may exist.

## For a person

Whether WWI's sample has other documentation worth reading (for instance the scripts that generate the data).
