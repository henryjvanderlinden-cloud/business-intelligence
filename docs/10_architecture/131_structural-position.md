# 131 — Position in the schema: how central each table is, and what kind of table it is

Part of the information analysis of [129](129_information-analysis.md), item 29. Drafted 2026-10-20, session 08, from
the author's question, verbatim:

> We have not said anything yet about the (network) centrality of the tables. There are tables that are more important
> and those that are less important, or core tables and peripheral tables. Can you think of a measure of the centrality
> of the tables (maybe using graph theory). Do you agree that centrality is an important measure to understand when
> starting modelling later on? Are there other measures that are important to understand in this vein? Do you agree
> with making a distinction between core tables, descriptive tables (like list of values, look up tables), and linking
> tables?

**Ruled 2026-10-20, 18:55, in [ADR-0021](../20_decisions/0021-position-in-the-schema.md)**: a new inventory item; the
method recorded for reuse on other sources; the classes of section 5 adopted in full; and, on leaving links out, the
author's principle, verbatim:

> Centrality per se is not the end all be all, I appreciate that you also applied business sense to the analysis. As
> you have done with excluding audit information, good move. The lesson is not to always exclude audit attributes, but
> to be cautious and sensitive to excluding attributes etc. that give a distorted picture of reality.

The method is written to be reused: sections 1 to 6 hold for any source with declared foreign keys; section 7 is the
first application, on the Wide World Importers sandbox; section 8 says how to run it on another source. Measures are
standard graph theory (networkx); the classes and their rules are this project's and are heuristics, not theorems.

## 1. Why position is inventoried

Items 1 to 28 describe a table on its own or one relation at a time. None says which tables hold the schema together,
which stand at its edge, and which are of a different kind altogether: a list of codes, a log of events, a single row
of settings. That is what a person new to a source asks first, and it decides where the attention of every later
stage goes. Position is a fact about the source as it is (ADR-0020): it is measured and recorded, not turned into a
design.

## 2. The graph

- **Nodes**: one per base table. History tables of system-versioning carry no declared keys; they stand outside the
  graph and take the position of the table whose versions they keep (class `history`, section 5).
- **Arcs**: one per declared foreign key, from the referring table to the referenced one. Several foreign keys between
  the same two tables are several *roles* (section 4) but one arc for the path measures. A self-reference is a role and
  not an arc.
