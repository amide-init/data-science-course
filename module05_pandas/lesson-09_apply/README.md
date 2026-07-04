# Lesson 09 — Apply (Custom Functions)

**Module:** 05 — Pandas
**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Use `Series.apply()` to run a custom function (or lambda) over every value in a column
- Use `DataFrame.apply(axis=1)` to run a function across each row, using multiple columns at once
- Use `Series.map()` to substitute values via a dictionary
- Explain why vectorized operations are usually faster than `.apply()`, and when `.apply()` is genuinely needed
- Avoid the classic `axis=0` vs `axis=1` mix-up in `DataFrame.apply()`

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — `Series.apply()`, `DataFrame.apply(axis=1)`, `.map()`, a vectorized-vs-apply timing comparison, common mistakes |
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
- Completed Lesson 08 (Merge and Join)

---

## Next Lesson

**Lesson 10 — Pivot Tables** reshapes a DataFrame into a summary grid, with rows and columns both becoming categories.
