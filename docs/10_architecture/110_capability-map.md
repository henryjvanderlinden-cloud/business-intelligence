# 110 — Capability map

The eight capabilities from [100_system-overview.md](100_system-overview.md), each with
its input, its output, its autonomy tier, and the thing that most plausibly goes wrong.
This is the map against which phasing is planned; it is not a dependency graph.

## Access

Holds source contracts: owner, legal basis, personal-data classification, permitted
operations, read budget, freshness expectation, credentials reference. Mediates every
read. Refuses rather than degrades.

*Tier: none — this is policy, not analysis.*
*Risk: that it is treated as paperwork and bypassed, at which point the whole system
becomes unauthorised.*

## Discovery

Enumerates the landscape from the cheapest surfaces first: existing catalogues, dbt
manifests, BI-tool lineage exports, `information_schema`, file listings. Data itself is
the last resort, not the first. Produces one card per object.

*Tier 1.*
*Risk: that discovery is confused with network scanning, which is a security incident
rather than a feature. See [150_trust-and-blast-radius.md](150_trust-and-blast-radius.md).*

## Profiling

Characterises discovered objects, and — critically — maintains sketches that make
cross-source overlap estimable without centralising data. Repeats over time to establish
volatility, growth and update semantics, which is what actually determines whether a
source needs historisation.

*Tier 1.*
*Risk: cost, and profiling load landing on production at month end.*

## Sense-making

Writes descriptive cards, proposes business keys, raises identity and joinability
hypotheses, infers entity and relationship structure, detects probable personal data,
and formulates questions it cannot resolve.

*Tier 2.*
*Risk: plausible, fluent, wrong. Mitigated by evidence thresholds, falsifiers and
cross-model review.*

## Adjudication

Maintains the ranked queue of open questions, routes them to the right person, records
rulings as assertions with provenance, and handles disagreement between adjudicators.

*Tier 2, human-facing.*
*Risk: that nobody answers. The queue's ranking exists precisely because attention is
the binding constraint.*

## Construction

Generates and maintains: capture jobs, raw vault objects, business vault structures,
marts, tests, analyses, visualisations and narrative. Everything it produces is a
declarative artifact under version control, executed by a deterministic engine.

*Tier 1 for the vault (mechanical given keys); Tier 3 for marts and analyses (must cite
a decision).*
*Risk: volume. A generator with no pruning counterpart is a liability.*

## Evaluation

Four distinct guarantees, elaborated in
[160_evaluation-and-regression.md](160_evaluation-and-regression.md): determinism,
quality contracts, semantic stability, and release regression on frozen data (added
2026-09-28). Plausibility checks were added on 2026-10-06, and the kinds of test are mapped to the
root causes they catch in [162_test-framework.md](162_test-framework.md).

*Tier 1 mechanically, Tier 2 in interpretation.*
*Risk: alert fatigue, which is indistinguishable in practice from having no tests.*

## Pruning

Retires artifacts that have lost demand justification, archives their definitions, and
reports what it removed. Equal standing with Construction.

*Tier 3 for the policy, Tier 1 for its execution.*
*Risk: that it is never built, because building things is more satisfying than removing
them.*
