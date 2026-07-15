# Lesson 01 — Handling Missing Values (Drop, Fill, or Impute?)

**Module:** 06 — Data Cleaning
**Duration:** ~55 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain the difference between data missing *at random* and missing *for a reason* (MCAR / MAR / MNAR, in plain English)
- Choose between **deletion**, **statistical imputation**, **group-wise imputation**, and **flagging** for a given column
- Impute per-group values with `groupby().transform()`, and explain why an overall mean/median can be the wrong fill value
- Build a **missing indicator** column to preserve the signal that a value was missing in the first place
- Avoid the classic imputation mistake: computing fill values from the *whole* dataset before a train/test split

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — a strategy-per-column decision framework (drop / impute / group-impute / flag), applied to a messy employee dataset |
| `script.py` | Standalone runnable version of all teaching code, organized as one function per strategy plus a full `clean_employees()` pipeline |
| `data/employees.csv` | Synthetic HR dataset (60 employees) with deliberately realistic missingness: random gaps in `age`, department-linked gaps in `salary`, and structural gaps in `performance_rating` for employees on probation |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/employees.csv`.

Requires `pandas` and `numpy` (`pip install pandas numpy`).

---

## Prerequisites

- Completed Module 05, Lesson 06 (Handling Missing Values — the pandas mechanics: `.isna()`, `.dropna()`, `.fillna()`, disguised placeholder strings)
- Comfortable with `.groupby()` from Module 05, Lesson 07

This lesson builds on that mechanical foundation and focuses on the *decision* — which strategy fits which column, and why.

---

## Next Lesson

**Lesson 02 — Finding and Removing Duplicates** continues the data-cleaning pipeline on the same kind of messy real-world data.
