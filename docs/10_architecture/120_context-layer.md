# 120 — The context layer

*Extended 2026-09-25, session 04, after a brainstorm with the author, who called the context
system "one of the key factors for a successful implementation of this idea". The original text
stands; the additions are the sections on the kinds of context, the new card kinds, one
store with two views, and the pointers to [122](122_context-retrieval.md),
[124](124_context-write-back.md), [126](126_context-gardening.md),
[127](127_temporal-behaviour.md) and [128](128_join-knowledge.md).*

*Revised the same day after external review on GPT-6 Astra (this document, 124 and 126) and
gpt-5.6-sol (122, 127 and 128), recorded in [XREV_2026-09-25_context-system_astra](../30_research/notes/XREV_2026-09-25_context-system_astra.md) and [XREV_2026-09-25_context-system_sol](../30_research/notes/XREV_2026-09-25_context-system_sol.md). The author accepted
every finding. Here that added a sixth kind of context, evidence snapshots and version
manifests, the split between what was decided and what is observed, and publication
boundaries for the shared store.*

*Revised again the same day after a crossed second review — sol on this document, 124 and 126;
astra on 122, 127 and 128 — recorded in
[XREV_2026-09-25_context-system-r2_sol](../30_research/notes/XREV_2026-09-25_context-system-r2_sol.md)
and
[XREV_2026-09-25_context-system-r2_astra](../30_research/notes/XREV_2026-09-25_context-system-r2_astra.md).
The author accepted every finding and ruled three of them as design decisions in [ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md):
assertions are the core record and cards are views of them; one identity plane over separate
stores; and a publication gate. Where the sections below conflict with that ADR, the ADR wins, and
the conflicting text is marked.*

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

## Six kinds of context

*Added 2026-09-25.* Not all context behaves the same, and storing it all the same way is the
mistake to avoid. Six kinds differ in volume, in how fast they change, in who writes them and
in how far they can be trusted:

| Kind | Example | Written by | Changes | Where it belongs |
|---|---|---|---|---|
| **Landscape facts** | tables, columns, profiles, lineage, row counts | Deterministic machinery | constantly | a database, regenerated, never hand-edited |
| **Knowledge** | what a column means, business keys, entity matches, temporal behaviour ([127](127_temporal-behaviour.md)), join knowledge ([128](128_join-knowledge.md)) | The agentic layer proposes; a person rules | slowly | cards, with the assertion record below |
| **Decisions and purpose** | KPI definitions, priorities, why something was built | People | rarely | decision cards; the highest *authority*, which is not the same as the highest truth (below) |
| **Know-how** | templates, conventions, runbooks, methodology, context recipes ([122](122_context-retrieval.md)) | The agentic layer drafts; a person approves | occasionally | versioned procedure cards — the agentic layer's skills |
| **Workflow state** | approvals awaited, retry checkpoints, records of actions taken | The agentic layer and deterministic machinery | per workflow | a durable store, kept until the workflow is explicitly closed |
| **Working memory** | what a task tried, what failed, what is still open | The agentic layer | per task | a task journal that expires unless something is promoted ([124](124_context-write-back.md)) |

This sharpens the objection above into a rule rather than a caveat. Cards in git are for
knowledge, decisions and know-how. Landscape facts are high-volume and volatile, so they live
in a database written by deterministic machinery, and only their *conclusions* are promoted to
cards. Workflow state lives in a durable store of its own, because losing an awaited approval
or a record of an action already taken makes the next heartbeat repeat or abandon work.
Working memory lives in a journal and expires. The derived graph and search index span the
stores and remain disposable. That is a candidate answer to `ARC-OP-7` — *both, split by kind*
— and not a ruling.

**Evidence must outlive the facts it was drawn from.** Landscape facts are regenerated, so a
card that approved a join because yesterday's profile showed unique keys could survive after
the profile that justified it is gone. Every promoted assertion therefore keeps an immutable
snapshot of the evidence it rests on and records what it depends on. When that evidence
changes, the assertion is marked stale. Retrieval runs against an explicit **version
manifest** — which database snapshot, which git commit, which journal state — so that a task
never combines incompatible versions of the stores.

**What was decided is not the same as what is.** A person with authority can define *net
revenue* correctly and still be wrong about how the warehouse actually computes it. So a card
separates **normative** claims (what something should be: authority, scope, effective dates)
from **descriptive** claims (what it is: evidence, confidence, freshness). When they
contradict, the contradiction is shown, not settled by which kind outranks the other.

## Assertions are the core record; cards are views

*Added 2026-09-25, from [ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md).* The six kinds above remain a useful **default** for where
typical context lives, but they are not the classification that decides trust or storage. That is
decided per claim. Every claim is a typed **assertion** carrying its own attributes:

