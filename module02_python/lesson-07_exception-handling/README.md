# Lesson 07 — Exception Handling

**Module:** 02 — Python for Data Science  
**Duration:** ~50 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Identify Python's most common exception types and when each is raised
- Use `try` / `except` to catch and handle errors gracefully
- Catch specific exception types vs multiple types in one block
- Use `else` (runs on success) and `finally` (always runs) clauses
- Raise exceptions deliberately with `raise` to signal bad inputs
- Define lightweight custom exception classes for your own libraries
- Apply the three core data science exception patterns: safe converter, batch processor with error log, resilient pipeline

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — all exception patterns and applied pipeline demos |
| `script.py` | Standalone runnable version of all teaching code |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

---

## Prerequisites
- Completed Lessons 01–06
- Python 3.8+, no external libraries needed
