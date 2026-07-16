# Titanic Project — The Complete Data Science Lifecycle

## What this project is
A hands-on project that walks students through the full **Data Science Lifecycle**
(Ask → Get → Clean → Explore → Communicate) on a single real dataset, combining
**NumPy**, **Pandas**, and **Matplotlib** in one place.

## Dataset
`data/titanic.csv` — the classic Titanic passenger dataset (891 passengers, 12 columns:
survival, class, name, sex, age, fare, cabin, etc.).

## Files
- `notebook.ipynb` — the full teaching walkthrough. Explains each lifecycle stage, then
  cleans, explores, and visualizes the data, ending with practice exercises for students.
- `script.py` — clean runnable version of the teaching code (no exercises). Running it
  prints the key statistics and saves the charts as PNG files.
- `data/titanic.csv` — the dataset used throughout.

## How to run
```bash
# From the projects/ folder
jupyter notebook notebook.ipynb
```
or run the script version directly:
```bash
python script.py
```

## What students learn
1. **Ask** — how to turn a vague topic into a specific, answerable question
2. **Get** — loading and first-inspecting a real CSV with Pandas
3. **Clean** — finding and handling missing data (`Age`, `Cabin`, `Embarked`)
4. **Explore** — using NumPy for stats and Pandas `groupby()` to compare survival rates
   by sex, age group, and passenger class
5. **Communicate** — turning `groupby()` results into Matplotlib charts and a plain-English
   written conclusion
