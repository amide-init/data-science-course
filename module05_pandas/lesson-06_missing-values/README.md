# Lesson 06 — Handling Missing Values

**Module:** 05 — Pandas
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect missing values with `.isna()` / `.isnull()`, and count them per column with `.sum()`
- Judge severity with the *percentage* missing per column, not just the raw count
- Remove missing data with `.dropna()` — scoped by `subset`, `thresh`, or `axis`
- Fill missing data with `.fillna()` — a constant, the column mean/median, or forward/backward fill
- Recognize that missing values aren't always `NaN` — some arrive disguised as strings like `"N/A"` or `"--"`

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — detecting, dropping, and filling missing values; choosing a per-column strategy; common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/planets.csv` | Confirmed exoplanet discoveries dataset (1,035 rows) — [seaborn-data](https://github.com/mwaskom/seaborn-data), public domain example data with real missing values in `orbital_period`, `mass`, and `distance` |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/planets.csv`.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites
- Completed Lesson 05 (Sorting Data)
- Comfortable with `.isna()`-style boolean masks from Lesson 04 (Selecting/Filtering)

---

## Next Lesson

**Lesson 07 — GroupBy** takes a cleaned dataset and starts summarizing it by category.
