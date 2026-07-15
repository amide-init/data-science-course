"""
Module 06 — Lesson 02: Finding and Removing Duplicates

Clean, runnable version of the notebook's teaching code.
"""

import pandas as pd


# ── Load ──

def load_employees_raw(path: str = "data/employees_raw.csv") -> pd.DataFrame:
    """Load the merged-export employees dataset, duplicates and all."""
    return pd.read_csv(path)


# ── Step 1: Exact Duplicate Rows ──

def drop_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove fully identical rows (e.g. a re-run import script)."""
    return df.drop_duplicates()


# ── Step 2: Business-Key Duplicates (keep the most recent submission) ──

def drop_business_key_duplicates(df: pd.DataFrame, key: str = "employee_id",
                                  date_col: str = "submitted_date") -> pd.DataFrame:
    """Resolve rows that share a business key but disagree on other columns
    (e.g. a re-submitted salary after a raise) by keeping the latest by date."""
    return (
        df.sort_values(date_col)
        .drop_duplicates(subset=[key], keep="last")
        .sort_values(key)
        .reset_index(drop=True)
    )


# ── Step 3: Normalize Text Before Trusting It ──

def normalize_names(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace and fix casing so text-based comparisons behave consistently."""
    df = df.copy()
    df["name"] = df["name"].str.strip().str.title()
    return df


# ── Full Cleaning Pipeline ──

def deduplicate_employees(path: str = "data/employees_raw.csv") -> pd.DataFrame:
    """Apply the full duplicate-resolution order from the lesson:
    exact dedup -> normalize text -> business-key dedup on the latest submission."""
    df = load_employees_raw(path)
    df = drop_exact_duplicates(df)
    df = normalize_names(df)
    df = drop_business_key_duplicates(df)
    return df


if __name__ == "__main__":
    raw = load_employees_raw()
    print(f"Raw shape: {raw.shape}")
    print(f"Exact duplicate rows: {raw.duplicated().sum()}")
    print(f"Rows sharing an employee_id with another row: "
          f"{raw.duplicated(subset=['employee_id'], keep=False).sum()}")
    print()

    cleaned = deduplicate_employees()
    print(f"Cleaned shape: {cleaned.shape}")
    print(f"Remaining duplicate employee_ids: {cleaned.duplicated(subset=['employee_id']).sum()}")
