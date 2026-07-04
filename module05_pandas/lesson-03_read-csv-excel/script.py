"""
Reading CSV and Excel Files
Module 05, Lesson 03

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import io
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "tips.csv")
XLSX_PATH = os.path.join(DATA_DIR, "tips.xlsx")


# ── Section 1: read_csv() Basics ─────────────────────────────────────────────

def section_read_csv_basics():
    print("─" * 55)
    print("SECTION 1: pd.read_csv() — The Basics")
    print("─" * 55)

    tips = pd.read_csv(CSV_PATH)
    print(tips.head())
    print(f"type: {type(tips)}")
    print()

    return tips


# ── Section 2: Useful read_csv() Parameters ──────────────────────────────────

def section_read_csv_parameters():
    print("─" * 55)
    print("SECTION 2: Useful read_csv() Parameters")
    print("─" * 55)

    preview = pd.read_csv(CSV_PATH, usecols=["total_bill", "tip", "day"], nrows=5)
    print("usecols + nrows:")
    print(preview)
    print()

    tips_by_bill = pd.read_csv(CSV_PATH, index_col="total_bill")
    print("index_col='total_bill':")
    print(tips_by_bill.head(3))
    print()

    semicolon_data = "name;age;city\nAisha;20;Pune\nBen;21;Delhi\n"
    custom_sep_df = pd.read_csv(io.StringIO(semicolon_data), sep=";")
    print("sep=';':")
    print(custom_sep_df)
    print()


# ── Section 3: read_excel() ──────────────────────────────────────────────────

def section_read_excel():
    print("─" * 55)
    print("SECTION 3: pd.read_excel() — Reading Excel Files")
    print("─" * 55)

    tips_first_sheet = pd.read_excel(XLSX_PATH)
    print(f"Default sheet shape: {tips_first_sheet.shape}")

    tips_sample = pd.read_excel(XLSX_PATH, sheet_name="tips_sample")
    print(f"'tips_sample' sheet shape: {tips_sample.shape}")
    print(tips_sample.head(3))
    print()

    workbook = pd.ExcelFile(XLSX_PATH)
    print(f"Sheets in tips.xlsx: {workbook.sheet_names}")
    print()


# ── Section 4: Saving DataFrames Back to Disk ────────────────────────────────

def section_saving(tips):
    print("─" * 55)
    print("SECTION 4: Saving DataFrames Back to Disk")
    print("─" * 55)

    dinner_only = tips[tips["time"] == "Dinner"]
    print(f"Dinner rows: {dinner_only.shape[0]} out of {tips.shape[0]} total")

    dinner_csv = os.path.join(DATA_DIR, "dinner_only.csv")
    dinner_xlsx = os.path.join(DATA_DIR, "dinner_only.xlsx")
    dinner_only.to_csv(dinner_csv, index=False)
    dinner_only.to_excel(dinner_xlsx, index=False, sheet_name="dinner")
    print(f"Saved {dinner_csv} and {dinner_xlsx}")
    print()

    # Clean up the files this demo just created, so re-running stays repeatable
    os.remove(dinner_csv)
    os.remove(dinner_xlsx)


# ── Section 5: The First-Look Habit, Applied to Real Data ───────────────────

def section_first_look(tips):
    print("─" * 55)
    print("SECTION 5: The First-Look Habit, Applied to Real Data")
    print("─" * 55)

    print(f"tips.shape: {tips.shape}")
    print("tips.dtypes:")
    print(tips.dtypes)
    print()
    tips.info()
    print()
    print("tips.describe():")
    print(tips.describe())
    print()


# ── Section 6: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips):
    print("─" * 55)
    print("SECTION 6: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — saving WITHOUT index=False bakes the row index into the file:")
    bad_path = os.path.join(DATA_DIR, "_bad_example.csv")
    tips.head(3).to_csv(bad_path)  # no index=False
    reloaded_bad = pd.read_csv(bad_path)
    print(reloaded_bad)
    print("Correct: always pass index=False unless you deliberately want it saved.")
    os.remove(bad_path)
    print()

    print("Mistake 2 — a path relative to the wrong folder raises FileNotFoundError:")
    try:
        pd.read_csv("tips.csv")  # missing the 'data/' folder in the path
    except FileNotFoundError as e:
        print(f"  Caught error: {e}")
    print(f"  Current working directory: {os.getcwd()}")
    print()

    print("Mistake 3 — read_excel() silently loads the FIRST sheet if you don't ask:")
    default_sheet = pd.read_excel(XLSX_PATH)
    print(f"  No sheet_name given -> shape {default_sheet.shape} (this is 'tips', not 'tips_sample')")
    print("  Correct: always pass sheet_name explicitly when a workbook has multiple sheets.")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 03 — Reading CSV and Excel Files")
    print("=" * 55)
    print()

    tips_df = section_read_csv_basics()
    section_read_csv_parameters()
    section_read_excel()
    section_saving(tips_df)
    section_first_look(tips_df)
    section_mistakes(tips_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
