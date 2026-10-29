---
id: nsdn:rv:sat:cold_room_sensor__wwi__reading
kind: satellite
name: sat_cold_room_sensor__wwi__reading
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.7
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_cold_room_sensor
source: wwi
source_table: Warehouse.ColdRoomTemperatures
parent_key: Warehouse.ColdRoomTemperatures.ColdRoomSensorNumber
satellite_kind: reading
split_reason: delivery (a reading series: one row per reading, Rule 10)
valid_time: Warehouse.ColdRoomTemperatures.RecordedWhen
class: open
subject_area: sensors
---

## Columns

- ColdRoomTemperatureID | reading_key=yes
- RecordedWhen
- Temperature

## Evidence

- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/06_keys.md#C1
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/06_keys.md#C2
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C5
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C6
