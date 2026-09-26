# 142 — The data model: declared as text, navigated by dimensions

**Status: draft, unreviewed.** Written 2026-09-26, session 07, at the author's request. Nothing here is
adopted; the open question it raises is [`ARC-OP-29`](../../registers/OPEN_POINTS.md). Subjunctive
throughout: none of what is described exists.

## 1. Why this note exists

The first sandbox matched PAR establishments to OpenStreetMap businesses, and at no point did anyone
draw a data model. The author noticed:

> We didn't do any data modelling. At least not explicitly or visibly. Why is this important? The data
> model (conceptual, logical, technical) is a means of communication and of tracking the big picture for
> humans. Furthermore if we do the data modelling correctly we can do data warehouse automation, and use
> templates to generate deterministic loading patterns.

The sandbox did in fact have a model; it was just hidden. "Establishment" was a business concept, PAR and
OSM were two sources describing it, the match proposals were candidate same-as links between them, and the
class crosswalks were mapping rules. All of that lived inside
[`match.py`](../../prototypes/par_osm_match/match.py) and its JSON files, where it could be executed but not
seen, discussed or reused. That is the failure this note is about. The fix is not a modelling phase; it is
making the model an artefact of its own, from which code is generated or against which code is checked.

## 2. What the data model is for

It does three jobs, and the design has to serve all three at once.

First, it is how people communicate about the warehouse and keep the big picture. A person should be able
to see what business concepts exist, where their data comes from, and what has been built on them, without
reading code.

Second, it is the declaration from which the warehouse is generated. If the model says that an entity has
a given business key, is fed by these two sources, and changes at these two rates, then the hub, the
satellites, the link, their tables and their loading code follow by template. Same declaration and same
template version give the same code, every time. This is what [140](140_data-vault-automation.md) means by
"Tier 1 generates, Tier 2 declares", and what [100](100_system-overview.md) means by the system's real output
being declarative artefacts rather than data.

Third, it is the map the agentic layer navigates. An agent asked about a dimension should be able to walk
from it to the vault objects it is derived from, to the sources those were loaded from, and up to the
business concept they all describe, by identity, without searching.

The author's reference point is SAP PowerDesigner, which he has used professionally. In his words, it has
"a complete suite around that generates all code", which is "actually quite powerful", but it "is a
nightmare to navigate through and it carries a lot of unnecesarry ballast". The aim is to keep the first
property and lose the second, using open-source parts or parts built here.

## 3. The truth is text; pictures are for people

The model would be held as plain text files — one file per model object, structured front matter with a
short prose body — in the same way as the cards in [120](120_context-layer.md), and under the same stable
identifiers. Those files are the truth. Agents read and write them; generators read them; the checker
validates them.

Every picture of the model is generated from those files and is for human consumption only. It does not
need to be machine-readable, and nobody edits it. The author put it this way:

> the truth is "in the code" and the graphical representation is mainly for human consumption it does not
> need to be machine readable, just optimized for human consumption.

That frees the human view to be whatever is easiest to read and move around in, and it removes the
PowerDesigner problem of a diagram and a model that can drift apart: there is only the model, and the
diagram is rebuilt from it.

What gets declared should be small. Under vault automation a person, or an agent proposing for a person to
rule on, would declare only the things that carry meaning: business concepts and their business keys,
relationships between them, how each concept's attributes split by source and rate of change, and for the
dimensional layer the grain, the facts and the conformed dimensions. Everything mechanical — logical
columns, hash keys, table definitions, loading code, standard tests — would be generated and never edited
by hand. PowerDesigner's ballast comes largely from asking people to maintain the generated layers too. If
only declarations are authored, the model stays roughly the size of the decisions behind it.

## 4. Navigating by dimensions

The author's framing is that moving through the model is moving along dimensions (not in Kimball's sense),
and that there are at least two.

**From conceptual to concrete.** A business concept, such as *establishment*, is realised by logical
structures, such as a hub with its satellites, which are implemented as physical tables with loading code.
Moving along this dimension answers "what is this, and how is it actually built?"

**From raw to refined.** Data arrives as delivered by a source, is captured and integrated in the vault,
has business rules applied in the business vault, and is shaped for use in the dimensional model. Moving
along this dimension answers "where does this come from, and what is made from it?"

Every model object would have a position on each dimension, and there would be one kind of link per
dimension: *refines* for conceptual to concrete, *derives from* for raw to refined. Moving from any object
to its neighbours along either dimension is then a matter of following links.

There are probably others. Candidates worth testing, none of them decided:

1. **Subject area** — which business domain an object belongs to (sales, purchasing, stock), for moving
   sideways between related concepts.
2. **Source** — which source system an object is fed from, for following one source through every layer.
3. **Time** — which version of the model an object is shown in, since the model itself changes and is kept
   in git; "what did this look like last month" is a navigation, not an archaeology exercise.
4. **Status** — proposed, accepted, contested or retired, per
   [ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md), so that a person can look
   at only what has been ruled, or only at what awaits a ruling.