- **Declared links only.** Candidate relations without a declared key (`across/candidates.md` in a source's record)
  are not arcs: a measure of the declared schema should not depend on a guess. Where a source declares few keys, the
  graph is thin and this is itself a finding (item 6), not a reason to fill it with candidates.
- Path measures (betweenness) use the graph **without direction**; reach (descendants, ancestors, longest path) and
  PageRank use the direction.

## 3. The distortion check

A link can make the graph describe the source falsely. The case that prompted the rule: in Wide World Importers every
table has a column `LastEditedBy` referring to the people table. With those links, `Application.People` is referred to
by 40 links from 28 other tables and has a betweenness of 0.60 (rank 1); without them, by 12 links from 5 tables, with 0.02
(rank 12).
The audit column made the people table the centre for a reason that says nothing about the business.

The rule, from the author's principle above:

1. **Do not exclude by habit.** Audit columns are not left out because they are audit columns; nor is anything else.
2. **Look for links that distort**: a column present in (almost) every table and pointing to one table; a technical
   column (audit, tenant, load batch, creating program); a link whose removal changes a table's rank by more than a few
   places.
3. **Measure both graphs**, with and without the suspected links, and **record both**. A reader then sees what the
   exclusion did and can disagree.
4. **Justify each exclusion in words**, in the tool's configuration and in the record: what the link means, and why it
   tells nothing about the business the graph is meant to show.
5. **Apply the same care beyond links.** Behaviour can be distorted the same way: an audit timestamp written on every
   row each night makes a table look "updated daily" when no business value changed. The behaviour labels are therefore
   computed on the columns other than the audit and system-time columns; a table whose updates touch only those is
   labelled "only audit or system-time columns change"; and the updated columns are recorded by name with their counts,
   so what the label leaves out can be seen.

## 4. The measures

Each measure is computed on the graph without the excluded links, and the link counts and betweenness also on the full
graph.

| Measure | What it says | Pitfall |
|---|---|---|
| links in / out, tables in / out | how many foreign keys point to it and from it, and from how many distinct tables | one table can refer to another several times (roles); count both |
| position | *source* (nothing refers to it), *sink* (it refers to nothing), *middle*, *isolated* | sources are often event tables or rules; sinks are often lists of codes |
| betweenness (rank) | the share of shortest paths between other tables that pass through it: whether it connects parts of the schema | without direction, two tables that refer to the same parent are connected through it, so a shared parent (an address table) can rank high though no process runs that way |
| roles | the number of foreign-key columns elsewhere that name it | a table can be central through many roles yet lie on few paths (persons) |
| rows referring | rows in other tables that name a row of it (filled key values) | depends on volume, not on structure; read beside betweenness, not instead |
| reaches / reached by | how many tables it reaches by following links outward, and from how many it is reached | the widest reach is often an event table that names both sides of the business |
| longest path out | the length of the longest chain of links from it | long chains run from line tables down to geography |
| PageRank | where the "weight" of references collects | in the referring-to-referenced direction it collects at the end of chains (a countries table at the end of cities and provinces ranks first): **reported, not used to find hubs** |
| rows and behaviour | rows in the base extract; inserts, updates and deletes over two transitions, labelled *grows*, *replaced daily*, *every row updated daily*, *changes without growing*, *only audit or system-time columns change* or *unchanged* | updates are judged on business columns (section 3, point 5); two transitions is a short window (section 6) |
| reach matrix | for each event or state table, the master tables it reaches | a reachability fact, not a design |

A **hub** is a table whose betweenness without the excluded links is at or above a threshold (0.1 in the first
application). The threshold is a heuristic, recorded with the result.

## 5. The classes

The author's three classes — core, descriptive, linking — are refined: core splits into *event* and *master*;
descriptive is *lookup*; linking is *bridge*; and four special cases get a class of their own. Each table gets the class
of the **first rule that fires**, in this order:

| # | Class | Rule | In plain terms |
|---|---|---|---|
| 1 | history | the catalogue declares it a history table of system-versioning | earlier versions of another table |
| 2 | configuration | one row, referred to by no table | settings of the system or the company |
| 3 | bridge | referred to by no table, refers to two or more tables, has no attribute besides keys and audit columns | links two tables many-to-many |
| 4 | extension | referred to by no table; its primary key is a foreign key to one parent | at most one row per row of another table, holding more of that table's attributes; whether every parent row has one is a separate count, recorded beside the class |
| 5 | event | rows added in both transitions, none deleted | things that happen; a *header* if another event table refers to it, else a *record* |
| 6 | state | rows replaced in both transitions without growing | the current state of something, overwritten |
| 7 | lookup | refers to no table and has at most two attributes besides keys and audit columns | a list of codes or values |
| 8 | master | none of the above | business objects that persist and change slowly |

The rules are evaluated on the graph without the excluded links. "Attributes besides keys and audit columns" are the columns that are neither in the primary key, nor a foreign key,
nor one of the audit columns named in the tool's configuration.

**Readings and overrides.** Centrality is not the whole picture. A reader who knows the business may read a table
differently from its class by rule: a two-row table of price conditions is master by the rules but a table of rules in
business terms; a geography table with many attributes is master by the rules but reference data in business terms.
Such a reading is recorded as a **separate claim beside the class**, with its reason and a link to the evidence or the
item it rests on (often item 5, role). The class by rule is not overwritten, so the rules stay reproducible and the
disagreement stays visible. Agreement between the class by rule and the role of item 5 is itself reported per source.

## 6. Limits

- Behaviour rests on the transitions available. Two transitions of consecutive weekdays cannot tell a table that
  changes monthly or yearly from one that never changes, nor catch a table that grows on some days only. Classes that
  depend on behaviour (rules 5, 6 and 8) are therefore medium confidence until a longer window is seen.
- The thresholds (hub betweenness, two attributes for a lookup) are heuristics; changing them changes classes at the
  margin. They are recorded with each result.
- Only declared keys are links; a source with few declared keys gives a graph that understates its structure.
- Betweenness says that a table connects parts of the schema; it does not establish that data or a process flows through it.

## 7. First application: Wide World Importers

Run 2026-10-20 on the extracts of 2016-05-31, 2016-06-01 and 2016-06-02; recorded in
[`analysis/wwi/_source/29_position.md`](../../analysis/wwi/_source/29_position.md) and one `29_position.md` per table.

- 31 base tables, 98 declared links, of which 29 are `LastEditedBy`; 2 tables isolated (the two temperature tables).
- Distortion check: `Application.People` rank 1 by betweenness with all links, rank 12 without; central through 12
  roles in 5 tables, not through paths.
- Hubs without the audit links: `Warehouse.StockItems`, `Purchasing.Suppliers`, `Sales.Customers`,
  `Application.Cities` (the last through the addresses: the shared-parent pitfall of section 4).
- Classes: event 10 (3 headers, 7 records), master 8, lookup 9, bridge 1, extension 1, configuration 1, state 1, and
  17 history tables. The classes agree with item 5's role on 27 of 31 base tables; they differ on the three geography
  tables and on `Sales.SpecialDeals`, whose readings are recorded beside their class.

## 8. Running it on another source

The tool is [`prototypes/information_analysis/structure.py`](../../prototypes/information_analysis/structure.py), with
[`write_position.py`](../../prototypes/information_analysis/write_position.py) for the record. Inputs:

1. the catalogue of each table — columns, primary key, declared foreign keys, temporal type — and its row count and
   empty counts (`scratch/ia_profile/<schema>.<table>.json`, written by `profile_tables.py`);
2. three extracts, for two transitions (`data/raw/<source>/<day>/`, with a `manifest.json`).

The prototypes were written for Wide World Importers, and the source's name and folders are set in more than one
place: `SOURCE`, `RAW`, `DAYS` and `BASE` in `structure.py`; the source and extract folders in `profile_tables.py` (which
also computes the transitions, run through `recheck.py`) and in `relations.py` (whose `load_catalogues` reads the
catalogue summaries); and the source as the second argument of `write_position.py`. On another source each is pointed
at it before the run; the catalogue summaries must exist first (`profile_tables.py` on each of the three extracts).

Steps:

1. Point the scripts above at the source; set `DAYS`, `BASE`, and the audit and system-time column names in `AUDIT`.
2. Do the distortion check of section 3 before deciding `EXCLUDE`: run with `EXCLUDE` empty, look at the top of the
   betweenness ranking and at columns present in almost every table, and only then name what to leave out, each with
   its reason. Both graphs are recorded whatever is excluded.
3. Run `structure.py`; it writes one evidence file and copies it into each table's evidence folder.
4. Write a readings module (as `scratch/ia_specs/position_notes.py`): business-sense readings beside the class, each
   linked to what it rests on; then run `write_position.py <readings module> <source>`.
5. Have the measures and the readings reviewed separately (code and counts; readings and links), as for any item.

Requires `networkx` (`pip install networkx`).
