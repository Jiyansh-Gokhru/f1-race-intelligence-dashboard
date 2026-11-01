"""
Formula 1 Race Intelligence Dashboard (2010–2026) — ETL & Data Preparation Pipeline
Dataset: F1 Racing Project Dataset.xlsx (5 Sheets, 13,748 Total Rows)
  - race_results: 6,464 rows x 42 columns
  - lap_intelligence: 3,814 rows x 14 columns
  - qualifying_results: 3,130 rows x 16 columns
  - championship_standings: 311 rows x 10 columns
  - circuits: 29 rows x 9 columns
"""

import os
import json
import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class F1GridIntelligenceETL:
    def __init__(self, excel_path: str, output_dir: str):
        self.excel_path = excel_path
        self.output_dir = output_dir
        self.sheets = {}

    def extract(self):
        logging.info(f"Loading 5-sheet Excel dataset from: {self.excel_path}")
        xl = pd.ExcelFile(self.excel_path)
        expected = ["circuits", "championship_standings", "lap_intelligence", "qualifying_results", "race_results"]
        for name in expected:
            assert name in xl.sheet_names, f"Missing required sheet: {name}"
            self.sheets[name] = xl.parse(name)
            logging.info(f"Loaded sheet '{name}': {self.sheets[name].shape[0]} rows x {self.sheets[name].shape[1]} cols")
        total_rows = sum(len(df) for df in self.sheets.values())
        logging.info(f"Total rows across all 5 sheets: {total_rows:,}")
        return self

    def clean_and_prepare(self):
        rr = self.sheets["race_results"].copy()
        ci = self.sheets["circuits"].copy()
        cs = self.sheets["championship_standings"].copy()
        li = self.sheets["lap_intelligence"].copy()
        qr = self.sheets["qualifying_results"].copy()

        # 1. Null and missing value treatment (as specified in To-Do 3: Prepare the Data for Visualization)
        # Retain records with missing finish_position (396 DNF entries) with dnf_reason populated
        dnf_count = int(rr["dnf"].sum())
        logging.info(f"Retained {dnf_count} DNF records with populated dnf_reason for Driver Reliability Analysis.")
        rr["dnf_reason_clean"] = rr["dnf_reason"].fillna("Finished")

        # Exclude null gap_to_leader_s for DNF rows in gap-based aggregations
        valid_gaps = rr.loc[rr["dnf"] == 0, "gap_to_leader_s"].dropna()
        logging.info(f"Valid non-DNF gap_to_leader_s records: {len(valid_gaps):,}")

        # 2. Data type validation
        continuous_measures = ["points", "laps_led", "drs_overtakes", "air_temp_celsius", "avg_pit_stop_time_s"]
        for col in continuous_measures:
            rr[col] = pd.to_numeric(rr[col], errors="coerce")

        # 3. Calculated fields created:
        # - DNF Count per driver across all seasons
        driver_dnf_map = rr.groupby("driver")["dnf"].sum().to_dict()
        rr["DNF_Count_Driver_Total"] = rr["driver"].map(driver_dnf_map)

        # - Points Cumulative: running total of points per driver per season
        rr = rr.sort_values(["season", "round", "driver"]).reset_index(drop=True)
        rr["Points_Cumulative"] = rr.groupby(["season", "driver"])["points"].cumsum()

        # 4. Relationship enrichment: join race_results to circuits on circuit_id
        rr_enriched = rr.merge(
            ci[["circuit_id", "laps", "lap_km"]],
            on="circuit_id",
            how="left",
            suffixes=("", "_circuit_ref")
        )

        self.sheets["race_results_clean"] = rr_enriched
        return self

    def export(self):
        os.makedirs(self.output_dir, exist_ok=True)
        rr = self.sheets["race_results_clean"]
        rr.to_csv(os.path.join(self.output_dir, "f1_race_intelligence_clean_tableau.csv"), index=False)
        for name in ["circuits", "championship_standings", "lap_intelligence", "qualifying_results", "race_results"]:
            self.sheets[name].to_csv(os.path.join(self.output_dir, f"{name}.csv"), index=False)
        logging.info(f"Exported cleaned CSVs to {self.output_dir}")
        return self


if __name__ == "__main__":
    excel_file = "/working_dir/c_773e548a9cf3d119/user_uploaded_files/ttl=63d/user_uploaded/F1 Racing Project Dataset.xlsx"
    out_dir = "/working_dir/c_773e548a9cf3d119/project_repo/data"
    pipeline = F1GridIntelligenceETL(excel_file, out_dir)
    pipeline.extract().clean_and_prepare().export()
