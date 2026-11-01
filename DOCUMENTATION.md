# FORMULA 1 Race Intelligence Dashboard Analysis Report — Step-by-Step Project Documentation

**Assigned To**: Jiyansh Gokhru

**Platform**: MySkillWallet — Formula 1 Race Intelligence Dashboard Project

**Dataset**: `F1 Racing Project Dataset.xlsx` (5 Relational Sheets • 13,748 Total Rows • 17 Seasons: 2010–2026)

**Live Web App Deployment**: <https://jiyansh-gokhru.github.io/f1-race-intelligence-dashboard/>

**Tableau Public Workbook**: [Formula 1 Race Intelligence Dashboard & Story](https://public.tableau.com/views/FORMULA1RaceIntelligenceDashboard/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## 1. Executive Summary & Problem Statement

Formula 1 generates complex multi-dimensional telemetry, qualifying, race classification, and championship standings data across every Grand Prix weekend. The objective of the **Formula 1 Race Intelligence Dashboard** project is to consolidate the 5-sheet multi-season dataset (**2010 to 2026**, comprising **13,748 combined rows**) into an interactive dark-themed analytics dashboard (**9 unique visualizations**) and narrative storyboard (**9 scenes**), embedded within a responsive **Flask & HTML web application**.

## 2. Multi-Sheet Dataset Architecture (To-Do 1 & To-Do 2)

### 2.1 Dataset Inventory (`F1 Racing Project Dataset.xlsx`)

The provided Excel workbook consists of **5 relational sheets** totaling **13,748 rows**:

| Sheet Name | Row Count | Column Count | Primary Key / Join Key | Core Contents | 
| ----- | ----- | ----- | ----- | ----- | 
| **`race_results`** | 6,464 | 42 | `race_id`, `circuit_id` | Full race classifications, grid vs. finish positions, points, DNF flags & reasons, pit stops, tyre strategy, starting compound, weather, safety cars, DRS overtakes, laps led | 
| **`lap_intelligence`** | 3,814 | 14 | `race_id`, `circuit_id` | Lap-by-lap telemetry (`lap_time_s`, `sector1_s`, `sector2_s`, `sector3_s`), tyre compound, tyre age, DRS active flag, speed trap (km/h), pit lap flag | 
| **`qualifying_results`** | 3,130 | 16 | `race_id`, `circuit_id` | Qualifying session times (`q1_lap_time_s`, `q2_lap_time_s`, `q3_lap_time_s`), gap to pole, sector splits, top speed (km/h) | 
| **`championship_standings`** | 311 | 10 | `season`, `driver`, `team` | Season-end driver and constructor standings, total points, wins, podiums, pole positions, DNFs, and World Champion binary indicator (`champion`) | 
| **`circuits`** | 29 | 9 | `circuit_id` | Master reference of 29 global circuits across 21 countries (`circuit_name`, `country`, `city`, `laps`, `lap_km`, `type`, `altitude_m`, `direction`) | 

### 2.2 Connecting Dataset to Tableau

The multi-sheet Excel dataset was loaded into Tableau Desktop using the **Microsoft Excel connector**. All 5 sheets — `circuits`, `race_results`, `championship_standings`, `lap_intelligence`, and `qualifying_results` — were connected using Tableau's **logical layer relationships**, with `race_id` and `circuit_id` serving as the primary join keys:

* `race_results` ↔ `circuits` joined on `circuit_id`

* `race_results` ↔ `lap_intelligence` joined on `race_id` (and `circuit_id`)

* `race_results` ↔ `qualifying_results` joined on `race_id`

* `championship_standings` maintained as an independent logical table for the Team Championship Performance Analysis chart.

* Connection configured in **Extract (`.hyper`) mode** to guarantee sub-second rendering across all 9 visualizations and 3 interactive global filters.

## 3. Data Preparation & Preprocessing (To-Do 3)

Preparing the data for visualization involved cleaning missing values, validating data types across all columns, creating calculated fields, and configuring parameters and relationships:

1. **Null and Missing Value Treatment**:

   * Records in `race_results` with missing `finish_position` (**396 DNF entries** out of 6,464 total rows) were retained with the `dnf_reason` column populated (`Engine`: 73, `Hydraulics`: 70, `Mechanical`: 67, `Brake failure`: 64, `Gearbox`: 62, `Collision`: 60) to support the **Driver Reliability Analysis** visualization.

   * Null `gap_to_leader_s` values on DNF rows were excluded from gap-based aggregations, preserving the **6,068 finished entries** for pace comparisons.

2. **Data Type Validation**:

   * Continuous numeric measures validated: `points`, `laps_led`, `drs_overtakes`, `air_temp_celsius`, `lap_time_s`, `speed_trap_kmh`, `avg_pit_stop_time_s`.

   * Discrete categorical dimensions validated: `driver` (19 drivers), `team` (10 constructors), `country` (21 nations), `circuit_type` (`Permanent`, `Street`), `starting_compound` / `tyre_compound` (`Soft`, `Medium`, `Hard`, `Intermediate`), and `dnf_reason` (6 failure categories).

3. **Calculated Fields Created (To-Do 9)**:

   * **`DNF Count`**: Derived from the `dnf` flag (`SUM([dnf])`) to count total career and seasonal DNFs per driver.

   * **`Points Cumulative`**: Computed as a running total of points (`RUNNING_SUM(SUM([points]))`) partitioned per driver per season.

   * **`Top N Filter`**: `INDEX() <= [Top N Parameter]` computed along Driver sorted descending by Points.

4. **Parameter & Global Filter Setup (To-Do 8)**:

   * **`Top N Parameter`**: Integer parameter (Default value: `10`, range `1–19`) dynamically controlling how many drivers appear on the **Driver Performance Leaderboard**.

   * **`DNF Reason` Filter**: Global dropdown filter allowing selection of specific retirement causes (`Engine`, `Hydraulics`, `Mechanical`, `Brake failure`, `Gearbox`, `Collision`).

   * **`Year of Race Date` Filter**: Global season filter (`2010` to `2026`) enabling single-season isolation or multi-season trend comparison.

## 4. The 9 Unique Visualizations & Exact Analytical Findings (To-Do 4, 5 & 10)

A total of **9 unique visualizations** were created and assembled into a unified dark-themed dashboard (`#000000` / `#141418` background with `#E10600` Formula 1 red and white accents):

### Visualization 1: 4 KPI Summary Cards (Top Row)

* **Competing Teams**: **10** (`Red Bull Racing`, `Mercedes`, `Ferrari`, `McLaren`, `Alpine`, `Aston Martin`, `Williams`, `RB (AlphaTauri)`, `Haas`, `Kick Sauber`)

* **Seasons in Play**: **17** (`2010`–`2026`)

* **Race Outcomes Logged**: **6,464**

* **Circuits Showcased**: **29**

### Visualization 2: Global Driver Distribution Across Grand Prix Nations (Geographic Map)

* **Chart Type**: Dark-themed filled/symbol Geographic Map across 21 host nations.

* **Key Findings**:

  * **Bahrain**: 2,168 race entries logged (115 races)

  * **USA**: 400 race entries logged (20 races across COTA, Miami, Las Vegas)

  * **Monaco, Hungary, Spain**: 328 race entries each (17 races each)

  * **Canada, UAE, Brazil**: 308 race entries each (16 races each)

  * **Singapore**: 288 entries • **Italy**: 220 entries • **Austria**: 180 entries • **Mexico**: 160 entries

  * **Australia, Netherlands, Azerbaijan, Saudi Arabia, Japan, UK, Qatar**: 140 entries each • **Belgium**: 120 entries • **China**: 40 entries.

### Visualization 3: Driver Reliability Analysis (Stacked Vertical Bar Chart)

* **Chart Type**: Vertical Stacked Bar Chart (`driver` on X-axis, `SUM(dnf)` on Y-axis stacked by `dnf_reason`).

* **Key Findings (396 Total DNFs)**:

  * **By Failure Mode**: `Engine` (73 DNFs • 18.43%), `Hydraulics` (70 DNFs • 17.68%), `Mechanical` (67 DNFs • 16.92%), `Brake failure` (64 DNFs • 16.16%), `Gearbox` (62 DNFs • 15.66%), `Collision` (60 DNFs • 15.15%).

  * **By Driver**: Carlos Sainz (34 DNFs: 10 Hydraulics, 6 Mechanical, 6 Gearbox, 5 Brake failure, 4 Engine, 3 Collision), Sergio Perez (29 DNFs), Charles Leclerc (28 DNFs), Fernando Alonso (25 DNFs), Liam Lawson (24 DNFs), Oscar Piastri (24 DNFs), Yuki Tsunoda (23 DNFs), while Lewis Hamilton recorded only 12 DNFs across 334 starts.

### Visualization 4: Driver Performance Leaderboard (Vertical Bar Chart — Top N Controlled)

* **Chart Type**: Vertical Bar Chart controlled by `Top N Parameter` (default: 10).

* **Key Findings (Direct Driver Points in `race_results` / `championship_standings`)**:

   1. **Max Verstappen**: 4,640 pts (100 wins, 187 podiums)

   2. **Lewis Hamilton**: 4,491 pts (118 wins, 174 podiums)

   3. **Sergio Perez**: 3,366 pts (97 podiums)

   4. **George Russell**: 3,299 pts (115 podiums)

   5. **Charles Leclerc**: 3,243 pts (44 wins, 113 podiums)

   6. **Carlos Sainz**: 3,147 pts (2 wins, 63 podiums)

   7. **Lando Norris**: 2,454 pts (35 wins, 85 podiums)

   8. **Oscar Piastri**: 1,816 pts (35 podiums)

   9. **Esteban Ocon**: 1,136 pts (7 wins, 25 podiums)

  10. **Pierre Gasly**: 811 pts (7 podiums)
      *(Note: When evaluated via `lap_intelligence` logical-layer circuit relationship, the 8 race-winning drivers rank as Lewis Hamilton `31,147`, Max Verstappen `31,126`, Charles Leclerc `27,673`, Lando Norris `26,408`, Yuki Tsunoda `14,438`, Esteban Ocon `14,205`, Carlos Sainz `11,004`, and Fernando Alonso `1,353`.)*

### Visualization 5: Team Performance Ranking (Horizontal Bar Chart)

* **Chart Type**: Horizontal Bar Chart (`team` on Y-axis sorted descending by `SUM(points)` on X-axis).

* **Key Findings**:

   1. **Red Bull Racing**: 8,006 pts

   2. **Mercedes**: 7,790 pts

   3. **Ferrari**: 5,778 pts

   4. **McLaren**: 4,270 pts

   5. **Alpine**: 1,947 pts

   6. **Aston Martin**: 1,181 pts

   7. **Williams**: 1,057 pts

   8. **RB (AlphaTauri)**: 923 pts

   9. **Haas**: 591 pts

  10. **Kick Sauber**: 363 pts

### Visualization 6: Team Championship Performance Analysis (Grouped/Vertical Bar Chart)

* **Chart Type**: Vertical Bar Chart built on `championship_standings` (`team` on X-axis, `Points` and `Wins` on Y-axis).

* **Key Findings**:

  * **Red Bull Racing**: 8,006 pts • 100 wins • 284 podiums • 7 Championships

  * **Mercedes**: 7,790 pts • 118 wins • 289 podiums • 7 Championships

  * **Ferrari**: 6,390 standings pts • 46 wins • 176 podiums

  * **McLaren**: 4,270 pts • 35 wins • 120 podiums • 3 Championships

### Visualization 7: Tyre Compound Usage Distribution (Pie Chart)

* **Chart Type**: Pie Chart of `starting_compound` across all 6,464 race results.

* **Key Findings**:

  * **Soft**: 1,889 entries (**29.22%**)

  * **Medium**: 1,884 entries (**29.15%**)

  * **Hard**: 1,849 entries (**28.60%**)

  * **Intermediate**: 842 entries (**13.03%**)

### Visualization 8: Country-wise Race Participation (Treemap / Highlight Table)

* **Chart Type**: Treemap sized and color-encoded by total race entries per host country.

* **Key Findings**: Bahrain (2,168 entries, 33.54% share) dominates the left block, followed by USA (400), Monaco (328), Hungary (328), Spain (328), Canada (308), UAE (308), Brazil (308), Singapore (288), Italy (220), and Austria (180).

### Visualization 9: Podium Achievements by Driver and Team (Packed Bubble Chart)

* **Chart Type**: Packed Bubble Chart (`driver` & `team`, bubble size = Podium count, bubble color = Constructor Team).

* **Key Findings (1,002 Total Podiums)**:

  * **Max Verstappen (Red Bull Racing)**: 187 podiums

  * **Lewis Hamilton (Mercedes)**: 174 podiums

  * **George Russell (Mercedes)**: 115 podiums

  * **Charles Leclerc (Ferrari)**: 113 podiums

  * **Sergio Perez (Red Bull Racing)**: 97 podiums

  * **Lando Norris (McLaren)**: 85 podiums

  * **Carlos Sainz**: 63 total podiums (`Ferrari`: 44, `Williams`: 19)

  * **Oscar Piastri (McLaren)**: 35 podiums • **Esteban Ocon (Alpine)**: 25 podiums • **Yuki Tsunoda (RB)**: 10 podiums • **Fernando Alonso (Aston Martin)**: 10 podiums.

## 5. 9-Scene Storyboard Structure (To-Do 6)

**Story Title**: *Formula 1 Race Intelligence: From Global Overview to Championship Success*

1. **Scene 1 — Global Scale Overview (KPIs)**: High-level overview of the 10 competing teams, 17 seasons (2010–2026), 6,464 logged race outcomes, and 29 circuits.

2. **Scene 2 — Global Driver Distribution Across Grand Prix Nations**: Geographic distribution across 21 nations led by Bahrain (2,168) and USA (400).

3. **Scene 3 — Driver Reliability and DNF Analysis**: Breakdown of 396 retirements across Engine, Hydraulics, Mechanical, Brake failure, Gearbox, and Collision.

4. **Scene 4 — Individual Driver Performance Leaderboard**: Top N parameter analysis led by Max Verstappen (4,640 pts) and Lewis Hamilton (4,491 pts, 118 wins).

5. **Scene 5 — Team Performance Ranking**: Constructor standings comparison led by Red Bull Racing (8,006 pts) and Mercedes (7,790 pts).

6. **Scene 6 — Season-by-Season Championship Analysis**: Multi-season analysis from `championship_standings` highlighting championship eras.

7. **Scene 7 — Tyre Strategy Patterns**: Pirelli compound distribution showing Soft (29.22%), Medium (29.15%), Hard (28.60%), and Intermediate (13.03%).

8. **Scene 8 — Country-Level Race Participation**: Hierarchical treemap comparing race participation density across global regions.

9. **Scene 9 — Podium Achievement Distribution Across Drivers and Teams**: Packed bubble synthesis of 1,002 podium finishes across constructors and drivers.

## 6. Web Integration with Flask & GitHub Pages (To-Do 11 & To-Do 12)

The published Tableau Public dashboard and story are integrated into a lightweight **Flask web application (`web/app.py`)** and standalone responsive HTML portal (`index.html`):

* **Local Flask Execution**: Run `python3 web/app.py` and navigate to `http://localhost:5000/`.

* **Static Hosting**: Deployed directly via GitHub Pages at `https://jiyansh-gokhru.github.io/f1-race-intelligence-dashboard/`.