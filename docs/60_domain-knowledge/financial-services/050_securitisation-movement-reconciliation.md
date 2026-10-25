# Securitisation: explaining position changes from postings

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-050_sol.md](../../30_research/notes/XREV_2026-10-25_fs-050_sol.md). The revision changes two recommendations from the original conversation: the time basis (§4.1) and the treatment of pool entry and exit (§3).

## 1. The requirement

1. Positions are reported monthly per loan.
2. The change between two monthly positions must be explained by the underlying transactions.

## 2. Core recommendation: roll-forwards per balance component

1. **One roll-forward per measured stock.** Don't build one bridge for "the balance". Build one per balance component: principal, accrued interest, fees, arrears buckets, impairment and write-off balances, and any linked savings balance.
2. **The grain** is the instrument at its native position grain (loan part, or contract where the source carries positions there) × period × balance component × currency × movement type, plus ledger or reporting basis where more than one exists. Loan-part allocation is a separate result, made only where required (§4.5).
3. **The identity, per component:** opening + Σ movements = closing.
4. **Select postings by component.** Use only the postings that debit or credit that component, with normalised signs. Example: capitalised interest debits principal and credits accrued interest. Summing both sides of the journal gives zero while principal rises, so a bridge that doesn't split by component fails.
5. **Rounding.** Keep source precision and apply one documented rounding policy at the same level as the reported position. Record rounding differences separately from unexplained differences.
6. **The residual** (closing − opening − classified movements) is a control result, not a movement:
   - Store it in its own reconciliation-result object, with the two compared snapshot versions, rule-set version, cut-off and run identifier.
   - Keep it out of movement totals and investor waterfalls, unless it is labelled as an unresolved difference.
   - It should trend to zero; every non-zero value is an investigation item.

## 3. Pool perimeter is a separate bridge

1. **A loan's own roll-forward is independent of whether it is in the pool.** A €200,000 loan that leaves the pool still opens and closes at €200,000. Putting a −€200,000 "removal" into its roll-forward would break its own identity.
2. **Build a separate pool-perimeter bridge:**

   > opening-population balance + economic movements while in scope + entry balances − exit balances = closing-population balance

3. **Entry and exit** are measured at the membership boundary, on the same reporting basis as the pool snapshots: the entry balance immediately before the first movement attributed to the pool, the exit balance immediately after the last one, under one explicit ordering rule.
   - Example: a loan enters on 15 July at €100 and amortises €10 on 20 July. The bridge closes only with the €100 entry balance (0 − 10 + 100 = 90), not with the €90 month-end balance.
   - Sale or repurchase consideration (which can include accrued interest or premium) is kept separate.
4. **Define the population rules:**
   - which loans are in the opening and closing populations
   - effective timestamps, time zone and whether boundaries are inclusive
   - which bridge a movement belongs to on an entry or exit date

## 4. Decisions that determine whether it closes

1. **Time basis: effective date for the period, with a knowledge cut-off.**
   1. Assign movements to periods by business-effective or value date, using the same end-of-day convention as the position.
   2. Separately, select the source versions known at a stated assertion cut-off.
   3. Example: a repayment value-dated 31 October but booked on 2 November belongs to October's bridge once known. Grouping it by November booking time can't explain the October position.
   4. Pin the opening and closing snapshots to compatible knowledge versions. Never mix a restated opening with a published close.
   5. Where required, produce both an original-as-published and a latest-restated reconciliation, and derive the restatement delta by comparing the two complete results. If the published series keeps the prior published close as its opening, its bridge needs an explicitly identified prior-period adjustment. Example: October was published at €100,000 and later corrected to €99,900, with November movements of −€1,000 and a November close of €98,900; the published-series bridge then needs a −€100 prior-period adjustment. The alternative is to restate the prior close and the whole bridge. A late-arriving event is an effective-period movement. A correction to an event is a new assertion about it. Don't lump either into "current-period movement".
   6. This replaces the original conversation's advice to reconcile on transaction time.
2. **Source postings, not payments.** Balances move for non-cash reasons too (capitalisation, fees, write-offs, restructurings, FX, adjustments), and a payment is split across components inside the servicing system. Payments are context. See [060_securitisation-cash-tracking.md](060_securitisation-cash-tracking.md).
3. **Prove the posting population is complete.**
   1. Some platforms change balances without emitting an ordinary posting: migrations, conversion corrections, end-of-day recalculations.
   2. Ingest balance-adjustment, conversion and calculation journals as their own sources where they exist.
   3. Otherwise, treat the difference as an unreconciled control exception, not an economic movement.
4. **A controlled, exhaustive movement taxonomy per component.**
   1. Example categories:
      - principal: scheduled principal, prepayment, further-advance draw, capitalisation, fee capitalisation, FX
      - arrears buckets: arrears reclassification
      - accounting balances: write-off (gross carrying amount or allowance, not necessarily contractual principal)
      - cash or income: post-write-off recovery
      - all components: reversal or cancellation, technical transfer, accounting correction
   2. A reclassification moves an amount between buckets and doesn't change total principal. Don't add it to the principal bridge.
   3. Scheduled principal versus prepayment can't be read from a posting code. Classify principal cash against the due amounts, schedule, arrears state, allocation order and resulting balance at the payment's effective date. Keep the source posting type separate from the derived investor-reporting class.
   4. Send unmapped source codes to a governed exception queue. The residual is not their default home.
   5. The mapping is a business rule: put it in the business vault and version it.
5. **Grain and identity of Dutch mortgages.**
   1. Keep each source event at its native grain: loan part (leningdeel), mortgage contract, borrower account or collateral set.
   2. Where the investor report needs part-level amounts, store explicit allocation results at posting line × loan part × balance component. Use the servicer's allocation lines if available, otherwise a versioned allocation rule. Keep unallocated amounts as exceptions. A link alone does not allocate an amount.
   3. Reconcile both the part totals and the parent contract.
   4. **Further advances** may create a new loan part (own redemption type, rate and start date) rather than increase an existing one. Model a new part as a new instrument with its own disbursement event and any pool-entry decision.
   5. **Restructurings, splits, merges and identifier changes** must be modelled explicitly. Reconcile them through a transfer bridge that balances at contract or obligation level.
   6. **Savings and bank-savings mortgages.** The savings account or insurance-policy value is a separate instrument, with its own movements, provider, pledge relationship and valuation basis. Contributions and credited returns don't amortise principal. Don't net them against principal unless the investor definition requires it. At maturity, record the savings proceeds and the principal redemption separately.

## 5. Data Vault placement

| Element | Data Vault construct |
|---|---|
| Posting events | Transactional link at the immutable event grain, with payload and source versions in satellites; corrections and reversals as new assertions or events linked to the original; effective and load timestamps |
| Positions | Observations at instrument (native position grain) × effective date × balance component × currency × basis, as a periodic-snapshot or multi-active pattern, with assertion and load versions kept |
| Month-end selection | A reproducible rule (effective date, close calendar, assertion cut-off), with published snapshot identity kept where reports must be reproduced. PIT tables only as rebuildable accelerators. |
| Pool membership | Raw membership relationships with effective and asserted history |
| Allocations | Immutable allocation inputs, plus versioned business-vault allocation results |
| Taxonomy and rules | Historised source-code reference data and rule-set versions |
| Movement facts | Derived in the business vault, economic movements only |
| Reconciliation result | A control object keyed by period, cut-off, rule set and input versions, holding the residual and status |
| Reconciliation mart | Reads the independently versioned opening and closing positions, the full posting population, perimeter events and the allocation and classification results. Publishes counts and amounts, unmapped and unallocated items, the residual, and lineage to both sides. |
