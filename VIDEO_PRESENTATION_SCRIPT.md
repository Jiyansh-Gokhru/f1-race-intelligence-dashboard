# FORMULA 1 Race Intelligence Dashboard (2010–2026) — 5 to 7 Minute Video Explanation Script

**Assigned To**: Jiyansh Gokhru  
**Target Duration**: 5 – 7 Minutes (as required by To-Do 13)  
**Project**: Formula 1 Race Intelligence Dashboard Analysis Report  

---

## Segment 1: Introduction & Problem Statement (0:00 – 1:00)

**[Screen Cue]**: Show the MySkillWallet project portal and the Hero section of the live web application (`index.html`).

**[Narration]**:
"Hello everyone, my name is **Jiyansh Gokhru**, and welcome to the end-to-end demonstration of my **Formula 1 Race Intelligence Dashboard** project.

Formula 1 generates thousands of race classification, qualifying, and lap telemetry data points across every season. The problem statement of this project is to transform a multi-sheet Formula 1 Excel dataset spanning **17 seasons from 2010 to 2026** into a unified, dark-themed interactive dashboard and a 9-scene narrative story, and integrate them into a responsive Flask web application for race strategists, analysts, and fans."

---

## Segment 2: 5-Sheet Dataset Connection & Data Preparation (1:00 – 2:15)

**[Screen Cue]**: Scroll to the **5-Sheet Schema & Data Preparation** section of the web app and show `scripts/etl_pipeline.py`.

**[Narration]**:
"Let's look at the dataset and preprocessing pipeline.
The provided Excel workbook contains **5 relational sheets with 13,748 combined rows**:
1. `race_results` with **6,464 rows and 42 columns** — our primary fact table.
2. `lap_intelligence` with **3,814 rows** of sector splits, tyre age, and speed trap telemetry.
3. `qualifying_results` with **3,130 rows** of Q1, Q2, and Q3 lap times.
4. `championship_standings` with **311 driver-season records**.
5. `circuits` with **29 global tracks across 21 countries**.

In Tableau and our Python pipeline, we connected `race_results` to `circuits`, `lap_intelligence`, and `qualifying_results` using `circuit_id` and `race_id` in Extract mode.
For data cleaning:
- We retained the **396 DNF records** where `finish_position` is null, keeping the `dnf_reason` column populated to power our Driver Reliability Analysis, while excluding null `gap_to_leader_s` values from pace aggregations.
- We created the `DNF Count` calculated field, the `Points Cumulative` running total, and the integer `Top N Parameter` (defaulting to 10)."

---

## Segment 3: Walkthrough of the 9 Unique Dashboard Visualizations & 3 Global Filters (2:15 – 4:30)

**[Screen Cue]**: Scroll to the **Formula 1 Race Intelligence Dashboard** section and demonstrate the 3 filters (`DNF Reason`, `Year of Race Date`, and `Top N Parameter`).

**[Narration]**:
"Here is our unified dark-themed **Formula 1 Race Intelligence Dashboard**, which features **9 unique visualizations**:
1. **4 KPI Summary Cards** at the top: **10 Competing Teams**, **17 Seasons in Play (2010–2026)**, **6,464 Race Outcomes Logged**, and **29 Circuits Showcased**, alongside our three global controls: **DNF Reason**, **Year of Race Date**, and **Top N Parameter**.
2. **Global Driver Distribution Across Grand Prix Nations**: A dark geographic map across 21 countries showing Bahrain leading with 2,168 entries, followed by the USA with 400, and Monaco, Hungary, and Spain with 328 each.
3. **Driver Reliability Analysis**: A stacked vertical bar chart breaking down all 396 DNFs by failure mode — Engine (73), Hydraulics (70), Mechanical (67), Brake failure (64), Gearbox (62), and Collision (60). Carlos Sainz (34 DNFs) and Sergio Perez (29 DNFs) experienced the most retirements, while Lewis Hamilton had only 12 DNFs in 334 starts.
4. **Driver Performance Leaderboard**: Dynamically controlled by our **Top N Parameter** slider. Max Verstappen leads career points with 4,640 points and 100 wins, closely followed by Lewis Hamilton with 4,491 points and 118 wins, Sergio Perez (3,366), George Russell (3,299), and Charles Leclerc (3,243). We can also toggle the Logical-Layer Circuit Points view.
5. **Team Performance Ranking**: A horizontal bar chart showing Red Bull Racing at #1 with 8,006 points and Mercedes at #2 with 7,790 points, ahead of Ferrari (5,778) and McLaren (4,270).
6. **Team Championship Performance Analysis**: Built from `championship_standings`, showing Red Bull Racing and Mercedes each capturing 7 Championships across the 17-season span, with McLaren winning 3.
7. **Tyre Compound Usage Distribution**: A pie chart showing a balanced slick allocation across Soft (29.22%), Medium (29.15%), Hard (28.60%), and wet-weather Intermediate tyres (13.03%).
8. **Country-wise Race Participation**: A proportional treemap highlighting host country volume.
9. **Podium Achievements by Driver and Team**: A packed bubble chart of all 1,002 podium finishes led by Max Verstappen (187 podiums) and Lewis Hamilton (174 podiums)."

---

## Segment 4: The 9-Scene Story & Flask Web Integration (4:30 – 6:00)

**[Screen Cue]**: Click through Scenes 1 to 9 in the **Formula 1 Race Intelligence: From Global Overview to Championship Success** Storyboard, then show the Flask Web Integration section.

**[Narration]**:
"Below the dashboard is our **9-Scene Interactive Story**, titled *Formula 1 Race Intelligence: From Global Overview to Championship Success*. Viewers can step sequentially from Scene 1 (Global Scale KPIs) through Geographic Distribution, Driver Reliability, Driver Leaderboard, Team Ranking, Season-by-Season Championship Analysis, Tyre Strategy, Country Participation, and Scene 9 (Podium Achievements).

Finally, the entire solution is integrated into a **Flask web application (`app.py`)** and deployed live on **GitHub Pages**, allowing analysts and fans to interact with all filters, parameters, and Tableau Public views directly in the browser. Thank you for watching!"
