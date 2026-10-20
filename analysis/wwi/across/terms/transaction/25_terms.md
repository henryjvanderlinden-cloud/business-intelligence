---
id: wwi:term:transaction
subject: wwi/across/terms/transaction
item: 25
topic: terms
tier: best-effort
summary: "Transaction" names three ledgers - customer, supplier and stock - that share one numbering; two record money, one goods.
confidence: medium
claims: 3
written_by: claude-opus-5-5
written_at: 2026-10-20T05:51:00Z
step: S08-092
method: readings by claude-opus-5-5 linking the claims that own each fact; written by prototypes/information_analysis/write_glossary.py (blob ffcc3813a793cc9facce4b98cc396d0f16cffa08)
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: none
last_checked_at: 2026-10-20T05:51:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: a linked claim changes
---

## Claims

- C1 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: The keys of Sales.CustomerTransactions, Purchasing.SupplierTransactions and Warehouse.StockItemTransactions never overlap and together fill one range (tables/Sales/CustomerTransactions/06_keys.md#C3).
- C2 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: That the three tables draw their keys from one shared numbering is the reading of that partition, not an observed mechanism.
- C3 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-20 | checked=2026-10-20 | evidence=none | recheck=a linked claim changes | text: The first two record amounts owed and paid; the third records quantities of goods moved, issued once per invoice line (across/reconciliations/invoice-lines-vs-stock-issues/16_reconciliation.md#C2). A "transaction" count adds unlike things unless the ledger is named.

## Reasoning

Each claim links the files that own the facts it reads.

## Uncertainties

None.

## For a person

None.
