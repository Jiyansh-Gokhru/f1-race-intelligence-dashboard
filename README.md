# FORMULA 1 Race Intelligence Dashboard (2010–2026)

> **Live Web Application:** [https://jiyansh-gokhru.github.io/f1-race-intelligence-dashboard/](https://jiyansh-gokhru.github.io/f1-race-intelligence-dashboard/)  
> **Tableau Public Dashboard & Story:** [https://public.tableau.com/views/FORMULA1RaceIntelligenceDashboard/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link](https://public.tableau.com/views/FORMULA1RaceIntelligenceDashboard/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

[![Tableau](https://img.shields.io/badge/Tableau%20Public-9%20Visualizations%20%7C%209%20Story%20Scenes-E97627.svg?logo=tableau)](https://public.tableau.com)
[![Python](https://img.shields.io/badge/Python-Flask%20%7C%20Pandas%20ETL-3776AB.svg?logo=python)](https://python.org)
[![Dataset](https://img.shields.io/badge/Dataset-5%20Sheets%20%7C%2013%2C748%20Rows-brightgreen.svg)]()
[![Seasons](https://img.shields.io/badge/Seasons-17%20(2010--2026)-red.svg)]()
[![Platform](https://img.shields.io/badge/MySkillWallet-Jiyansh%20Gokhru-6366F1.svg)](https://myskillwallet.ai)

An end-to-end Formula 1 Race Intelligence analytics platform, dark-themed interactive dashboard (**9 unique visualizations**), **9-scene data story**, and **Flask web application** built on the official **5-sheet `F1 Racing Project Dataset.xlsx` (13,748 total rows across 17 seasons from 2010 to 2026)**.

---

## 📊 Multi-Sheet Dataset Overview (`F1 Racing Project Dataset.xlsx`)

| Sheet Name | Rows | Columns | Primary Join Keys | Description |
| :--- | :---: | :---: | :--- | :--- |
| **`race_results`** | 6,464 | 42 | `race_id`, `circuit_id` | Complete Grand Prix race outcomes, grid/finish positions, points, 396 DNFs with `dnf_reason`, pit stops, starting tyre compound, weather, safety cars, DRS overtakes, laps led |
| **`lap_intelligence`** | 3,814 | 14 | `race_id`, `circuit_id` | Sector splits (`sector1_s`, `sector2_s`, `sector3_s`), lap time (s), tyre compound & age, DRS status, speed trap (km/h), pit lap indicator |
| **`qualifying_results`** | 3,130 | 16 | `race_id`, `circuit_id` | Q1, Q2, and Q3 qualifying lap times, gap to pole, sector times, and top speed (km/h) |
| **`championship_standings`** | 311 | 10 | `season`, `driver`, `team` | Season-end driver and constructor classifications, points, wins, podiums, pole positions, DNFs, and World Champion indicator |
| **`circuits`** | 29 | 9 | `circuit_id` | Master directory of 29 circuits across 21 countries (`circuit_name`, `country`, `city`, `laps`, `lap_km`, `type`, `altitude_m`, `direction`) |

---

## 📈 The 9 Unique Dashboard Visualizations

1. **4 KPI Summary Cards**: Competing Teams (**10**), Seasons in Play (**17**), Race Outcomes Logged (**6,464**), Circuits Showcased (**29**).
2. **Global Driver Distribution Across Grand Prix Nations** *(Geographic Map)*: Interactive dark map across 21 host nations led by Bahrain (2,168 entries), USA (400), Monaco (328), Hungary (328), and Spain (328).
3. **Driver Reliability Analysis** *(Stacked Bar Chart by DNF Reason)*: Breakdown of all 396 DNFs across `Engine` (73), `Hydraulics` (70), `Mechanical` (67), `Brake failure` (64), `Gearbox` (62), and `Collision` (60).
4. **Driver Performance Leaderboard** *(Vertical Bar Chart — Top N Parameter Controlled)*: Dynamically displays Top N drivers (default: 10) led by Max Verstappen (4,640 pts, 100 wins) and Lewis Hamilton (4,491 pts, 118 wins).
5. **Team Performance Ranking** *(Horizontal Bar Chart)*: Constructor ranking led by Red Bull Racing (8,006 pts), Mercedes (7,790 pts), Ferrari (5,778 pts), and McLaren (4,270 pts).
6. **Team Championship Performance Analysis** *(Grouped Vertical Bar Chart)*: Built on `championship_standings` comparing multi-season points, wins, and championships across all 10 teams.
7. **Tyre Compound Usage Distribution** *(Pie Chart)*: `Soft` (29.22% / 1,889), `Medium` (29.15% / 1,884), `Hard` (28.60% / 1,849), and `Intermediate` (13.03% / 842).
8. **Country-wise Race Participation** *(Treemap / Highlight Table)*: Proportional country participation blocks highlighting Bahrain (33.54% share), USA, Monaco, Hungary, Spain, Canada, UAE, and Brazil.
9. **Podium Achievements by Driver and Team** *(Packed Bubble Chart)*: 1,002 podium finishes sized by driver podiums and colored by constructor team (Max Verstappen: 187, Lewis Hamilton: 174, George Russell: 115, Charles Leclerc: 113, Sergio Perez: 97, Lando Norris: 85, Carlos Sainz: 63).

---

## 🚀 Quick Start (Flask & Web Integration)

```bash
# 1. Run the Python ETL & Data Preparation Pipeline
python3 scripts/etl_pipeline.py

# 2. Launch the Flask Web Application (Port 5000)
python3 web/app.py
```
