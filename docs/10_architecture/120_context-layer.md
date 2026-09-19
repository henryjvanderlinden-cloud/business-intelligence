# 120 — The context layer

The brief's most acute observation is that the system must "grow very large, but with
enough breadcrumb trails everywhere that LLMs can still find their way without hogging
the context windows." This document takes that seriously, because it is the engineering
problem on which the whole design turns.

## The problem stated precisely

A mid-sized landscape holds tens of thousands of columns. No agent will ever hold that
in context, and no retrieval scheme that works by similarity search alone will reliably
surface the *right* twelve columns for a given question, because the relevant relation is
frequently structural rather than lexical. What is needed is not a bigger window and not
a better embedding; it is an **addressable, traversable, summarised** representation in
which an agent can navigate by identity rather than by search.

Three properties are required together.

**Stable addressing.** Every object has a permanent identifier that does not change when
the object is renamed, moved or re-platformed. A URN scheme —
`nsdn:source/<source>/schema/<schema>/table/<table>/column/<column>` — with an alias
history, so that an assertion made in 2026 still resolves in 2029.

**Cheap summaries.** Every object has a *card*: a bounded document, on the order of two
hundred to five hundred tokens, that states what the object is, what is known about it,
how confident that knowledge is, and what it connects to. An agent should be able to
load a hundred cards and still have room to think.

**Traversal by identity.** Cards link to other cards by URN. An agent answering a
question walks the graph — from a metric to its mart, to its satellites, to their hubs,
to the sources — rather than searching for each hop. Search is the entry point; traversal
is the method.

## The proposal: cards in git, graph derived

The context layer is a **git repository of markdown files with structured front
matter**, from which a graph index is derived and disposable.

One file per object. Front matter carries the structured facts — URN, kind, aliases,
profile summary, assertions with provenance and confidence, links, demand justification,
lifecycle state. The body carries prose: what this is, in the words of whoever knew.

The argument for files over a catalogue service is not aesthetic.

*Git is the audit log.* Every thing the system learns is a commit with an author, a
timestamp and a diff. Provenance, attribution, rollback and blame are inherited rather
than implemented. For a system whose central risk is confident machine error, being able
to ask "when did we start believing this, and who changed it" is not a convenience.

*Pull requests are the adjudication interface.* A hypothesis is a proposed diff to a
card. A human ruling is a review. This is a working, familiar, zero-build human
interface available on day one, and it can be replaced later by something friendlier
without changing the substrate.

*Text is what models are good at.* The artifacts the agents read, write and maintain are
the same artifacts a person reads. There is no serialisation boundary, no API to keep in
sync, and no schema migration that breaks the agent's ability to read its own memory.
This is also what the brief means by "lightweight so it can be maintained by LLMs".

*The graph can be rebuilt from the files.* Load the cards into DuckDB or a graph store
for traversal and query; if the index is lost, regenerate it. Never the reverse. The
files are the truth.

The honest objections: this does not scale indefinitely — a hundred thousand files is
uncomfortable in git and the derived index becomes the working surface in practice; and
high-frequency profile updates would thrash the history, so volatile measurements belong
in the derived store with only their *conclusions* promoted to cards. Both are
manageable, and both are cheaper than the alternative of losing the audit trail. This
should nonetheless be decided explicitly rather than by drift — see open question 12.

## Card kinds

`source`, `dataset` (table, file, topic, endpoint), `field`, `entity` (a business
concept, possibly spanning sources), `metric`, `decision`, `hypothesis`, `assertion`,
`artifact` (a generated vault object, mart, test or analysis), `question`.

The ones that are not obvious are `entity`, `decision` and `hypothesis`. `entity` is
where the semantic layer actually lives — the thing that outlives any particular table.
`decision` is the teleological anchor described in
[105_autonomy-tiers.md](105_autonomy-tiers.md). `hypothesis` is a first-class card
rather than a transient, because the system's reasoning must be inspectable and because
a retired hypothesis is useful evidence that a question was already considered.

## The assertion record

Every fact in the context layer carries, without exception:

- **what** — the claim, in a form narrow enough to be wrong;
- **provenance** — `inferred` | `asserted` | `documented` | `derived`, with the source:
  a computation, a named person, a named document, or a set of other assertions;
- **when** — and, separately, when it was last re-checked;
- **confidence** — a coarse band, not a false precision;
- **falsifier** — the observation that would overturn it, where one can be stated;
- **scope** — the qualifications the adjudicator attached ("same entity, but this source
  retains deletions").

A catalogue without these decays invisibly. This is the single discipline most likely to
determine whether the context layer is still trustworthy in its third year.

## Navigation aids

Beyond cards and links, three indexes are worth maintaining, all derived:

a **landscape map** — one document per source and one for the whole, written for an
agent arriving cold; a **question index** — open questions by area, so an agent knows
what is not known before it spends tokens rediscovering it; and a **dependency index** —
what depends on what, which is what makes pruning and impact analysis possible at all.

## The retrieval contract

An agent working on a task should be able to establish, in at most three loads: what
exists here, what is known about it, what is uncertain about it, and what depends on it.
If a task requires more than three, the context layer has failed at its job and the fix
belongs here rather than in the agent's prompt.
