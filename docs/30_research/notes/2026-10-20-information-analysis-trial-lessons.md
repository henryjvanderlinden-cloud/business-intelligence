# Lessons of the first information-analysis trial (Wide World Importers sandbox, 2026-10-18 to 2026-10-20)

Written 2026-10-20, session 08, at the close of the analysis stage
([ADR-0022](../../20_decisions/0022-the-analysis-stage-closes.md)), on the author's instruction to write down the
lessons the model proposed. The counts are from `records/steps/S08.jsonl` and from the record under `analysis/wwi/` as
committed that evening. They describe one trial, on a sandbox, by one agent; they are observations, not rules.

1. **Cross-model review carried real weight.** Every one of the 19 cross-model reviews of analysis work in the session
   failed the first version it was given (step log: role `check`, agents gpt-5.6-sol and gpt-6-astra; the twentieth
   check was a syntax parse of two scripts, not a review). The findings seldom overturned a count. They narrowed what
   the claims said. Of the 11 defect entries recorded on the rework steps that followed these reviews (an entry may group
   several findings), 9 are *overreach* - a reading presented as an observation, a formula or a mechanism called the
   source's rule because the data fit it, a comparison that could not fail, a link cited for more than it says. The other
   2 are counting errors (self-references counted as roles with a too-loose update test; distinct ratios counted after
   rounding), and counting errors also sit inside some overreach entries (rows confused with key-filled rows). Without the
   reviews these would have stood in the record at high or medium confidence.

2. **The author's distortion principle reaches beyond links.** It was stated for the graph of item 29 - "be cautious and
   sensitive to excluding attributes etc. that give a distorted picture of reality" (ADR-0021) - and turned out to apply
   to behaviour as well: an audit or system-time column written on every row made `Application.People` look updated
   daily and `Warehouse.StockItemHoldings` look updated on every row, when no business value had changed on People and
   one or two items' quantities had not changed on Holdings. Behaviour is now judged on business columns, and the
   updated columns are recorded by name.

3. **A formula found by looking is a reading until shown otherwise.** Several formulas hold on every row of the extract
   (tax per line, extended price, line profit at current cost, the recommended retail price at a 30 % mark-up with tax,
   the expected purchase price at current cost). One, the recommended retail price, was found by inspecting ratios first,
   and its claim says so; the others were tried because a description or a column name suggested them. That
   a formula holds on every row is observed; that it is the source's rule, and how it behaves when an input changes
   (a cost price, for instance), is not established from one extract.

4. **The items that need people are untested.** Provenance (14), ownership (20) and demand (21), and every confirmation
   of a reading by someone who knows the source, cannot be done in a sandbox that has no owners or users. The method's
   human-facing part is therefore unproven; so is the cost of putting questions to people, which a real source will
   impose.

5. **Generated files must be regenerated after every edit of their inputs.** Once, readings were edited after the
   writer had run, and the files shipped for review still held the earlier text; astra found it. The record holds up only
   if every file is written by its writer from the current evidence and readings, never edited by hand.

6. **The window is short.** The record describes one extract, rechecked against the next day: two transitions, both on
   weekdays, no month or quarter end, no weekend. Everything that rests on behaviour stays at medium confidence, and
   anything that happens rarely (a part payment, a credit note, a cost change, a part receipt) has not been seen at all.

7. **The working arrangement shaped the work.** The shell on the author's desktop runs whole-repository checks in
   minutes and often hits its time limit; the same checker on a copy in the agent's cloud workspace runs in under a
   second. Heavy scripts and checks therefore ran in the cloud on staged copies, and results went back as archives.
   Calls to the reviewers time out at the device bridge by design and their answers are read from files; a broad brief
   to sol sometimes produced no answer, a narrower one did.
