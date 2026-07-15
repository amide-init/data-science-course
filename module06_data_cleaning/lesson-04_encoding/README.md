# Lesson 04 — Encoding Categorical Variables (Label, One-Hot)

**Module:** 06 — Data Cleaning
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Distinguish **nominal** categories (no natural order) from **ordinal** categories (a real order) and explain why that distinction picks the encoding method
- Apply **ordinal encoding** with an explicit, meaningful order using `.map()`
- Apply **one-hot encoding** with `pd.get_dummies()` for nominal categories
- Explain why naively label-encoding a nominal column invents a false numeric relationship between categories
- Recognize the **dummy variable trap** and when `drop_first=True` matters

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — ordinal encoding `performance_band` by hand, one-hot encoding `department`, and why swapping the two approaches breaks each column |
| `script.py` | Standalone runnable version of all teaching code, ending in an `encode_employees()` pipeline |
| `data/employees_clean.csv` | The employee dataset from Lessons 01-03 (numerically clean), with a new `performance_band` column (derived from the earlier `performance_rating`) added to give this lesson both a nominal and an ordinal example |

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

- Completed Lessons 01-03 (this lesson picks up the same employee dataset immediately after outlier correction)
- Comfortable with `.map()` and boolean columns from earlier pandas lessons

---

## Next Lesson

**Lesson 05 — Feature Scaling** normalizes and standardizes the now fully-numeric dataset so no single column's scale dominates a model.
