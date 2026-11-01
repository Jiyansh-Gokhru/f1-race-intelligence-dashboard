# Data Dictionary — F1 Racing Project Dataset (2010–2026)

Source Workbook: **`F1 Racing Project Dataset.xlsx`** (`13,748` total records across 5 relational sheets).

## Sheet 1: `race_results` (`6,464` rows × `42` columns)
- **Primary Keys & Identifiers**: `race_id`, `season` (`2010–2026`), `round`, `race_name`, `circuit_id`, `circuit_name`, `country`, `city`, `race_date`
- **Competitor Entities**: `driver_id`, `driver_name` (`19` drivers), `driver_number`, `driver_nationality`, `team_id`, `team` (`10` constructors)
- **Performance Metrics**: `grid_position`, `finish_position`, `position_Text`, `positions_gained`, `points`, `laps_completed`, `race_time_sec`, `fastest_lap`, `fastest_lap_time_sec`, `avg_lap_time_sec`, `pit_stops`, `total_pit_time_sec`
- **Strategy & Reliability**: `starting_compound` (`Soft`, `Medium`, `Hard`, `Intermediate`), `tyre_stints`, `dnf` (`0` or `1`), `dnf_reason` (`Engine`, `Hydraulics`, `Mechanical`, `Brake failure`, `Gearbox`, `Collision`, `None`), `status`, `podium` (`0` or `1`), `win` (`0` or `1`)
- **Track Environment**: `weather` (`Dry`, `Wet`, `Mixed`, `Overcast`, `Clear`), `track_temp_c`, `air_temp_c`, `humidity_pct`, `wind_speed_kmh`, `safety_car_deployments`, `red_flags`, `drs_zones`

## Sheet 2: `lap_intelligence` (`3,814` rows × `14` columns)
- `lap_record_id`, `race_id`, `season`, `circuit_id`, `driver_id`, `driver_name`, `team`, `lap_number`, `lap_time_sec`, `sector_1_sec`, `sector_2_sec`, `sector_3_sec`, `tyre_compound`, `tyre_age_laps`

## Sheet 3: `qualifying_results` (`3,130` rows × `16` columns)
- `qual_id`, `race_id`, `season`, `round`, `circuit_id`, `driver_id`, `driver_name`, `team`, `q1_time_sec`, `q2_time_sec`, `q3_time_sec`, `best_qual_time_sec`, `qual_position`, `pole_position`, `tyre_compound`, `weather`

## Sheet 4: `championship_standings` (`311` rows × `10` columns)
- `standing_id`, `season` (`2010–2026`), `standing_type` (`Driver` = 160 rows, `Constructor` = 151 rows), `entity_id`, `driver_name`, `team`, `position`, `points`, `wins`, `podiums`

## Sheet 5: `circuits` (`29` rows × `9` columns)
- `circuit_id`, `circuit_name`, `country`, `city`, `latitude`, `longitude`, `circuit_length_km`, `num_turns`, `lap_record_sec`
