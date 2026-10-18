---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 19
topic: sensitivity
tier: minimum
summary: No names or contact details in the table, but four columns identify people whose names, e-mail addresses and phone numbers are in Application.People; three free-text columns are empty today.
confidence: unknown
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-18T12:40:00Z
step: S08-042
method: reading of evidence written by prototypes/information_analysis/evidence_orders.py (blob 5b39164821d92e89109688e68c204752d9edeff5) and of catalogue queries through the sandbox request folder
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: df493a1a20d890a2e0931a1a6e6ddd9510bec9c2a6d09162f4d0a907b0bebca6
last_checked_at: 2026-10-18T12:40:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: analysis layout 1 of c7b7aa2 (moved out of the repository)
superseded_by: none
recheck_when: a free-text column fills, Application.People changes, or the author rules
---

## Claims

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=597ef697da37cd0e | recheck=a foreign key changes | text: SalespersonPersonID, PickedByPersonID, ContactPersonID and LastEditedBy refer to Application.People.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7aa3df3f1beb91b7 | recheck=Application.People changes | text: The 10 salespersons are flagged salespersons, the 19 pickers are employees, and the 663 contacts are not employees; all 663 contacts have an e-mail address and a phone number in Application.People.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8,b6da684f0b7581f7 | recheck=a free-text column fills | text: Comments and DeliveryInstructions (described as sent to the customer) and InternalComments are empty in every row.
- C4 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=597ef697da37cd0e,7aa3df3f1beb91b7 | recheck=the author rules | text: Proposed reading, not legal advice: under the GDPR a linkable person id is personal data, so the table is personal data while Application.People is reachable, and salesperson and picker with dates are employee-activity data.
- C5 | type=observed | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=customer names are classified | text: Some customer names read as a person's name rather than a company's - an impression from reading, not a measurement; if so, CustomerID identifies natural persons too.
- C6 | type=intended | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=the author rules | text: Legal basis, retention and whether person ids are pseudonymised before the warehouse are not established; a person must rule.

## Reasoning

The structure is declared and observed. The legal classification is the model's reading and needs a person. WWI's data is synthetic, so no real person is affected; the classification is practised as if it were real.

## Uncertainties

C4 to C6. A check that alerts when the free-text columns fill would settle C3 per load.

## For a person

1. Is Sales.Orders personal data, and are salesperson and picker treated as employee-monitoring data? 2. May the person ids be loaded as they are, or pseudonymised first?
