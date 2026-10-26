# XREV 2026-10-26 — 144 sections 3 and 5: several sources for the same entities; WWI citations — sol

```yaml
object:        docs/10_architecture/144_raw-vault-business-vault-calculation-engines.md §3 and §5, as committed in ad64b5b/68090d3.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch.
assignment:    question 1, assume the six multi-source rules are wrong for a bank with several core systems or after an
               acquisition, up to five modelling errors with failure cases; question 2, check every path#Cn citation in §5
               against the analysis record; the rule-8 hedge, ARC-OP-37's open items and that nothing is built excluded.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 09 on 2026-10-26; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [a migration split loaded as same-as makes two successor accounts equivalent]. Resolved in the revised text,
               unreviewed.
```

## sol's answer, verbatim

# Review of sections 3 and 5

## Question 1

### Finding 1

quote / “Satellites are always per source. The acquired company's customer data gets its own satellite on the same hub.”

what is wrong / A single record source per satellite is a lineage constraint, not a rule that one source maps to exactly one satellite. The proposed rule makes source the only decomposition axis and ignores different grains, rates of change, confidentiality classes and descriptive contexts within one core system.

failure case / An acquired core supplies stable KYC identity attributes, frequently changing AML risk scores and specially restricted tax identifiers for the same customer. Putting all three in `sat_customer__acquired_core` produces a new full satellite version for every risk-score change and forces consumers with access to ordinary customer descriptions into the same security boundary as tax identifiers.

correction / Require every satellite row set to have one declared record source, but allow several satellites for that source when grain, change rate, security or semantic context differs. State the satellite grain and historisation rule explicitly; do not infer “one source, one satellite” from source isolation.

confidence / high

### Finding 2

quote / “Two sources share a hub key only when their keys are the same identifier with the same meaning.”

what is wrong / “Same identifier” and “same meaning” omit the identifier's issuer, namespace, business-key grain and valid-time scope. Equal values with equally named meanings are not enough to justify a shared raw-vault identity, while a source code added indiscriminately can also split a genuinely governed enterprise identifier into permanent source-local identities.

failure case / Two acquired banks both have `AccountNumber = 00012345`, and in both systems the field means “deposit-account number.” The numbers were issued independently. A hash based only on the value and semantic label merges two customers' accounts; a policy that instead always includes source creates two hub identities when both systems are replicas of the same issuer-governed account number.

correction / Define the canonical business-key composition per hub, including issuer or namespace and grain, and document when that namespace is shared across systems. Qualify local keys by their issuing key space; omit source qualification only when evidence establishes a common governed namespace. Relate distinct keys later without rewriting the raw identities.

confidence / high

### Finding 3

quote / “Links are shared only for the same declared relationship. A relationship that only one system holds gets its own link.”

what is wrong / Whether only one source currently supplies relationship instances does not define a different relationship type. Creating a source-specific link for source exclusivity confuses provenance with business grain and guarantees structural fragmentation when another core later supplies the same relationship.

failure case / At acquisition, only the acquired core records the relationship between a customer and an authorised account signatory, so the design creates `lnk_customer_signatory__acquired`. Six months later the incumbent core starts sending the same customer-signatory relationship. Loading it into a second link prevents one raw relationship history and makes duplicate or conflicting assertions visible only through downstream union logic.

correction / Define a link by the participating business keys, relationship semantics and grain. Load semantically identical assertions from any source into that link with record-source metadata and, where attributes or status must be historised, source-aligned link satellites. Use separate links only for genuinely different relationships or grains.

confidence / high

### Finding 4

quote / “That customer 42 in A is customer 9137 in B, concluded from name, date of birth, address or a national identifier, is a judgement with a confidence; it becomes a same-as link with its evidence, adjudicated and not generated.”

what is wrong / The phrase “adjudicated and not generated” collapses proposal, decision and publication into one state and makes large-scale identity resolution operationally impossible. A generated candidate is not yet an authorised equivalence, but generation is a valid way to produce candidates; adjudication must be represented as a separate, historised decision rather than as a ban on generated links.

