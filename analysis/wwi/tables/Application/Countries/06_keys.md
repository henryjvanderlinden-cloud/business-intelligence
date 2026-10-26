---
id: wwi:object:1461580245
subject: wwi/tables/Application/Countries
item: 06
topic: keys
tier: minimum
summary: Primary key unique and gapless; CountryName and FormalName are each declared unique.
confidence: medium
claims: 6
written_by: claude-opus-5-5
written_at: 2026-10-20T08:31:00Z
step: S08-095
method: mechanical claims by prototypes/information_analysis/write_dossiers.py from the evidence of profile_tables.py and evidence_shared.py; judgement claims (type intended, or interpretations) by claude-opus-5-5 reading that evidence; script blobs: write_dossiers.py ee7ed532e7ed7d38cce305ca07736b31a32cabaf, profile_tables.py a03f3066fca3634fb4f03bdc6b7c5672e6faf621, evidence_shared.py 4174839b1036cd70f0c837acdee322e7071ca4b0; C5 added 2026-10-26 by claude-opus-5-5 in step S10-003 from evidence_versions.py (blob cbe6cce7ec5676092c3eecfa4110fe576c205b43) on the extract of 2016-06-02; C6 added 2026-10-26 by claude-opus-5-5 in step S10-003 from evidence_codes.py (blob 19e1e69420e2cdd1e9e6bf4b08141fe2ec504802) on the extract of 2016-06-02
input_source: wwi
input_extract: 2016-06-01
input_manifest_sha256: 35b71b2e3ff4bb9ef4e24afc9c56f914e8386df4060a794b862e7f5a00d2774f
input_schema_sha256: 4840337d7b437a1e0ba71ae6b072f3f504e276f802274f763ad925b52a0bcc05
last_checked_at: 2026-10-20T08:31:00Z
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

- C1 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f3e79ea442f46838 | recheck=a unique constraint changes | text: Declared unique besides the primary key: UQ_Application_Countries_CountryName (CountryName); UQ_Application_Countries_FormalName (FormalName).
- C2 | type=observed | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f4e8a61674553cd9 | recheck=the key range changes | text: The key runs from 1 to 241 with 51 unused numbers.
- C3 | type=declared | status=proposed | confidence=high | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f3e79ea442f46838 | recheck=a foreign key changes | text: 1 declared foreign key, all enabled and trusted: LastEditedBy -> Application.People.PersonID.
- C4 | type=intended | status=proposed | confidence=medium | effective=2016-06-01 | observed=2026-10-18 | checked=2026-10-18 | evidence=f3e79ea442f46838 | recheck=every new extract, or a schema change | text: Business key candidate: the unique name (CountryName and FormalName are each declared unique); the numeric key is the source's surrogate.
- C5 | type=observed | status=proposed | confidence=high | effective=2016-06-02 | observed=2026-10-26 | checked=2026-10-26 | evidence=6f99d13cc9e8ab85 | recheck=every new extract, or a schema change | text: Across the 227 versions of 190 CountryID values held in the extract (current and history table together), CountryID persists, and the columns whose value differs between the versions of one key are, with the number of keys concerned: CountryName (1); FormalName (1); LastEditedBy (35); LatestRecordedPopulation (35); ValidFrom (36); ValidTo (36). The declared-unique CountryName was changed for 1 key while CountryID stayed the same: the name is unique at any moment but not constant over time.
- C6 | type=observed | status=proposed | confidence=medium | effective=2016-06-02 | observed=2026-10-26 | checked=2026-10-26 | evidence=a1aa88207164a0fd,ba3bd2eccde7a2db | recheck=every new extract, or a schema change | text: All 190 countries carry an (IsoAlpha3Code, IsoNumericCode) pair that appears in the ISO 3166-1 list of 249 current codes as read on the web on 2026-10-26; no code lies outside it. The list was obtained through a summarising fetch and not checked against the page by hand.

## Reasoning

Mechanical claims follow the confidence rules of analysis/README.md section 5; judgement claims are the writer's reading of the evidence.

## Uncertainties

None.

## For a person

None.
