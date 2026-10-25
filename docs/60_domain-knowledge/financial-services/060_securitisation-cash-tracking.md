# Securitisation: tracking cash for operational-risk reporting

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. Why investors care

1. Investors track cash movements from an operational-risk standpoint, not a credit-risk one. (This is Rick's experience.)
2. They don't only ask what explains a balance. They also ask where the cash physically is, and whether it moved on time.

## 2. Three chains

1. **Postings → instruments.** Explains balance changes. See [050_securitisation-movement-reconciliation.md](050_securitisation-movement-reconciliation.md).
2. **Payments → postings.** Explains how received cash was allocated.
3. **Payments and transfers → accounts.** Explains where cash sits along the structure: borrower → collection account → issuer account → waterfall.

## 3. Modelling the third chain

1. Make **Account** a hub covering every account in the structure: the servicer's collection account, the issuer transaction account, reserve accounts, GIC accounts.
2. Model **Transfers** as a transactional link between a from-account and a to-account. Its attributes:
   - amount
   - value date
   - booking date
   - transfer type: collection, sweep or waterfall payment
3. This answers the commingling question directly:
   - Cash collected but not yet swept to the issuer account is exposure to the servicer.
   - Its ageing against the contractual sweep deadline is the metric investors watch.

## 4. Payments → postings

1. The relationship is many-to-many:
   - One payment allocates to interest, principal, arrears and fees.
   - One arrears posting can be settled by several payments.
2. Model it as a link with an allocated-amount satellite.
3. Model unallocated cash explicitly, as a suspense position, rather than leaving it as a gap.
4. Unapplied cash, and how long it stays unapplied, is itself an operational-risk indicator.

## 5. Sweeps aggregate

1. A daily sweep moves the sum of many collections.
2. Reconcile sweeps at collection-period level: collections received = swept + in transit.
3. Don't force loan-level lineage through an aggregate transfer. It only produces artificial allocations.

## 6. Reversals

1. SEPA direct debits can be returned or refunded weeks after collection, so cash already swept may have to come back.
2. Model each reversal as a new event, linked to the original through the end-to-end ID or mandate reference. Never model it as an update.
3. The reversal rate per collection period is another figure investors ask about.

## 7. Independent source: the account bank

1. If you can get them, ingest the account bank statements (camt.053) as an independent source.
2. The servicer report says what the servicer claims happened. The account bank says what actually moved.
3. Reconciling the two is the strongest operational control you can offer investors.
4. It falls naturally out of a vault that keeps record sources separate.

## 8. Candidate investor metrics

1. Commingling exposure: cash at the servicer not yet swept, with its ageing.
2. Sweep timeliness against the contractual deadline.
3. Unapplied/suspense cash and its ageing.
4. Collection-to-posting lag.
5. Direct-debit reversal rate per collection period.
6. Breaks between the servicer report and the account bank statements.
