# Lesson 08 — Merge and Join

**Module:** 05 — Pandas
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Combine two DataFrames on a shared key column with `pd.merge()`
- Explain the difference between `how='inner'`, `'left'`, `'right'`, and `'outer'`, and when each row-survival rule matters
- Merge tables whose key columns have different names using `left_on` / `right_on`
- Merge a `groupby()` summary back onto the original detail rows
- Recognize when duplicate keys cause a merge to unexpectedly multiply rows

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — inner/left/right/outer joins, `left_on`/`right_on`, merging a groupby summary back onto data, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows), reused from earlier lessons — used for the groupby-summary merge example |

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
- Completed Lesson 07 (GroupBy) — this lesson merges a groupby summary back onto the original data

---

## Next Lesson

**Lesson 09 — Apply (Custom Functions)** goes beyond built-in aggregations, letting you run your own function across every row or column.
