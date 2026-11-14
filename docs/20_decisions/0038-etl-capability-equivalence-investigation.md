# ADR-0038 — The ETL capability equivalence investigation: its name, place, order, method and principles

- **Status:** Accepted
- **Date:** 2026-11-14
- **Supersedes:** —
- **Superseded by:** —

## Context

On 2026-11-14 the author asked what standard ETL suites do that the bare-bones setup cannot, and the answer was a list
of thirteen capabilities. At his request it was set up as a research programme of its own in
[`docs/30_research/equivalence/`](../30_research/equivalence/README.md), with the questions
([010](../30_research/equivalence/010_capability-inventory.md)) kept apart from existing answers
([020](../30_research/equivalence/020_databricks-anatomy.md)), and held open as `ARC-OP-38`. The model proposed a
working title, the folder, an order, and three ways a capability could end: *match*, *delegate* or *decline*. He
replied at 21:29, verbatim:

> Yes, let's call it "Imperative ETL capability equivalence investigation" if you agree. Otherwise I'll go with your
> suggestion. Subfolder in 30_research seems appropriate. I agree on the order. With regards to the proposed outcomes,
> I think we mainly want to identify gaps, then identify requirements given a client's environment, size etc. and then
> judge if and how we should bridge the gap. From what I've seen, I don't think that any of the gaps are real
> showstoppers. Most of it should be doable, using some Apache licensed products. I think that given some thorough
> requirements analysis, a solid architecture, separation of concerns and generation guidelines an LLM is perfectly
> capable to design, build and implement most functionalities. This is what the project is about. Stay away from
> proprietary products, keep it all machine-readable (FAIR acronym), have the agentic layer manage, build and supervise
> the deterministic layer, use the human adjudication economy properly.

## Options considered

**The name.** *"Imperative ETL capability equivalence investigation"*, the author's. Its case: it says what nsdn is
measured against, tools in which a person builds each flow step by step, and so marks the contrast with a setup that
generates its machinery from declarations. *The same without "Imperative"*, the model's. Its case: the thirteen
capabilities are about what surrounds the transformation (connectors, capture, a console, access, promotion), not about
whether flows are written imperatively; and the yardstick is not uniformly imperative, since Databricks, one of his
three examples, now declares its pipelines (020 §1). He made his name conditional on the model's agreement and said he
would otherwise go with the model's suggestion.

**How a capability ends.** *Match, delegate or decline, against a standard stated beforehand*, the model's: a fixed
set of outcomes decided once, in nsdn. *Gaps, then requirements, then a judgement*, the author's: the gaps are found
once, but what is required depends on the client's environment and size, so whether and how a gap is bridged is judged
then. The second does not need the first's fixed outcomes and puts the decision where the facts are.

## Decision

1. **The programme is called the ETL capability equivalence investigation.** "Imperative" is left out for the reason
   above, on the author's own condition. He can put the word back by saying so.
2. **It lives in `docs/30_research/equivalence/`**, a subfolder beside `notes/`.
3. **Capabilities 1, 2, 5 and 6 come first**: connectivity, incremental capture, the operations console, security
   administration.
4. **The method has three steps.** Identify the gaps. Identify the requirements given a client's environment, size and
   so on. Then judge if and how the gap should be bridged.
5. **Five principles govern how a gap is bridged**, in the author's words where quoted:
   1. "Stay away from proprietary products."
   2. Bridge with open-source parts: "Most of it should be doable, using some Apache licensed products."
   3. "Keep it all machine-readable (FAIR acronym)."
   4. "Have the agentic layer manage, build and supervise the deterministic layer."
   5. "Use the human adjudication economy properly."

**Recorded as the author's expectation, not as a decision:** that none of the gaps is a showstopper, and that "given
some thorough requirements analysis, a solid architecture, separation of concerns and generation guidelines an LLM is
perfectly capable to design, build and implement most functionalities. This is what the project is about."

## Consequences

The model's three outcomes are not adopted. *Match*, *delegate* and *decline* remain words for what a judgement in
step 3 may come to, nothing more; the first thoughts in 010 that use them are the model's.

Step 1 is generic and belongs in this repository; 010 is its first pass. Steps 2 and 3 depend on a client, so by
[ADR-0035](0035-reference-case-and-client-repositories.md) their results would sit in the client's repository, with
what is learned coming back as upstream notes ([ADR-0036](0036-releases-and-upstream-notes.md)). That is the model's
reading of how the method meets the repositories, not a ruling. The reference case can play the client for a first
trial.

His expectation names four things an LLM needs: requirements analysis, an architecture, separation of concerns and
generation guidelines. For the thirteen capabilities none of the four exists yet. They are owed under `ARC-OP-38`
before a gap is bridged, and the expectation itself is tested by the first gap bridged that way.

Principle 4 does not put the agentic layer in the run path: models stay out of the data path
([ADR-0004](0004-models-out-of-the-data-path.md)), and loads and checks keep running without agents (the author's
ruling of 2026-10-07, [420](../40_roadmap/420_next-sandbox-setup.md)). Supervising means building, watching and
repairing the machinery, not being needed for it to run. Principle 5 refers to
[155](../10_architecture/155_adjudication-economy.md).

FAIR stands for findable, accessible, interoperable and reusable, principles for data that are meant to make it usable
by machines as well as people (from general knowledge, not looked up).

**Two readings are not ruled and are held in `ARC-OP-38`.** First, whether "stay away from proprietary products"
covers only what nsdn itself brings, or also what a client already runs: its directory (AD), its database, its cloud.
Step 2 takes the client's environment as given, which suggests the first. Second, whether "Apache licensed" means the
Apache licence as such or permissive open-source licences in general: DuckDB, the warehouse engine of
[ADR-0015](0015-sandbox-warehouse-dbt-duckdb.md), is under the MIT licence, and dbt-core 1.x under Apache 2.0
(<https://duckdb.org/faq>, <https://www.getdbt.com/licenses-faq>, found 2026-11-14, extracts only).

Unreviewed on another model. **Revisit** when the first client's requirements are in hand, since that is the first
time steps 2 and 3 are done; and if the author restores "Imperative".

## Added 2026-11-14, 23:06: the two readings ruled

The two readings were put to the author as points 7 and 8. He replied, verbatim:

> 7. Oh sorry, it should be read more narrowly. No proprietary ETL products. Of course they can use SQL Server, AD directories, AWS cloud etc.
>
> 8. Permissive open source, definitely, not just limited to Apache licenses.

So principle 1 reads **no proprietary ETL products**: what nsdn uses to extract, move and transform data is never a
proprietary ETL product, while a client's own database, directory and cloud are used as they are. And principle 2 reads
**permissive open-source licences**, of which Apache 2.0 is one and DuckDB's MIT licence another. The text above stands
as written on the day; where it calls these readings not ruled, this section replaces it.

Read by the model and not ruled: a client's Databricks would count as its platform, as SQL Server or AWS do, so
generated SQL may run on it, while its managed ingestion and orchestration parts
([020](../30_research/equivalence/020_databricks-anatomy.md) §1) would count as proprietary ETL products.
