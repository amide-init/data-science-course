"""
Selecting Rows and Columns, Filtering
Module 05, Lesson 04

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "tips.csv")


# ── Section 1: Boolean Filtering Basics ──────────────────────────────────────

def section_boolean_basics(tips):
    print("─" * 55)
    print("SECTION 1: Boolean Filtering — The Basic Pattern")
    print("─" * 55)

    is_dinner = tips["time"] == "Dinner"
    dinner_only = tips[is_dinner]
    print(f"Dinner rows: {dinner_only.shape}")

    big_bills = tips[tips["total_bill"] > 30]
    print(f"Bills over $30: {big_bills.shape[0]} rows")
    print()


# ── Section 2: Combining Multiple Conditions ─────────────────────────────────

def section_combining_conditions(tips):
    print("─" * 55)
    print("SECTION 2: Combining Multiple Conditions")
    print("─" * 55)

    no_smoke_dinner = tips[(tips["smoker"] == "No") & (tips["time"] == "Dinner")]
    print(f"Non-smokers at dinner: {no_smoke_dinner.shape[0]} rows")

    weekend = tips[(tips["day"] == "Sat") | (tips["day"] == "Sun")]
    print(f"Saturday or Sunday: {weekend.shape[0]} rows")
    print()

    return weekend


# ── Section 3: .isin() ────────────────────────────────────────────────────────

def section_isin(tips, weekend):
    print("─" * 55)
    print("SECTION 3: .isin() — Membership in a List")
    print("─" * 55)

    weekend_isin = tips[tips["day"].isin(["Sat", "Sun"])]
    print(f".isin(['Sat', 'Sun']): {weekend_isin.shape[0]} rows")
    print(f"Matches OR version: {weekend_isin.shape[0] == weekend.shape[0]}")
    print()


# ── Section 4: .between() ────────────────────────────────────────────────────

def section_between(tips):
    print("─" * 55)
    print("SECTION 4: .between() — Filtering a Numeric Range")
    print("─" * 55)

    mid_range_bills = tips[tips["total_bill"].between(10, 20)]
    print(f"Bills between $10 and $20: {mid_range_bills.shape[0]} rows")
    print()


# ── Section 5: .loc — Filter Rows AND Select Columns ─────────────────────────

def section_loc(tips):
    print("─" * 55)
    print("SECTION 5: Filtering Rows AND Selecting Columns — .loc")
    print("─" * 55)

    dinner_bills_only = tips.loc[tips["time"] == "Dinner", ["total_bill", "tip"]]
    print(dinner_bills_only.head())
    print()


# ── Section 6: .query() ──────────────────────────────────────────────────────

def section_query(tips):
    print("─" * 55)
    print("SECTION 6: .query() — A Readable Alternative")
    print("─" * 55)

    via_boolean = tips[(tips["total_bill"] > 30) & (tips["size"] <= 2)]
    via_query = tips.query("total_bill > 30 and size <= 2")

    print(f"Boolean indexing shape: {via_boolean.shape}")
    print(f"query() shape:          {via_query.shape}")
    matches = via_boolean.reset_index(drop=True).equals(via_query.reset_index(drop=True))
    print(f"Results match: {matches}")
    print()


# ── Section 7: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips):
    print("─" * 55)
    print("SECTION 7: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — Python's `and` doesn't work element-by-element on a Series:")
    try:
        tips[tips["smoker"] == "No" and tips["time"] == "Dinner"]
    except ValueError as e:
        print(f"  Caught error: {e}")
    print(f"  Correct: {tips[(tips['smoker'] == 'No') & (tips['time'] == 'Dinner')].shape}")
    print()

    print("Mistake 2 — `&` binds tighter than `==`, so skipping parentheses breaks:")
    try:
        tips[tips["smoker"] == "No" & tips["time"] == "Dinner"]
    except TypeError as e:
        print(f"  Caught error: {e}")
    print(f"  Correct: {tips[(tips['smoker'] == 'No') & (tips['time'] == 'Dinner')].shape}")
    print()

    print("Mistake 3 — chained indexing when assigning to a filtered result:")
    tips_copy = tips.copy()
    tips_copy.loc[tips_copy["size"] > 4, "tip"] = 0
    print("  Correct: use .loc with row condition AND column in ONE lookup.")
    print(tips_copy[tips_copy["size"] > 4].head(3))
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 04 — Selecting Rows/Columns, Filtering")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(CSV_PATH)

    section_boolean_basics(tips_df)
    weekend_df = section_combining_conditions(tips_df)
    section_isin(tips_df, weekend_df)
    section_between(tips_df)
    section_loc(tips_df)
    section_query(tips_df)
    section_mistakes(tips_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
