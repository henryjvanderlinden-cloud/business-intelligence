# XREV 2026-10-29 — 149: the satellites of Wide World Importers — sol

```yaml
object:        docs/10_architecture/149_wwi-satellites.md §2 to §5, as committed in bbd82b4.
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write sandbox,
               no browsing; answer written to the ignored scratch/ folder with apply_patch; confined to the note, it
               wrote in about 2 minutes.
assignment:    assume a Data Vault 2.0 and bitemporal practitioner rejects the rules, splits, valid-time assignments,
               effectivity, reference tables and loading; up to five findings with failure cases, testing change
               detection without source system time, split satellites against point-in-time reconstruction, the
               multi-active vehicle readings, status tracking and the first-day history load; nothing built, access
               rules, the hub and link lists, hashing and time zones excluded; praise, summary and general assessment
               forbidden. Because the reviewer read only the note, its citations were not checked against the record.
second reader: assignment set by Claude Opus 5.5, which drafted the object in session 10 on 2026-10-29; the revisions
               made in response are unreviewed by construction.
verdict:       FAILS [two readings for the same vehicle and sensor in one daily batch collide at the proposed
               multi-active satellite grain]. Resolved in the revised text, unreviewed.
```

## sol's answer, verbatim

1. **Quoted text:** “The payload satellites detect change on their payload and business valid time only … so that an edit that changed nothing visible … adds a row to the audit satellite and none to the others.”

   **What is wrong:** Source-system time is one of the asserted temporal axes, but it is not part of the payload-satellite version identity. An audit-satellite row proves that some source version existed; it does not make a payload row addressable at that source version. This loses the distinction between “the value was asserted again at a later source-system time” and “no new assertion occurred,” and makes reconstruction depend on an undocumented temporal join from the audit satellite to every independently changing payload satellite. Excluding `LastEditedBy` from a business hashdiff is reasonable; excluding the source-version discriminator from the insert key is not.

   **Concrete failure case:** Extracted history for customer 42 contains `(ValidFrom=10:00, CreditLimit=1000, LastEditedBy=7)` and `(ValidFrom=11:00, CreditLimit=1000, LastEditedBy=9)`. The credit satellite contains only the 10:00 assertion, while the audit satellite contains both. A query for “payload versions asserted by the source between 10:30 and 11:30” returns no credit row, although the source asserted a version at 11:00. Joining by warehouse load time cannot repair this on the first load because both source versions have the same knowledge time.

   **Minimal correction:** Keep audit attributes out of the business hashdiff, but give every source version a stable source-version discriminator (for example, record source plus `ValidFrom`) and carry it in every satellite populated from that version. Define insertion and as-of joining on that discriminator; optionally suppress repeated payload storage only through an explicit assertion-to-payload mapping.

   **Confidence:** High.

2. **Quoted text:** “a satellite holds what one source row asserts about one hub or link, and splits only for a stated reason” and “Every satellite filled from one source row carries the same load time and batch.”

   **What is wrong:** Equal load time and batch do not preserve the identity of a split source-row version. The proposed satellites change independently and sometimes use different or unknown valid-time assignments, but no common source-row-version key or deterministic point-in-time join rule is specified. A PIT query can therefore combine attributes that were never co-asserted by the source, especially after historical rows have been backloaded under one knowledge timestamp.

   **Concrete failure case:** A supplier source row is `(name=A, address=X, bank=B1)` at source time 10:00; at 11:00 only the bank becomes `B2`; at 12:00 only the address becomes `Y`. All three versions are learned in the first batch. Selecting the latest row from each split satellite by load time is tied, and an implementation may return `(A, X, B2)` for source time 12:30 or `(A, Y, B1)` for 11:30—neither is the required source-row image for that instant.

   **Minimal correction:** Add a shared source-row-version identifier to every split satellite row and specify the PIT algorithm: for each component, choose the latest assertion for the same business key whose source-system interval contains the requested instant. Where a field has its own business-valid time, model that assertion separately rather than assigning one ambiguous valid time to a mixed payload.

   **Confidence:** High.

