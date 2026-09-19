# 150 — Trust, authorisation and blast radius

The brief says "of course with proper security clearance etc." That phrase is carrying
more weight than any other in the document. This is where projects of this shape die,
and treating it as an operational detail to be arranged later guarantees the outcome.

## The crawler analogy and where it breaks

A web crawler reads a public, idempotent, effectively free surface. The worst outcome of
a bad crawl is a rate limit, and the crawled party has consented by publishing.

A crawler inside a corporate network reads production. It consumes warehouse credits or
database capacity; it can take locks; it can trip data-loss-prevention tooling; it
touches personal data under a legal basis that must exist *before* the read; it will be
observed by a security operations team that was not told it was coming; and the party
being read has not consented to anything. None of this is a reason not to build it. All
of it is a reason that authorisation is a component rather than a prerequisite.

## Source contracts

Nothing is read except through a contract, which is a card in the context layer and
states: the owner, the legal basis for processing, the personal-data classification, the
permitted operations (metadata only / sampling / full read), the read budget and
permitted window, the credentials reference, and the expiry.

The Access capability enforces contracts. An agent that wants data it has no contract
for does not get it and does not improvise; it raises a question. This makes the
system's reach auditable at any moment by reading a directory of files, which is exactly
the artifact a security review asks for and rarely receives.

## Order of reading

Cheapest and least invasive first, always: existing catalogues and lineage exports; dbt
manifests and BI-tool definitions; `information_schema` and system views; query logs;
bounded samples; full reads last and only under contract. Most of the structural
evidence the system needs is available without reading a single business row, and the
system should be able to demonstrate that.

## Discovery versus scanning

The brief's image of a crawler that finds sources on the network is the most evocative
element of the vision and the most legally fraught. Active network discovery is, in most
organisations, indistinguishable from reconnaissance, and running it without explicit
written authorisation is a security incident regardless of intent.

The defensible version is **inventory-driven discovery**: the system begins from a
human-supplied inventory of sources and from the metadata of systems it already has
contracts for, and it *proposes* sources it has inferred exist — because they are
referenced in a lineage export, a connection string, a report definition — without
touching them. Proposal, then contract, then read.

## Personal data

The system will encounter personal data whether or not it is looking for it. Two
requirements follow. Detection is part of profiling, not an afterthought, and detected
personal data is classified on the card before any sample is retained. And samples are
treated as the most dangerous artifact the system holds: minimised, redacted where
possible, never committed to the context-layer repository, and expired aggressively.
A card may say that a column holds Dutch postcodes; it must not contain them.

## Blast radius

The system writes to exactly one place: the warehouse it builds, plus its own
repository. It never writes to a source. It never mutates a system it does not own.
Every artifact it creates is generated from a definition under version control and can
therefore be dropped and rebuilt.

Stated as a property: **the worst thing an uncontrolled run can do is waste money and
create objects nobody wanted.** That is a boundary an organisation can be asked to
accept. Anything broader is not.

## Auditability

Because the context layer is version-controlled and every assertion carries provenance,
three questions have answers at any moment without special tooling: what does the system
believe, when did it come to believe it, and on whose authority. For an autonomous
system operating on corporate data, the ability to answer those three is not a
compliance nicety — it is the precondition for being allowed to operate at all.
