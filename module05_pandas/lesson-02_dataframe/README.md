# Lesson 02 — DataFrame

**Module:** 05 — Pandas
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what a `DataFrame` is and how it relates to a collection of Series
- Create a DataFrame from a dict of lists, a list of dicts, and a NumPy array
- Inspect a DataFrame using `.head()`, `.tail()`, `.shape`, `.columns`, `.dtypes`, `.info()`, and `.describe()`
- Select a single column (returns a Series) versus multiple columns (returns a DataFrame)
- Add a computed column and drop a column
- Select rows with `.loc` / `.iloc`, the same way you did with a Series

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — creating DataFrames, inspection methods, column/row selection, adding and dropping columns |
| `script.py` | Standalone runnable version of all teaching code |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Requires `pandas` and `numpy` (`pip install pandas numpy`).

---

## Prerequisites
- Completed Lesson 01 (Series) — a DataFrame is a collection of Series sharing an index

---

## Next Lesson

**Lesson 03 — Reading CSV and Excel Files** applies everything from this lesson to real files on disk via `pd.read_csv()` and `pd.read_excel()`.
