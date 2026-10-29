# XREV 2026-10-29 — the model declaration format — sol

```yaml
object:        model/README.md, as committed in 53362ee (the format only; the declaration files and the checker unread).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; answer written to the ignored scratch/ folder with apply_patch; confined to the one
               file, it wrote in about 3 minutes.
assignment:    assume a Data Vault 2.0 practitioner who has built metadata-driven generators rejects the format, judged
               against four stated standards (only decisions declared; a deterministic generator needs no guessing;
               identity stable under renames; a forgotten or doubly placed column caught mechanically); up to five
               findings with failure cases; folder layout, YAML, naming taste, business vault and marts excluded;
               praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 11 on 2026-10-29; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [the exactly-once column rule rejects necessary reuse of source keys across hub and link loads].
               Resolved in the revised text, unreviewed.
```

## sol's answer, verbatim

### 1. The exactly-once column rule rejects necessary multi-use

**Quoted text:** “Every column of every base table has exactly one place: a hub's business key, a link, one satellite, a reference table, or a rule of the source file.”

**What is wrong:** A source column does not have exactly one raw-vault use. The same foreign-key or business-key value commonly identifies a hub and supplies an endpoint of one or more links. Treating those uses as mutually exclusive confuses source-column classification with generated-model consumption. It therefore cannot meet the stated requirement that double placement be caught without also rejecting valid models.

**Concrete failure case:** Given a hub declaration containing `- Sales.Orders.OrderID | key_space=wwi | key_kind=source-key` and a link declaration containing `- Sales.Orders.OrderID | names=hub_order` plus `- Sales.Orders.CustomerID | names=hub_customer`, the checker rejects `Sales.Orders.OrderID` as doubly placed. If the author removes it from the hub to satisfy the checker, the generator no longer has a declaration that `Sales.Orders.OrderID` is a source of `hub_order`; if the author removes it from the link, the link loader cannot calculate the order endpoint.

**Minimal correction:** Give every catalogue column exactly one exhaustive **disposition** (`business-key`, `relationship-key`, `payload`, `metadata`, or `ignored` with reason), separately declare one or more permitted **uses**, and validate the legal use pattern for each disposition. A relationship-key use must be allowed to reuse a column already used to load its endpoint hub.

**Confidence:** High.

### 2. Alternative source mappings are indistinguishable from composite keys or one joined record

**Quoted text:** “**Hub**: ... section *Business key*, one line per source column that feeds the key” and “**Link**: ... sections *Columns* (the source column, with `names=<hub>`)”.

**What is wrong:** Neither section has a source-record/load-unit identifier or a key-component ordinal. Consequently, several lines cannot say whether they are components of one key, alternative mappings from different records, or endpoints that must be read together. A catalogue can describe columns and types, but it cannot supply that modeling decision.

**Concrete failure case:** A customer hub has `- Sales.Customers.CustomerID | key_space=wwi | key_kind=source-key` and `- CRM.Account.AccountNumber | key_space=crm | key_kind=governed`. These are two alternative single-column hub loads. The grammar also represents a two-column composite business key with exactly two lines. A deterministic generator must either concatenate the two values into one impossible cross-system key, emit two loaders by guessing from table qualification, or reject the declaration. For a link, four lines representing two endpoint pairs from `Sales.Orders` and `CRM.Opportunity` likewise give no deterministic pairing.

**Minimal correction:** Introduce explicit repeatable load mappings. Each mapping must identify one source record set, group its endpoint or business-key columns, give component order, and state any required filter or join; columns inside different mappings are alternatives, while columns inside one named key are components.

**Confidence:** High.

### 3. A satellite parent cannot be identified deterministically for composite hub or link keys

**Quoted text:** “**Satellite**: `parent`, `source`, `source_table`, `parent_key` (the column of the source table that identifies the parent)”.

**What is wrong:** `parent_key` is singular and has no mapping from ordered source components to the parent's business-key or link-endpoint components. Link parents inherently require all endpoint keys, and hubs may have composite business keys. The generator therefore cannot calculate the parent hash key without guessing.

**Concrete failure case:** Declare a link `lnk_order__line` whose endpoints are order `(OrderID)` and line `(OrderID, LineNumber)`, then declare a payload satellite with `parent: lnk_order__line`, `source_table: Sales.OrderLines`, and `parent_key: OrderID`. Rows 42/1 and 42/2 receive the same parent key, so the generated satellite attaches both payloads to one link identity. Setting `parent_key: LineNumber` merely collides across orders; the format cannot declare both ordered endpoint mappings.

