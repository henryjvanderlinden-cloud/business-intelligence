# XREV 2026-09-25 — overview schematic (080 SVG) — astra

```yaml
object:        docs/00_concept/080_overview-schematic.svg, at commit a930af0.
reviewer:      gpt-6-astra (model_reasoning_effort medium), via the Codex MCP server on the
               author's desktop (pinned Codex 0.153 in C:\Tools\codex-0153), sandbox read-only,
               thread 01a0d8c3-ee70-76a1-8cb7-f54183aee31a. Read the SVG source, no other files.
assignment:    one question, adversarial ("assume the picture implies something false"): which
               arrows, directions, labels, placements, missing arrows or the gate's position induce
               a wrong belief about how the framework works; ranked, with minimal fixes to the
               drawing, 300 words; praise, assessment, summary and visual style forbidden. Supplied
               the design facts the picture must respect. Declared out of scope: density, and the
               placement of the adjudication band, which the author accepted. The twelve points
               went to sol in parallel.
second reader: assignment set by Claude Opus 5.5, which drew the object. The author accepted all
               four findings; the second in part, as proposed below.
verdict:       FAILS — four findings; all integrated 2026-09-25, the second in part.
```

Astra's answer, verbatim:

1. **Context → Humans “catalogue” arrow, originating beside Assertions; no publication pipeline drawn.** This suggests that assertions—including agent write-backs—become human catalogue content directly. The pipeline sentence does not establish a boundary in the flow. **Minimal fix:** draw a distinct human-catalogue compartment fed exclusively through a labelled publication pipeline; originate the human-facing arrow there.

2. **Agentic → Data “approved code, templates and tests,” with no approval-result connection from adjudication.** The executable route bypasses the mechanism that authorizes it, suggesting the proposing layer can approve its own output. The four lanes also lack outcomes, leaving automatic acceptance and parking disconnected from execution. **Minimal fix:** connect adjudication outcomes to the delivery route; show scoped acceptance, human decisions, and Park as distinct outcomes. Mark auto-accept/Park as the usual destinations and human escalation as exceptional.

3. **Publication gate after the box labelled “Dimensional marts.”** A practitioner could read that box as already available marts, with tests gating only their onward exposure through the semantic layer. That permits direct consumption of an untested mart. **Minimal fix:** rename the upstream box “Candidate mart version”; label the gate’s output “Published mart version—tests passed for this version.” Show every consumer downstream of that boundary.

4. **“One identity plane” entirely inside the Context System column; unqualified Data → Agentic “observes” arrow.** This suggests identity and pre-retrieval access filtering apply only to context stores, while agents observe data through a separate, unrestricted route. **Minimal fix:** depict the identity/access boundary spanning all stores, and label observation and context retrieval as access-filtered before retrieval.

FAILS + the drawn routes leave publication, execution authorization, and shared access boundaries bypassable or ambiguously scoped.

## Dispositions

Integrated into [080_overview-schematic.svg](../../00_concept/080_overview-schematic.svg) on
2026-09-25, after the author's reaction.

1. **Accepted.** The catalogue for people is now its own compartment at the top of the context
   column, fed by an arrow labelled *publication pipeline*; the arrow to humans starts there.
2. **Accepted in part.** The agentic layer no longer sends "approved code" straight to machinery;
   execution now runs from the adjudication band's outcomes to the data band, labelled *accepted
   work only — executed by machinery*, and the band's subtitle says most proposals never reach a
   person. Separate drawn outcomes per lane were not added: they would crowd a picture already dense
   by choice.
3. **Accepted.** The flow now reads *Mart build (candidate version) → publication gate → Published
   marts → semantic layer → dashboards*, so every consumer sits downstream of the gate.
4. **Accepted.** A dashed boundary labelled as the one identity plane now spans the data band and the
   context column, with access filtered before retrieval by people or agents; the observation arrow
   reads *observes profiles and metadata, not data rows — access-filtered*, consistent with
   [ADR-0004](../../20_decisions/0004-models-out-of-the-data-path.md).
