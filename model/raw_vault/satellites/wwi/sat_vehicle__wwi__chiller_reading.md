---
id: nsdn:rv:sat:vehicle__wwi__chiller_reading
kind: satellite
name: sat_vehicle__wwi__chiller_reading
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.7
written_by: claude-opus-5-5
written_at: 2026-10-29T11:34:00Z
step: S11-010
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_vehicle
source: wwi
source_table: Warehouse.VehicleTemperatures
parent_key: Warehouse.VehicleTemperatures.VehicleRegistration
satellite_kind: reading
split_reason: delivery (a reading series: one row per reading, Rule 10)
valid_time: Warehouse.VehicleTemperatures.RecordedWhen
class: internal
subject_area: sensors
---

## Columns

- VehicleTemperatureID | reading_key=yes
- ChillerSensorNumber
- RecordedWhen
- Temperature
- IsCompressed

## Evidence

- analysis/wwi/tables/Warehouse/VehicleTemperatures/06_keys.md#C1
- analysis/wwi/tables/Warehouse/VehicleTemperatures/06_keys.md#C2
- analysis/wwi/tables/Warehouse/VehicleTemperatures/03_temporal.md#C5
