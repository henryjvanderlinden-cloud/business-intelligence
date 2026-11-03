# XREV 2026-11-03 — the vault generator (143) — sol

```yaml
object:        docs/10_architecture/143_the-vault-generator.md, first draft (copied to scratch/143_draft1.md; uncommitted).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; answer written to the ignored scratch/ folder with apply_patch; confined to the one
               file, it wrote in about 3 minutes.
assignment:    assume an experienced Data Vault 2.0 practitioner who has built and run metadata-driven vault generators
               in production rejects the note, judged against the standard: buildable without guessing; loads
               deterministic, idempotent and append-only; exact reconstruction by source version, first day and ties
               included; nothing silently lost or duplicated; no batch visible half-loaded. Up to five findings with
               failure cases; naming, folder layout, SHA-256 over MD5, business vault and marts excluded; praise,
               summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 12 on 2026-11-03; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [late arrivals can make later source-version reconstruction incorrect].
               All five findings applied in the revised text (143 §5, §6, §8, §10), unreviewed.
```

## sol's answer, verbatim

## 1. A late arrival can make every later reconstruction wrong

> “A late arrival … is inserted like any other … and compared with the version before it in source order. Nothing already loaded is changed.”

This is not sufficient for a change-only satellite. Inserting a version between two previously processed versions can change whether the later version must have a satellite row. Because the design never revisits that later version, forward-filling the satellite can produce a state the source never had.

Concrete failure: on day 1 the source delivers versions `(t1, colour='red')` and `(t3, colour='red')`. The payload satellite inserts only `t1`, because `t3` does not differ from its then-known predecessor. On day 2 a late version `(t2, colour='blue')` arrives. The generator inserts `t2` because it differs from `t1`, but does not insert or amend `t3`. Reconstructing the row at source version `t3` now forward-fills `blue`; the source row at `t3` was `red`.

## 2. A failed partial batch can preserve bad rows and later publish them

> “A failed build can leave a part of a batch in the working warehouse … and the rerun after a fix completes the batch without duplicates, because every model inserts only what is not yet there.”

“Not yet there” prevents a corrected model from replacing a row inserted by the failed run. Append-only recovery therefore works only when the retry uses exactly the same transformations and the failure occurred after correct inserts. The note gives no batch-scoped quarantine, rollback, immutable build database, or validation that pre-existing rows for the failed batch equal the newly computed rows.

Concrete failure: model A inserts source version `(CustomerID=7, source_ts=t1, Name='Acem')`; a later test fails and the batch is not published. The mapping is fixed so the same delivered input should produce `Name='Acme'`. On retry, model A sees `(7,t1)` already present and inserts nothing. The remaining models and tests pass, and the working database is published with `Acem`. The batch is whole by row count but contains output from two generator definitions, and append-only SQL cannot repair it.

## 3. The proposed audit hash does not distinguish every source version

> “Its `hashdiff` includes both [`LastEditedBy` and source system time], so every source version is one row: it is the source's version log.”

Neither field is unique per version. In particular, multiple updates in one SQL Server transaction can have the same `ValidFrom`, and the same user can perform all of them. The note does not say that the audit satellite bypasses change suppression; if it follows the stated satellite comparison rule, an audit version disappears. If it always inserts versions, the claimed purpose of this hashdiff is false and the generator still needs that distinct rule stated explicitly.

Concrete failure: one key has delivered versions `(source_ts=10:00, source_seq=1, LastEditedBy=4, payload='A')` and `(source_ts=10:00, source_seq=2, LastEditedBy=4, payload='B')`. Both audit hashdiffs are identical. Change suppression retains only sequence 1, so the audit satellite is not a version log and the generated “every source version” test fails on the first load.

## 4. Tie numbering has no defined, object-independent input

> “Among the versions of one key with equal `source_ts`, they are numbered by their end time … then by `hashdiff`.”

> “The staging view … computes … each satellite's `hashdiff`.”

There is no single `hashdiff`: payload, milestone, audit, and other satellites hash different columns, and reading satellites have none. A source version identifier must be assigned once from a canonical, fully specified row representation and reused by every object. The generator otherwise has to guess which hashdiff controls `source_seq`, or can assign the same physical versions different sequence numbers in different satellites.

Concrete failure: two zero-length versions of key 7 have the same `ValidFrom` and `ValidTo`: the first has `(Name='A', LastEditedBy=20)` and the second `(Name='B', LastEditedBy=10)`. Suppose the payload hashes sort A before B while the audit hashes sort editor 10 before editor 20. Independent generation gives payload sequence 1 to A but audit sequence 1 to editor 10. Reconstructing by `(parent key, record_source, source_ts, source_seq)` yields the nonexistent combinations `(A, editor 10)` and `(B, editor 20)`.

## 5. The design knowingly makes exact source-row reconstruction impossible

> “A column declared `load=never` (`HashedPassword`, ADR-0033) is generated as an always-empty column of its type.”

An always-empty projection discards delivered evidence. No side record, digest, rejection record, or explicit reconstruction exception is defined, yet the required reconstruction test says the rebuilt state must equal the source row. The generator cannot both implement this rule and meet exact reconstruction.

Concrete failure: landing contains `(PersonID=42, source_ts=t1, HashedPassword='0xA1B2')`. The generated satellite stores `HashedPassword=NULL`. Reconstruction of version `t1` returns `NULL`, not `0xA1B2`; two delivered versions differing only in `HashedPassword` also become indistinguishable in the vault.

VERDICT: FAILS [late arrivals can make later source-version reconstruction incorrect]
