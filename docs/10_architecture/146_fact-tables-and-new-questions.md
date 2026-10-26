# 146 — Fact tables and new questions: when to extend, when to build anew

**Status: draft, partly ruled.** Written 2026-10-26, session 09, at the author's request for "a number of
considerations to base the decision on". What he ruled is in
[ADR-0026](../20_decisions/0026-conformed-dimensions-and-fact-table-changes.md); the considerations and the
classification below are proposed and open under [`ARC-OP-37`](../../registers/OPEN_POINTS.md) item 8. Unreviewed.
The dimensional-modelling terms are the model's general knowledge of common practice (grain, conformed and
role-playing dimensions, transaction and snapshot fact tables), not verified in this session (rule 8 of
[AGENTS.md](../../AGENTS.md)).

## 1. The question

Marts share conformed dimensions, so the design work for a new business question is mostly about fact tables. The
author, verbatim, on 2026-10-26:

> Like you said, dimensions should be shared. So we're focused mainly on fact tables. I think there is a consideration
> / deliberation necessary if for a new question a fact table only kind of fits. We should do an analysis then, to see
> how much we have to alter the fact table to make it compatible with the new request and how much we are drifting
> away from the original intent. If we can formalize these questions, then fine, otherwise human adjudication is
> necessary. Under normal circumstances this is not a continuous process / going concern thing. Expanding fact tables
> to fit new business questions is quite the fundamental decision. If you can list a number of considerations to base
> the decision on, that is very helpful. Maybe when enough experience has been built up the decision making can be
> automated.

The considerations below are the analysis he asks for. Each is put as a question that can be answered from the fact
table's declaration and the new request, so that as many as possible can be formalised.

## 2. Considerations

**Grain.**

1. *Does the new question need the fact table's grain, a coarser one, or a finer one?* Coarser is an aggregation and
   needs no change. Finer cannot be served by the table at all; a fact table's grain is never changed in place.
2. *Would the change put rows of another grain into the same table?* Mixed grain is the commonest way a fact table is
   ruined: totals double count without anyone noticing.

**Business process and kind of measurement.**

3. *Is it the same business process?* A fact table records one process, such as order lines, invoice lines or stock
   movements. A question about another process (payments, say) belongs to another fact table, even when the
   dimensions overlap.
4. *Is it the same kind of measurement?* A transaction fact table records events; a periodic snapshot records a state
   at regular moments; an accumulating snapshot follows one thing through its milestones (an order from placement to
   payment). A question about state ("outstanding balance at month end") does not fit a transaction table, however
   close the data looks.

**Measures.**

5. *Are new measures needed, and are they at the table's grain?* A new measure at the same grain, from the same
   population, is the cheapest change there is.
6. *How do the new measures add up?* Additive measures can be summed along every dimension; semi-additive ones (a
   balance) not along time; non-additive ones (a rate, a ratio) not at all. A non-additive measure is stored as its
   additive parts.
7. *Does the request define an existing measure differently?* For example revenue with or without tax, with or without
   credit notes. A different definition gets a different name and its own engine rule; an existing measure is never
   redefined in place.

**Dimensions.**

8. *Are new dimensions needed, and are they single-valued at the grain?* Adding a dimension that has exactly one value
   per row is cheap. One with several values per row (an item in several stock groups) needs a bridge, and is a
   significant change.
9. *Does it need another role or time perspective?* Adding a role-played dimension (the billed-to customer beside the
   delivered-to customer, or the invoice date beside the order date) is cheap. Changing which date or which role is
   the default is drift, because it changes what existing reports mean.

**Population.**

10. *Does the request count the same rows?* Inclusion rules decide this: credit notes, cancelled or back orders,
    internal customers, test data. A narrower population is a filter in the mart. A different base population is a
    sign of another fact table.

**Time and versions.**

11. *Does it need other temporal semantics?* As-was against as-is, a knowledge date (what we knew on date X), or
    another engine version (ADR-0024). A view over the same bitemporal facts may serve; if not, the request differs
    in kind.

**Effect on what exists.**

12. *Do existing numbers change?* Any change that alters a figure an existing report shows is fundamental. It needs a
    release note, and the regression diff of [`ARC-OP-30`](../../registers/OPEN_POINTS.md) to show its impact.
13. *Who uses the table now, and how much is at stake?* The number of consumers and their weight: a regulatory report
    weighs more than an exploratory dashboard.

**Drift from the original intent.**

14. *Is the table's statement of purpose still true after the change?* Every fact table would carry a short statement
    of the question it was built for (the use case it cites, per [140](140_data-vault-automation.md)). If that
    statement has to be rewritten, the table is drifting. A rough measure is the share of its columns and rows that
    serve the new request rather than the original one.

**Cost and consistency.**

15. *What does each path cost?* Extending costs build time, testing and the risk of changing existing numbers. A new
    table is cheap to generate under machine authorship, but adds an object to maintain
    ([145](145_entropy-and-pruning.md)).
16. *Would two tables then give two answers to one question?* If a new table holds a measure an existing one also
    holds, a reconciliation test between them is required, or the same measure must come from one engine rule.

**Durability of the request.**

17. *Is the question recurring or one-off?* A one-off or exploratory question is answered by a query against the
    business vault or an existing mart, and changes no fact table.

## 3. A first classification, proposed

The considerations sort a request into four outcomes, in order of increasing weight:

- **Serve without change.** The existing table answers by aggregation, filtering or dimensions it already has
  (considerations 1, 10 and 17 pass with no change). A view or a query; no adjudication needed.
- **Minor extension.** A new measure at the same grain and population, a new single-valued dimension, or a new
  role-played dimension, with no existing number changed (5, 8 and 9 cheap; 12 passes). The agent layer proposes; the
  author has not said whether these need adjudication, and as experience builds they are the first candidates to run
  on a rule.
- **Fundamental change.** Anything that touches grain, the default role or date, the base population, the definition
  of an existing measure, a multi-valued dimension, or changes an existing number (2, 7, 8 with a bridge, 9 on a
  default, 10 on the base, 12). Always adjudicated by a person, as the author ruled for anything that cannot be
  formalised.
- **New fact table.** Another grain, another process or another kind of measurement (1 finer, 3, 4). Built beside the
  existing one, with conformed dimensions, and with a reconciliation test where measures overlap (16).

## 4. Building the experience that would allow automation

The author expects the decision might be automated once enough experience exists. That requires each decision to be
recorded in a form that can be learnt from: the request; the fact table it was weighed against; the answer to each
consideration, with its evidence; the outcome; who decided; and later, whether the decision held up. Kept as one small
text file per decision, like the analysis record, these would form a case base. Agreement between a proposed rule and
past adjudications would then measure whether the rule can take over, in the spirit of
[155](155_adjudication-economy.md). This is proposed, not ruled.

## 5. What this note does not decide

The list of considerations, the classification, whether minor extensions need adjudication, and the case base are open
under `ARC-OP-37` item 8.
