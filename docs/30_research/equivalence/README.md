# The equivalence investigation

**Status: set up 2026-11-14, session 12, by Claude Fable 5.2 on the author's instruction; a proposal, not ruled, and
unreviewed.** The name, this folder's place and the method below are the model's proposals. What is open is held in
[`ARC-OP-38`](../../../registers/OPEN_POINTS.md).

## The question

How does a lightweight, bare-bones, AI-assisted data environment (text declarations, generated plain SQL, small
single-purpose parts) reach the level of an "enterprise grade" environment, capability by capability?

## Where it comes from

On 2026-11-14 the author asked what standard ETL suites do that this setup could not do, or only with more trouble. His
message, verbatim:

> Now I have a number of follow up questions.
>
> * What is it that ETL tools do exactly that this "bare-bones" / "AI assisted" set up wouldn't be able to do, or would be noticeably more cumbersome?
> * If I do it in the "bare-bones" manner, i.e. with md text files, generative principles, generating simple deterministic (SQL) engines etc, I can have it read and edited by LLMs quite simply.
> * In my experience the standard ETL suites (like PowerCenter, SSIS, Azure Databricks) are able to do the bread and butter standard things, but they all have their own difficulties dealing with edge cases, which then require special interventions, voiding the advantage of having everything in one tool, or requiring 'weird' implementations and work arounds within the tool. In my opinion we often run into the limits of what is possible pretty quickly.
> * Maybe sometimes the administration / management console of standard ETL tools is better, like authorizations, or integration with AD, or building DTAP streets and promoting strategies.
> * I also don't find them helpful in keeping "overzicht" (for lack of a proper english translation. They become messy to look at pretty quickly, so they are not helpful in quickly comprehensing what is happening.
>
> Maybe I am missing something, so please also give me the relevant categories of functionality that these ETL tools provide, and that I should not miss in this setup.

The answer was a list of thirteen capabilities. He then asked for it to be kept and turned into a programme of its own,
verbatim:

> Yes, please store these findings somewhere. They are real gaps that need to be addressed. They also comprise a kind of research project, i.e. we need to address these issues. Please set up this separate research program. Not sure what to call it, these are kind of non-functional requirements, but also functional requirements. Maybe this is an equivalence investigation, how to get this light-weight, bare bones, AI assisted programma on the same level as "enterprise grade" environments. What I also find interesting is that Databricks, which is becoming a kind of industry standard, is made up of several open source projects. Maybe we could also draw some inspiration from that. These are separate from the research questions, because in a way they are already answers. Interested to hear your thoughts.

## The files

Questions and answers are kept apart, as he asked.

| File | Side | Holds |
|---|---|---|
| [010_capability-inventory.md](010_capability-inventory.md) | questions | the thirteen capabilities: what the suites give, where nsdn stands, what is asked |
| [020_databricks-anatomy.md](020_databricks-anatomy.md) | answers | what Databricks is made of, mapped onto the thirteen, and what can be learned from it |

Further answers would get files of their own from 030 on, one per reference stack or per component evaluated, each
citing the capability numbers it answers. The numbers 1 to 13 are permanent and never reused; a new capability takes
the next number.

## Proposed and not ruled

1. **The name.** "Equivalence investigation" is the author's own tentative wording and is used as the working title.
   The yardstick should be the list of capabilities in 010 and not any one product, because "enterprise grade" names a
   reputation and not a standard.
2. **Three ways a capability can end.** *Match*: nsdn provides it with a lightweight part. *Delegate*: the client's
   platform provides it (its database, its directory, its secrets store) and nsdn states what it needs from that
   platform. *Decline*: nsdn does not offer it and says so. Equivalence would then mean that every capability has one
   of the three, with a stated standard and evidence on the reference case, and not that nsdn rebuilds a suite.
3. **A standard before an answer.** Each capability gets a sentence saying what an answer must be able to do before
   candidates are compared, as [510](../../50_process/510_external-review.md) asks of a review.
4. **The order.** Capabilities 1, 2, 5 and 6 first, because a first client would feel them first.
5. **The place.** This folder under `docs/30_research/`, which [ADR-0002](../../20_decisions/0002-repository-layout.md)
   gives to tool evaluations. [ADR-0023](../../20_decisions/0023-domain-knowledge-folder.md) gave maintained knowledge a
   group of its own; whether this programme should have one too is the author's to rule.

## What this programme is not

It does not test the claim [410](../../40_roadmap/410_first-vertical-slice.md) calls the one that is either true or
not, that business keys and identity across sources can be proposed by a machine at a useful precision
(`EVI-OP-1`; point 6 of the [assessment of 2026-11-14](../notes/2026-11-14-general-assessment.md)). The capabilities
here are engineering with known answers in the industry. Their risk is cost and weight, not truth.

It adopts no technology. A candidate becomes part of nsdn only through an ADR, and `ARC-OP-20` puts principles before
languages and engines. [180_technology-posture.md](../../10_architecture/180_technology-posture.md) holds the earlier
candidates and its four properties of what a model can maintain; they apply here unchanged.
