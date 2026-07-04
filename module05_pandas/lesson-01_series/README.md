# Lesson 01 — Series

**Module:** 05 — Pandas
**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what a pandas `Series` is and how it relates to a NumPy array and a Python dict
- Create a Series from a list, a dict, and a scalar
- Understand the index and how it differs from plain positional access
- Access values by label (`.loc`) versus by position (`.iloc`)
- Perform vectorized arithmetic and boolean filtering on a Series
- Recognize missing values (`NaN`) using `.isna()` / `.notna()`

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — creating Series, custom indexes, `.loc`/`.iloc`, vectorized arithmetic, boolean filtering, and a first look at missing values |
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
- Basic Python: lists, dicts (Module 02)
- Module 04 (NumPy) is helpful background but not required — a Series is introduced here from first principles

---

## This Is the First Lesson of Module 05

Next up: **Lesson 02 — DataFrame**, the two-dimensional structure built from multiple Series sharing an index — think of it as a full spreadsheet instead of a single column.
