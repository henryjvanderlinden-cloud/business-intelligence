# Registers — conventions

The register is the single authoritative answer to *what is open?* Documents in
`docs/` describe the design; ADRs record what was settled; the register records what
is not.

These conventions are adapted from the compendium repository's master register, whose
central lesson was learned the hard way there and is inherited here without having to
repeat the mistake: **a register that cannot answer "what is open?" is not a register.**
The compendium's `Status` column spent months holding the status a row had *when it was
opened*, with current state recorded elsewhere, and nothing said so. Rows disagreed with
themselves. The fix — an explicit state token in a fixed position, mechanically
enforced — is adopted here from the start.

## The state rule

Every row's first line after its heading is exactly one state token:

```
**✅ STATE: EXECUTED <date>**    the work is done
**✅ STATE: RULED <date>**       a decision was taken; the work may still be owed
**⛔ STATE: OPEN**               live, nothing decided
**⚠ STATE: HELD**               deliberately parked, with a stated condition for resuming
**📦 STATE: ARCHIVED <cut>**     moved to an archive cut; no residual obligation
```

Only `EXECUTED` and `ARCHIVED` close a row. `OPEN`, `HELD` and `RULED` leave it live.

**`RULED` does not mean settled.** A ruling is a decision, not the work. This
distinction is the compendium's second hard-won lesson and the more consequential of
the two: it is what stops a register from quietly reporting a project as finished
because its decisions have all been taken.

**Partial settlement is not settlement.** A row settled on one side and open on the
other stays `OPEN` and says so in its name — `PARTLY`, `PARTIALLY`, `SUB-ITEM` are the
recognised words. A name that claims a settlement the row does not have is a defect.

## Supersession

Superseded text is kept, not deleted; it carries the argument that produced the ruling,
and deleting it leaves the ruling unexplained. It must be introduced by a phrase
containing the word **superseded**, which is load-bearing and machine-read: the first
occurrence of `superseded` in a row's body opens the historical block, and **nothing
after it is a current claim about the row.**

## Identifiers

`<SCOPE>-OP-<n>`, allocated sequentially within a scope and **never reused**, including
after archiving. Scopes:

| scope | covers |
| --- | --- |
| `CON` | the concept and the argument — is the thesis true? |
| `ARC` | architecture and mechanism |
| `EVI` | data, evidence, measurement, ground truth |
| `PRC` | how the work itself is conducted |
| `BIZ` | commercial premises and positioning |

A row spanning scopes takes `X-OP-<n>`, following the compendium's practice.

## Format, and a deliberate deviation

The compendium's register is a markdown table. This one uses one heading per row.

The reason is the retrieval constraint in
[`../docs/10_architecture/120_context-layer.md`](../docs/10_architecture/120_context-layer.md)
applied to this repository's own working materials: a heading-per-row file can be read
in part, diffs cleanly line by line, and does not require every `|` inside a cell to be
escaped — a rule the compendium had to add after five rows were found silently broken
by unescaped pipes, one of them introduced by the same session that found them. Tables
are better for scanning a hundred short rows; headings are better for a register whose
rows carry argument. This register expects the latter.

## Archiving

`archive/` holds append-only cuts, indexed by `archive/README.md`. Cut files are never
rewritten. The compendium's rules are adopted verbatim in substance:

- A row is archived only if it carries **no** residual obligation.
- A row with a residual is trimmed, not archived, and trimming runs as its own pass in
  its own commit.
- Every residual named inside an archived row is promoted to an explicit live
  destination **before** the parent moves. This is the only step where content can be
  lost.
- Content moves verbatim.
- Numbers are never reused.

Archiving is premature until the register is large enough to be unwieldy. It is
documented now so that the first cut does not have to invent the rules under pressure.

## Enforcement

`python tools/check_repo.py` enforces the state rule, identifier uniqueness, closing
states carrying dates, the name-claims-settlement check, link integrity and ADR index
completeness. Per [500_working-method.md](../docs/50_process/500_working-method.md), a
rule here that the checker does not enforce is decoration.
