---
id: wwi:object:1301579675
subject: wwi/tables/Application/People
item: 27
topic: peculiarities
tier: minimum
summary: Several kinds of person in one table (staff, contacts, technical user), told apart by four flags and filled columns; JSON with nested employee data; a computed column derived from JSON.
confidence: high
claims: 10
written_by: claude-opus-5-5
written_at: 2026-10-18T20:32:00Z
step: S08-061
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py 102dceeb7d85ec3db493afa75ff1e907c8b3f3a6, profile_tables.py e61ada2547265905e3558722cd127e81fa5cd770, evidence_shared.py 03d3dfbc0522d76aef793a33dc2bc491abc70529
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 5f24e9163953099bd97211216302ba9edbe184de9237880789cd61681982e529
last_checked_at: 2026-10-18T20:32:00Z
last_checked_by: claude-opus-5-5
last_checked_against: 2016-06-01
reviewed_by: none
reviewed_at: none
ruled_by: none
ruled_at: none
supersedes: none
superseded_by: none
recheck_when: every new extract, or a schema change
---

## Claims

- C1 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the empty-column patterns change | text: Test 8: 5 distinct patterns of empty columns; the most common: 929 rows with HashedPassword, UserPreferences, Photo, CustomFields, OtherLanguages empty; 138 rows with Photo, CustomFields, OtherLanguages empty; 24 rows with HashedPassword, Photo, CustomFields, OtherLanguages empty.
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the pattern changes | text: Test 8, by IsEmployee (partial): IsEmployee=0 (1,092 rows): empty CustomFields, OtherLanguages; filled -; partly empty HashedPassword (954 empty), UserPreferences (929 empty), PhoneNumber (1 empty), FaxNumber (1 empty), EmailAddress (1 empty) | IsEmployee=1 (19 rows): empty -; filled HashedPassword, UserPreferences, PhoneNumber, FaxNumber, EmailAddress, CustomFields, OtherLanguages.
- C3 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the pattern changes | text: Test 8, by IsPermittedToLogon (partial): IsPermittedToLogon=0 (956 rows): empty -; filled -; partly empty HashedPassword (954 empty), UserPreferences (929 empty), PhoneNumber (1 empty), FaxNumber (1 empty), EmailAddress (1 empty), CustomFields (954 empty), OtherLanguages (954 empty) | IsPermittedToLogon=1 (155 rows): empty -; filled HashedPassword, UserPreferences, PhoneNumber, FaxNumber, EmailAddress; partly empty CustomFields (138 empty), OtherLanguages (138 empty).
- C4 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the pattern changes | text: Test 8, by IsSalesperson (partial): IsSalesperson=0 (1,101 rows): empty -; filled -; partly empty HashedPassword (954 empty), UserPreferences (929 empty), PhoneNumber (1 empty), FaxNumber (1 empty), EmailAddress (1 empty), CustomFields (1,092 empty), OtherLanguages (1,092 empty) | IsSalesperson=1 (10 rows): empty -; filled HashedPassword, UserPreferences, PhoneNumber, FaxNumber, EmailAddress, CustomFields, OtherLanguages.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the pattern changes | text: Test 8, by IsSystemUser (partial): IsSystemUser=0 (1,072 rows): empty CustomFields, OtherLanguages; filled -; partly empty HashedPassword (936 empty), UserPreferences (929 empty), PhoneNumber (1 empty), FaxNumber (1 empty), EmailAddress (1 empty) | IsSystemUser=1 (39 rows): empty -; filled UserPreferences, PhoneNumber, FaxNumber, EmailAddress; partly empty HashedPassword (18 empty), CustomFields (20 empty), OtherLanguages (20 empty).
- C6 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=a row breaks a dependency | text: Test 1: 23 functional dependencies between non-key columns over the whole extract (0 involving audit columns, a batch-edit signature, not listed): LogonName -> IsPermittedToLogon; LogonName -> IsEmployee; LogonName -> IsSalesperson; LogonName -> CustomFields; LogonName -> OtherLanguages; HashedPassword -> IsPermittedToLogon; HashedPassword -> LogonName; HashedPassword -> IsEmployee; HashedPassword -> IsSalesperson; HashedPassword -> CustomFields; and 13 more in the evidence.
- C7 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=the structured columns change | text: Test 6: UserPreferences holds JSON in 182 rows, 182 of which parse; CustomFields holds JSON in 19 rows, 19 of which parse; OtherLanguages holds JSON in 19 rows, 19 of which parse.
- C8 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=a column is added | text: Test 16: no column name ends in a digit.
- C9 | type=intended | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=419f7b85d80b0191 | recheck=every new extract, or a schema change | text: Test 8, subtypes: employees have CustomFields, logon and password; customer and supplier contacts have contact details but mostly no logon; the technical user has nothing. What a row means depends on its kind.
- C10 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=3654cc5be0d96b13 | recheck=the description changes | text: OtherLanguages is described as computed from CustomFields, and SearchName as computed: derived columns (item 9).

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
