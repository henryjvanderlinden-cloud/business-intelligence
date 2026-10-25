# Financial Services — domain knowledge

Reference notes on data modelling for banks and other financial institutions. They are kept so that later work (including nsdn work for a financial client) does not have to rediscover them.

- Written by: Claude, at Rick's request, on 2026-10-25.
- Based on: a conversation of 2026-10-22, with web sources checked at the time.
- Review status: put through [external review](../../50_process/510_external-review.md) on 2026-10-25, two passes per file on sol, and revised accordingly. The review notes are `XREV_2026-10-25_fs-010_sol.md` to `fs-060` in [the research notes](../../30_research/notes/). The final edits after each second pass adopt sol's own correction wording and were not reviewed a third time.
- Confidence markers: claims checked against a source are left unmarked. Claims from general knowledge that were not checked are marked **(unverified)**.

## Files

| File | Covers |
|---|---|
| [010_industry-data-models.md](010_industry-data-models.md) | FSLDM/FSDM and its proprietary peers; publicly available alternatives |
| [020_bird.md](020_bird.md) | What the ECB's BIRD is, its layers, and which systems feed it |
| [030_bird-as-data-vault-foundation.md](030_bird-as-data-vault-foundation.md) | Using the BIRD LDM as the base for a (bitemporal) Data Vault; central entities |
| [040_transactions-and-payments.md](040_transactions-and-payments.md) | Open references for modelling transaction events and payments; Data Vault patterns |
| [050_securitisation-movement-reconciliation.md](050_securitisation-movement-reconciliation.md) | Explaining month-to-month position changes from postings |
| [060_securitisation-cash-tracking.md](060_securitisation-cash-tracking.md) | Tracking cash through the structure for operational-risk reporting to investors |

## How the pieces fit

1. **Positions** (stocks at a reference date) come from a BIRD-style model. See 020 and 030.
2. **Postings** explain how positions change between dates. See 050.
3. **Payments** explain how received cash was allocated to postings. See 050 and 060.
4. **Cash transfers between accounts** explain where the money physically is. See 060.

Chains 2 to 4 together are the "three chains" of the securitisation notes.
