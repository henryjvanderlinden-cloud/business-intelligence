# Modelling transaction events and payments

Written by Claude, 2026-10-25, from a conversation of 2026-10-22. Revised the same day after review by sol; see [XREV_2026-10-25_fs-040_sol.md](../../30_research/notes/XREV_2026-10-25_fs-040_sol.md).

## 1. BIRD does not cover this

BIRD is organised mainly around reporting reference dates, not events. Event modelling needs other references.

## 2. Open references

1. **ISO 20022.** The strongest reference, because it is a logical model with message types on top, not just a message catalogue.
   1. **Account reporting** uses three messages with the same entry structure under different containers:
      - camt.052: Account Report → Report → Entry → Entry Details → Transaction Details
      - camt.053: Statement → Statement → Entry → Entry Details → Transaction Details
      - camt.054: Debit/Credit Notification → Notification → Entry → Entry Details → Transaction Details

      Entry Details and Transaction Details are optional and repeatable, so not every entry carries transaction-level detail.
   2. One booked entry can batch several underlying transactions.
   3. **The Bank Transaction Code (`BkTxCd`)** classifies the bank transaction. It has a standard branch (domain, family, sub-family) and a proprietary branch (code plus issuer). Keep both, plus the raw code. It can occur at entry level or at transaction-detail level. Keep the level at which each code was reported, and don't copy an entry-level code onto the transaction details of a batched entry. It classifies; it is not an event identity or lifecycle state.
   4. **The Reversal Indicator (`RvslInd`)** says an entry is the result of a reversal. It does not identify the original entry, and its absence doesn't mean "false". Link to the original only from reference data or reconciliation evidence.
   5. **The message families:**
      - pain covers payment initiation and related customer status and cancellation messages.
      - pacs covers financial-institution-to-financial-institution (FI-to-FI) clearing, settlement, status, returns and reversals.
      - camt.052/053/054 cover account reporting.

      These are families, not phases before or after booking. Booking can happen at different banks at different points in a payment's life, so model lifecycle stage and each party's booking separately.
2. **BIAN service domains**, such as Payment Execution and Current Account. Useful for event semantics and lifecycle states, less so for attributes.
3. **Open Banking APIs** (Berlin Group NextGenPSD2, UK Open Banking). These publish consent-controlled account and transaction resources for booked and, where supported, pending transactions. They are regulated external API contracts, usually a normalisation layer over one or more core systems. Use them as source-interface patterns, not as evidence of how core banking systems model transactions.
4. **Silverston, *The Data Model Resource Book*, Vol. 2.** Financial-transaction and account-transaction patterns at the logical level.

## 3. Data Vault patterns

1. **Separate the grains.** Payment instructions, payment and settlement events, and account postings each need their own grain and a durable business key, unique within a stated scope. A source-local transaction ID is often not unique enough to be a hub key.
2. **Associations are links.** Where an association can be asserted, corrected or withdrawn (say, which posting a payment settled), historise or effectivity-date its status. A bare non-historised link would leave both the wrong and the corrected association looking active.
3. **Keep economic events and observations of them apart.** These are the three kinds of change:
   - A reversal or return is a new economic event, linked to the original.
   - A correction to remittance text, classification, counterparty or even value date is a new version of the observation of the same event, not a new event. Store it as a new satellite version.
   - Never overwrite raw vault history.
4. **Valid time is defined per question.** Booking date and value date are different facts and can differ (back-valued postings):
   - Use booking time for "what was on the account", and value time for interest and value questions.
   - Keep settlement time and lifecycle-status intervals separately where supplied.
5. **The load timestamp is warehouse system time**, not when the source knew the fact. Keep the source's own creation, change or report timestamps as well.
6. **Insert-only storage doesn't remove versioning logic.** Late corrections and retractions still need explicit version succession, deduplication and a rule for deriving which version is current, valid-time and system-time intervals included. Otherwise two contradictory versions are both "current".
7. **Keep every lifecycle timestamp the source supplies, each with its role:**
   - initiation and acceptance
   - requested execution
   - clearing or settlement per leg
   - account booking
   - value date

   Define each in-transit metric by a named start event and a named end event. Execution date and settlement date are not interchangeable.

## Sources

- Novalnet, SEPA account statement information: https://www.novalnet.com/?p=2789
- Numeral, camt.053.001.08 schema and business logic: https://docs.numeral.io/docs/camt053-xsd-business-logic
- ISO 20022, change request CR0023 (entry-level reversal semantics): https://iso20022.org/milestone/12576/download
