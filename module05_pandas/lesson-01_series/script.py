"""
Series
Module 05, Lesson 01

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import numpy as np
import pandas as pd

STUDENTS = ["Aisha", "Ben", "Chen", "Diya", "Elan"]


# ── Section 1: Creating Your First Series ────────────────────────────────────

def section_first_series():
    print("─" * 55)
    print("SECTION 1: Creating Your First Series")
    print("─" * 55)

    scores = pd.Series([88, 92, 79, 95, 61])
    print(scores)
    print(f"type: {type(scores)}")
    print()


# ── Section 2: Giving the Index Meaning ──────────────────────────────────────

def section_custom_index():
    print("─" * 55)
    print("SECTION 2: Giving the Index Meaning")
    print("─" * 55)

    scores = pd.Series([88, 92, 79, 95, 61], index=STUDENTS)
    print(scores)
    print(f"scores['Chen'] = {scores['Chen']}")
    print()

    return scores


# ── Section 3: Series from a Dict ────────────────────────────────────────────

def section_from_dict():
    print("─" * 55)
    print("SECTION 3: Creating a Series from a Dictionary")
    print("─" * 55)

    grades_dict = {"Aisha": 88, "Ben": 92, "Chen": 79, "Diya": 95, "Elan": 61}
    grades = pd.Series(grades_dict)

    print(grades)
    print(f"grades.index  : {list(grades.index)}")
    print(f"grades.values : {grades.values}")
    print()

    return grades


# ── Section 4: Series from a Scalar ──────────────────────────────────────────

def section_from_scalar():
    print("─" * 55)
    print("SECTION 4: Creating a Series from a Scalar")
    print("─" * 55)

    default_attendance = pd.Series(100, index=STUDENTS)
    print(default_attendance)
    print()


# ── Section 5: .loc vs .iloc ──────────────────────────────────────────────────

def section_loc_iloc(grades):
    print("─" * 55)
    print("SECTION 5: Accessing Values — .loc vs .iloc")
    print("─" * 55)

    print(f"grades.loc['Ben']  : {grades.loc['Ben']}")
    print(f"grades.iloc[1]     : {grades.iloc[1]}")
    print()
    print("grades.loc['Ben':'Diya'] (label slice, inclusive):")
    print(grades.loc["Ben":"Diya"])
    print()
    print("grades.iloc[1:4] (position slice, exclusive):")
    print(grades.iloc[1:4])
    print()


# ── Section 6: Vectorized Arithmetic ──────────────────────────────────────────

def section_arithmetic(grades):
    print("─" * 55)
    print("SECTION 6: Vectorized Arithmetic")
    print("─" * 55)

    curved = grades + 5
    scaled = grades * 1.1

    print("Curved (+5):")
    print(curved)
    print("Scaled (x1.1):")
    print(scaled.round(1))
    print()


# ── Section 7: Boolean Filtering ──────────────────────────────────────────────

def section_boolean_filtering(grades):
    print("─" * 55)
    print("SECTION 7: Boolean Filtering")
    print("─" * 55)

    mask = grades >= 90
    print("Boolean mask (grades >= 90):")
    print(mask)
    print("Filtered Series:")
    print(grades[mask])
    print()


# ── Section 8: Missing Values ─────────────────────────────────────────────────

def section_missing_values():
    print("─" * 55)
    print("SECTION 8: A First Look at Missing Values")
    print("─" * 55)

    grades_with_gaps = pd.Series([88, np.nan, 79, np.nan, 61], index=STUDENTS)
    print(grades_with_gaps)
    print(f"Count of missing values: {grades_with_gaps.isna().sum()}")
    print()


# ── Section 9: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(grades):
    print("─" * 55)
    print("SECTION 9: Common Mistakes")
    print("─" * 55)

    custom_index_series = pd.Series([10, 20, 30], index=[5, 6, 7])
    print(f"Mistake 1 — custom_index_series[5]={custom_index_series[5]} "
          f"vs .iloc[0]={custom_index_series.iloc[0]}")

    top_scorers = grades[grades >= 90]
    try:
        top_scorers.iloc[2]
    except IndexError as e:
        print(f"Mistake 2 — {e}")

    monday_sales = pd.Series([100, 200, 300], index=["apple", "banana", "cherry"])
    tuesday_sales = pd.Series([10, 20, 30], index=["banana", "cherry", "date"])
    total = monday_sales + tuesday_sales
    fixed_total = monday_sales.add(tuesday_sales, fill_value=0)
    print("Mistake 3 — plain + produces NaN for unmatched labels:")
    print(total)
    print("Fixed with .add(fill_value=0):")
    print(fixed_total)
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 01 — Series")
    print("=" * 55)
    print()

    section_first_series()
    grades = section_custom_index()
    section_from_dict()
    section_from_scalar()
    section_loc_iloc(grades)
    section_arithmetic(grades)
    section_boolean_filtering(grades)
    section_missing_values()
    section_mistakes(grades)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