3. **Quoted text:** “`sat_vehicle__wwi__chiller_reading` … `ChillerSensorNumber (sub-key), VehicleTemperatureID, RecordedWhen, Temperature, IsCompressed` … ‘multi-active, keyed within the vehicle by sensor number’.”

   **What is wrong:** `ChillerSensorNumber` distinguishes simultaneous sensors, not repeated readings from the same sensor. A multi-active satellite at the proposed grain still permits only one active member per vehicle and sensor at a load instant; a daily batch can contain many readings for that pair. Moreover, a reading is an immutable event, not a revision of a vehicle description.

   **Concrete failure case:** The daily extract contains vehicle 3, sensor 1 readings `(VehicleTemperatureID=501, RecordedWhen=10:00, 4.1)` and `(502, 10:01, 4.3)`. Both have the same vehicle key, sensor sub-key, load time, and batch. A conventional multi-active satellite key collides, so one row is rejected or overwritten; a 10:00:30 temperature query then returns no reading or the future 10:01 reading.

   **Minimal correction:** Model each reading at event grain, using the immutable `VehicleTemperatureID` (or vehicle, sensor, and `RecordedWhen` if proven unique) as its identity, and load it insert-only. Link it to the vehicle and sensor if those relationships are required; do not use sensor number alone as the multi-active discriminator.

   **Confidence:** High.

4. **Quoted text:** “every hub loaded from a full extract gets a status-tracking satellite … recording in which complete extract the key was present. A key’s absence is recorded as unresolved until … evidence … show[s] a deletion.”

   **What is wrong:** Recording only presence does not record the absence event or its epistemic state. The model cannot distinguish “not yet evaluated,” “absent from a complete extract,” “confirmed deleted,” and “present again.” It also supplies no temporal rule by which an unresolved absence later becomes a deletion without rewriting history.

   **Concrete failure case:** Customer 17 is present on day 1, absent from complete extracts on days 2 and 3, and present again on day 4. A day-3 current-customer query that takes the latest status row sees only day-1 presence and incorrectly returns customer 17. If the loader instead closes presence on day 2 as deletion, the day-4 row looks like a new customer unless reactivation is represented. The proposed rows cannot answer either case correctly.

   **Minimal correction:** Emit a status observation for every key-state transition, including `observed_absent`, with batch/knowledge time and an explicit status such as present, absent-unresolved, deletion-confirmed, and reactivated. Preserve the original absence observation when later evidence confirms deletion, and state the as-of rule used by “current” queries.

   **Confidence:** High.

5. **Quoted text:** “On the first day each system-versioned table loads its history table and its current rows together, in the order of source system time … all carry the first load’s knowledge time and their own source system time.”

   **What is wrong:** Ordering inserts does not distinguish multiple satellite rows that share the same parent key and knowledge/load time. Standard Data Vault satellite uniqueness includes the parent key and load timestamp (with a multi-active discriminator where applicable); backloading several versions under one first-load timestamp causes key collisions or nondeterministic deduplication. Loading history and current together can also load the terminal history/current boundary twice.

   **Concrete failure case:** The history table has product 8 at source times 09:00 (`price=10`), 10:00 (`price=11`), and 11:00 (`price=12`), while the current table repeats the 11:00 version. All four inputs receive first-load time 15:00. A satellite keyed by product and load time accepts at most one; the resulting price history is either truncated or load-order-dependent, and a query as of 09:30 can return 12 instead of 10.

   **Minimal correction:** Deduplicate the history/current boundary by source-version identity and use that identity (or an explicit source sequence) as an additional satellite key for initial backloads while retaining the common knowledge time. Define interval ordering and end dating from source-system time; do not synthesize different knowledge times merely to avoid collisions.

   **Confidence:** High.

FAILS [two readings for the same vehicle and sensor in one daily batch collide at the proposed multi-active satellite grain].

## Dispositions

1. **Partly accepted.** Accepted: every satellite row carries a source-version identifier (record source with source
   system time), shared by all satellites filled from one source version and part of the satellite key (Rule 2), and
   point-in-time reconstruction is defined on it (Rule 10). Not accepted: storing a payload row for every source version
   whose payload did not change. Suppressing unchanged payloads is the standard satellite behaviour; which versions the
   source recorded is answered by the audit satellite, the source's version log, and the state at any instant by the
   latest source version at or before it.
2. **Accepted.** The shared source version and the point-in-time rule of Rule 10 recombine split satellites only into
   states the source held.
3. **Accepted, and extended to the cold-room readings,** which arrive many per sensor per day in the same way: both
   reading series are one row per reading, keyed by the reading's own identifier, inserted once.
4. **Accepted.** Status tracking records present, absent-unresolved, deletion-confirmed and reappeared, keeps the
   absence when a deletion is confirmed, and states the rule for current queries (Rule 7).
5. **Accepted.** The source version keeps the first day's versions apart under one load time; the history table never
   holds the current version (`Sales/Customers_Archive/05_role.md#C5`), and duplicates by source version are removed
   before inserting all the same (section 5).
