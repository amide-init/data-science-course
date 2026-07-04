# Lesson 10 — Pivot Tables

**Module:** 05 — Pandas
**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Build a summary grid with `pivot_table(values=, index=, columns=, aggfunc=)`
- Apply multiple aggregation functions in one pivot table
- Add row/column totals with `margins=True`
- Handle missing combinations in the grid with `fill_value`
- Explain why `pivot()` fails on data with repeated rows, and why `pivot_table()` doesn't

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — basic pivot tables, `aggfunc`, multiple aggregations, `margins`, `fill_value`, `pivot()` vs `pivot_table()`, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows), reused from earlier lessons |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites
- Completed Lesson 07 (GroupBy) — a pivot table is the same summarization, laid out as a grid instead of a list

---

## Next Up

**Module 05 Project** — an IPL or Netflix dataset analysis using everything from Lessons 01-10: loading, filtering, sorting, cleaning, grouping, merging, and pivoting.
