# ADR-0045 — The sales viewer is a proof of concept, not a supported tool; house styles stay outside the repository

- **Status:** Accepted
- **Date:** 2026-11-19
- **Supersedes:** —
- **Superseded by:** —

## Context

On 2026-11-19 the author asked for an HTML visualization of the datamart, with slicing and dicing, a line chart and a
table underneath, in the style of the VDL-DIAA website. The model built
[`prototypes/sales_viewer/`](../../prototypes/sales_viewer/README.md): a single self-contained page over
`analyses.sales_by_customer_segment_month` ([ADR-0039](0039-first-use-case-and-where-marts-read-from.md)), and a
script, `verify.py`, that reconciles the page's figures from staging through the raw vault, the business vault and the
mart to the page, with plausibility checks on the way (22 checks, all passing on the warehouse known on 2016-06-06).

Two questions were left open in `ARC-OP-39`: whether the viewer graduates to a supported reader of the marts, and
where a house style lives. The model had built the page neutral by default, with the VDL-DIAA style kept in
`C:\Git\vdl-diaa\huisstijl\brand.json` and passed in at build time, because
[ADR-0035](0035-reference-case-and-client-repositories.md) decision 2 keeps company material out of this repository
and [ADR-0041](0041-cc0-public-domain-dedication.md) dedicates the repository to the public domain. The author ruled on
2026-11-19 at 11:13, verbatim:

> so we've created the first step towards a Test Framework. Let's also record that somewhere. I think in the
> architecture section there's already a mention, but we can now also state that a first test was created.
> The sales viewer is not a supported tool, but it is a proof of concept, most importantly that the agentic layer can
> generate a functioning visualization of the datamart, given all the context the LLM has. The house style should
> stay outside this repo.

## Options considered

*Graduate the viewer to a supported reader of the marts.* Its case: business readers need some way to see the marts,
and the page already works and reconciles. Against it: a supported tool carries maintenance, tests and a promise to
clients that nothing in the design has yet weighed, and the presentation layer is not what nsdn is testing.

*Keep it as a proof of concept.* Its case: what the page demonstrates is that the agentic layer, given the context in
this repository (declarations, generated SQL, analysis record, ADRs), can produce a functioning, reconciled
visualization of the mart in one session. That is a claim about the agentic layer, and a proof of concept is the right
weight for it. Adopted.

*Keep a house style in this repository.* Its case: one place, no build-time argument. Against it: it would bring
company material into a public-domain repository, against ADR-0035 decision 2.

*Keep house styles outside, passed in at build time.* Adopted. A client's house style travels the same way, from its
own repository.

## Decision

1. The sales viewer is a **proof of concept**, not a supported tool. It stays under `prototypes/`, is not maintained,
   and is not offered to clients as a feature. What it demonstrates is that the agentic layer can generate a
   functioning visualization of the datamart, given the context the model has.
2. **House styles stay outside this repository.** A page is built neutral by default; a style is read at build time
   from a folder outside the repository (for VDL-DIAA, `C:\Git\vdl-diaa\huisstijl\`), and branded output is written
   to a folder ignored by git.
3. `verify.py` is recorded as **a first test towards the test framework** of
   [162](../10_architecture/162_test-framework.md), held in `ARC-OP-31`. This records that the test exists; it does not
   adopt the framework or its tooling, which still needs an ADR of its own.

## Consequences

The page may fall out of step with the marts as they change; nobody is obliged to keep it working, and a broken viewer
is not a defect of nsdn. If business readers come to need a view on the marts, that is a new decision, and this
prototype is evidence for it, not a commitment. `ARC-OP-39` is closed by this ADR. Revisit if a client asks for
presentation as part of an engagement, or if a second generated visualization shows the same result on a source other
than Wide World Importers. Unreviewed on another model.
