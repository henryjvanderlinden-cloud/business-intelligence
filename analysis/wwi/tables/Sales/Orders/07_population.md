---
id: wwi:object:1154103152
subject: wwi/tables/Sales/Orders
item: 07
topic: population
tier: minimum
summary: All 73,653 orders of 2013-01-01 to 2016-06-01 for 663 customers, backorders included; no placeholder found; no cancellation status exists; 3,087 never picked.
confidence: unknown
claims: 8
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
recheck_when: every new extract
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=a new extract | text: OrderDate runs from 2013-01-01 to 2016-06-01; 2016 is a part year (9,675 orders).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7aa3df3f1beb91b7 | recheck=a customer is added or removed | text: 663 customers, all present in Sales.Customers.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=c6e5d1bc0af05898 | recheck=a new backorder is created | text: Backorders are rows of the population (7,546); a count of orders includes them unless excluded (01_granularity.md#C6).
- C4 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8,7aa3df3f1beb91b7 | recheck=a new customer name or a placeholder-like row appears | text: No placeholder order or customer was found: OrderID is gapless and no customer name contains unknown, test, dummy or n/a; a name search is not proof.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=7aa3df3f1beb91b7 | recheck=another technical user appears | text: 5 rows, ordered between 2013-08-13 and 2016-05-06, were last edited by person 1, Data Conversion Only, who is not an employee and cannot log on.
- C6 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=none | recheck=a deletion, a status value or documentation of cancellation is found | text: There is no status column, so cancelled, rejected or held orders cannot be told apart; whether WWI cancels orders at all is not established.
- C7 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=old unpicked orders are picked as days advance | text: Whether the 3,087 never-picked orders are a real backlog or an artefact of the generated history is not established (03_temporal.md#C7).
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=77ee039bf95c3ee8 | recheck=an order on a Sunday | text: No orders on Sundays and about half the weekday volume on Saturdays (6,564 against about 13,400).

## Reasoning

Counts are exact over the whole extract. Two questions about who belongs to the population cannot be answered from the data.

## Uncertainties

C6: cancellations. C7: the meaning of the never-picked orders.

## For a person

Should never-picked orders older than some age count as open orders in reports, or be excluded?
