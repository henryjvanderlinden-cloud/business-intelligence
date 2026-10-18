---
id: wwi:object:1154103152:column:6
subject: wwi/tables/Sales/Orders/columns/BackorderOrderID
item: 03
topic: temporal
tier: minimum
summary: Static during the simulation: no daily procedure sets it, so all 7,546 links come from the generated 2013-2016 history.
confidence: low
claims: 2
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

- C1 | type=implemented | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=ecb87399219a74ce | recheck=the simulator procedures change | text: The daily simulation inserts orders with BackorderOrderID empty and no daily procedure read sets it; read through a summarising fetch.
- C2 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=339f4ab018dfda14 | recheck=a simulated day changes the column | text: No change to the column between 31 May and 1 June 2016.

## Reasoning

Implementation and the one transition agree.

## Uncertainties

Two procedures were read, second-hand; another procedure could set it. Settled by watching the column over more simulated days.

## For a person

None.
