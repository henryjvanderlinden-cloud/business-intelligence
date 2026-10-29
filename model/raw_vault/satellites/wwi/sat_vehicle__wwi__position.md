---
id: nsdn:rv:sat:vehicle__wwi__position
kind: satellite
name: sat_vehicle__wwi__position
status: accepted
ruled_in: ADR-0033
defined_in: docs/10_architecture/149_wwi-satellites.md#3.7
written_by: claude-opus-5-5
written_at: 2026-10-29T11:25:00Z
step: S11-008
method: transcribed by prototypes/model_declarations/transcribe_wwi.py from the ruled note
parent: hub_vehicle
source: wwi
source_table: Warehouse.VehicleTemperatures
parent_key: Warehouse.VehicleTemperatures.VehicleRegistration
satellite_kind: reading
split_reason: sensitivity (position history that can track a driver)
valid_time: Warehouse.VehicleTemperatures.RecordedWhen
class: restricted
subject_area: sensors
---

## Columns

- VehicleTemperatureID | reading_key=yes | repeats=sat_vehicle__wwi__chiller_reading
- RecordedWhen | repeats=sat_vehicle__wwi__chiller_reading
- FullSensorData
- CompressedSensorData

## Evidence

- analysis/wwi/tables/Warehouse/VehicleTemperatures/19_sensitivity.md#C2
- analysis/wwi/tables/Warehouse/VehicleTemperatures/19_sensitivity.md#C3
