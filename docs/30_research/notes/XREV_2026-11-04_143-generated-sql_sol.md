# XREV 2026-11-04 — the vault generator (143, revised) and five generated files — sol

```yaml
object:        docs/10_architecture/143_the-vault-generator.md as committed in 0b89d59 (revised after the first review,
               with section 13), followed by five generated files (stg_wwi__application__people,
               sat_sales_order__wwi__picking, eff_sales_order__picker__wwi, sts_sales_order__wwi, hub_sales_order),
               bundled as scratch/REVIEW_143b.md.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, no browsing; answer written to the ignored scratch/ folder with apply_patch; confined to the one
               file. A first call never started on the desktop; the second wrote in about 3 minutes.
assignment:    assume an experienced Data Vault 2.0 practitioner who has built and run metadata-driven vault generators
               in production rejects it, judged against the standard: the SQL does what the note says; loads
               deterministic, idempotent, append-only for every published batch; exact reconstruction by source version,
               zero-length and tied versions included; nothing silently lost or duplicated; no batch visible half-loaded;
               a failed batch leaves nothing after its retry. Up to five findings, defects in SQL preferred; naming,
               layout, SHA-256, performance at scale, business vault and marts excluded; praise, summary and general
               assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which drafted the note and wrote the generator in session 12; the
               revisions made in response are unreviewed by construction.
verdict:       FAILS [a failed rebuild of an already-successful date can leave stale rows that its retry publishes].
               Findings 1, 2, 4 and 5 fixed in the generator and 143 section 13; finding 3 answered in 143 section 6 as a
               stated assumption with a loud failure. Unreviewed.
```

## sol's answer, verbatim

## 1. A failed rebuild of an already-successful date is not cleaned up

> `delete from {{ this }} where batch_id = 'wwi:{{ var('load_date') }}' and not exists (select 1 from nsdn_meta.load_log where load_date = cast('{{ var('load_date') }}' as date) and status = 'ok')`

The cleanup predicate confuses a successful earlier build of a date with success of the current build attempt. Section 8 explicitly says that the runner rebuilds the latest successful date after a project change, so an `ok` row for that date already exists before the rebuild starts. If that rebuild fails after inserting rows, its retry will not delete them. The satellite SQL then makes them immutable with `where c.stored_hd is null`, even if the generator or declaration was fixed between attempts.

Concrete failure: `2016-06-02` was published successfully and has an `ok` load-log row. A newly generated satellite is then added. Its first rebuild inserts `(order=1, source_ts=t1, hashdiff=Hbad, PickingCompletedWhen='2016-06-03')`, after which a later test fails. The model is corrected so the same source version should be `(Hgood, NULL)`. On retry, the pre-hook sees the old `ok` row and leaves `Hbad`; `stored_hd` is non-null, so the corrected row is not inserted. The retry can publish a row from the failed attempt, contrary to “a failed batch leaves nothing after its retry.”

## 2. Staging silently collapses distinct, identical source versions

> `qualify row_number() over (partition by "PersonID", row_hash, "ValidTo" order by _is_history) = 1`

This treats multiplicity as a delivery duplicate without possessing a source-version identifier that can prove it. Two genuine SQL Server history versions can be identical in every delivered column: for example, two no-op updates in one transaction can both produce zero-length rows with the same `ValidFrom`, `ValidTo`, key and payload. They are distinct source events, but this partition retains only one. That directly contradicts keeping every delivered zero-length version and makes exact reconstruction by source version impossible.

Concrete failure: the archive delivers two rows `(PersonID=7, FullName='Ada', ValidFrom=t, ValidTo=t, all other columns equal)`, representing two updates, plus the current row `(7, 'Ada', t, 9999-12-31...)`. The `hashed` CTE reduces the two archive rows to one. Staging consequently assigns only two sequence numbers and the audit satellite records two versions, although three rows and three source versions were delivered.

## 3. `source_seq` is renumbered when a tied late version arrives

> `row_number() over (partition by "PersonID", source_ts order by source_end nulls last, row_hash) as source_seq`

> “The numbering is stable from day to day”

The number is recomputed from the contents of each full extract, not assigned permanently. A late row with the same `source_ts` and `source_end` can sort before an already-loaded row by `row_hash`, shifting every following sequence number. Because `(record_source, source_ts, source_seq)` is then treated as the immutable source-version identity, the loader either reports a false history rewrite or joins new rows to the wrong old versions.

Concrete failure: day 1 delivers key 7 with zero-length version A `(ValidFrom=t, ValidTo=t, row_hash=80...)` and current version C `(ValidFrom=t, ValidTo=9999..., row_hash=40...)`; they receive sequences 1 and 2. Day 2 additionally delivers late zero-length version B `(ValidFrom=t, ValidTo=t, row_hash=10...)`. The new order is B=1, A=2, C=3. Audit already says sequence 1 is A and sequence 2 is C, so B collides with A and A collides with C as “same source version, different content”; the legitimate late delivery cannot load as the note promises.

## 4. The source period end is never persisted

> “`ValidTo` is not part of the source version, so a version whose end has since been set is still recognised as the same.”

> `-- row_hash covers every delivered column except the end of the source's validity period`

Although staging retains `source_end`/`ValidTo` temporarily, none of the shown raw-vault inserts persists it, and a later closure is deliberately treated as the already-loaded version. The final source row therefore cannot always be reconstructed exactly. Deriving an end from the next version does not cover deletion, and status knowledge time is not the source system's period end.

Concrete failure: day 1 delivers current row `(PersonID=7, ValidFrom=10:00, ValidTo=9999-12-31...)`. At source time `14:37:12.1234567` it is deleted. Day 2 delivers only the archive row `(7, 10:00, 14:37:12.1234567)`. Its row hash and source identity equal day 1's, so no new audit or payload row records the closure; status records only absence on day 2. The vault cannot recover the delivered `ValidTo=14:37:12.1234567` for that source row.

## 5. An empty full extract creates an unowned, non-idempotent status row

> `select any_value(load_date) as load_date, any_value(batch_id) as batch_id from {{ ref('stg_wwi__sales__orders') }}`

> `cross join batch b`

For an empty staging relation, the aggregate still produces one row, but both values are null. Existing keys are consequently marked absent with null `load_date` and `batch_id`. Such a row is not owned by the current batch, so the pre-hook cannot remove it using `batch_id = 'wwi:<date>'`; it also cannot be ordered reliably as the latest status.

Concrete failure: a non-system-versioned full table contains key 9 on day 1 and is empty on day 2. Day 1 stores `(9, 2016-06-01, 'wwi:2016-06-01', 'present')`. Day 2 emits `(9, NULL, NULL, 'absent-unresolved')`. On a retry, cleanup does not match that row; with the dated `present` row selected as latest by `order by load_date desc`, another null-dated absence can be appended. The same extract has changed the table twice and left rows that no published batch identifies.

VERDICT: FAILS [a failed rebuild of an already-successful date can leave stale rows that its retry publishes]
