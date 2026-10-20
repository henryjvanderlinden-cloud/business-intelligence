---
id: wwi:process:procure-to-pay
subject: wwi/across/processes/procure-to-pay
item: 24
topic: processes
tier: best-effort
summary: Purchase orders are received 1 to 3 days after ordering, mostly 19 days before the expected date; invoiced on receipt; paid 0 to 6 days later.
confidence: unknown
claims: 7
written_by: claude-opus-5-5
written_at: 2026-10-20T08:30:00Z
step: S08-095
method: counts by prototypes/information_analysis/processes.py (blob b1a37f986a92a0860a190d3cc4c50e10a4b4ecf7); readings by claude-opus-5-5
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: fcde434e98483313d7df81238d36ffe0605ffe7989b722d8e436ebebe2572268
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

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=371a4a630b3b80d9 | recheck=every new extract | text: Steps reached: purchase order 2,076; order finalized 2,074; received (stock movement) 2,074; every line finalized 2,074; every line received in full (ReceivedOuters = OrderedOuters) 2,074; supplier invoice 2,074; paid (invoice finalized) 2,070.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=371a4a630b3b80d9 | recheck=every new extract | text: Of 8,376 purchase-order lines, 0 on received orders have ReceivedOuters different from OrderedOuters.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=371a4a630b3b80d9 | recheck=every new extract | text: Days between steps: order to expected delivery: 3 to 20 days, median 20, most often 20 (1,886 rows); order to first receipt: 1 to 3 days, median 1, most often 1 (1,434 rows); expected delivery to first receipt: -19 to -2 days, median -19, most often -19 (1,410 rows); first receipt to supplier invoice: 0 to 0 days, median 0, most often 0 (2,074 rows); supplier invoice to payment: 0 to 6 days, median 4, most often 0 (641 rows).
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=371a4a630b3b80d9 | recheck=every new extract | text: As the data records it: a purchase order is first received 1 to 3 days after its order date, every line of every received order has ReceivedOuters equal to OrderedOuters (C2), each receipt line is one stock movement (across/relations/Warehouse.StockItemTransactions.PurchaseOrderID.StockItemID__Purchasing.PurchaseOrderLines.PurchaseOrderID.StockItemID/01_granularity.md), the supplier invoices on the day of the first receipt, and WWI pays 0 to 6 days later (across/reconciliations/supplier-payments-vs-invoices). ExpectedDeliveryDate is mostly 20 days after ordering and the goods arrive well before it.
- C5 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a process description, the generating script or a second extract settles it | text: Whether the 2 purchase orders without a receipt and the 4 unpaid supplier invoices (C1) are open and will complete, or will stay as they are, is not established from one extract.
- C6 | type=observed | status=proposed | confidence=unknown | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a process description, the generating script or a second extract settles it | text: Why the expected delivery is set 20 days out when receipts come in 1 to 3 days is not established.
- C7 | type=observed | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=every new extract | text: Partly settled by the extract of 2016-06-02 (analysis/wwi/_source/22_stability.md#C19, #C21): the 2 purchase orders without a receipt were received in full the next day, one movement per line; the 4 unpaid supplier invoices were still open in full.

## Reasoning

Each purchase order is followed to its stock receipts (Warehouse.StockItemTransactions.PurchaseOrderID), its lines and its supplier invoice (Purchasing.SupplierTransactions.PurchaseOrderID).

## Uncertainties

Part receipts and supplier credit notes: none occurs.

## For a person

None.
