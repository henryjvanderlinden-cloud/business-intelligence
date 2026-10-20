---
id: wwi:process:order-to-cash
subject: wwi/across/processes/order-to-cash
item: 24
topic: processes
tier: best-effort
summary: Order, picking, invoice and stock issue fall on one day; delivery and payment the next; a shortage becomes a backorder, picked and invoiced later.
confidence: unknown
claims: 8
written_by: claude-opus-5-5
written_at: 2026-10-20T08:30:00Z
step: S08-095
method: counts by prototypes/information_analysis/processes.py (blob b1a37f986a92a0860a190d3cc4c50e10a4b4ecf7); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: ec6e8f59e2532a4e0b933b8d45e479a973d9b948c25f9a6a21fb8355bb43df1f
last_checked_at: 2026-10-20T08:30:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change of the tables followed
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dacde258e08a38d | recheck=every new extract | text: Steps reached: order 73,653; order split: has a backorder 7,546; order is a backorder 7,546; picked 70,566; invoiced 70,566; delivery confirmed 70,510; stock issued 70,566; booked in the customer ledger 70,566; paid (entry finalized) 70,510.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dacde258e08a38d | recheck=every new extract | text: Days between steps: order to picking completed: 0 to 1,116 days, median 0, most often 0 (66,087 rows); picking completed to invoice: 0 to 0 days, median 0, most often 0 (70,566 rows); order to invoice: 0 to 1,116 days, median 0, most often 0 (66,087 rows); invoice to delivery confirmed: 1 to 1 days, median 1, most often 1 (70,510 rows); invoice to payment: 1 to 1 days, median 1, most often 1 (70,510 rows).
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dacde258e08a38d | recheck=every new extract | text: Orders picked but not invoiced: 0.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dacde258e08a38d | recheck=every new extract | text: As the data records it: an order is picked, invoiced and issued from stock on the day picking is completed, which is the order date for all orders but backorders; the goods are confirmed delivered the next day and the bill-to customer's payment settles the invoice that same next day (across/reconciliations/customer-payments-vs-invoices). Every picked order is invoiced and every invoiced order is picked.
- C5 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=6dacde258e08a38d | recheck=every new extract | text: 7,546 orders have a backorder and 7,546 orders are backorders (C1); 4,464 of the 4,479 invoices dated after their order are for backorders, up to 1,116 days later (across/relations/Sales.Invoices.OrderID__Sales.Orders.OrderID/03_temporal.md#C3).
- C6 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=every new extract | text: Round 1 found each original picked without a picker and its backorder sharing the customer and the customer's purchase-order number (tables/Sales/Orders/columns/BackorderOrderID/02_meaning.md#C2); that a shortage of stock is what splits an order is the reading of Microsoft's description, not tested here.
- C7 | type=intended | status=proposed | confidence=low | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=every new extract | text: The tables record the process as states on rows - PickingCompletedWhen, an invoice, ConfirmedDeliveryTime, a finalized ledger entry - not as an event log: a step's time is a column of the row it changes, and a step that was undone or repeated would leave no trace.
- C8 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a process description, the generating script or a second extract settles it | text: Whether the one-day rhythm is WWI's process or an artefact of the daily simulation is not established.

## Reasoning

Each order is followed through the declared relations (Orders to Invoices on OrderID, Invoices to stock movements and ledger entries on InvoiceID); days are counted between the dates the rows carry.

## Uncertainties

The process for credit notes, returns and part deliveries: none occurs. Whether the timing is the business's or the simulation's.

## For a person

None.
