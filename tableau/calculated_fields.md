# Tableau Calculated Fields & Parameter Definitions (2010–2026 Dataset)

This reference documents all calculated fields, parameters, and shelf mappings built on **`F1 Racing Project Dataset.xlsx`** (13,748 rows across 5 sheets: `race_results`, `lap_intelligence`, `qualifying_results`, `championship_standings`, `circuits`).

## 1. Calculated Fields

| Field Name | Formula | Purpose |
| :--- | :--- | :--- |
| **`DNF Count`** | `IF [dnf] = 1 THEN 1 ELSE 0 END` | Counts technical and on-track retirements (`396` total DNFs across 6 `dnf_reason` categories). |
| **`DNF Rate (%)`** | `SUM([DNF Count]) / COUNT([race_id])` | Computes retirement percentage per driver, team, or circuit (`6.13%` overall). |
| **`Points Cumulative`** | `RUNNING_SUM(SUM([points]))` | Tracks cumulative points progression across seasons `2010–2026`. |
| **`Podium Count`** | `IF [podium] = 1 THEN 1 ELSE 0 END` | Counts top-3 finishes (`1,002` total podiums across 6,464 race starts). |
| **`Top N Filter`** | `INDEX() <= [Top N Parameter]` | Filters Driver Performance Leaderboard dynamically to the user-selected Top N drivers (Default: `10`). |

## 2. Parameter Setup (`Top N Parameter`)
- **Name**: `Top N Parameter`
- **Data Type**: Integer
- **Current Value**: `10`
- **Allowable Values**: Range (`Minimum: 3`, `Maximum: 19`, `Step size: 1`)

## 3. Exact Shelf Mapping for All 9 Worksheets

1. **KPI Overview Cards (4 Sheets)**:
   - *Competing Teams*: `COUNTD([team])` -> **`10`**
   - *Seasons in Play*: `COUNTD([season])` -> **`17`** (`2010–2026`)
   - *Race Outcomes Logged*: `COUNT([race_results])` -> **`6,464`**
   - *Circuits Showcased*: `COUNTD([circuit_id])` (from `circuits`) -> **`29`** (`24` active race circuits across `21` countries)
2. **Global Driver Distribution Across Grand Prix Nations (Filled Map)**:
   - *Detail*: `country` (Geographic Role: Country/Region)
   - *Color / Label*: `COUNT([race_results])` (Bahrain `2,168`, USA `400`, Monaco/Hungary/Spain `328` each)
3. **Driver Reliability Analysis (Stacked Bar Chart)**:
   - *Columns*: `driver_name` | *Rows*: `SUM([dnf])` | *Color*: `dnf_reason` (`Engine` 73, `Hydraulics` 70, `Mechanical` 67, `Brake failure` 64, `Gearbox` 62, `Collision` 60)
4. **Driver Performance Leaderboard (Vertical Bar Chart + Top N Parameter)**:
   - *Columns*: `driver_name` | *Rows*: `SUM([points])` | *Filter*: `Top N Filter = True`
   - *Direct `race_results`*: Verstappen (`4,640`), Hamilton (`4,491`), Perez (`3,366`), Russell (`3,299`), Leclerc (`3,243`)
   - *Logical Join (`lap_intelligence` -> `race_results` on `circuit_id`)*: Hamilton (`31,147`), Verstappen (`31,126`), Leclerc (`27,673`), Norris (`26,408`)
5. **Team Performance Ranking (Horizontal Bar Chart)**:
   - *Columns*: `SUM([points])` | *Rows*: `team` (Sorted descending: Red Bull Racing `8,006`, Mercedes `7,790`, Ferrari `5,778`, McLaren `4,270`)
6. **Team Championship Performance Analysis (Grouped Bar Chart)**:
   - *Source*: `championship_standings` (`standing_type = 'Constructor'`)
   - *Columns*: `team`, `Measure Names` | *Rows*: `SUM([points])`, `SUM([wins])`, `SUM([podiums])`
7. **Tyre Compound Usage Distribution (Pie Chart)**:
   - *Marks*: Pie | *Color*: `starting_compound` | *Angle*: `COUNT([race_results])`
   - *Breakdown*: Soft `1,889` (`29.22%`), Medium `1,884` (`29.15%`), Hard `1,849` (`28.60%`), Intermediate `842` (`13.03%`)
8. **Country-wise Race Participation (Treemap)**:
   - *Marks*: Square / Treemap | *Size & Color*: `COUNT([race_results])` | *Label*: `country`
9. **Podium Achievements by Driver and Team (Packed Bubble Chart)**:
   - *Marks*: Circle | *Size*: `SUM([podium])` (`1,002` total) | *Color*: `team` | *Label*: `driver_name`
