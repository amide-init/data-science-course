# Lesson 08 — File Handling (TXT, CSV, JSON)

**Module:** 02 — Python for Data Science  
**Duration:** ~55 minutes

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Open, read, and write text files using the `with` statement
- Use `open()` with the correct modes (`r`, `w`, `a`) and always specify `encoding="utf-8"`
- Parse CSV files with both the `csv.reader` and `csv.DictReader` built-ins
- Write structured data back to CSV with `csv.writer` and `csv.DictWriter`
- Read and write JSON files using `json.load()` / `json.dump()`
- Build a complete file-based data pipeline: load → clean → analyse → save report
- Handle file errors gracefully (`FileNotFoundError`, `PermissionError`)

---

## Files

| File | Description |
|------|-------------|
| `notebook.ipynb` | Main lesson — all file handling patterns |
| `script.py` | Standalone runnable version of all teaching code |
| `data/students.csv` | Sample dataset used in exercises (25 rows, some dirty) |

---

## How to Run

```bash
jupyter notebook notebook.ipynb
# or
python script.py
```

---

## Prerequisites
- Completed Lessons 01–07
- Python 3.8+, no external libraries needed (uses `csv`, `json`, `os` from the standard library)
