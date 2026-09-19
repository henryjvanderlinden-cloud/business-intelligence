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
