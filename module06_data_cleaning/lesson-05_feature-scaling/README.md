# Lesson 05 — Feature Scaling (Normalization, Standardization)

**Module:** 06 — Data Cleaning
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain why unscaled features distort distance-based and gradient-based algorithms
- Apply **Min-Max normalization** to rescale a column into `[0, 1]`
- Apply **standardization (Z-score)** to rescale a column to mean 0, standard deviation 1
- Apply **robust scaling** (median/IQR) and explain why it handles outliers better than the other two
- Recognize which columns should usually be left unscaled (like one-hot dummy columns)
- Avoid fitting scaling parameters on data that includes what should be a held-out test set

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — Min-Max vs. standardization vs. robust scaling on the same `salary` column, using the genuine outlier kept from Lesson 03 to show why the choice of scaler matters |
| `script.py` | Standalone runnable version of all teaching code: `min_max_scale()`, `standardize()`, `robust_scale()`, and a `scale_employees()` pipeline |
| `data/employees_clean.csv` | The fully-encoded employee dataset from Lesson 04 (numeric + one-hot columns), unchanged — this lesson only rescales it |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/employees_clean.csv`.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites

- Completed Lesson 03 (Outliers) — this lesson reuses the deliberate genuine outlier (Preeti Patel's salary) to demonstrate why Min-Max scaling is outlier-sensitive
- Completed Lesson 04 (Encoding) — starts from the fully-numeric, one-hot encoded dataset

---

## Next Lesson

**Lesson 06 — Data Transformation** tackles skewed distributions with log and other transforms, the last step before this dataset is fully analysis-ready.
