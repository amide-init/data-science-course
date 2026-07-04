"""
Apply (Custom Functions)
Module 05, Lesson 09

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os
import time

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "tips.csv")


def categorize_bill(amount):
    if amount < 15:
        return "Low"
    elif amount < 30:
        return "Medium"
    else:
        return "High"


def tip_percentage(row):
    return round(row["tip"] / row["total_bill"] * 100, 1)


# ── Section 1: Series.apply() ─────────────────────────────────────────────────

def section_series_apply(tips):
    print("─" * 55)
    print("SECTION 1: Series.apply() — A Custom Function, One Value at a Time")
    print("─" * 55)

    tips["bill_category"] = tips["total_bill"].apply(categorize_bill)
    print(tips[["total_bill", "bill_category"]].head(8))

    tips["rounded_bill"] = tips["total_bill"].apply(lambda x: round(x))
    print(tips[["total_bill", "rounded_bill"]].head(3))
    print()


# ── Section 2: DataFrame.apply(axis=1) ───────────────────────────────────────

def section_dataframe_apply(tips):
    print("─" * 55)
    print("SECTION 2: DataFrame.apply(axis=1) — A Custom Function, One Row at a Time")
    print("─" * 55)

    tips["tip_pct"] = tips.apply(tip_percentage, axis=1)
    print(tips[["total_bill", "tip", "tip_pct"]].head(5))
    print()


# ── Section 3: Series.map() ───────────────────────────────────────────────────

def section_map(tips):
    print("─" * 55)
    print("SECTION 3: Series.map() — Substituting Values via a Dictionary")
    print("─" * 55)

    day_full_names = {"Thur": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
    tips["day_full"] = tips["day"].map(day_full_names)
    print(tips[["day", "day_full"]].drop_duplicates())
    print()


# ── Section 4: Vectorized vs apply() Timing ──────────────────────────────────

def section_timing(tips):
    print("─" * 55)
    print("SECTION 4: Why Vectorized Operations Usually Beat .apply()")
    print("─" * 55)

    start = time.perf_counter()
    vectorized_result = tips["tip"] / tips["total_bill"] * 100
    vectorized_time = time.perf_counter() - start

    start = time.perf_counter()
    apply_result = tips.apply(lambda row: row["tip"] / row["total_bill"] * 100, axis=1)
    apply_time = time.perf_counter() - start

    print(f"Vectorized time: {vectorized_time * 1000:.3f} ms")
    print(f"apply() time:    {apply_time * 1000:.3f} ms")
    print(f"Results match: {vectorized_result.round(5).equals(apply_result.round(5))}")
    print()


# ── Section 5: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips):
    print("─" * 55)
    print("SECTION 5: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — don't wrap simple arithmetic in apply() at all (see timing above)")
    print()

    print("Mistake 2 — DataFrame.apply() defaults to axis=0 (column-wise):")
    try:
        tips.apply(tip_percentage)
    except Exception as e:
        print(f"  Caught error: {type(e).__name__}: {e}")
    print(f"  Correct, axis=1: {tips.apply(tip_percentage, axis=1).head(3).tolist()}")
    print()

    print("Mistake 3 — .map() with an incomplete dict silently produces NaN:")
    incomplete_map = {"Thur": "Thursday", "Fri": "Friday"}
    mapped = tips["day"].map(incomplete_map)
    print(f"  Missing after incomplete map: {mapped.isna().sum()} of {tips.shape[0]}")
    safe_mapped = tips["day"].map(incomplete_map).fillna(tips["day"])
    print(f"  Missing after fillna() fallback: {safe_mapped.isna().sum()}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 09 — Apply (Custom Functions)")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(CSV_PATH)

    section_series_apply(tips_df)
    section_dataframe_apply(tips_df)
    section_map(tips_df)
    section_timing(tips_df)
    section_mistakes(tips_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
