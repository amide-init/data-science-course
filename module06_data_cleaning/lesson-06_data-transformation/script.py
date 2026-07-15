"""
Module 06 — Lesson 06: Data Transformation (Skewness, Log Transform)

Clean, runnable version of the notebook's teaching code.
"""

import numpy as np
import pandas as pd


# ── Load ──

def load_employees(path: str = "data/employees_clean.csv") -> pd.DataFrame:
    """Load the fully-encoded employees dataset (picking up after Lesson 04)."""
    return pd.read_csv(path)


# ── Transforms ──

def log1p_transform(series: pd.Series) -> pd.Series:
    """log(1 + x) -- safe for columns that contain 0, unlike plain log."""
    return np.log1p(series)


def log_transform(series: pd.Series) -> pd.Series:
    """Plain log -- only safe for strictly positive columns."""
    return np.log(series)


def sqrt_transform(series: pd.Series) -> pd.Series:
    """Square root -- a gentler fix for moderate skew, safe at 0."""
    return np.sqrt(series)


def inverse_log1p(series: pd.Series) -> pd.Series:
    """Reverse a log1p transform back to original units."""
    return np.expm1(series)


# ── Full Pre-Scaling Transform Pipeline ──

def transform_before_scaling(df: pd.DataFrame) -> pd.DataFrame:
    """Fix skewness in the columns that need it, before any scaling step (Lesson 05)."""
    df = df.copy()
    df["years_experience"] = log1p_transform(df["years_experience"])
    df["salary"] = log_transform(df["salary"])
    return df


if __name__ == "__main__":
    employees = load_employees()
    print(f"Raw shape: {employees.shape}")
    print("Skewness before transform:")
    print(employees[["age", "years_experience", "salary"]].skew().round(3))

    transformed = transform_before_scaling(employees)
    print("\nSkewness after transform:")
    print(transformed[["age", "years_experience", "salary"]].skew().round(3))
