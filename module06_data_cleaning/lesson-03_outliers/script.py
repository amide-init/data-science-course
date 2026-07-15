"""
Module 06 — Lesson 03: Detecting and Handling Outliers (IQR, Z-Score)

Clean, runnable version of the notebook's teaching code.
"""

import pandas as pd


# ── Load ──

def load_employees(path: str = "data/employees_clean.csv") -> pd.DataFrame:
    """Load the deduplicated employees dataset (picking up after Lessons 01-02)."""
    return pd.read_csv(path)


# ── Detection: IQR (robust to multiple outliers) ──

def iqr_outliers(series: pd.Series):
    """Return (lower_bound, upper_bound, boolean_mask) using the 1.5x IQR fence."""
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return lower, upper, (series < lower) | (series > upper)


# ── Detection: standard Z-score (sensitive to the masking effect) ──

def z_scores(series: pd.Series) -> pd.Series:
    """Standard Z-score using mean/std -- can be masked by other outliers."""
    return (series - series.mean()) / series.std()


# ── Detection: robust (median/MAD) Z-score ──

def robust_z_scores(series: pd.Series) -> pd.Series:
    """Modified Z-score using median/MAD -- resistant to masking."""
    median = series.median()
    mad = (series - median).abs().median()
    return 0.6745 * (series - median) / mad


# ── Fix: correct known data-entry errors, leave genuine values alone ──

def fix_known_errors(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the investigated, row-specific fixes from the lesson.

    employee_id 1021: age typo (missing a digit, 5 -> 50)
    employee_id 1003: salary typo (extra digit, 10x too high)
    employee_id 1047: salary glitch (sign flipped on import)
    employee_id 1034: genuine high earner -- left untouched
    """
    df = df.copy()
    df.loc[df["employee_id"] == 1021, "age"] = 50
    df.loc[df["employee_id"] == 1003, "salary"] = df.loc[df["employee_id"] == 1003, "salary"] / 10
    df.loc[df["employee_id"] == 1047, "salary"] = df.loc[df["employee_id"] == 1047, "salary"].abs()
    return df


if __name__ == "__main__":
    employees = load_employees()

    _, _, age_mask = iqr_outliers(employees["age"])
    print(f"Age outliers (IQR): {age_mask.sum()}")

    salary_lower, salary_upper, salary_mask = iqr_outliers(employees["salary"])
    print(f"Salary outliers (IQR): {salary_mask.sum()}")

    z = z_scores(employees["salary"])
    print(f"Salary outliers (standard Z-score, |z| > 3): {(abs(z) > 3).sum()} "
          f"<- masked by the 744,000 typo inflating std")

    rz = robust_z_scores(employees["salary"])
    print(f"Salary outliers (robust Z-score, |z| > 3.5): {(abs(rz) > 3.5).sum()}")

    fixed = fix_known_errors(employees)
    _, _, salary_mask_after = iqr_outliers(fixed["salary"])
    print(f"Salary outliers remaining after fixing known errors: {salary_mask_after.sum()} "
          f"(the genuine high earner, correctly left flagged)")
