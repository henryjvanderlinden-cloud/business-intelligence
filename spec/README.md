# Specifications

Machine-readable contracts for context-layer artifacts: JSON Schema for card front
matter, the assertion record, source contracts, hypotheses and job definitions.

Empty by design. Schemas are written when the shape of a thing has been settled by an
ADR and exercised by a prototype — not before. A schema written ahead of its use encodes
guesses in a form that is expensive to change and easy to mistake for a decision.

The first schemas likely needed, in order: the assertion record (see
[`../docs/10_architecture/120_context-layer.md`](../docs/10_architecture/120_context-layer.md)),
the source contract (see
[`../docs/10_architecture/150_trust-and-blast-radius.md`](../docs/10_architecture/150_trust-and-blast-radius.md)),
and the card front matter common to all card kinds.
