"""
Module 06 — Lesson 05: Feature Scaling (Normalization, Standardization)

Clean, runnable version of the notebook's teaching code.
"""

import pandas as pd

COLUMNS_TO_SCALE = ["age", "years_experience", "salary", "performance_band_encoded"]


# ── Load ──

def load_employees(path: str = "data/employees_clean.csv") -> pd.DataFrame:
    """Load the fully-encoded employees dataset (picking up after Lesson 04)."""
    return pd.read_csv(path)


# ── Min-Max Normalization ──

def min_max_scale(series: pd.Series) -> pd.Series:
    """Rescale to [0, 1]. Sensitive to outliers -- min/max are the most extreme values."""
    return (series - series.min()) / (series.max() - series.min())


# ── Standardization (Z-Score) ──

def standardize(series: pd.Series) -> pd.Series:
    """Rescale to mean 0, std 1. Somewhat sensitive to outliers via mean/std."""
    return (series - series.mean()) / series.std()


# ── Robust Scaling ──

def robust_scale(series: pd.Series) -> pd.Series:
    """Rescale using median/IQR instead of mean/std -- least sensitive to outliers."""
    median = series.median()
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    return (series - median) / iqr


# ── Full Scaling Pipeline ──

def scale_employees(path: str = "data/employees_clean.csv", method: str = "robust") -> pd.DataFrame:
    """Scale only the continuous columns; leave IDs, names, and one-hot dummies untouched."""
    scalers = {"minmax": min_max_scale, "standard": standardize, "robust": robust_scale}
    scale_fn = scalers[method]

    df = load_employees(path)
    for col in COLUMNS_TO_SCALE:
        df[col] = scale_fn(df[col])
    return df


if __name__ == "__main__":
    employees = load_employees()
    salary = employees["salary"]

    minmax_spread = min_max_scale(salary).quantile(0.75) - min_max_scale(salary).quantile(0.25)
    robust_spread = robust_scale(salary).quantile(0.75) - robust_scale(salary).quantile(0.25)

    print(f"Raw shape: {employees.shape}")
    print(f"Salary middle-50% spread after Min-Max scaling:  {minmax_spread:.3f}")
    print(f"Salary middle-50% spread after Robust scaling:   {robust_spread:.3f}")
    print("(Robust scaling preserves far more separation among typical employees.)")

    scaled = scale_employees(method="robust")
    print(f"\nScaled columns: {COLUMNS_TO_SCALE}")
    print(f"Untouched columns: {[c for c in scaled.columns if c not in COLUMNS_TO_SCALE]}")
