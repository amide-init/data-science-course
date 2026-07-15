# Module 06 — Data Cleaning

**Week:** 6
**Goal:** Take a messy real-world dataset and make it analysis-ready — the step that separates a raw export from something you can actually trust.
**Estimated time:** ~8 hours across 6 lessons + project

---

## Why This Module?

Module 05 taught you the pandas mechanics for handling gaps, duplicates, and outliers as they came up. This module steps back and treats data cleaning as its own discipline: a repeatable set of decisions you make on *any* new dataset before you're allowed to trust a single number from it. Real datasets — from Kaggle, from a company database, from a scraped API — are never as clean as `tips.csv` or `planets.csv`. Missing values cluster in patterns that mean something, duplicate rows sneak in from merged exports, outliers are sometimes typos and sometimes the most important rows in the dataset.

By the end of this module, you'll have a mental checklist for cleaning any table, and you'll apply it end-to-end on a real, messy employee dataset.

---

## Lesson List

| # | Folder | Topic |
|---|--------|-------|
| 01 | `lesson-01_missing-values/` | Handling Missing Values — strategies: drop, fill, impute, flag |
| 02 | `lesson-02_duplicates/` | Finding and Removing Duplicates |
| 03 | `lesson-03_outliers/` | Detecting and Handling Outliers (IQR, Z-score) |
| 04 | `lesson-04_encoding/` | Encoding Categorical Variables (Label, One-Hot) |
| 05 | `lesson-05_feature-scaling/` | Feature Scaling (Normalization, Standardization) |
| 06 | `lesson-06_data-transformation/` | Data Transformation (skewness, log transform) |

---

## Project

**Employee Dataset Cleaning**
Folder: `project/`
Students take a real, messy Kaggle employee dataset and apply everything from this module — missing value strategy, duplicate removal, outlier handling, encoding, and scaling — to produce an analysis-ready dataset.

---

## Dataset Sources

- Kaggle: Employee dataset (used in the project)
- `lesson-01_missing-values/data/employees.csv` — a synthetic 60-row HR dataset built for this module, with deliberately realistic missingness patterns (random, group-linked, and structural) for teaching purposes

---

## Tools Used

- `pandas`
- `numpy`
- scikit-learn preprocessing tools are previewed conceptually here and used properly starting in Module 10
