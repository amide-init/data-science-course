"""
Pivot Tables
Module 05, Lesson 10

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "tips.csv")


# ── Section 1: A Basic Pivot Table ───────────────────────────────────────────

def section_basic_pivot(tips):
    print("─" * 55)
    print("SECTION 1: A Basic Pivot Table")
    print("─" * 55)

    avg_tip_grid = tips.pivot_table(values="tip", index="day", columns="time")
    print("Average tip, day x time:")
    print(avg_tip_grid)
    print()


# ── Section 2: Choosing the Aggregation ──────────────────────────────────────

def section_aggfunc(tips):
    print("─" * 55)
    print("SECTION 2: Choosing the Aggregation — aggfunc")
    print("─" * 55)

    total_tip_grid = tips.pivot_table(values="tip", index="day", columns="time", aggfunc="sum")
    print("Total tip $, day x time:")
    print(total_tip_grid)

    count_grid = tips.pivot_table(values="tip", index="day", columns="time", aggfunc="count")
    print("Number of bills, day x time:")
    print(count_grid)
    print()


# ── Section 3: Multiple Aggregations ─────────────────────────────────────────

def section_multi_agg(tips):
    print("─" * 55)
    print("SECTION 3: Multiple Aggregations at Once")
    print("─" * 55)

    multi_agg = tips.pivot_table(values="tip", index="day", columns="time", aggfunc=["mean", "count"])
    print(multi_agg)
    print()


# ── Section 4: margins=True ──────────────────────────────────────────────────

def section_margins(tips):
    print("─" * 55)
    print("SECTION 4: Row and Column Totals — margins=True")
    print("─" * 55)

    with_totals = tips.pivot_table(values="tip", index="day", columns="time", aggfunc="sum", margins=True)
    print(with_totals)
    print()


# ── Section 5: fill_value ────────────────────────────────────────────────────

def section_fill_value(tips):
    print("─" * 55)
    print("SECTION 5: Filling Missing Combinations — fill_value")
    print("─" * 55)

    filled = tips.pivot_table(values="tip", index="day", columns="time", aggfunc="sum", fill_value=0)
    print(filled)
    print()


# ── Section 6: pivot() vs pivot_table() ──────────────────────────────────────

def section_pivot_vs_pivot_table(tips):
    print("─" * 55)
    print("SECTION 6: pivot() vs pivot_table()")
    print("─" * 55)

    dup_count = ((tips["day"] == "Sat") & (tips["time"] == "Dinner")).sum()
    print(f"Sat/Dinner alone has {dup_count} rows -- pivot() can't handle that")

    try:
        tips.pivot(index="day", columns="time", values="tip")
    except ValueError as e:
        print(f"pivot() error: {e}")

    print("pivot_table() handles it fine:")
    print(tips.pivot_table(index="day", columns="time", values="tip").head(2))
    print()


# ── Section 7: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips):
    print("─" * 55)
    print("SECTION 7: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — pivot() fails on repeated index/columns combinations:")
    try:
        tips.pivot(index="day", columns="time", values="total_bill")
    except ValueError as e:
        print(f"  Caught error: {e}")
    print()

    print("Mistake 2 — default aggfunc is 'mean', not 'sum':")
    default_grid = tips.pivot_table(values="tip", index="day", columns="time")
    print(default_grid)
    print()

    print("Mistake 3 — NaN means 'no rows for this combination', not zero:")
    grid = tips.pivot_table(values="tip", index="day", columns="time")
    print(grid)
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 10 — Pivot Tables")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(CSV_PATH)

    section_basic_pivot(tips_df)
    section_aggfunc(tips_df)
    section_multi_agg(tips_df)
    section_margins(tips_df)
    section_fill_value(tips_df)
    section_pivot_vs_pivot_table(tips_df)
    section_mistakes(tips_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
