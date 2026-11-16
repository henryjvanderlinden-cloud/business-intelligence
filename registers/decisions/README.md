# The decision register

One small file per decision the organisation makes, `DEC-<nnnn>_<slug>.md`, in the grammar of
[`model/README.md`](../../model/README.md) §2: the decision in one sentence, its owner, its cadence, the evidence it
uses now, its status and the ADR that recorded it, and under *Served by* the fact tables and analyses that cite it.
Ruled in [ADR-0040](../../docs/20_decisions/0040-the-first-slice-design.md) decision 3; designed in
[141](../../docs/10_architecture/141_the-first-slice-business-vault-and-mart.md) §7.

Every fact table and every analysis under `model/` cites a decision here, and `python tools/check_repo.py` refuses
one that does not, or a decision that lists an object which does not cite it. Who keeps such a register up at a real
organisation is open (`ARC-OP-12`).
