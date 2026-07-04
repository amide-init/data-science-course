# Module 04 — NumPy

**Week:** 4
**Goal:** Use NumPy's `ndarray` for fast, memory-efficient numerical computation — the foundation Pandas, visualization, and every ML library in this course are built on.
**Estimated time:** ~6 hours across 7 lessons + project

---

## Why This Module?

Every dataset you'll touch from Module 05 onward — a spreadsheet, an image, a batch of sensor readings — is, underneath, a grid of numbers. Python lists can hold grids of numbers too, but they're slow and memory-hungry because every element is a separate, scattered Python object.

NumPy's `ndarray` fixes this: one object, one fixed data type, packed contiguously in memory, with math operations that run in compiled C instead of a Python loop. This module builds your fluency with arrays before Module 05 (Pandas) hides most of this machinery behind a friendlier interface — understanding what's underneath makes Pandas far less mysterious.

---

## Lesson List

| # | Folder | Topic |
|---|--------|-------|
| 01 | `lesson-01_ndarray/` | The ndarray (N-dimensional array) |
| 02 | `lesson-02_creating-arrays/` | Creating Arrays (zeros, ones, arange, linspace, random) |
| 03 | `lesson-03_indexing-slicing/` | Indexing and Slicing |
| 04 | `lesson-04_broadcasting/` | Broadcasting |
| 05 | `lesson-05_vectorization/` | Vectorization (why it's faster than loops) |
| 06 | `lesson-06_matrix-operations/` | Matrix Operations |
| 07 | `lesson-07_random-module/` | Random Module |

---

## Project

**Image as a Matrix — Basic Image Operations**
Folder: `project/`
Students represent an image as a NumPy array and perform basic operations: grayscale conversion, cropping, and flipping.

---

## Dataset Sources
- A small sample image (included in `project/data/`, or loaded inline via a public image URL)

---

## Tools Used
- `numpy`
- `matplotlib` (only for displaying images, introduced properly in Module 07)

---

## Learning Progression

```
The ndarray  ← "one grid, one dtype, one block of memory"
      ↓
Creating Arrays  ← "generate data without typing every value"
      ↓
Indexing / Slicing  ← "grab exactly the piece of the array you need"
      ↓
Broadcasting  ← "combine arrays of different shapes without writing a loop"
      ↓
Vectorization  ← "why array math replaces Python for-loops"
      ↓
Matrix Operations  ← "the dot products and transposes from Module 03, in NumPy"
      ↓
Random Module  ← "simulate data, shuffle, and sample"
```
