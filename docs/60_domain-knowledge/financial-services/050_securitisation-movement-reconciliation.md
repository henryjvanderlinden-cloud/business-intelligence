# Securitisation: explaining position changes from postings

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. The requirement

1. Positions are reported monthly per loan.
2. The change between two monthly positions must be explained by the underlying transactions.

## 2. Core recommendation: a roll-forward (movement) model

1. Build a fact at the grain **instrument × period × movement type**.
2. Per loan it closes the identity: opening balance + Σ movements = closing balance.
3. Store the unexplained remainder as its own movement type ("residual"). Never absorb it silently.
4. The residual is the data-quality instrument:
   - it should trend to zero
   - every non-zero value is an investigation item
5. Investor reports and the pool-level movement waterfall are aggregations of this one fact.

## 3. Decisions that determine whether it closes

1. **Source postings, not payments.**
   1. Payments explain cash. Balances also move for non-cash reasons: interest capitalisation, fees, write-offs, restructurings, FX and accounting adjustments.
   2. A received payment is split across arrears, interest, principal and fees inside the loan servicing system.
   3. Loan sub-ledger postings, after allocation, are what reconcile to the position. Payments are context, linked to postings where possible. See [060_securitisation-cash-tracking.md](060_securitisation-cash-tracking.md).
2. **A controlled movement taxonomy.**
   1. Map raw transaction codes to securitisation categories:
      - scheduled principal
      - partial and full prepayment
      - further advance
      - capitalisation
      - arrears change
      - write-off and recovery
      - repurchase
      - substitution
      - pool addition and removal
   2. The mapping is a business rule. Put it in the business vault and version it, so you can tell which mapping produced which report.
3. **Pool membership as a temporal link.**
   1. Model Instrument ↔ securitisation as a link with an effectivity satellite (valid time).
   2. Entering and leaving the pool (sale, repurchase, substitution, redemption) are movement types in their own right.
   3. Otherwise the pool-level reconciliation breaks whenever the composition changes.
4. **One time basis on both sides.**
   1. This is where most reconciliations fail. Example: a posting booked in November but value-dated October.
   2. Reconcile positions and transactions on the same axis, preferably transaction time: what was known at month-end close.
   3. Report back-dated corrections separately, as restatement deltas against the earlier as-of view. The bitemporal model exists for exactly this split.
5. **Grain alignment.**
   1. Postings often arrive at account or contract level. Securitisation reporting sits at loan-part level; for Dutch mortgages, that means individual loan parts (leningdelen) with different redemption types.
   2. Resolve the mapping explicitly in a link.
   3. Savings and bank-savings mortgages need extra care, because the linked savings balance moves separately from the loan balance.

## 4. Data Vault placement

| Element | Data Vault construct |
|---|---|
| Postings | Non-historised link |
| Positions | Snapshot satellites on the Instrument hub |
| Month-end views | PIT tables |
| Movement fact and residual | Derived in the business vault |
| Reconciliation mart | Reads only from the movement fact, so the identity stays auditable end to end |
