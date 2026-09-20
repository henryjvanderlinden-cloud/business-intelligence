# 2026-09-20 — The canon survey, first half: verification

**Question this note answers.** `ARC-OP-14`, whose first half is verification: are the
claims [190_machine-authored-design-canon.md](../../10_architecture/190_machine-authored-design-canon.md)
makes about Anchor Modelling, SQL:2011, and the rejection reasons attributed to Kimball
and to 6NF true, and what are the eight candidates in its §3 once each is classified by
*where its lifecycle work accumulates* rather than by what it was rejected for?

Written in session 04, 2026-09-20. Sources are cited inline. Per the conventions in
[`../README.md`](../README.md) this note is allowed to be wrong and is superseded rather
than revised.

Two documents depend on the outcome and are named here so that the dependency is not
rediscovered later: [002_mission-statement.md](../../00_concept/002_mission-statement.md)
version 0.6, whose load-bearing empirical assumption is that Data Vault's burden is the
kind machine authorship can absorb, and `CON-OP-8`, which requires the §III rewrite either
to argue an interaction between the two theses or to state its absence.

---

## 1. Verification verdicts

Verdict shapes follow [510_external-review.md](../../50_process/510_external-review.md):
**HOLDS**, **FAILS** with a counterexample, or **UNDETERMINED** with what is owed.

### 1.1 Anchor Modelling is 6NF — HOLDS WEAKLY, and §190 overstates the source