- **subject** — the object or objects it is about, by identifier;
- **claim type** — intended, declared, implemented, observed or certified (below);
- **lifecycle status** — proposed, accepted, contested, superseded or retracted;
- **authority** — who, with what mandate, ruled it, if anyone;
- **evidence bundle** — below;
- **scope** — the population and conditions it holds for;
- **volatility, owner, retention class and privacy class**.

Where an assertion is stored follows from those attributes, not from a category. A **card** is a
bounded, readable view of the assertions about one stable business object, generated for people
and for agents. Hypotheses and approvals are statuses of assertions, not separate objects; a
relationship between two objects and a rule over a set are assertion types.

**The evidence bundle** is what makes an assertion re-checkable. It is content-addressed and holds:
the source version or as-of time; the query or computation; its parameters; the tool and code
version; the privacy classification; the retained aggregate or sample; and an assertion-specific
**invalidation predicate** — the condition under which the assertion must be re-checked. Staleness
is decided by that predicate, not by the mere fact that some evidence changed.

**Five claim types, not two.** The normative/descriptive split above is too coarse for a warehouse,
where the ETL code and the observed data can disagree while both describe "what is". Claims are
therefore typed as:

| Type | Meaning | Example |
|---|---|---|
| **Intended** | what it should be | the business definition of *net revenue* |
| **Declared** | what a system or document says | a constraint in the source, a data contract |
| **Implemented** | what the code does | the transformation that computes it |
| **Observed** | what the data shows | a profile, a reconciliation |
| **Certified** | what someone with authority has signed off | a published KPI |

Each carries an **effective time** (when it holds in the business) and an **observation time** (when
it was established). Contradictions between types are shown, never resolved by rank.

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

*Proposed additions, 2026-09-25, not yet ruled:* `relationship`, for knowledge about a pair
of objects — joins, cardinality, referential integrity and join risks
([128](128_join-knowledge.md)); `procedure`, for know-how — templates, conventions, runbooks
and context recipes ([122](122_context-retrieval.md)); and `rule`, for a claim holding over a
set of objects, which is `ARC-OP-16`. Temporal behaviour ([127](127_temporal-behaviour.md))
does not need its own kind; it is a section in dataset and field cards.

~~*Proposed additions … `relationship` … `rule` …*~~ **Superseded by [ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md):** `relationship`
and `rule` are assertion types, not card kinds, and `hypothesis` and `assertion` in the original
list above are respectively a status and the underlying record rather than kinds of card. Card
kinds are the business objects — `source`, `dataset`, `field`, `entity`, `metric`, `decision`,
`artifact`, `question` — plus `procedure` for know-how.

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

## One store, two views

> **Refined by [ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md):** not one store, but **one identity plane over separate stores**. All
> stores share one scheme of permanent identifiers; indexes are filtered by access policy before
> retrieval, so that even the *existence* of a sensitive object or a draft claim is not revealed to
> those not entitled to it; and material reaches the human catalogue only through an explicit
> **publication pipeline**. No unfiltered graph is shared. The argument below — that sharing makes
> the catalogue stay current — still holds for the identity plane and the published assertions.

*Added 2026-09-25.* The context store the agents use and the metadata catalogue people use
could be **the same thing, shown two ways**: a readable catalogue for people, cards and
recipes for agents. That would make the metadata value area of
[ADR-0009](../20_decisions/0009-separate-capabilities-open-value-areas.md) and the context
system one investment rather than two. It also attacks the failure `ARC-OP-23` records —
human-maintained catalogues decay because nobody's work depends on them — because the agents
need this catalogue to do their work, so keeping it current is part of every task rather than
a separate chore. `ARC-OP-26` holds the idea; it is promising and unexamined.

Two cautions from review. **A shared store needs boundaries, not just two presentations.** Task
journals may hold sensitive sample values; unapproved hypotheses must not appear beside
approved catalogue definitions; retrieved prose must never be mistaken for an executable
procedure. So access rights, publication status (draft, approved, retired) and executable
authority are enforced *before* retrieval, in graph traversal and search as well. The two views
share identifiers and assertions; they need not show the same content.

**Agents depending on the catalogue does not by itself keep it current.** Agents can succeed
with stale shortcuts and never visit neglected objects, and repeated use can reinforce
unsupported claims. Every assertion therefore carries an explicit revalidation trigger and an
owner, and freshness and contradiction coverage are measured separately from task success
([126](126_context-gardening.md)).

## The rest of the context system

- [122_context-retrieval.md](122_context-retrieval.md) — context recipes per task type, zoom
  levels, trust labels, and how to measure whether retrieval works.
- [124_context-write-back.md](124_context-write-back.md) — mandatory write-back, sorted by the
  chain, and the promotion ladder from note to rule.
- [126_context-gardening.md](126_context-gardening.md) — the standing upkeep jobs that keep the
  store true.
- [127_temporal-behaviour.md](127_temporal-behaviour.md) — how each table and attribute
  behaves over time, and what history to keep.
- [128_join-knowledge.md](128_join-knowledge.md) — which tables join, cardinality in three
  layers, referential integrity and join risks.
