# ADR-0010 — The second faculty is the agentic layer

- **Status:** Accepted
- **Date:** 2026-09-21
- **Supersedes:** —
- **Superseded by:** —

## Context

[ADR-0008](0008-faculties-substrate-mandate.md) ruled that three faculties act on a substrate
of data, and that a faculty is named by its function and never by its implementation. It left
the second faculty without a name, and `CON-OP-10` held the question. The candidates recorded
there — *sense-making*, *analysis*, *interpretation and design*, *design* — each covered part
of the work and missed another.

On 2026-09-21 the author proposed *agents* or *agentic*. His ground is that the faculty is not
a model but a working system: a heartbeat (in his musical terms, a MIDI clock), workflows,
documented procedures, memory, and LLMs. Its work has also grown: under
[ADR-0009](0009-separate-capabilities-open-value-areas.md) it builds known designs, proposes
meaning, and has room for monitoring, troubleshooting, testing and continuous improvement. No
function-name covers that range. He ratified *the agentic layer* the same day.

## Options considered

*Sense-making*, *analysis*, *interpretation and design*, *design.* Each names part of the work.
Rejected for the reasons recorded in `CON-OP-10`, and more decisively now that ADR-0009 leaves
the list of value areas open: any name built from today's functions goes stale when the next
area is added.

*Agents.* The author's first form. Workable, but it names the parts rather than the whole, and
the architecture already uses *agent* for the unit of work.

*The agentic layer.* Adopted.

## Decision

**The second faculty is called the agentic layer.** An **agent** is a unit of work inside it,
as [130_agent-loop.md](../10_architecture/130_agent-loop.md) and `ARC-OP-8` already use the
word. The three faculties are therefore: the deterministic machinery, the agentic layer, and
the human faculty.

**Two points of ADR-0008 are read explicitly, not left to interpretation.**

The rule that a faculty is never named after its implementation was written to stop *the LLM*,
*the model* or *the AI* becoming the name, because models will be replaced. *Agentic* names
the arrangement — clock, workflows, procedures, memory and models together — rather than any
one replaceable component, and is held to be within the rule's intent. *The LLM* and its
equivalents remain forbidden.

ADR-0008 rejected *agents* as the collective noun for all three faculties because of the
collision with "AI agent". That objection was to calling people and deterministic engines
agents. It does not apply to the one faculty that is built from agents.

*Layer* is used here in its ordinary architectural sense. ADR-0008 ruled out *layers* as the
collective noun because it implies a false stacking of the three faculties and collides with
the autonomy tiers; naming one faculty a layer does neither.

## Consequences

`CON-OP-10` is ruled, and the rename in `CON-OP-9` is unblocked. It lands with the §III
rewrite, together with the check ADR-0008 deferred, which can now forbid *component* for a
faculty and *the LLM* as a faculty's name.

*Agentic* is this period's buzzword. That costs nothing inside the repository. In material for
outside readers it may date and read as marketing, and a gloss on first use — *the agentic
layer: the clock, workflows, procedures, memory and models that do the system's analysis,
design and upkeep* — is the mitigation.

**Revisit** if *agentic* comes to mean something narrower in the industry than this faculty
does, or if outside readers take it as a product claim rather than a description.
