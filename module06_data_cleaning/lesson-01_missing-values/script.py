"""
Module 06 — Lesson 01: Handling Missing Values (Drop, Fill, or Impute?)

Clean, runnable version of the notebook's teaching code.
"""

import numpy as np
import pandas as pd


# ── Load and Clean the Disguised Placeholder ──

def load_employees(path: str = "data/employees.csv") -> pd.DataFrame:
    """Load the employees dataset and convert the 'Not Provided' placeholder to real NaN."""
    df = pd.read_csv(path)
    df["department"] = df["department"].replace("Not Provided", np.nan)
    return df


# ── Strategy 1: Deletion ──

def drop_missing_department(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows missing 'department' — small % missing, no clear pattern (MCAR)."""
    return df.dropna(subset=["department"])


# ── Strategy 2: Simple Statistical Imputation ──

def impute_age_median(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing 'age' with the column median — safe for random (MCAR) gaps."""
    df = df.copy()
    df["age"] = df["age"].fillna(df["age"].median())
    return df


# ── Strategy 3: Group-Wise Imputation ──

def impute_salary_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing 'salary' with each row's own department median (MAR: pattern
    depends on department, so a single overall median would bias the result)."""
    df = df.copy()
    dept_median_salary = df.groupby("department")["salary"].transform("median")
    df["salary"] = df["salary"].fillna(dept_median_salary)
    return df


# ── Strategy 4: Flagging Instead of Faking ──

def add_rating_missing_flag(df: pd.DataFrame) -> pd.DataFrame:
    """Add a missing-indicator column for 'performance_rating' instead of imputing it —
    the gap is structural (MNAR: employee too new to have been reviewed yet)."""
    df = df.copy()
    df["rating_missing"] = df["performance_rating"].isna().astype(int)
    return df


# ── Full Cleaning Pipeline ──

def clean_employees(path: str = "data/employees.csv") -> pd.DataFrame:
    """Apply the full strategy-per-column decision framework from the lesson."""
    df = load_employees(path)
    df = drop_missing_department(df)
    df = impute_age_median(df)
    df = impute_salary_by_department(df)
    df = add_rating_missing_flag(df)
    return df


if __name__ == "__main__":
    raw = load_employees()
    print(f"Raw shape: {raw.shape}")
    print("Missing values per column:")
    print(raw.isna().sum())
    print()

    cleaned = clean_employees()
    print(f"Cleaned shape: {cleaned.shape}")
    print("Missing values per column after cleaning:")
    print(cleaned.isna().sum())
    print()
    print("Median salary by department (used to fill gaps):")
    print(cleaned.groupby("department")["salary"].median().round(0))
