# Lesson 03 — Reading CSV and Excel Files

**Module:** 05 — Pandas
**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Load a real CSV file into a DataFrame with `pd.read_csv()`, and use its key parameters: `sep`, `header`, `index_col`, `usecols`, `nrows`
- Load an Excel workbook with `pd.read_excel()`, including picking a specific sheet with `sheet_name`
- Save a DataFrame back to disk with `.to_csv()` and `.to_excel()` without creating a stray index column
- Apply the "first look" habit (`.head()`, `.info()`, `.shape`, `.describe()`) to a freshly loaded real dataset
- Diagnose and fix the most common file-loading errors: wrong path, wrong separator, wrong sheet

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — reading CSV/Excel files, key parameters, saving back to disk, common mistakes |
| `script.py` | Standalone runnable version of all teaching code |
| `data/tips.csv` | Restaurant tips dataset (244 rows) — [seaborn-data](https://github.com/mwaskom/seaborn-data), public domain example data |
| `data/tips.xlsx` | Same dataset as an Excel workbook with two sheets: `tips` (all rows) and `tips_sample` (first 20 rows), used to demo `sheet_name` |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/tips.csv` (relative to the notebook) or a path built from the script's own location.

Requires `pandas` and `openpyxl` (`pip install pandas openpyxl`).

---

## Prerequisites
- Completed Lesson 02 (DataFrame) — this lesson loads real files into the same DataFrame structure you built by hand there

---

## Next Lesson

**Lesson 04 — Selecting Rows and Columns, Filtering** uses the `tips` DataFrame you can now load from disk to answer real questions about it.
