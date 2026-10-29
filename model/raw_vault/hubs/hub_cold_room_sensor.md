---
id: nsdn:rv:hub:cold_room_sensor
kind: hub
name: hub_cold_room_sensor
status: accepted
ruled_in: ADR-0029, ADR-0030, ADR-0028
defined_in: docs/10_architecture/147_wwi-concepts-keys-and-business-time.md#3 item 21
written_by: claude-opus-5-5
written_at: 2026-10-29T11:20:00Z
step: S11-004
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
concept: cold-room sensor
grain: one sensor
subject_area: sensors
---

## Business key

- Warehouse.ColdRoomTemperatures.ColdRoomSensorNumber | key_space=wwi | key_kind=source-key

## Evidence

- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/06_keys.md#C2
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C5
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/03_temporal.md#C6
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/columns/ColdRoomSensorNumber/02_meaning.md#C1
- analysis/wwi/tables/Warehouse/ColdRoomTemperatures/columns/ColdRoomSensorNumber/02_meaning.md#C4
