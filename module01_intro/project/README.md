# Module 01 — Mini Project
# Personal Expenses Analysis

**Module:** 01 — Introduction to Data Science  
**Type:** End-of-module project  
**Estimated time:** 1–2 hours

---

## What You'll Build

A complete personal finance analysis — from raw expense data to actionable insights — using only Python built-ins. No Pandas, no NumPy, no shortcuts. Just you, your data, and the lifecycle.

By the end you will have answered:
1. How much did I spend in total this week?
2. Which category eats up the most of my budget?
3. Which day am I most likely to overspend?
4. What does my spending look like day by day?
5. Are there any unusual one-off spikes in my expenses?

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main project notebook — follow it step by step |
| `data/sample_expenses.csv` | Sample one-week expense dataset (college student) |
| `data/my_expenses.csv` | **Your file** — replace this with your own data (see below) |

---

## How to Use Your Own Data

1. Open `data/sample_expenses.csv` to see the format
2. Create a new file `data/my_expenses.csv` with the same columns:

```
date,category,description,amount
2024-01-08,Food,Breakfast at canteen,45
2024-01-08,Transport,Auto to college,80
...
```

3. Track your real expenses for 7 days — every purchase, no matter how small
4. In the notebook, change `FILENAME = "data/sample_expenses.csv"` to `FILENAME = "data/my_expenses.csv"`
5. Re-run all cells

**Columns explained:**
| Column | Format | Example |
|---|---|---|
| `date` | YYYY-MM-DD | `2024-01-08` |
| `category` | One word | `Food`, `Transport`, `Entertainment`, `Shopping`, `Education`, `Health`, `Other` |
| `description` | Short note | `Lunch at mess`, `Uber to mall` |
| `amount` | Number (₹), no ₹ sign | `45`, `299`, `1200` |

---

## What to Submit (for class)

- [ ] Your filled `my_expenses.csv` with at least 5 days of real data
- [ ] Your completed `notebook.ipynb` with all cells run
- [ ] The final summary section filled with **your** insights (not the sample answers)
- [ ] One sentence: *"The most surprising thing I found in my own data was..."*

---

## Skills Practised

- Data Science lifecycle (all 7 steps)
- Reading CSV files with Python
- Aggregation, grouping, and sorting
- Identifying data types in a real dataset
- Translating numbers into written insights
- ASCII data visualisation

---

## Concepts Used From This Module

| Lesson | Concept applied |
|---|---|
| Lesson 01 | Data → questions → insights workflow |
| Lesson 03 | 7-step lifecycle structure |
| Lesson 05 | Personal finance as a real-world DS application |
| Lesson 06 | Identifying column types (date, category, amount) |