The primary source is Lars Rönnbäck, Olle Regardt, Maria Bergholtz, Paul Johannesson and
Petia Wohed, "Anchor modeling — Agile information modeling in evolving data environments,"
*Data & Knowledge Engineering* 69, no. 12 (2010), read as the authors' hosted preprint at
[anchormodeling.com](https://www.anchormodeling.com/wp-content/uploads/2011/05/Anchor-Modeling.pdf).
Pagination of the published version was not checked and is not asserted here.

The paper says an anchor model realised relationally "will have a high degree of
normalization" and carries 6NF as a keyword; it does not prove 6NF compliance in the body.
The 6NF attribution is standard in secondary literature — the
[Wikipedia article on sixth normal form](https://en.wikipedia.org/wiki/Sixth_normal_form)
names Anchor Modeling as a methodology employing it, and gives the definition and the
attribution to C. J. Date, Hugh Darwen and Nikos Lorentzos, *Temporal Data and the
Relational Model* (2003). That primary source has **not** been read here, so the definition
of 6NF and its attribution remain second-hand under rule 8.

The practical consequence is small but real: §190's phrasing, that Anchor "takes the same
logic to 6NF," attributes to the primary source a claim the primary source hedges.

### 1.2 Anchor's schema-evolution property — HOLDS

The paper states that "all changes are done in the form of extensions, which make different
versions of a model continuously available as subsets of the latest model," and that
"none of the schema modifications above affected the existing objects in the model. Only
additions were made," so evolution proceeds "on-line and non-destructively, through
extensions." Adding an attribute migrates nothing. §190's claim is accurate.

### 1.3 Anchor Modelling is "almost unused" — FAILS AS WORDED; the point it was making survives

The same paper reports use "in the insurance, logistics and retail domains, within projects
spanning from departmental to enterprise wide data warehouses," including an OLTP system
managing a million customers at an insurer and warehouses up to a terabyte. That is
self-reported by the method's own authors and is weak evidence of adoption, but it defeats
"almost unused" as an unqualified claim.

This matters because the sentence was load-bearing twice over. It is §190 §3's example, and
it is the counterexample that refuted `CON-OP-11`: a design with a discipline-wide domain
that is nonetheless rarely codified into practice. **That counterexample survives.** What
the evidence supports is that Anchor is rare *relative to what its generality would
predict* and rare relative to Kimball, Inmon and Data Vault — not that it is unused. The
repository has no adoption figure for any of these and should stop writing as though it
does.

### 1.4 6NF's cost is "object count and join complexity, one of which no longer matters" — UNDETERMINED, and the relief is conditional

This is the most consequential verdict in the note, because the re-evaluation programme
depends on it.

The Anchor paper's performance claim rests explicitly on table elimination: "modern query
optimizers utilize a technique called table (or join) elimination … tables containing not
selected attributes in queries are automatically eliminated." The supporting experiment
used Microsoft SQL Server 2008 and, by the authors' own description, "only one table in the
less normalized and up to 25 tables in the anchor database" — a small-scale test the paper
acknowledges as a limitation. A four-thousand-table anchor model is not what was measured.

Current engines do implement the optimisation, and the conditions under which they do are
the finding. [Snowflake's documentation](https://docs.snowflake.com/en/user-guide/join-elimination)
states that redundant joins are removed only where the relevant `UNIQUE`, `PRIMARY KEY` and
`FOREIGN KEY` constraints are declared **and** carry the `RELY` property; `NORELY` is the
default and suppresses the optimisation; Snowflake enforces such constraints only on hybrid
tables, so on standard tables "you are responsible for enforcing constraints on the data";
and if that integrity is not maintained, "the query results might differ if the `RELY`
constraint property is set." BigQuery is the same shape: Abdullah Alamoudi and Zewen Zhang,
["Join optimizations with BigQuery primary and foreign keys," Google Cloud blog, 14 July
2023](https://cloud.google.com/blog/products/data-analytics/join-optimizations-with-bigquery-primary-and-foreign-keys),
describe inner-join elimination, outer-join elimination and constraint-informed join
reordering, all requiring constraints declared `NOT ENFORCED`, with the warning that
violated constraints "may cause queries to return incorrect results."

So the honest statement is not that join complexity no longer matters. It is that **join
complexity is relieved on condition that key constraints are declared, trusted and true,
and the engine checks none of those three things.** Whether the relief survives at anchor
scale on a real workload is unmeasured, here and in the literature read.

### 1.5 SQL:2011's temporal features, and the third axis — HOLDS, and sharpens §190 §1

Krishna Kulkarni and Jan-Eike Michels, "Temporal features in SQL:2011," *SIGMOD Record* 41,
no. 3 (September 2012): 34–43,
[PDF](https://sigmodrecord.org/publications/sigmodRecord/1209/pdfs/07.industry.kulkarni.pdf),
adds application-time period tables, system-versioned tables and bitemporal tables, with
periods defined as metadata over pairs of datetime columns rather than as a period type.
IBM DB2 is the only implementation the paper names.

The paper covers versioning of **data** and says nothing about versioning the logic that
derived it, neither as provided nor as proposed among the extensions its authors list. The
author's third axis — the rule set — is therefore genuinely outside the standard rather
than merely underused, which is a stronger position than §190 §1 claims for it.

### 1.6 Kimball's rejection reason — FAILS

§190 §3 says "Kimball's star schema is explicitly a usability compromise — denormalise so
that humans can query and maintain it," and uses it as one of three examples of designs
rejected on the cost side of a correctness/cost trade. Ralph Kimball, ["A Dimensional
Modeling Manifesto," *DBMS Magazine*, August
1997](https://www.kimballgroup.com/1997/08/a-dimensional-modeling-manifesto/), does not
support that reading on either half.

He gives **two** reasons, not one. Understandability: end users "cannot understand or
remember an ER model," whereas with a dimensional model they "agree immediately that this
is 'their business.'" And query performance, as a property of predictability rather than of
tuning: the engine "can make very strong assumptions about first constraining the dimension
tables and then 'attacking' the fact table," so that "even a big suite of dimensional models
has an overall deterministic strategy for evaluating every possible query."

More damaging to §190's use of him, he does not frame it as a compromise that accepts a
known-correct design at a cost. He frames normalised ER modelling for decision support as
unsuitable — it "defeats the basic allure of data warehousing, namely intuitive and
high-performance retrieval of data," a situation that "is not just an annoyance, it is a
showstopper," producing "databases that cannot be queried."

**Consequence.** Kimball is not an instance of the pattern §3 is claiming. If a design's
proponent says the alternative is wrong for the purpose rather than merely expensive, then
citing him as a cost-side rejection misdescribes the source, and the argument loses one of
its three opening examples. Whether he was *right* is a separate question this note does not
reach; the survey's claim is about what the canon says, and the canon says something else.

### 1.7 Data Vault's object count as an acknowledged price — HOLDS, with a consequence

Ben Morris, ["Data Vault 2.0 modelling: the good, the bad and the downright confusing," 12
December 2020](https://www.ben-morris.com/data-vault-2-modelling-the-good-the-bad-and-the-downright-confusing/),
is practitioner commentary rather than a primary methodological source, and is cited as
testimony rather than as authority. It reports "at least three times as many tables in a
vault than in an equivalent relational model," a model "difficult to understand and awkward
to query," partial relief from bridge and point-in-time tables, and an "explanation tax"
paid indefinitely to technical and non-technical stakeholders.

The consequence is the part that matters here. Morris states that the method requires "a
high level of automation to ensure a consistent implementation across the many hundreds of
vault tables," without which a team is "extremely vulnerable to human error." Data Vault
does not merely tolerate generation; it presupposes it. And the generators exist and are
mature: [WhereScape](https://www.wherescape.com/solutions/project-types/data-vault-automation/),
[VaultSpeed](https://www.vaultspeed.com/), [AutomateDV](https://automate-dv.com/) and
Varigence all generate vault structures and loading logic from metadata today, with no
language model anywhere in the pipeline.

---

## 2. Classification of the §3 candidates

`ARC-OP-14`, as narrowed on 2026-09-20, asks for each candidate to be classified by **where
its lifecycle work accumulates**, with two things recorded separately because they are not
labour: runtime and compute cost, and the adjudication surface per `ARC-OP-15`.

Running that classification exposes something the list's presentation conceals: the eight
are not eight of a kind. Three are designs with a literature and a rejection history. Two
are artifacts a system emits. Three are disciplines about what a declaration must say. The
distinction matters because only the first group is a candidate for re-evaluation under
cheaper authorship at all; the third group's binding cost was never authorship.

**Rule-versioned bitemporality.** Dominant location: authoring the interval predicates, and
keeping every downstream query consistent with them; secondarily re-derivation on change.
Runtime: temporal predicates and period joins are a real recurring cost, unmeasured here.
Adjudication surface: **new** — someone must rule which rule version governs a restatement,
and no existing surface presents that. A design, and the strongest candidate in the list.

**6NF and anchor-style modelling.** Dominant location: not authoring, which extensions make
cheap, but query construction and performance tuning — the relocation the author argued and
external review conceded on 2026-09-20. Runtime: conditional relief, §1.4. Adjudication
surface: unmeasured, and per `ARC-OP-15` it is the surface and not the object count that
must be assessed. A design.

**Insert-only everything.** Dominant location: query construction, in the view logic that
reconstructs current state; operationally, storage growth and compaction. Runtime: the
current-state views are the cost and they are paid on every read. Adjudication surface:
unchanged. Closer to a storage discipline than a design, and largely subsumed by SQL:2011
system-versioned tables where those exist.

**Column-level lineage, exhaustively.** An emitted artifact, not a design. Dominant
location: mechanical derivation from parsed SQL, with maintenance tied to dialect coverage
— which is `ARC-OP-11` and is not free. Runtime: none in the data path; it is metadata.
Adjudication surface: it *supplies* the surface rather than consuming it. Note that this is
the neighbourhood of the interaction candidate refuted on 2026-09-20 against `CON-OP-8`; it
is recorded here as classification and is not re-proposed as an argument.

**Per-fact provenance.** An emitted artifact. Dominant location: generation, which is cheap;
the honest cost is write amplification and storage, which is compute rather than labour.
Adjudication surface: supplies evidence to it.

**Explicit units, currencies, timezones and grain.** A declaration discipline, and the
clearest case in the list. Its cost was never authoring — writing `EUR` is free. The cost is
*determining* what the unit is, which is elicitation and semantic judgement. Machine
authorship does not unlock it at all; contextual inference might propose it and a human must
rule on it. **This candidate belongs to the second thesis and is misfiled under the first.**

**Redundant physical representations.** Dominant location: authoring and maintenance,
genuinely multiplied per representation, and genuinely a compile-target problem given one
declaration. Runtime: storage and refresh compute multiply and keep multiplying; this is the
candidate where runtime cost most clearly is *not* relieved. Adjudication surface: mutual
consistency between representations becomes a claim someone has to be able to check.

**Assertions at maximum granularity, pruned by usage.** An emitted artifact. Dominant
location: **adjudication volume**, which is the scarce faculty per `ARC-OP-15` and the
ranking problem in `ARC-OP-6`. Generation is cheap and that is precisely the difficulty.
Not a canon design at all.

---

## 3. Findings

**F1. The §3 list is heterogeneous and its binding costs sit in different faculties.**
Three designs (rule-versioned bitemporality, 6NF/anchor, redundant representations), two
emitted artifacts (column lineage, per-fact provenance), three disciplines or practices
(insert-only, explicit units, maximum-granularity assertions). Only the designs are
re-opened by cheaper authorship. Explicit units is bound by semantic determination and
maximum-granularity assertions by adjudication capacity, so presenting them as instances of
*correct-but-unaffordable designs now affordable* overstates the first thesis by counting
its own dependencies as its evidence.

**F2. One of §3's three headline examples does not survive its source.** §1.6. Kimball
argued unsuitability, not cost.

**F3. The runtime relief the programme depends on is conditional on trusted, unenforced key
constraints.** §1.4. Columnar execution did not abolish the join objection; it made the
objection contingent on the truth of declared key constraints that no engine checks.

**F4. In the Data Vault case, the authoring half of the burden is already absorbed by
conventional metadata-driven generators**, and what those generators require as input is the
model metadata — which entity is a hub, what the business key is, which relationships are
links. That input is the second thesis's output. This is the comparison `CON-OP-8` demands
— machine authorship *relative to an otherwise equivalent conventionally authored
warehouse* — arriving earlier than expected and pointing away from the first thesis: in this
case the deterministic machinery already exists and the binding input is semantic.

**F5. An interaction candidate, drafted here and therefore unreviewed.** F3 and F4 compose.
The designs the first thesis makes affordable are decomposed designs; decomposed designs are
performant only where key constraints are declared and trusted; those constraints are
semantic assertions about identity, which is exactly what the second faculty proposes and a
human adjudicates. If that holds, the first thesis does not merely sit beside the second —
it *generates demand* for it, and the volume of key adjudication scales with the
decomposition that cheap authorship enables.

Two warnings travel with F5 and are not decoration. First, its direction is adverse as often
as it is favourable: an interaction in which thesis 1 loads the scarce faculty that thesis 2
feeds is a coupling, not a synergy, and the manifesto cannot present it as mutual support.
Second, it has the same shape as the candidate refuted on 2026-09-20 and may fail the same
way — the objection to test first is whether the dependency is on *cheap machine* authorship
or merely on decomposition, which a conventionally authored 6NF warehouse would share. It
must be reviewed on another model before anything is built on it.

> **F5 was refuted within the hour, 2026-09-20, session 04**, by
> [XREV_2026-09-20_canon-survey-interaction_sol](XREV_2026-09-20_canon-survey-interaction_sol.md),
> which is the superseding record; this note is annotated rather than revised, per
> [`../README.md`](../README.md). It fails on the axis its own second warning named, and on a
> second objection it did not anticipate: most keys that decomposition generates are
> mechanical or surrogate, not hypotheses about business identity. The pass also returned a
> correction that outlives it — a demonstrated *adverse* coupling is stronger evidence that
> the theses describe one system, not weaker — which contradicts the first warning above and
> is recorded against `CON-OP-8`. F1 through F4 were not reviewed in that pass and stand as
> written.

---

## 4. What this note does not establish

No primary reading of Date, Darwen and Lorentzos; 6NF's definition here is second-hand
(§1.1). No measurement of join elimination at anchor scale on a modern engine, which is the
open empirical question behind §1.4 and is not answerable from literature. No adoption
figures for any methodology (§1.3). No reading of Linstedt and Olschimke, so §1.7 rests on
practitioner testimony and vendor material rather than on the methodology's primary source.
No pricing of anything: `CON-OP-2` is untouched.

The second half of `ARC-OP-14` — re-evaluating the designs that survive classification —
is not attempted, because F1 changes which candidates are eligible and F2 removes one of the
examples that motivated the programme.
