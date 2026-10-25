# Modelling transaction events and payments

Written by Claude, 2026-10-25, from a conversation of 2026-10-22.

## 1. BIRD does not cover this

BIRD is stock-based: positions at a reference date, not events. Event modelling needs other references.

## 2. Open references

1. **ISO 20022.** The strongest reference, because it is a logical data model with message types on top, not just a message catalogue.
   1. camt.053 (statement) and camt.054 (debit/credit notification) have the structure Statement → Entry → Entry Details → Transaction Details.
   2. One booked entry can batch several underlying transactions.
   3. The Bank Transaction Code (`BkTxCd`) is a ready-made event-type taxonomy with three levels: domain, family and sub-family.
   4. The reversal indicator (`RvslInd`) flags an entry as the reversal of a previously booked entry.
   5. pain (customer to bank) and pacs (interbank) messages cover the payment lifecycle before booking.
2. **BIAN service domains**, such as Payment Execution and Current Account. Useful for event semantics and lifecycle states, less so for attributes.
3. **Open Banking APIs** (Berlin Group NextGenPSD2, UK Open Banking). Their transaction resources are pragmatic, public and close to how core banking systems actually expose transactions **(unverified in detail)**.
4. **Silverston, *The Data Model Resource Book*, Vol. 2.** Financial-transaction and account-transaction patterns at the logical level.

## 3. Data Vault patterns

1. Model payments and postings as **non-historised (transactional) links**, or as a hub on the transaction ID with an insert-only satellite.
2. Events are immutable. Corrections arrive as new events, the way ISO 20022 handles reversals, never as updates.
3. Time axes:
   - valid time = booking or value date
   - transaction time = load timestamp

   With this, the bitemporal model needs no update logic for events at all.
4. Keep three dates where available: value date, booking date and settlement/transfer date. In-transit measurement needs all three. See [060_securitisation-cash-tracking.md](060_securitisation-cash-tracking.md).

## Sources

- Novalnet, SEPA account statement information: https://www.novalnet.com/?p=2789
- Numeral, camt.053.001.08 schema and business logic: https://docs.numeral.io/docs/camt053-xsd-business-logic
- ISO 20022, change request CR0023 (entry-level reversal semantics): https://iso20022.org/milestone/12576/download
