# Lesson 02 — Finding and Removing Duplicates

**Module:** 06 — Data Cleaning
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect exact duplicate rows with `.duplicated()` and remove them with `.drop_duplicates()`
- Detect **business-key duplicates** — rows that repeat on an identifying column (like an ID) even though other columns differ — using `subset=`
- Decide which duplicate to keep using `keep='first'`, `keep='last'`, or an explicit sort beforehand
- Catch **near-duplicates** caused by inconsistent text formatting (case, whitespace) that `.duplicated()` misses by default
- Recognize when two identical-looking rows are *not* duplicates at all, and shouldn't be merged

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — resolving four kinds of duplicate problems (exact, business-key, re-submitted/updated, near-duplicate text) on a simulated merged HR export |
| `script.py` | Standalone runnable version of all teaching code, ending in a `deduplicate_employees()` pipeline |
| `data/employees_raw.csv` | Synthetic dataset (61 rows) simulating two merged HR system exports: exact duplicate rows, employees re-submitted with an updated salary, and names typed inconsistently across systems |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/employees_raw.csv`.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites

- Completed Lesson 01 (Handling Missing Values — the same employee dataset, minus the missing-value gaps, is the starting point here)
- Comfortable with `.sort_values()` from Module 05, Lesson 05

---

## Next Lesson

**Lesson 03 — Detecting and Handling Outliers** continues the pipeline, using IQR and Z-score methods on the same kind of real-world numeric noise.
