"""
Merge and Join
Module 05, Lesson 08

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TIPS_PATH = os.path.join(DATA_DIR, "tips.csv")

CUSTOMERS = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Aisha", "Ben", "Chen", "Diya"],
})

ORDERS = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 5],  # customer_id 5 doesn't exist in CUSTOMERS
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "amount": [50000, 500, 1500, 8000],
})


# ── Section 1: Basic Inner Join ───────────────────────────────────────────────

def section_inner_join():
    print("─" * 55)
    print("SECTION 1: pd.merge() — The Basic Inner Join")
    print("─" * 55)

    inner = pd.merge(ORDERS, CUSTOMERS, on="customer_id")
    print(f"inner join: {inner.shape[0]} rows")
    print(inner)
    print()


# ── Section 2: The Other Three Join Types ────────────────────────────────────

def section_join_types():
    print("─" * 55)
    print("SECTION 2: The Other Three Join Types")
    print("─" * 55)

    left = pd.merge(ORDERS, CUSTOMERS, on="customer_id", how="left")
    print("how='left':")
    print(left)

    right = pd.merge(ORDERS, CUSTOMERS, on="customer_id", how="right")
    print("how='right':")
    print(right)

    outer = pd.merge(ORDERS, CUSTOMERS, on="customer_id", how="outer")
    print(f"how='outer': {outer.shape[0]} rows")
    print(outer)
    print()


# ── Section 3: left_on / right_on ────────────────────────────────────────────

def section_left_on_right_on():
    print("─" * 55)
    print("SECTION 3: Different Key Names — left_on / right_on")
    print("─" * 55)

    customers_alt_name = CUSTOMERS.rename(columns={"customer_id": "cust_id"})
    merged_alt = pd.merge(ORDERS, customers_alt_name, left_on="customer_id", right_on="cust_id")
    print(merged_alt)
    print()

    return customers_alt_name


# ── Section 4: Merging a groupby() Summary Back onto the Data ───────────────

def section_merge_summary(tips):
    print("─" * 55)
    print("SECTION 4: Merging a groupby() Summary Back onto the Data")
    print("─" * 55)

    avg_tip_by_day = tips.groupby("day")["tip"].mean().reset_index()
    avg_tip_by_day = avg_tip_by_day.rename(columns={"tip": "avg_tip_for_day"})
    print(avg_tip_by_day)

    tips_with_avg = tips.merge(avg_tip_by_day, on="day")
    tips_with_avg["above_day_average"] = tips_with_avg["tip"] > tips_with_avg["avg_tip_for_day"]
    print(f"tips_with_avg.shape: {tips_with_avg.shape}")
    print(tips_with_avg[["day", "tip", "avg_tip_for_day", "above_day_average"]].head(6))
    print()


# ── Section 5: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(customers_alt_name):
    print("─" * 55)
    print("SECTION 5: Common Mistakes")
    print("─" * 55)

    print("Mistake 1 — default how='inner' silently drops unmatched rows:")
    accidental_inner = pd.merge(ORDERS, CUSTOMERS, on="customer_id")
    print(f"  Default merge: {accidental_inner.shape[0]} rows")
    print(f"  Correct, how='left': {pd.merge(ORDERS, CUSTOMERS, on='customer_id', how='left').shape[0]} rows")
    print()

    print("Mistake 2 — merge() can't find a shared column if names don't match:")
    try:
        pd.merge(ORDERS, customers_alt_name, on="customer_id")
    except KeyError as e:
        print(f"  Caught error: {e}")
    print(f"  Correct: {pd.merge(ORDERS, customers_alt_name, left_on='customer_id', right_on='cust_id').shape}")
    print()

    print("Mistake 3 — duplicate keys on both sides multiply rows:")
    customers_with_dup = pd.concat([
        CUSTOMERS,
        pd.DataFrame({"customer_id": [2], "name": ["Ben (duplicate record)"]}),
    ], ignore_index=True)
    surprising = pd.merge(ORDERS, customers_with_dup, on="customer_id")
    print(f"  Result: {surprising.shape[0]} rows (started with {ORDERS.shape[0]} orders)")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 08 — Merge and Join")
    print("=" * 55)
    print()

    tips_df = pd.read_csv(TIPS_PATH)

    section_inner_join()
    section_join_types()
    customers_alt = section_left_on_right_on()
    section_merge_summary(tips_df)
    section_mistakes(customers_alt)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
