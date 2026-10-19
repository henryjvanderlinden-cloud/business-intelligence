# XREV 2026-10-19 — round-2 reconciliations on suppliers and stock — astra

```yaml
object:        analysis/wwi/across/reconciliations/{supplier-payments-vs-invoices, supplier-invoices-vs-purchase-order-lines, stock-holdings-vs-movements}/, as first generated on 2026-10-19 (uncommitted; moved to scratch/_superseded/reconciliations_v1).
reviewer:      gpt-6-astra, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by sol on the other three.
assignment:    against ADR-0017, ADR-0019, analysis/README.md section 5 and ADR-0020: up to three false or overstated
               claims; up to two places where the code measures something else than the claim says; up to two
               confidences breaking section 5; any design advice. 400 words; praise, summary and general assessment
               forbidden. Python allowed so that the reviewer could read what each count measures.
second reader: assignment set by Claude Opus 5.5, which wrote reconcile.py and the readings the same evening.
verdict:       FAILS [equal expected-price totals do not establish line prices; stock discrepancies do not establish independent maintenance]
```

Astra's answer, verbatim:

1. `analysis/wwi/across/reconciliations/stock-holdings-vs-movements/16_reconciliation.md#C4`: "holdings are maintained apart from the movement ledger" and "stock is added ... without a stock movement." Evidence `a2fca43ecf81447c` establishes discrepancies, not their cause. C5 explicitly allows movements missing from the extract, which would invalidate this inference about the source.

   `analysis/wwi/across/reconciliations/supplier-invoices-vs-purchase-order-lines/16_reconciliation.md#C3`: "the invoice adds no actual price of its own." Evidence `57d69874b8999d1a` compares invoice totals with expected-price totals; it never observes actual invoice line prices. Two quantity-one lines expected at 10 and 20 but actually invoiced at 11 and 19 satisfy the comparison. This is a logical counterexample, not an observed discrepancy.

2. `payments_vs_invoices()` labels `fin_n[(SupplierID, FinalizationDate)]` as `invoices_settled_per_payment`. `supplier-payments-vs-invoices/16_reconciliation.md#C2` consequently says "Invoices settled per payment." The code counts invoices finalized on the same supplier-day, not allocations from that payment. Equal totals support an inferred match, not an observed settlement link.

   `stock_holdings_vs_movements()` defines additions solely by previously unseen transaction IDs. It ignores quantity changes and deletions of existing transactions and does not filter by occurrence date. C2 accurately describes additions between extracts, but C4's "a day's movements" is broader: this is neither the net ledger change nor necessarily that day's business activity. An existing transaction corrected upward changes the ledger without entering `added`.

3. `analysis/wwi/across/reconciliations/supplier-payments-vs-invoices/16_reconciliation.md#C2` assigns high confidence to settlement attribution. High is supported for the supplier-day count; the allocation interpretation belongs with C5's medium-confidence implicit matching.

   `analysis/wwi/across/reconciliations/stock-holdings-vs-movements/16_reconciliation.md#C4` assigns medium confidence to an unestablished maintenance mechanism. This is not a consistently observed rule: only discrepancies were measured. Whether the source adds stock without movements remains unknown, as C5 already acknowledges; source procedures or complete change evidence would settle it.

4. No design advice or future decision found in the three files.

VERDICT: FAILS + matching expected-price totals does not establish actual line prices; stock discrepancies do not establish independent maintenance.

## Dispositions

All findings accepted and fixed the same evening (step S08-085):

1. **"Holdings are maintained apart from the ledger".** Replaced by what the counts show - a level and a day's change
   that the movements do not explain, in this extract - and the cause left to the unknown claim, which now also names
   a movement history that does not start from zero.
2. **"The invoice adds no actual price of its own".** Restated: a supplier invoice holds no lines or prices, and its
   total equals the expected-price total; a new unknown claim says that offsetting line differences would pass.
3. **"Invoices settled per payment"** (shared code with the customer side): renamed as in sol's note; the confidence
   of the count stays high because it now claims only the count.
4. **Movements by new ids only.** stock_holdings_vs_movements now also counts earlier movements whose quantity changed
   (0) and earlier movements deleted (0) between the extracts, and the claims say so.
5. **The maintenance mechanism at medium.** Gone with 1: the remaining reading is an observed consequence of the
   counts, and the mechanism is unknown.

Section 4: none found.
