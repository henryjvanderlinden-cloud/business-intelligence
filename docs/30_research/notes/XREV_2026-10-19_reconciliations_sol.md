# XREV 2026-10-19 — round-2 reconciliations on invoices, the ledger and customer payments — sol

```yaml
object:        analysis/wwi/across/reconciliations/{invoice-lines-vs-stock-issues, ledger-invoices-vs-invoice-lines, customer-payments-vs-invoices}/, as first generated on 2026-10-19 (uncommitted; moved to scratch/_superseded/reconciliations_v1).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; the call timed out at the device bridge and the
               answer was retrieved from the file. Run in parallel with a pass by astra on the other three.
assignment:    against ADR-0017, ADR-0019, analysis/README.md section 5 and ADR-0020: up to three false or overstated
               claims; up to two places where the code measures something else than the claim says; up to two
               confidences breaking section 5; any design advice. 400 words; praise, summary and general assessment
               forbidden. Python allowed so that the reviewer could read what each count measures.
second reader: assignment set by Claude Opus 5.5, which wrote reconcile.py and the readings the same evening.
verdict:       FAILS [the one-to-one of lines and issues claimed from a lookup that cannot see duplicates or unused lines]
```

Sol's answer, verbatim:

1. Claims false or overstated:

   - `analysis/wwi/across/reconciliations/invoice-lines-vs-stock-issues/16_reconciliation.md#C1`: "matches one invoice line" and the implied one-to-one are not established by the cited evidence. The code checks that each movement key exists in a dictionary of line keys, but never checks movement-key uniqueness or that every line key was used.
   - `analysis/wwi/across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C5`: "Matching payments to invoices ... is recorded only by state, not by key" exceeds a profile of `Sales.CustomerTransactions`; the code neither searches other tables nor observes an allocation record. Same-customer, same-day equality permits a candidate grouping, not the asserted recording mechanism.
   - `analysis/wwi/across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C6`: "every payment is fully used" and "The simulation pays all" are not observations made by the code. Zero `OutstandingBalance` on a payment plus aggregate equality does not reveal which invoices the payment was allocated to or the generating process.

2. Code measuring something else:

   - In `invoice_lines_vs_stock_issues`, `invoice_lines` is `len(lines)` after dictionary construction, hence distinct `(InvoiceID, StockItemID)` keys, not invoice-line rows. Per-movement lookup proves existence, not one issue per line.
   - In `payments_vs_invoices`, `invoices_settled_per_payment` is `fin_n[(party, payment date)]`: invoices finalized for that party and date. With no allocation key, it does not measure invoices settled by that payment.

3. Confidence or guessed uncertainty:

   - `analysis/wwi/across/reconciliations/invoice-lines-vs-stock-issues/16_reconciliation.md#C3` guesses that backorder splitting explains the absence of partial issues. `confidence=low` does not cure the admitted untested causal link; this belongs as an uncertainty.
   - `analysis/wwi/across/reconciliations/customer-payments-vs-invoices/16_reconciliation.md#C5` cannot be `medium` for the source-wide absence of a matching key. That is unknown until the full recording mechanism or all possible allocation stores are checked.

4. None.

VERDICT: FAILS + two movements with the same line key and one unused line key can produce every reported reconciliation count while violating the claimed one-to-one.

## Dispositions

All findings accepted and fixed the same evening (step S08-085):

1. **One-to-one not measured.** invoice_lines_vs_stock_issues now counts the invoice-line rows and distinct keys, the
   keys with more than one movement (0) and the lines with no movement (0); C1 says "finds an invoice line" and a new
   C2 states the one-to-one counts.
2. **"Recorded only by state, not by key".** Restated as what was examined: no key in Sales.CustomerTransactions links a
   payment to invoices, and the match can be rebuilt on (CustomerID, date) in this extract; a new unknown claim says
   that another store of allocations is not ruled out.
3. **"Every payment is fully used", "the simulation pays".** Replaced by the observed facts (payment OutstandingBalance
   0, equal to the invoices finalized that day, invoices finalized one day after) and "consistent with" a pattern.
4. **"Invoices settled per payment".** Renamed in the code and the claim: invoices finalized on the payment's
   customer-day, with the note that these are candidates, not allocations.
5. **The backorder explanation as a low claim.** Moved to the Uncertainties section as an untested link.

Section 4: none found.
