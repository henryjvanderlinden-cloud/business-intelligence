# Securitisation: tracking cash for operational-risk reporting

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-060_sol.md](../../30_research/notes/XREV_2026-10-25_fs-060_sol.md).

## 1. Why investors care

1. Investors track cash movements from an operational-risk standpoint, not a credit-risk one. (This is Rick's experience.)
2. They don't only ask what explains a balance. They also ask where the cash is, who controls it, and whether it moved on time.

## 2. Three chains, plus the waterfall

1. **Postings → instruments.** Explains balance changes. See [050_securitisation-movement-reconciliation.md](050_securitisation-movement-reconciliation.md).
2. **Payments → postings.** Explains how received cash was allocated.
3. **Cash events → accounts.** Explains which actual accounts the cash moved between.
4. **The waterfall** is not a place where cash sits. It is a priority-of-payments calculation that produces allocations and payment instructions. Model each waterfall run (basis, priority items, allocations, resulting instructions) separately from the cash events it triggers.

## 3. Accounts

1. **Key the Account hub by real account identity:** account identifier within the account bank and source namespace. Never key it by role name.
   - A move to another account bank creates a new scoped identity, not a satellite change. Link the old and new accounts with an explicit succession relationship.
   - Where an account is renumbered but remains legally the same account, record a same-as relationship between the identifiers.
2. **Roles are effective-dated relationships**, not identities:
   - one account can be both "collection" and "issuer"
   - a role can move to another account, for example after an account-bank downgrade
3. Holder and currency go in historised satellites. The provider is part of the key; see point 1. Control and ownership relationships are modelled separately.
4. **Reserves and GICs** are their own business concepts when they don't coincide with a bank account. A reserve can be a designated balance within an account. A GIC is a contractual investment claim.

## 4. Commingling exposure is a legal question, not a location

1. Cash at the servicer before a sweep is not automatically servicer exposure. Equally, cash can be exposed before or after a sweep.
2. Exposure depends on:
   - account holder and beneficial ownership
   - security, trust or control arrangements, and whether each is perfected and enforceable against the servicer's insolvency estate (notice, registration or control steps completed), under which jurisdiction
   - segregation
   - permitted commingling period
   - insolvency treatment
   - account-bank eligibility
   - any commingling reserve or guarantee
3. Record these per account and role, with effective dates. Report unswept cash as servicer exposure only where they make it part of, or vulnerable to, the servicer's estate.

## 5. Cash events

1. **Give statement entries and transaction details identities at their own reported grain.** A batched camt.053 entry may supply only an entry reference for the aggregate. A transfer's debit and credit postings may carry different bank references and nothing in common. So model a cross-account movement or instruction as a separate event, linked to the postings by explicit matching evidence. That evidence can be unresolved; don't invent identity. Link postings to accounts in typed debit and credit roles.
2. **A link keyed only on from-account and to-account would not work.** It would collapse every daily sweep between the same two accounts into one relationship.
3. **Keep instruction, booking, value, settlement, rejection and reversal states distinct.** Store amount and currency at event grain.
4. **Model a payment instruction separately from its bank postings,** for when one instruction is split, netted or retried.
5. **Direct-debit collections and waterfall payments** often involve an account outside the vault (the borrower's or the noteholder's). Allow a counterparty account that is known only by identifier.

## 6. Payments → postings

1. **Allocation is an event,** with its own identity, linked to payment and posting, with effective time, currency, status and source transaction identity.
2. **Deallocation and reallocation are compensating events or effectivised states.** Example: allocate 100, unallocate, reallocate 80. Both the net allocation and the audit trail must be derivable.
3. **Capture allocations as they happen.** A current-snapshot source can lose the first allocation before it was ever stored.
4. **Suspense is an account or ledger classification fed by immutable events:** receipt, allocation, release, write-off, reversal.
   1. Derive the open balance as of a business time, by account and currency.
   2. Age it from the unresolved event, including partial clearings and reopenings.
   3. Unapplied cash and its ageing is itself an operational-risk indicator.

## 7. Reconciliation

1. **Per account, by currency and bank cut-off:**

   > opening booked balance + booked credits − booked debits = closing booked balance

   Classify sweeps, returns and refunds, fees, interest and adjustments separately.
2. **Transfers that have been initiated but not yet settled** reconcile through their own status bridge, between the debit posting and the credit posting.
3. **A collection-cohort reconciliation** is extra, never a replacement. It must state whether "received" means instructed, booked, value-dated or settled.
4. **Sweep lineage.** Where the servicer supplies a remittance or sweep batch listing the collections included, keep that membership:
   1. Link the batch to the bank transfer.
   2. Reconcile batch total, transfer amount and exceptions.
   3. Don't invent amount allocations the source doesn't give. Stop at aggregate lineage only when no finer evidence exists.

   Without batch membership, an omitted receipt can hide behind an equal over-remittance.

## 8. SEPA direct-debit returns, refunds and reversals

1. **These are distinct event types**, each with a reason code, scheme (Core or B2B) and deadline:
   - reject
   - return
   - refund
   - reversal
   - revocation
2. **Store or derive each event's deadline** from the rulebook version, settlement date and interbank business-day calendar. Rejects, returns, reversals and revocations have their own, much shorter scheme deadlines.
   - Under SEPA Core, an authorised debit can be refunded for eight weeks from the debit date. An unauthorised debit can be notified without undue delay, and no later than thirteen months after the debit date.
   - B2B has no authorised-debit refund right. For non-consumer payers, the framework contract may disapply the statutory thirteen-month rule.
   - Example of the failure this prevents: testing a post-settlement technical return against the eight-week refund window reports it as timely after its own deadline has passed.
3. **A refund doesn't necessarily reverse the original sweep.** It may hit the collection account and be funded by later collections, liquidity support, a reserve or the servicer. Record which account was actually debited and how the shortfall was funded.
4. **Linking every dependent exception event (return, refund, reversal) to the original debit:**
   1. Keep every reference the scheme and bank provide: original message, payment-information, instruction, end-to-end and transaction identifiers, and the bank's own reference.
   2. Resolve the link using creditor, debtor, mandate, amount, currency, requested collection date and booking context.
   3. A mandate reference identifies a mandate, not one debit. End-to-end IDs can be missing (`NOTPROVIDED`), reused or truncated.
   4. Keep ambiguous or unmatched cases explicitly, rather than forcing a match.

## 9. Independent source: the account bank

1. If you can get them, ingest the account bank statements (camt.053) as an independent source.
2. **A camt.053 is the bank's end-of-day assertion of booked entries.** It is not proof of economic finality:
   - it usually omits pending instructions
   - it can contain batched entries that need their transaction detail
   - it can later be corrected
3. Reconcile it to the servicer's records, and to notifications, intraday reports and payment-status messages where timing matters.
4. Keep disagreements between sources visible rather than declaring either one the truth. Reconciling the servicer and the account bank is still the strongest operational control you can offer investors, and it follows naturally from a vault that keeps record sources apart.

## 10. Candidate investor metrics

1. **Commingling exposure:** unswept cash that, per §4, is genuinely exposed to the servicer, with its ageing.
2. **Sweep timeliness** against the contractual deadline.
3. **Unapplied or suspense cash** and its ageing.
4. **Collection-to-posting lag**, defined by named start and end events.
5. **Direct-debit returns, authorised refunds and unauthorised claims:**
   - reported separately
   - by original debit cohort, both by count and by amount
   - with seasoning and completeness stated, and reason-code breakdowns

   Show a posting-period cash-impact measure separately. A same-period rate (this month's reversals over this month's collections) mixes cohorts and understates recent ones.
6. **Breaks between the servicer report and the account bank statements.**
