# 100 — System overview

*Subjunctive throughout: nothing described here exists.*

## The one law

**The model is never in the data path.** Language models read metadata, samples and
context; they emit code, configuration, assertions and prose. Deterministic engines move
and transform the data. Every property the system needs in order to be trusted —
reproducibility, auditability, cost predictability, the ability to re-run last quarter
and get last quarter's numbers — follows from this separation, and all of them are lost
the moment a model is permitted to produce a row.

The corollary is that the system's real output is not data. It is **a body of
declarative artifacts** — cards, assertions, model definitions, tests — from which the
data infrastructure is generated. If the entire warehouse were deleted, the artifacts
would rebuild it. If the artifacts were deleted, the warehouse would be an orphan.

## Shape

Eight capabilities, each of which can be built, evaluated and operated separately. They
are not a pipeline in the sense that each waits for the previous one; they are
continuous processes that share the context layer.

**Access** holds the source contracts and mediates every read. Nothing reaches a source
except through it, and it enforces budget, classification and permitted operations.

**Discovery** enumerates what exists: sources, schemas, tables, columns, files, and the
existing catalogues, lineage exports and BI definitions that describe them. It prefers
metadata surfaces to data surfaces and reads the cheapest thing that will answer the
question.

**Profiling** characterises what was found: types, distributions, cardinality, nullity,
key candidates, temporal behaviour under repeated observation, and sketches that make
cross-source overlap estimable without moving data.

**Sense-making** is the first capability where a model earns its keep. It writes cards,
proposes business keys, raises joinability and identity hypotheses, infers entity
structure, and formulates the questions it cannot answer.

**Adjudication** puts those questions to humans, ranked by information gain, and records
the rulings as first-class assertions with named provenance.

**Construction** generates the raw vault, the capture jobs, the business vault
structures, the marts, the tests and the analyses, as deterministic artifacts that a
deterministic engine executes.

**Evaluation** continuously checks three different things — pipeline determinism, data
quality contracts, and semantic stability — and is elaborated in
[160_evaluation-and-regression.md](160_evaluation-and-regression.md).

**Pruning** retires what has lost its justification, with the same standing as
Construction. See [145_entropy-and-pruning.md](145_entropy-and-pruning.md).

All eight read and write the **context layer**, which is the system's memory and the
only thing that makes the eight cohere. See
[120_context-layer.md](120_context-layer.md).

## Flow of a single fact

It is worth tracing one fact from birth to use, because the architecture is easier to
judge that way than from a diagram.

Discovery observes a column `KLANTNR` in a source table. Profiling records that it is
an eight-digit integer, ninety-nine percent distinct, never null, and that a MinHash
sketch of its values overlaps 0.87 with `CUSTOMER_NO` in a different source.
Sense-making raises a hypothesis — *these two columns denote the same entity* —
attaches the overlap as evidence, assigns a confidence, and notes what would falsify it.
Because eleven downstream hypotheses depend on it, the adjudication queue ranks the
question highly and puts it to the named owner of the second source. She rules that they
are the same entity but that the second source retains records deleted from the first.
That ruling becomes an assertion with provenance `asserted`, her name, a timestamp, and
a scope qualifier. Construction now has a business key, and generates a hub, two
satellites and a link, plus a test asserting the population difference she described.
Evaluation watches that test. If the overlap drifts, the falsifier fires and the
assertion is flagged rather than silently retained.

Nothing in that trace is exotic. What makes it work is that every step is recorded, has
a provenance, and can be reversed.

## What is deliberately absent

There is no decision-making unit. There is no autonomous action against any system other
than the warehouse the system itself builds. There is no write to a source. These are
not phase-one omissions; they are the boundary that keeps the design honest.
