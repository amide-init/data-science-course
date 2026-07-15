# Lesson 06 — Data Transformation (Skewness, Log Transform)

**Module:** 06 — Data Cleaning
**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Measure **skewness** with `.skew()` and read what the sign and size of the number mean
- Apply a **log transform** (`np.log`, `np.log1p`) to pull in a long right tail
- Apply a **square root transform** as a gentler alternative for moderate skew
- Explain why `np.log1p` (not plain `np.log`) is required for columns that contain zero
- Reverse a transform (`np.expm1`) to bring a value back to its original, interpretable units
- Place transformation correctly in a cleaning pipeline: **before** scaling, not after

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — measuring skew, log vs. log1p vs. sqrt on `salary` and `years_experience`, reversing a transform, and why transformation belongs before scaling in a real pipeline |
| `script.py` | Standalone runnable version of all teaching code: `log1p_transform()`, `log_transform()`, `sqrt_transform()`, `inverse_log1p()`, and a `transform_before_scaling()` pipeline |
| `data/employees_clean.csv` | The same fully-encoded employee dataset from Lesson 04 (unscaled) — this lesson intentionally works from the pre-scaling numbers, since transforms are meant to run before scaling |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/employees_clean.csv`.

Requires `pandas` and `numpy` (`pip install pandas numpy`).

---

## Prerequisites

- Completed Lesson 03 (Outliers) — the genuine high-salary outlier kept there is why `salary`'s skew doesn't fully disappear even after a log transform
- Completed Lesson 05 (Feature Scaling) — this lesson explicitly revisits why transformation should precede scaling in a real pipeline

---

## Next Up

This is the final lesson of Module 06. The **project** (`../project/`) applies every lesson in this module — missing values, duplicates, outliers, encoding, scaling, and transformation — to a full real-world Kaggle employee dataset.
