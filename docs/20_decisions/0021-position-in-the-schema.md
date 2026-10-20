# ADR-0021 — Position in the schema is inventoried: measured on the declared keys, checked for distortion, classed by rules

- **Status:** Accepted
- **Date:** 2026-10-20
- **Supersedes:** —
- **Superseded by:** —
- **Amends:** [ADR-0017](0017-information-analysis-before-building.md) (item 29 added to the inventory)

## Context

The 28 items of [129](../10_architecture/129_information-analysis.md) describe each table and each relation, but none
says which tables hold the schema together and which stand at its edge. The author asked on 2026-10-20 at 11:25 for a
measure of the centrality of tables, whether other measures matter "in this vein", and whether tables should be told
apart as core, descriptive and linking. The model proposed graph measures on the declared foreign keys, computed with
and without the audit links that tie every table to the people table, and a finer set of classes assigned by rules.
The author answered at 18:55, verbatim:

> This is a new inventory item.I think you did a wonderful job of analyzing. Please also record the method, so that it
> can be reused in future projects. Centrality per se is not the end all be all, I appreciate that you also applied
> business sense to the analysis. As you have done with excluding audit information, good move. The lesson is not to
> always exclude audit attributes, but to be cautious and sensitive to excluding attributes etc. that give a distorted
> picture of reality. I agree with your entire section 5, good addition.

"Section 5" is the proposed classification: core split into event and master, lookup, bridge, the special cases
(extension, configuration, history, headers and lines), and classes assigned by measurable rules.

## Options considered

*Leave position to the reader of items 5 (role) and 6 (keys).* Its case: the facts are there, a person can see the
hubs. Rejected: what is obvious to a practitioner on 31 tables is not on 3,000, and the distortion by audit links
shows that the obvious reading can be wrong.

*A single centrality score.* Its case: one number ranks tables simply. Rejected: each measure has a known artefact
(PageRank collects at the end of chains; betweenness without direction runs through shared parents), and a table can
be central through roles without lying on paths. Several measures are recorded side by side.

*Classes by judgement only.* Its case: business sense finds what rules miss. Rejected as the only basis: it is not
reproducible across sources. Adopted as a separate reading beside the class by rule.

## Decision

1. **Item 29, position in the schema**, is added to the inventory: best effort, recorded per table
   (`tables/<schema>/<table>/29_position.md`) and per source (`_source/29_position.md`).
2. **The method is [131](../10_architecture/131_structural-position.md)**, written to be reused on other sources: the
   graph of declared foreign keys, the measures and their pitfalls, the classes and their rules in order, the
   thresholds as heuristics, and how to run the tool.
3. **The classes** are those of 131 section 5, adopted in full: history, configuration, bridge, extension, event
   (header or record), state, lookup, master, assigned by the first rule that fires.
4. **The distortion principle.** Nothing is excluded by habit, audit columns included. A link or attribute that would
   give a distorted picture of reality is left out only with a stated reason, both the graph with it and the graph
   without it are measured and recorded, and the same care applies to behaviour (an audit column written on every row
   is not a business change).
5. **Business sense beside the rules.** A reading that differs from the class by rule is recorded as a separate claim
   with its reason; the class by rule is kept.

## Consequences

Every source analysed later gets a map of its structure early, and the exclusions behind it are visible and
contestable. The classes depend on behaviour over a short window, so they stay medium confidence until a longer window
is seen; and they rest on declared keys, so a source that declares few keys is understated until round 2 confirms
candidate relations. The tool depends on `networkx`. Revisit if a source's classes by rule disagree with item 5's role
on many tables: the rules or their thresholds would then need revising.
