# Lesson 04 — Selecting Rows and Columns, Filtering

**Module:** 05 — Pandas
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Filter rows with a single boolean condition (`df[df['col'] > x]`)
- Combine multiple conditions correctly using `&` / `|` with parentheses (not Python's `and`/`or`)
- Use `.isin()` for membership checks and `.between()` for range checks
- Filter rows AND select columns in one step with `.loc[row_condition, column_list]`
- Recognize and avoid the two most common filtering bugs: operator precedence and chained indexing

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — boolean filtering, combining conditions, `.isin()`, `.between()`, `.loc`, `.query()`, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows), reused from Lesson 03 |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/tips.csv`.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites
- Completed Lesson 03 (Reading CSV and Excel Files) — this lesson filters the same `tips` DataFrame loaded there

---

## Next Lesson

**Lesson 05 — Sorting Data** takes the filtered results from this lesson and orders them by one or more columns.
