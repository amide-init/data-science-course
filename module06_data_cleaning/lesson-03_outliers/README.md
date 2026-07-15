# Lesson 03 — Detecting and Handling Outliers (IQR, Z-Score)

**Module:** 06 — Data Cleaning
**Duration:** ~55 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect outliers with the **IQR method** (quartiles and the 1.5×IQR fence)
- Detect outliers with the **Z-score method**, and explain why it can be fooled by the very outliers it's trying to find (the *masking effect*)
- Use a **robust (median/MAD-based) Z-score** as a fix for that weakness
- Investigate *why* a value is extreme before deciding what to do with it — a typo, a data glitch, or a genuine real-world extreme value each need a different fix
- Apply the right fix per case: correct, cap (winsorize), remove, or keep unchanged

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — IQR vs. standard Z-score vs. robust Z-score on the same messy salary column, then a per-row investigate-and-fix pass |
| `script.py` | Standalone runnable version of all teaching code: `iqr_outliers()`, `z_scores()`, `robust_z_scores()`, `fix_known_errors()` |
| `data/employees_clean.csv` | The employee dataset from Lessons 01-02 (missing values handled, duplicates resolved), with four deliberately planted numeric problems: an age typo, a 10x salary typo, a sign-flipped negative salary, and one genuine high earner |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

Run from inside this lesson folder — both files load data using the path `data/employees_clean.csv`.

Requires `pandas` (`pip install pandas`).

---

## Prerequisites

- Completed Lesson 01 (Handling Missing Values) and Lesson 02 (Finding and Removing Duplicates) — this lesson picks up the same employee dataset immediately after both cleaning steps
- Comfortable with `.quantile()` and basic descriptive statistics from Module 03

---

## Next Lesson

**Lesson 04 — Encoding Categorical Variables** turns the now-numerically-clean dataset's text columns (like `department`) into a form models can use.
