# Module 03 — Mathematics for Data Science

**Week:** 3  
**Goal:** Get just enough math to understand ML algorithms — intuition over theory.  
**Estimated time:** ~6–7 hours across 9 lessons + project

---

## Why This Module?

Machine learning algorithms are built on three mathematical pillars:
- **Statistics** — describing and summarising data
- **Probability** — quantifying uncertainty and making predictions
- **Linear Algebra** — representing data as vectors and matrices (the native language of ML)

You do not need to prove theorems. You need to understand *what* each concept measures, *why* it matters, and *how* to compute it in Python — so that when scikit-learn reports a standard deviation or a dot product, you know exactly what it means.

---

## Lesson List

### Statistics (Lessons 01–03)
| # | Folder | Topic |
|---|--------|-------|
| 01 | `lesson-01_mean-median-mode/` | Mean, Median, Mode |
| 02 | `lesson-02_variance-stddev/` | Variance and Standard Deviation |
| 03 | `lesson-03_percentiles-correlation/` | Percentiles and Correlation |

### Probability (Lessons 04–06)
| # | Folder | Topic |
|---|--------|-------|
| 04 | `lesson-04_basic-probability/` | Basic Probability |
| 05 | `lesson-05_random-variables/` | Random Variables and Distributions |
| 06 | `lesson-06_normal-distribution/` | The Normal Distribution |

### Linear Algebra (Lessons 07–09)
| # | Folder | Topic |
|---|--------|-------|
| 07 | `lesson-07_scalars-vectors/` | Scalars and Vectors |
| 08 | `lesson-08_matrices/` | Matrices and Matrix Multiplication |
| 09 | `lesson-09_dot-product/` | Dot Product and Its Applications |

---

## Project

**Marks Analysis — Statistical Report Generator**  
Folder: `project/`  
Students load a real marks dataset and produce a complete statistical report: per-subject descriptive stats, department comparisons, outlier detection, grade distribution, and a correlation between study hours and scores.

---

## Dataset Sources
- Generated marks dataset (included in project/data/)
- Kaggle: Student Performance Dataset (optional extension)

---

## Tools Used
- Pure Python (no NumPy/Pandas yet — those come in Modules 4–5)
- `math` module for `sqrt`, `pi`, `exp`
- `random` module for simulations
- All core algorithms built from scratch to expose the underlying math

---

## Learning Progression

```
Mean / Median / Mode
      ↓
Variance / Std Dev  ← "how spread out is the data?"
      ↓
Percentiles / Correlation  ← "where do I rank? do two things move together?"
      ↓
Probability  ← "how likely is this outcome?"
      ↓
Normal Distribution  ← "why does a bell curve appear everywhere?"
      ↓
Vectors  ← "a data row is a point in space"
      ↓
Matrices  ← "a dataset is a matrix"
      ↓
Dot Product  ← "the engine inside linear regression and neural networks"
```
