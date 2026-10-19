# XREV 2026-10-18 — round-1 dossiers of Warehouse.ColdRoomTemperatures and its history table — sol

```yaml
object:        analysis/wwi/tables/Warehouse/ColdRoomTemperatures/ and Warehouse/ColdRoomTemperatures_Archive/, as committed on 2026-10-18 (5cf9db1).
reviewer:      gpt-5.6-sol, via the Codex MCP server on the author's desktop, reasoning effort medium, workspace-write
               sandbox, answer written to the ignored scratch/ folder; brief restricted to Markdown and JSON after an
               earlier single pass over more tables never arrived. Run in parallel with a second sol pass.
assignment:    against ADR-0017 (hard effort, no guessing, confidence supported by the cited evidence) and ADR-0020
               (describe the as-is): up to three false or overstated claims; up to two unsupported confidences or
               guesses; any design advice or future decision. 350 words; praise, summary and general assessment forbidden.
second reader: assignment set by Claude Opus 5.5, which wrote the dossiers' judgement claims and the generator of their
               mechanical claims.
verdict:       FAILS [the history table's versions called readings on catalogue evidence only]
```

Sol's answer, verbatim:

1. Claims false or overstated against their cited evidence:

- `analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C5`: `d661ae2a5f707ded` shows only four current rows, all with `RecordedWhen=2016-06-01T23:59:29`; it contains no archive data and cannot establish that those rows' earlier readings are archive versions.
- `analysis/wwi/tables/Warehouse/ColdRoomTemperatures_Archive/05_role.md#C4`: `fe99989aa94f128c` establishes 3,676,804 rows, 3,676,804 distinct first-column IDs, and column ranges. It does not establish that each row is an earlier version of the current table or that `ValidFrom`/`ValidTo` delimit when it was current; those are uncited temporal-semantics assertions.
- `analysis/wwi/tables/Warehouse/ColdRoomTemperatures_Archive/05_role.md#C6`: `a3812e9428769e55` establishes `HISTORY_TABLE`, schema metadata, and row count. It does not show that every version is a temperature reading, that the data cover four sensors, or the asserted reading interval. In particular, no value profile is cited here.

2. Unsupported confidence or guessing:

- `analysis/wwi/tables/Warehouse/ColdRoomTemperatures/06_keys.md#C2`: `confidence=high` is unsupported. One extract shows sensor numbers unique; one PK-based transition shows all IDs replaced. Neither tracks sensor numbers across the transition or supplies a declared identity rule. “Stable identity” is therefore guessed; the item should state that uncertainty and what longitudinal or source evidence would settle it.
- `analysis/wwi/tables/Warehouse/ColdRoomTemperatures/19_sensitivity.md#C2`: `confidence=high` is unsupported by catalogue metadata alone. Empty descriptions and names such as `Temperature` support an inferred technical-telemetry reading at low confidence, not high.

3. `analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C6` says, “For analysis the history table is the event table.” That prescribes an analytical role/model choice rather than describing only the as-is, contrary to ADR-0020. The factual latest-state observation can remain separately.

VERDICT: FAILS — counterexample: `ColdRoomTemperatures_Archive/05_role.md#C6` calls every history version a reading on evidence that establishes only catalogue history-table status.

## Dispositions

All six findings accepted and fixed on 2026-10-19 (step S08-066):

1. **Earlier readings in the history table** (03 C5), 2. **versions and periods** (Archive 05 C4) and 3. **every version
   a reading** (Archive 05 C6). A new evidence (832defd8d73a4d23), written into both tables, profiles the history
   table: 919,201 rows for each of sensors 1 to 4, RecordedWhen from 2015-12-20 to 2016-06-01 23:59:20, ValidFrom equal
   to RecordedWhen in all 3,676,804 rows, ids 1 to 3,676,804 directly below the current 3,676,805 to 3,676,808, and the
   same four sensors with new ids on both extract days. 03 C5 and Archive 05 C6 cite it and state those counts; the
   history-table template (all 16 history tables) now cites the profile next to the catalogue for its version claim.
4. **Sensor as stable identity** (06 C2): lowered to medium, restated as an observation over two extracts with no
   declared rule, citing the new evidence.
5. **Technical telemetry** (19 C2): lowered to low, stated as a reading from the column names.
6. **"For analysis the history table is the event table"** (03 C6): design advice against ADR-0020; replaced by the
   as-is statement "This table holds only the latest state of each sensor; the earlier readings are in the history
   table."
