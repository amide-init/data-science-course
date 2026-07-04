"""
Sorting Data
Module 05, Lesson 05

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "tips.csv")


# ── Section 1: Sorting by One Column ─────────────────────────────────────────

def section_single_column_sort(tips):
    print("─" * 55)
    print("SECTION 1: Sorting by One Column")
    print("─" * 55)

    by_bill_asc = tips.sort_values(by="total_bill")
    print("Smallest bills first:")
    print(by_bill_asc.head(3))

    by_bill_desc = tips.sort_values(by="total_bill", ascending=False)
    print("Largest bills first:")
    print(by_bill_desc.head(3))

    reindexed = by_bill_desc.reset_index(drop=True)
    print("Same sort, with a clean new index:")
    print(reindexed.head(3))
    print()


# ── Section 2: Sorting by Multiple Columns ───────────────────────────────────

def section_multi_column_sort(tips):
    print("─" * 55)
    print("SECTION 2: Sorting by Multiple Columns")
    print("─" * 55)

    by_day_then_bill = tips.sort_values(by=["day", "total_bill"])
    print(by_day_then_bill.head(6))

    mixed_directions = tips.sort_values(by=["day", "total_bill"], ascending=[True, False])
    print(mixed_directions.head(6))
    print()


# ── Section 3: Sorting by the Index ──────────────────────────────────────────

def section_sort_index(tips):
    print("─" * 55)
    print("SECTION 3: Sorting by the Index — .sort_index()")
    print("─" * 55)

    shuffled = tips.sort_values(by="tip", ascending=False)
    print(f"After sorting by tip, index is shuffled: {shuffled.head(3).index.tolist()}")

    restored = shuffled.sort_index()
    print(f"sort_index() restores order: {restored.head(3).index.tolist()}")
    print()


# ── Section 4: nlargest() / nsmallest() ──────────────────────────────────────

def section_nlargest_nsmallest(tips):
    print("─" * 55)
    print("SECTION 4: .nlargest() / .nsmallest()")
    print("─" * 55)

    print("Top 5 tips:")
    print(tips.nlargest(5, "tip"))

    print("3 smallest bills:")
    print(tips.nsmallest(3, "total_bill"))
    print()


# ── Section 5: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(tips):
    print("─" * 55)
    print("SECTION 5: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — sort_values() without reassigning does nothing:")
    tips_copy = tips.copy()
    tips_copy.sort_values(by="total_bill")  # return value thrown away
    print(f"  Unchanged order: {tips_copy.head(3).index.tolist()}")
    tips_copy = tips_copy.sort_values(by="total_bill")
    print(f"  Correct, reassigned: {tips_copy.head(3).index.tolist()}")
    print()

    print("Mistake 2 — ascending list length must match by list length:")
    try:
        tips.sort_values(by=["day", "total_bill"], ascending=[True])
    except ValueError as e:
        print(f"  Caught error: {e}")
    print()

    print("Mistake 3 — sorting a numeric-looking column stored as text:")
    messy = pd.DataFrame({"code": ["9", "10", "2", "21"]})
    print(f"  As text: {messy.sort_values(by='code')['code'].tolist()}")
    messy["code"] = messy["code"].astype(int)
    print(f"  As int:  {messy.sort_values(by='code')['code'].tolist()}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 05 — Sorting Data")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(CSV_PATH)

    section_single_column_sort(tips_df)
    section_multi_column_sort(tips_df)
    section_sort_index(tips_df)
    section_nlargest_nsmallest(tips_df)
    section_mistakes(tips_df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
