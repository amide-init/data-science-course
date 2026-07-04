"""
GroupBy
Module 05, Lesson 07

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TIPS_PATH = os.path.join(DATA_DIR, "tips.csv")
PLANETS_PATH = os.path.join(DATA_DIR, "planets.csv")


# ── Section 1: Split-Apply-Combine Basics ────────────────────────────────────

def section_basics(tips):
    print("─" * 55)
    print("SECTION 1: Split-Apply-Combine, in One Line")
    print("─" * 55)

    grouped = tips.groupby("day")
    print(f"type: {type(grouped)}")

    avg_bill_by_day = grouped["total_bill"].mean()
    print("Average total_bill per day:")
    print(avg_bill_by_day)
    print()


# ── Section 2: Common Single-Column Aggregations ─────────────────────────────

def section_common_aggregations(tips):
    print("─" * 55)
    print("SECTION 2: Common Single-Column Aggregations")
    print("─" * 55)

    print("Total tip $ collected per day:")
    print(tips.groupby("day")["tip"].sum())

    print("Largest single bill per day:")
    print(tips.groupby("day")["total_bill"].max())
    print()


# ── Section 3: size() vs count() ──────────────────────────────────────────────

def section_size_vs_count(tips, planets):
    print("─" * 55)
    print("SECTION 3: .size() vs .count()")
    print("─" * 55)

    print("size() -- rows per day:")
    print(tips.groupby("day").size())

    print("count() -- non-null values per column, per day:")
    print(tips.groupby("day").count())
    print()

    size_per_method = planets.groupby("method").size()
    mass_count_per_method = planets.groupby("method")["mass"].count()
    comparison = pd.DataFrame({
        "size (all rows)": size_per_method,
        "count (non-null mass)": mass_count_per_method,
    })
    print("planets.csv -- size() vs count() on 'mass':")
    print(comparison)
    print()


# ── Section 4: Grouping by Multiple Columns ──────────────────────────────────

def section_multi_column(tips):
    print("─" * 55)
    print("SECTION 4: Grouping by Multiple Columns")
    print("─" * 55)

    avg_tip_by_day_time = tips.groupby(["day", "time"])["tip"].mean()
    print("Average tip by day AND time:")
    print(avg_tip_by_day_time)

    avg_tip_flat = avg_tip_by_day_time.reset_index()
    print("After reset_index():")
    print(avg_tip_flat)
    print()


# ── Section 5: .agg() ─────────────────────────────────────────────────────────

def section_agg(tips):
    print("─" * 55)
    print("SECTION 5: Multiple Aggregations — .agg()")
    print("─" * 55)

    bill_stats_by_day = tips.groupby("day")["total_bill"].agg(["mean", "max", "count"])
    print("Mean, max, count of total_bill, per day:")
    print(bill_stats_by_day)

    summary_by_day = tips.groupby("day").agg({
        "total_bill": "mean",
        "tip": "max",
        "size": "sum",
    })
    print("Custom per-column aggregation:")
    print(summary_by_day)
    print()


# ── Section 6: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips, planets):
    print("─" * 55)
    print("SECTION 6: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — a groupby object isn't usable until you aggregate it:")
    grouped = tips.groupby("day")
    print(f"  print(grouped): {grouped}")
    print(f"  Correct: {grouped['tip'].mean().to_dict()}")
    print()

    print("Mistake 2 — .size() and .count() can disagree when a column has NaNs:")
    size_per_method = planets.groupby("method").size()
    mass_count_per_method = planets.groupby("method")["mass"].count()
    print(pd.DataFrame({"size": size_per_method, "mass count": mass_count_per_method}))
    print()

    print("Mistake 3 — a grouped result has a (Multi)Index, not columns:")
    avg_by_day = tips.groupby("day")["total_bill"].mean()
    try:
        avg_by_day[avg_by_day["total_bill"] > 18]
    except Exception as e:
        print(f"  Caught error: {type(e).__name__}: {e}")
    avg_by_day_flat = avg_by_day.reset_index()
    print(f"  Correct: {avg_by_day_flat[avg_by_day_flat['total_bill'] > 18]}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 07 — GroupBy")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(TIPS_PATH)
    planets_df = pd.read_csv(PLANETS_PATH)

    section_basics(tips_df)
    section_common_aggregations(tips_df)
    section_size_vs_count(tips_df, planets_df)
    section_multi_column(tips_df)
    section_agg(tips_df)
    section_mistakes(tips_df, planets_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
