# Lesson 07 — GroupBy

**Module:** 05 — Pandas
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain the split-apply-combine pattern that `.groupby()` implements
- Group by one column and summarize with a single aggregation (`.mean()`, `.sum()`, `.count()`, `.size()`)
- Group by multiple columns at once
- Apply several aggregations in one call with `.agg()`, including different functions per column
- Turn a grouped result back into a normal flat DataFrame with `.reset_index()`

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — split-apply-combine, single/multi-column grouping, `.size()` vs `.count()`, `.agg()`, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows), reused from earlier lessons — primary dataset for this lesson |
| `data/planets.csv` | Exoplanet dataset, reused from Lesson 06 — used only to show `.size()` vs `.count()` diverging on real missing data |

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
- Completed Lesson 06 (Handling Missing Values) — the `.size()` vs `.count()` comparison reuses that lesson's dataset

---

## Next Lesson

**Lesson 08 — Merge and Join** combines separate tables side by side — including grouped summaries with the original data.