failure case / A bank acquisition introduces eight million customer records. A deterministic match on a verified national identifier can propose millions of high-confidence pairs, while fuzzy name-and-address matches need review. If no generated candidate relation may exist, reviewers have no durable queue or evidence trail; if generated output is loaded directly as same-as, a false fuzzy match contaminates every integrated customer exposure report.

correction / Persist generated match candidates separately with rule version, evidence, confidence and run time. Persist adjudication decisions, overrides and their valid/effective periods separately. Publish only the policy-authorised subset as resolved identity, while retaining rejected and superseded candidates for audit and reprocessing.

confidence / high

### Finding 5

quote / “A migration's old-to-new number table is a fact delivered by a system, not an inference of ours, and loads into the raw vault as a same-as link.”

what is wrong / A delivered crosswalk is raw evidence, but its relationship is not necessarily identity equivalence. Migrations contain replacements, consolidations, splits, product conversions and technical row mappings. Labelling every old-to-new pair `same-as` asserts symmetry and transitivity that the source table may not claim.

failure case / During a core migration, one joint mortgage account is split into two successor servicing accounts, so the crosswalk has one old number mapped to two new numbers. Loading both rows as same-as makes the two successor accounts equivalent to each other through the old account. An integrated exposure view then collapses two live contracts and can undercount balances or attach payments to the wrong contract.

correction / Load the delivered crosswalk in the raw vault with its source-defined relationship type, cardinality, migration event, effective dates and provenance. Treat it as same-as only when the source contract establishes one-to-one identity preservation; otherwise model replacement, split, merge or technical translation explicitly and let the business vault derive the permitted integrated view.

confidence / high

## Question 2

### Finding 6

quote / “because WWI's keys are integers the database assigns (`analysis/wwi/tables/Sales/Orders/06_keys.md#C1`)”

what is wrong / C1 establishes only that `Sales.Orders.OrderID` is an `int` primary key described as a numeric ID used within the database, with no other unique constraint on that table. It does not establish that the database assigns `OrderID`, and it cannot support the plural claim that WWI's keys generally are assigned integers.

failure case / A different WWI hub candidate may use a text or externally issued business key, or an integer supplied by an upstream system rather than generated by this database. C1 contains no observation about that key, yet the sentence would require adding a key-space code to it on the strength of the Orders claim.

correction / Narrow the sentence to `Sales.Orders.OrderID` and remove “the database assigns” unless identity/default/catalogue evidence establishes assignment. Cite corresponding key claims for every other WWI business key before generalising to all hub keys.

confidence / high

### Finding 7

quote / “whether they are known outside the database is not established (`#C7`)”

what is wrong / C7 says only that whether `OrderID` appears on documents sent to customers is not established. It does not support “they,” whose antecedent is “WWI's keys,” and it does not test other external channels or other keys.

failure case / `OrderID` may indeed be unverified externally while an invoice number, customer account number or stock-item code is printed on documents and governed outside the database. Applying C7 to all keys would incorrectly treat those externally meaningful identifiers as source-local collision risks.

correction / Say “whether `OrderID` is shown on documents sent to customers is not established,” or obtain and cite evidence for the external visibility and issuing scope of each proposed hub business key.

confidence / high

VERDICT: FAILS [a migration split loaded as same-as makes two successor accounts equivalent]

## Dispositions

1. **Accepted.** Every satellite has exactly one source; one source may fill several satellites.
2. **Accepted.** Each hub declares its key composition (identifier, issuer or namespace, grain); the key-space code
   names the issuer, not the system; leaving it out needs evidence of a common governed namespace.
3. **Accepted.** A link is defined by its keys, meaning and grain, not by its source.
4. **Accepted.** Proposal, decision and publication are kept apart, per ADR-0011; generated candidates are allowed and
   stored with their evidence, and only the authorised subset is published.
5. **Accepted.** A delivered crosswalk loads with the relationship the source states; same-as only for one-to-one
   identity.
6. and 7. **Accepted.** The §5 sentence is narrowed to `Sales.Orders.OrderID` and what #C1 and #C7 actually say; the
   other keys are said to be integer identifiers of unestablished issuing scope.
