# Lesson 05 — Sorting Data

**Module:** 05 — Pandas
**Duration:** ~40 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Sort a DataFrame by one column, ascending or descending, with `.sort_values()`
- Sort by multiple columns at once, with a different direction per column
- Sort by the row index with `.sort_index()`
- Grab the top/bottom N rows directly with `.nlargest()` / `.nsmallest()`
- Avoid the two most common sorting mistakes: forgetting sorting isn't in-place, and mismatched `ascending` lists

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — single/multi-column sorting, `.sort_index()`, `.nlargest()`/`.nsmallest()`, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows), reused from Lesson 03/04 |

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
- Completed Lesson 04 (Selecting Rows and Columns, Filtering) — this lesson sorts the same `tips` DataFrame

---

## Next Lesson

**Lesson 06 — Handling Missing Values** covers strategies (drop, fill, impute) for the gaps that most real datasets have.
