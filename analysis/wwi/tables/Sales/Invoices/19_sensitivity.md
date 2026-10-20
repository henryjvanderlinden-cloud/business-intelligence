---
id: wwi:object:2018106230
subject: wwi/tables/Sales/Invoices
item: 19
topic: sensitivity
tier: minimum
summary: Names of the people who received deliveries, with GPS positions and times in JSON; contact and accounts persons; possibly delivery addresses.
confidence: low
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: d89a1e72bf72f1577926929cb7c514b71af6cf08eb13a8181f4f8688da7f99ce
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

- C1 | type=declared | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a column is added or renamed | text: Columns whose names or descriptions point to personal, contact, location, credential or free-text content: Comments, DeliveryInstructions, InternalComments, ConfirmedReceivedBy.
- C2 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a foreign key changes | text: Every row names the person who last edited it (LastEditedBy -> Application.People): attribution of work to identifiable staff, employee data whatever the table's content.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=a foreign key changes | text: Columns referring to people in Application.People (names, contact details): AccountsPersonID, ContactPersonID, PackedByPersonID, SalespersonPersonID, besides the audit column LastEditedBy.
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a,3163d80faa939828 | recheck=every new extract, or a schema change | text: ConfirmedReceivedBy holds a person's name on 70,510 invoices (663 distinct names); the delivery JSON repeats it, and its 70,510 delivery events carry a DriverID, a Latitude and a Longitude.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract, or a schema change | text: DeliveryInstructions has 663 distinct values and CustomerID determines it (27_peculiarities.md, test 1); its lowest and highest values are address lines.
- C6 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=b7b43b18cf6be97a | recheck=every new extract, or a schema change | text: So DeliveryInstructions may hold delivery addresses, personal data where the customer is an individual; only two values were seen.
- C7 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=98f988a2bfe42550 | recheck=the author rules | text: Proposed reading, not legal advice: the receiver's name with time and place of delivery is personal data, as is the driver's movement.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None for the as-is analysis.
