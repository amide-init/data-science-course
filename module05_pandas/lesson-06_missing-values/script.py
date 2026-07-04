"""
Handling Missing Values
Module 05, Lesson 06

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import io
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "planets.csv")


# ── Section 1: Detecting Missing Values ──────────────────────────────────────

def section_detecting(planets):
    print("─" * 55)
    print("SECTION 1: Detecting Missing Values")
    print("─" * 55)

    print("Missing values per column:")
    print(planets.isna().sum())
    print(f"Total missing cells: {planets.isna().sum().sum()}")
    print()
    planets.info()
    print()


# ── Section 2: Percentage Missing ────────────────────────────────────────────

def section_percentage(planets):
    print("─" * 55)
    print("SECTION 2: Judging Severity — Percentage, Not Just Count")
    print("─" * 55)

    missing_pct = (planets.isna().mean() * 100).round(1)
    print("Percentage missing per column:")
    print(missing_pct)
    print()


# ── Section 3: Dropping Missing Values ───────────────────────────────────────

def section_dropna(planets):
    print("─" * 55)
    print("SECTION 3: Dropping Missing Values — .dropna()")
    print("─" * 55)

    dropped_any = planets.dropna()
    print(f"Default dropna(): {planets.shape[0]} -> {dropped_any.shape[0]} rows")

    dropped_distance_only = planets.dropna(subset=["distance"])
    print(f"dropna(subset=['distance']): {planets.shape[0]} -> {dropped_distance_only.shape[0]} rows")

    dropped_thresh = planets.dropna(thresh=5)
    print(f"dropna(thresh=5): {planets.shape[0]} -> {dropped_thresh.shape[0]} rows")

    dropped_columns = planets.dropna(axis=1)
    print(f"dropna(axis=1) columns kept: {list(dropped_columns.columns)}")
    print()


# ── Section 4: Filling Missing Values ────────────────────────────────────────

def section_fillna(planets):
    print("─" * 55)
    print("SECTION 4: Filling Missing Values — .fillna()")
    print("─" * 55)

    orbital_filled_zero = planets["orbital_period"].fillna(0)
    print(f"Missing after fillna(0): {orbital_filled_zero.isna().sum()}")

    orbital_median = planets["orbital_period"].median()
    orbital_filled_median = planets["orbital_period"].fillna(orbital_median)
    print(f"orbital_period median: {orbital_median:.2f}")
    print(f"Missing after fillna(median): {orbital_filled_median.isna().sum()}")

    small_example = pd.Series([10, None, None, 40, None])
    print(f"Original: {small_example.tolist()}")
    print(f"ffill:    {small_example.ffill().tolist()}")
    print(f"bfill:    {small_example.bfill().tolist()}")
    print()


# ── Section 5: Choosing a Strategy Per Column ────────────────────────────────

def section_strategy(planets):
    print("─" * 55)
    print("SECTION 5: Choosing a Strategy, Column by Column")
    print("─" * 55)

    planets_clean = planets.copy()
    planets_clean["orbital_period"] = planets_clean["orbital_period"].fillna(
        planets_clean["orbital_period"].median()
    )
    planets_clean["distance"] = planets_clean["distance"].fillna(planets_clean["distance"].median())
    planets_clean = planets_clean.drop(columns=["mass"])

    print("After applying our per-column strategy:")
    print(planets_clean.isna().sum())
    print()

    return planets_clean


# ── Section 6: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(planets):
    print("─" * 55)
    print("SECTION 6: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — default dropna() drops a row if ANY column is missing:")
    over_dropped = planets.dropna()
    print(f"  planets.dropna() keeps only {over_dropped.shape[0]} of {planets.shape[0]} rows")
    scoped = planets.dropna(subset=["distance"])
    print(f"  Correct: dropna(subset=['distance']) keeps {scoped.shape[0]} rows")
    print()

    print("Mistake 2 — the mean is pulled around by outliers, the median often isn't:")
    print(f"  orbital_period mean:   {planets['orbital_period'].mean():.1f}")
    print(f"  orbital_period median: {planets['orbital_period'].median():.1f}")
    print()

    print("Mistake 3 — pandas auto-recognizes SOME placeholders ('N/A') but not others ('--'):")
    disguised = "planet;distance\nKepler-10b;N/A\nKepler-11b;60.4\nKepler-12b;--\n"
    naive = pd.read_csv(io.StringIO(disguised), sep=";")
    print(f"  Without na_values=: {naive['distance'].isna().sum()} missing (should be 2)")
    fixed = pd.read_csv(io.StringIO(disguised), sep=";", na_values=["--"])
    print(f"  With na_values=['--']: {fixed['distance'].isna().sum()} missing (correct)")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 06 — Handling Missing Values")
    print("=" * 55)
    print()

    planets_df = pd.read_csv(CSV_PATH)

    section_detecting(planets_df)
    section_percentage(planets_df)
    section_dropna(planets_df)
    section_fillna(planets_df)
    section_strategy(planets_df)
    section_mistakes(planets_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
