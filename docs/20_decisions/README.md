# Architecture decision records

A decision that shapes the system goes here. A document elsewhere in `docs/` may
describe options; only an ADR adopts one.

## Rules

- Sequential four-digit numbers. Never reuse, never renumber.
- Status is one of `Proposed`, `Accepted`, `Superseded by ADR-NNNN`, `Rejected`.
- Superseded records stay in place. The history of what was believed is part of the
  record.
- Copy [`0000-template.md`](0000-template.md) to start.

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-repository-layout.md) | Repository layout and documentation conventions | Accepted |
| [0003](0003-codename-nsdn.md) | Internal codename `nsdn`; metaphor stays private | Accepted |
| [0004](0004-models-out-of-the-data-path.md) | Models never operate in the data path | Accepted |
| [0005](0005-three-autonomy-tiers.md) | Autonomy is tiered: structural, semantic, teleological | Accepted |
| [0006](0006-project-mode.md) | Project mode: argument, then proof of concept, then offering | Accepted |
| [0007](0007-register-and-handover-apparatus.md) | Adopt the register, handover and enforcement apparatus | Accepted |
| [0008](0008-faculties-substrate-mandate.md) | Three faculties act on a substrate, each under a mandate | Accepted |
| [0009](0009-separate-capabilities-open-value-areas.md) | Separate capabilities, an open list of value areas, and no interaction owed | Accepted |
| [0010](0010-the-agentic-layer.md) | The second faculty is the agentic layer | Accepted |
| [0011](0011-assertions-identity-plane-publication-gate.md) | Assertions are the core record; one identity plane over separate stores; a publication gate | Accepted |
| [0012](0012-generic-framework-lean-start.md) | A generic framework; every implementation starts lean | Accepted |
| [0013](0013-data-vault-or-equivalent.md) | The integration layer is Data Vault or a functionally equivalent layer | Accepted |
