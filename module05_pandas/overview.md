# Module 05 — Pandas

**Week:** 5
**Goal:** Load, inspect, filter, and summarize real tabular data — the single most-used skill in this entire course.
**Estimated time:** ~9 hours across 10 lessons + project

---

## Why This Module?

Almost every dataset you'll ever touch — a CSV export, a spreadsheet, a database query result — is a table: rows and columns, often with messy gaps and mixed types. Pandas is the standard Python tool for exactly this job. It's built directly on top of NumPy (Module 04), adding row/column labels and a huge library of table operations: filtering, grouping, joining, reshaping.

By the end of this module, you'll be comfortable taking any raw CSV file and turning it into answers — which is the core loop you'll repeat in every module from here to the capstone.

---

## Lesson List

| # | Folder | Topic |
|---|--------|-------|
| 01 | `lesson-01_series/` | Series |
| 02 | `lesson-02_dataframe/` | DataFrame |
| 03 | `lesson-03_read-csv-excel/` | Reading CSV and Excel files |
| 04 | `lesson-04_selecting-filtering/` | Selecting Rows and Columns, Filtering |
| 05 | `lesson-05_sorting/` | Sorting Data |
| 06 | `lesson-06_missing-values/` | Handling Missing Values |
| 07 | `lesson-07_groupby/` | GroupBy |
| 08 | `lesson-08_merge-join/` | Merge and Join |
| 09 | `lesson-09_apply/` | Apply (custom functions) |
| 10 | `lesson-10_pivot-tables/` | Pivot Tables |

---

## Project

**IPL / Netflix Dataset Analysis**
Folder: `project/`
Students load a real Kaggle dataset (IPL match data or Netflix titles) and use everything from this module — filtering, sorting, grouping, merging — to answer real questions about it.

---

## Dataset Sources
- Kaggle: IPL Ball-by-Ball / Matches dataset
- Kaggle: Netflix Movies and TV Shows dataset

---

## Tools Used
- `pandas`
- `numpy` (as the foundation underneath every Series)

---

## Learning Progression

```
Series  ← "one labeled column"
      ↓
DataFrame  ← "many Series sharing an index — a whole table"
      ↓
Reading CSV/Excel  ← "get real data into a DataFrame"
      ↓
Selecting / Filtering  ← "grab exactly the rows and columns you need"
      ↓
Sorting  ← "order rows by a column's value"
      ↓
Missing Values  ← "handle the gaps every real dataset has"
      ↓
GroupBy  ← "summarize data by category"
      ↓
Merge / Join  ← "combine two tables into one"
      ↓
Apply  ← "run your own custom logic across rows or columns"
      ↓
Pivot Tables  ← "reshape a table into a summary grid"
```
