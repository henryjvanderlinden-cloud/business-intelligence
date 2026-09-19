# 140 — Data Vault under machine authorship

The brief proposes Data Vault as the target model. The choice is right, and for reasons
worth making explicit, since they also bound what the system can be expected to do.

## Why the usual objections stop applying

Data Vault is criticised for verbosity, object count, and the amount of mechanical work
it imposes between a source and anything a business user can read. Every one of those
objections is a complaint about *human* labour, and every one of them weakens when the
author is a machine that does not mind writing four hundred satellites.

Two properties then become decisive.

**It is insert-only and non-destructive.** A wrong modelling decision does not destroy
information; it produces a structure that must be reinterpreted. Under machine
authorship — where the error rate is low but not zero and the volume is high —
recoverability is worth more than elegance. This is the strongest single argument for
the pairing, and it should be stated whenever the choice is questioned.

**It separates the mechanical from the semantic exactly where this system's tiers
separate.** Given a declared set of business keys, hub/link/satellite generation is a
template. The semantics are entirely concentrated in the declaration. That is a
remarkably clean fit with [105_autonomy-tiers.md](105_autonomy-tiers.md): Tier 1
generates, Tier 2 declares.

## What is therefore hard

Not the vault. The **keys**. Everything difficult about this project is compressed into
the question *which identifiers does the business actually use to refer to this thing,
and do these two identifiers refer to the same thing?* Existing automation — AutomateDV
and its commercial equivalents — already generates a vault from declared metadata. The
contribution claimed here is the declaration, and if the declaration is not
substantially machine-producible then the project reduces to a documentation tool.

That is the falsifiable core of the idea, and it should be tested first. See
[`../40_roadmap/410_first-vertical-slice.md`](../40_roadmap/410_first-vertical-slice.md).

## The key-hypothesis pipeline

Structural evidence, gathered without asking anyone: cardinality and uniqueness,
nullity, format regularity, whether the value space is stable over time, whether the
column participates in declared foreign keys, and cross-source value overlap by sketch.

Naming and documentary evidence: column names and comments, existing catalogue entries,
BI-tool definitions, join predicates observed in existing query logs and dbt models.
Query logs are underrated here — they are a record of joins that humans already believed
were valid, and they are usually available.

Semantic evidence, model-produced: what this column appears to denote given its context,
whether two columns plausibly denote the same entity given their neighbourhoods.

The output is a ranked set of hypotheses with evidence attached, not a schema. A
hypothesis becomes a key declaration by evidence threshold or by adjudication, and never
silently.

## Historisation is a Tier 1 question

Whether a source needs capturing at all — and at what grain and cadence — follows from
observation rather than opinion: does it overwrite, does it soft-delete, does it carry
its own valid-time, how fast does it change, is history recoverable from the source
itself. Repeated profiling answers this. The brief's instinct to ask "can the data stay
where it is" is correct and unusual; the default answer in most organisations is to copy
everything, and a system that can argue from measurement against copying is worth having
for that reason alone.

## Business vault and marts

The raw vault is mechanical. The business vault — derived satellites, point-in-time and
bridge structures, applied business rules — is not, because it encodes interpretation.
It belongs at Tier 2 with full adjudication, and each object should cite the decision or
metric that motivates it. Marts are Tier 3 and must cite a decision in the register.