**Minimal correction:** Replace `parent_key` with a parent-key mapping that names every parent component in canonical order; for a link satellite, group components by link endpoint. Validate the mapping against the parent's declared load mapping.

**Confidence:** High.

### 4. Effectivity and status generation lack the record-set semantics needed for correct SQL

**Quoted text:** “**The status-tracking satellite** of every hub loaded from a full extract” and “**The effectivity satellite** of every link ... whose start is declared on the link.”

**What is wrong:** A source-level `extract` flag and one link-level `effectivity_start` do not define the scope of absence, the source record set that asserts it, tie-breaking, or which alternative link load the date belongs to. Those are decisions, not mechanical consequences of column metadata. Generating end dates or deletion/status rows without them can manufacture business events.

**Concrete failure case:** `Sales.Customers` is a full extract filtered to active region `NL`, while yesterday's extract contained customer 17 and today's does not. The source declaration can still say `extract: full`, so the generated status tracker marks customer 17 inactive even if it merely moved to another region. Similarly, a link loaded from both `Orders` with `effectivity_start: OrderDate` and a CRM snapshot with no event date has only one link-level setting; applying `OrderDate` to both is impossible, while substituting load time for CRM is an undeclared guess.

**Minimal correction:** Put status and effectivity policy on each explicit load mapping: snapshot population/scope identity, presence key, deletion evidence or absence contract, start-event expression, ordering/tie-break rule, and late-arrival/end-dating rule. Generate these satellites only when that mapping is complete.

**Confidence:** High.

### 5. References by mutable names do not provide stable identity under rename

**Quoted text:** “`name` is the table's name and may change; a renamed object keeps its id and records the earlier name under `aliases`. Other files refer to an object by its name, which the checker resolves.”

**What is wrong:** The stable identifier exists but is not used for references. Correct resolution then depends on aliases being globally unique and reserved forever, neither of which is stated. A later object can acquire an old name, making an unchanged declaration ambiguous or silently retargeted. Source-table and source-column references have no stable identifiers at all.

**Concrete failure case:** `hub_party` is renamed to `hub_customer` and retains `aliases: hub_party`; a new, distinct hub is then created with `name: hub_party`. An existing satellite with `parent: hub_party` can resolve to the new hub by current name, or become ambiguous, even though its text did not change. The analogous rename of `Sales.Customers.CustomerID` makes the checker report one forgotten new column and one missing old column, but it cannot establish continuity.

**Minimal correction:** Store object references by immutable `id`, retaining names and aliases only for display and migration diagnostics. Assign immutable catalogue IDs to source tables and columns and reference those IDs from mappings; require aliases to be globally reserved if name-based input remains accepted as shorthand.

**Confidence:** High.

VERDICT: FAILS [the exactly-once column rule rejects necessary reuse of source keys across hub and link loads].

## Dispositions

1. **Accepted in substance.** The first version declared only the named end of a link and left the driving end
   implicit, so a link that declared both would have failed the check. Every link mapping now declares both ends
   (`end=from`, `end=to`), and the check gives every column one disposition with the reuse each disposition implies:
   a business key is also the `from` end of the hub's links and the key of its satellites (README section 6 item 4).
   The finding's example, a column used as hub key and link endpoint, now passes; a column in two satellites still
   fails.
2. **Accepted.** A hub's *Business key* line is one mapping, lines are alternatives, and a composite key is one line
   joined by ` + `; a link's mapping is the pair of lines from one source table, exactly one `from` and one `to`, each
   with as many parts as its hub's key, checked. Joins and filters within a mapping are not provided for: no WWI
   mapping needs one, and they would come with the first source that does.
3. **Accepted.** `parent_key` lists every part of the parent's key in key order, and `from=…, to=…` for a link parent;
   the number of parts is checked for hub parents. WWI has neither a composite key nor a link satellite yet.
4. **Partly accepted.** Accepted: completeness is declared per table (`extract=full` or `delta`) rather than per source,
   status tracking is generated only for full tables, and the start of effectivity moves to the mapping's `from` line
   so that a second mapping can have its own. Not accepted for now: ordering, tie-breaking and late arrival are
   recorded under `ARC-OP-29` as owed by the generator's design, since the format cannot be tested on them before a
   generator exists; absence is already governed by 127 and 149 Rule 7.
5. **Partly accepted.** References stay by name, which people and agents read, and the check now forbids reusing any
   name or alias across the model and fails a reference to an alias, which removes the silent retargeting of the
   failure case. Source columns keep their qualified names; a source rename is a change of source contract and shows
   as one column missing and one new, which is the wanted behaviour until continuity is evidenced.
