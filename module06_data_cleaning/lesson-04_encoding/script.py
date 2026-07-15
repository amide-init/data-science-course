"""
Module 06 — Lesson 04: Encoding Categorical Variables (Label, One-Hot)

Clean, runnable version of the notebook's teaching code.
"""

import pandas as pd

PERFORMANCE_ORDER = {
    "Needs Improvement": 0,
    "Meets Expectations": 1,
    "Exceeds Expectations": 2,
    "Outstanding": 3,
}


# ── Load ──

def load_employees(path: str = "data/employees_clean.csv") -> pd.DataFrame:
    """Load the numerically-clean employees dataset (picking up after Lessons 01-03)."""
    return pd.read_csv(path)


# ── Ordinal Encoding ──

def encode_performance_band(df: pd.DataFrame) -> pd.DataFrame:
    """Map performance_band to an explicit ordinal scale. NaN (never reviewed) stays NaN."""
    df = df.copy()
    df["performance_band_encoded"] = df["performance_band"].map(PERFORMANCE_ORDER)
    return df


# ── One-Hot Encoding ──

def encode_department(df: pd.DataFrame, drop_first: bool = True) -> pd.DataFrame:
    """One-hot encode the nominal department column. drop_first avoids the dummy variable trap
    for linear models; tree-based models generally don't need it."""
    dummies = pd.get_dummies(df["department"], prefix="dept", drop_first=drop_first)
    return pd.concat([df, dummies], axis=1)


# ── Full Encoding Pipeline ──

def encode_employees(path: str = "data/employees_clean.csv") -> pd.DataFrame:
    """Apply both encodings and drop the original text columns, leaving a model-ready table."""
    df = load_employees(path)
    df = encode_performance_band(df)
    df = encode_department(df)
    return df.drop(columns=["department", "performance_band"])


if __name__ == "__main__":
    employees = load_employees()
    print(f"Raw shape: {employees.shape}")
    print(f"department unique values: {employees['department'].nunique()}")
    print(f"performance_band unique values: {employees['performance_band'].nunique()} "
          f"(+ {employees['performance_band'].isna().sum()} not-yet-reviewed)")
    print()

    ready = encode_employees()
    print(f"Encoded shape: {ready.shape}")
    print(f"Columns: {list(ready.columns)}")
