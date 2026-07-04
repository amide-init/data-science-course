"""
DataFrame
Module 05, Lesson 02

Standalone runnable version of all teaching code from the notebook.
Usage: python script.py
"""

import numpy as np
import pandas as pd

STUDENT_DATA = {
    "name": ["Aisha", "Ben", "Chen", "Diya", "Elan"],
    "age": [20, 21, 19, 22, 20],
    "score": [88, 92, 79, 95, 61],
}

ORDERS = [
    {"order_id": 1, "product": "Notebook", "quantity": 3, "price": 45},
    {"order_id": 2, "product": "Pen", "quantity": 10, "price": 10},
    {"order_id": 3, "product": "Eraser", "quantity": 5, "price": 5},
]


# ── Section 1: DataFrame from a Dict of Lists ────────────────────────────────

def section_from_dict_of_lists():
    print("─" * 55)
    print("SECTION 1: Creating a DataFrame from a Dict of Lists")
    print("─" * 55)

    df = pd.DataFrame(STUDENT_DATA)
    print(df)
    print(f"type: {type(df)}")
    print()

    return df


# ── Section 2: DataFrame from a List of Dicts ────────────────────────────────

def section_from_list_of_dicts():
    print("─" * 55)
    print("SECTION 2: Creating a DataFrame from a List of Dicts")
    print("─" * 55)

    orders_df = pd.DataFrame(ORDERS)
    print(orders_df)
    print()

    return orders_df


# ── Section 3: DataFrame from a NumPy Array ──────────────────────────────────

def section_from_numpy_array():
    print("─" * 55)
    print("SECTION 3: Creating a DataFrame from a NumPy Array")
    print("─" * 55)

    scores_array = np.array([[88, 92, 79], [95, 61, 70]])
    scores_df = pd.DataFrame(scores_array, columns=["Quiz1", "Quiz2", "Quiz3"])
    print(scores_df)
    print()


# ── Section 4: Inspecting a DataFrame ────────────────────────────────────────

def section_inspecting(df):
    print("─" * 55)
    print("SECTION 4: Inspecting a DataFrame")
    print("─" * 55)

    print(f"df.shape   : {df.shape}")
    print(f"df.columns : {list(df.columns)}")
    print(f"df.index   : {list(df.index)}")
    print("df.dtypes:")
    print(df.dtypes)
    print()

    print("df.head(3):")
    print(df.head(3))
    print("df.tail(2):")
    print(df.tail(2))
    print()

    print("df.info():")
    df.info()
    print()

    print("df.describe():")
    print(df.describe())
    print()


# ── Section 5: Single vs Double Bracket Selection ────────────────────────────

def section_column_selection(df):
    print("─" * 55)
    print("SECTION 5: Selecting Columns — Single vs Double Bracket")
    print("─" * 55)

    single_column = df["score"]
    single_column_as_df = df[["score"]]
    multiple_columns = df[["name", "score"]]

    print(f"df['score'] type    : {type(single_column).__name__}")
    print(f"df[['score']] type  : {type(single_column_as_df).__name__}")
    print("df[['name', 'score']]:")
    print(multiple_columns)
    print()


# ── Section 6: Selecting Rows ─────────────────────────────────────────────────

def section_row_selection(df):
    print("─" * 55)
    print("SECTION 6: Selecting Rows — .loc and .iloc")
    print("─" * 55)

    print("df.loc[2]:")
    print(df.loc[2])
    print()
    print("df.iloc[0:2]:")
    print(df.iloc[0:2])
    print()
    print(f"df.loc[1, 'score'] = {df.loc[1, 'score']}")
    print()


# ── Section 7: Adding a Computed Column ──────────────────────────────────────

def section_add_column(orders_df):
    print("─" * 55)
    print("SECTION 7: Adding a New Column")
    print("─" * 55)

    orders_df = orders_df.copy()
    orders_df["total"] = orders_df["quantity"] * orders_df["price"]
    print(orders_df)
    print()

    return orders_df


# ── Section 8: Dropping a Column ─────────────────────────────────────────────

def section_drop_column(orders_df):
    print("─" * 55)
    print("SECTION 8: Dropping a Column")
    print("─" * 55)

    orders_no_price = orders_df.drop(columns=["price"])
    print("After dropping 'price':")
    print(orders_no_price)
    print("Original is unchanged:")
    print(orders_df)
    print()


# ── Section 9: Common Mistakes ────────────────────────────────────────────────

def section_mistakes(df):
    print("─" * 55)
    print("SECTION 9: Common Mistakes")
    print("─" * 55)

    as_series = df["name"]
    as_dataframe = df[["name"]]
    print(f"Mistake 1 — df['name']={type(as_series).__name__}  "
          f"df[['name']]={type(as_dataframe).__name__}")

    try:
        df.drop("score")
    except KeyError as e:
        print(f"Mistake 2 — {e}")
    print(df.drop(columns=["score"]))

    df = df.copy()
    print("Mistake 3 — use .loc for combined row+column assignment:")
    df.loc[df["score"] < 70, "score"] = 70
    print(df)
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE 05 LESSON 02 — DataFrame")
    print("=" * 55)
    print()

    df = section_from_dict_of_lists()
    orders_df = section_from_list_of_dicts()
    section_from_numpy_array()
    section_inspecting(df)
    section_column_selection(df)
    section_row_selection(df)
    orders_df = section_add_column(orders_df)
    section_drop_column(orders_df)
    section_mistakes(df)

    print("=" * 55)
    print("  All sections complete.")
    print("=" * 55)