No single picture can show all of these, and it should not try. Each view would fix some dimensions and
show a small neighbourhood along the others: one concept across all refinement stages; one layer across all
concepts in a subject area; one table from its concept down to its loading pattern.

## 5. Connected to meaning and to loading patterns

Each model object would be, or would point to, a card in the context layer, so that retrieving it retrieves
what is known about it: its definition, its business key and the evidence for it, who ruled on it and when,
and what is still open. That is the "retrieve meaning" half of the author's requirement, and it needs no new
machinery beyond [120](120_context-layer.md) and
[ADR-0011](../20_decisions/0011-assertions-identity-plane-publication-gate.md).

The other half is loading patterns. Each concrete object would name the template it is generated from and
that template's version — for example a hub loader, a satellite loader, a link loader, a type-2 dimension
loader — together with the parameters the template needs. Templates are versioned know-how, which
[120](120_context-layer.md) already places in procedure cards. The agentic layer would write and propose
declarations; deterministic generators would turn declarations and templates into code; deterministic
engines would run the code. That keeps the model out of the data path, as
[ADR-0004](../20_decisions/0004-models-out-of-the-data-path.md) requires.

## 6. The human view: a generated HTML site

For people, the natural form is a small static website generated from the model files: one page per model
object, with its definition, its neighbours along each dimension as links, and a small diagram of its
immediate neighbourhood. Clicking moves along a dimension. A few overview pages — per subject area, per
source, per layer — give the entry points. Because it is static HTML it needs no server and no database,
and it can be rebuilt in seconds whenever the model changes, which fits the posture in
[180](180_technology-posture.md).

This is the concrete form of what [`ARC-OP-15`](../../registers/OPEN_POINTS.md) asks for — a
human-comprehensible surface generated from the same declaration as the machine-optimal physical model —
and it is a candidate for the human view of the catalogue in
[`ARC-OP-26`](../../registers/OPEN_POINTS.md). It belongs among the surfaces in
[170](170_human-interfaces.md).

## 7. The agents' view

Agents would not use the HTML. They would read the model files directly, and a derived index — rebuilt from
the files, never the other way round — would let them follow *refines* and *derives from* links by
identifier. The retrieval contract of [120](120_context-layer.md) applies unchanged: from any object, an
agent should establish what it is, what is known and uncertain about it, and what depends on it, in at most
three loads.

## 8. Existing tools to borrow from

The following is from the model's general knowledge as of mid-2026 and has not been verified in this
session; per [AGENTS.md](../../AGENTS.md) rule 8, it is a list of hypotheses to check, not facts.

**LinkML** is an open-source schema language written in YAML that generates JSON Schema, SQL table
definitions, documentation and diagrams from one declaration. It is the closest existing fit for a model
that people and machines both read, and a candidate language for the declarations rather than inventing a
syntax. **DBML** is a compact text notation for logical and physical entity-relationship models.
**AutomateDV** and **datavault4dbt** generate Data Vault loading code for dbt from metadata, which shows the
template half works; they cover only the concrete end of one dimension. **Mermaid** is a text diagram
language that GitHub renders, and would serve for the small per-page diagrams.

As far as is known here, none of these covers conceptual-to-concrete and raw-to-refined together, with
links between the layers that can be walked in both directions. That gap is what would be built, and it is
small: a file format, a validator, a handful of generators and a static-site builder.

## 9. Risks

**Rebuilding the ballast.** A model object that nothing is generated from and no decision cites is
documentation, and documentation decays. The guard would be a checker rule: every declared object is
either consumed by a generator or cited by a decision, or it is flagged.

**Drift between model and code.** If any loading code is written by hand, the model can stop describing
the warehouse. The guard is that generated code is never edited, and hand-written code, where unavoidable,
is checked against the model rather than trusted.

**Tying the format to Data Vault.** [ADR-0013](../20_decisions/0013-data-vault-or-equivalent.md) makes the
integration layer Data Vault *or a functionally equivalent layer*. The declarations should therefore speak
of business keys, history and integration, with hubs, links and satellites as one implementation of them,
so that another equivalent layer would need new templates but not a new model.

**Declaring before there is evidence.** Business keys are the hard part ([140](140_data-vault-automation.md)).
A declaration format makes it easy to write a key down; it does not make the key right. Declarations would
carry assertion status and evidence like everything else in the context layer.

## 10. What this note does not decide

Whether the data model is a first-class part of the context layer, navigated by dimensions and authored
only as declarations, is open: [`ARC-OP-29`](../../registers/OPEN_POINTS.md). The declaration language is
part of [`ARC-OP-20`](../../registers/OPEN_POINTS.md), which says principles are ratified before languages
are adopted. Per [`spec/README.md`](../../spec/README.md), no schema for model files would be written until
an ADR has ruled on the shape and a prototype has exercised it. The obvious first exercise is to write the
model of a case already run, or of the next sandbox, by hand in the proposed format and generate the HTML
from it; the author has not yet asked for that.
