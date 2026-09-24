# 080 — Overview for discussion: main points and a schematic

**Status: working draft, 2026-09-24.** The main points of the project for discussing it with
other people, and a first sketch of the schematic that shows them. Stored at the author's
request, verbatim from the conversation in which it was drafted. The SVG is not yet drawn.

---

**On the schematic.** Here are the points I'd put in front of other people. They cover the whole project, not just the task table.

1. **The premise.** LLMs lower the cost of building and maintaining a data landscape so much that what humans contribute in BI changes. Plenty of designs that were too laborious for ordinary teams become affordable.
2. **Three faculties, working on one substrate.** Data is what gets worked on. The three that do the work are deterministic machinery, the agentic layer and humans.
3. **Mandate is separate from capability.** Each faculty has a mandate, meaning what it is *allowed* to do. Models never touch the data path. The agentic layer proposes; humans rule on meaning and set purpose.
4. **The agentic layer is a system, not a model.** It is a heartbeat, workflows, documented procedures, memory and LLMs.
5. **Work is allocated by strength, as a chain.** Every task runs proposes → decides → executes → checks.
   - Machinery runs everything that touches data.
   - The agentic layer writes and explains: code, templates, metadata, tests, diagnoses.
   - Humans decide meaning, disputes, consequences and commitment.
6. **The reference architecture is familiar.**
   - Sources → raw.
   - Data Vault, for all the data, all the time.
   - Dimensional marts and a semantic layer, human-readable and for self-service.
   - Rule versioning, so any past report can be reproduced.
7. **The value areas are separate, and the list is open.**
   - Cheaper building (the vault-to-mart projection).
   - Metadata, where human-made catalogues fail today.
   - Monitoring, troubleshooting and testing.
   - Continuous improvement.
8. **Safeguards.**
   - Every accepted claim traces to evidence or to a responsible person.
   - Where machines can check the output, the agentic layer scales. Where only judgement can check it, humans stay the bottleneck.
   - Cost must not simply move elsewhere.
9. **Honestly open.**
   - The central bet: can the agentic layer propose business keys well enough to be worth checking?
   - The economics aren't quantified.
   - Nothing is built yet. A proof of concept on public data comes next.

**How I'd draw it.** I'd use a layered architecture picture, because BI people read a left-to-right data flow instantly. The new part is overlaying *who does what* on top of it.

```
┌──────────────────────── HUMANS ─────────────────────────┐
│ set purpose · decide meaning · approve · act on insight │
└────────▲ asks, reports ─────────────────── decides ▼────┘
┌───────────────────── AGENTIC LAYER ─────────────────────┐
│ heartbeat │ workflows │ procedures │ memory │ LLMs      │
│ writes templates & rules · metadata · tests · diagnoses │
└────────▲ observes ──────────────────── proposes ▼───────┘
┌─────────────── DATA (substrate) · run by DETERMINISTIC MACHINERY ───────────────┐
│ sources → raw → DATA VAULT → MARTS → SEMANTIC LAYER → dashboards / users        │
│             (all data,        (human-readable,                                  │
│              all time)         self-service)       + rule versioning, lineage   │
└─────────────────────────────────────────────────────────────────────────────────┘
 side panel: value areas        footer: principles (mandate, no models in data path,
                                traceability) · open questions (central bet, economics)
```

The three bands stack the faculties by mandate: machinery at the bottom running the pipeline, the agentic layer in the middle, humans on top. The arrows show the chain: the agentic layer observes and proposes, humans decide, machinery executes. The side panel holds the value areas and the footer holds the principles and open questions, so one picture covers all nine points.
