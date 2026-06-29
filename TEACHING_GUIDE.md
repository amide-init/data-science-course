# Teaching Guide — Data Science Course

## Core Philosophy
**Learning by building.** Every concept is introduced to solve a real problem, not for its own sake. Students should always know *why* they are learning something before they learn *how*.

---

## Lesson Delivery Pattern
Every lesson follows this flow:

```
1. Real-world hook (2 min)
   "Netflix uses this to recommend shows..."

2. Concept explanation (5–10 min)
   Simple language, one analogy, one diagram

3. Live coding (15–20 min)
   Instructor types, students follow along

4. Students try it (10–15 min)
   Short exercise on their own machine

5. Common mistakes review (5 min)
   Show what goes wrong and why

6. Wrap-up (2 min)
   3 bullet takeaways
```

---

## Code Example Standards

### Always include
- What the code does in plain English (before the code block)
- Inline comments explaining WHY, not WHAT
- Expected output shown in a comment or separate block
- A "what happens if..." question to spark curiosity

### Example format
```python
# Why: groupby lets us aggregate per category without a loop
revenue_by_region = df.groupby('region')['revenue'].sum()
print(revenue_by_region)
# Output:
# region
# East     42000
# North    38500
# South    51200
# West     29800
```

---

## Exercise Difficulty Levels
Each lesson has 3–5 exercises:

| Level | Description |
|-------|-------------|
| Starter | Copy-modify: change one variable or parameter |
| Practice | Apply the concept to a new dataset column |
| Challenge | Combine with a previous lesson's concept |
| Bonus | Open-ended — no single right answer |

---

## Dataset Guidelines
- Use **real, interesting datasets** — students disengage with toy data
- Source from Kaggle, UCI ML Repository, or government open data
- Keep file size under 50MB for class exercises
- Always explain the dataset's real-world context before using it

### Preferred Datasets Per Module
| Module | Dataset | Source |
|--------|---------|--------|
| 5 | IPL Ball-by-Ball | Kaggle |
| 5 | Netflix Movies & TV Shows | Kaggle |
| 6 | HR Employee Attrition | Kaggle |
| 7 | COVID-19 World Data | Our World in Data |
| 8 | Titanic | Kaggle / sklearn |
| 11 | California Housing | sklearn built-in |
| 12 | Loan Prediction | Kaggle |
| 13 | Mall Customers | Kaggle |
| 14 | MovieLens 100K | GroupLens |

---

## Common Student Struggles by Module

### Python (Module 2)
- Indentation errors (whitespace matters in Python)
- Mutable vs immutable confusion (list vs tuple)
- Not understanding when to use a function

### Pandas (Module 5)
- Confusing `.loc` vs `.iloc`
- Forgetting `inplace=True` vs reassignment
- Boolean indexing syntax errors

### Data Cleaning (Module 6)
- Dropping too many rows and losing important data
- Not checking class balance before encoding
- Applying scaling to target variable (don't do this)

### Machine Learning (Modules 10–12)
- Fitting the scaler on the full dataset (data leakage)
- Not checking class imbalance before classification
- Treating accuracy as the only metric

---

## Assessment Ideas

### Weekly (Module level)
- Submit Jupyter notebook with mini project
- Peer review (read one classmate's notebook and give feedback)
- 5-minute "explain your project" demo

### Midterm (Week 8 — after EDA)
- Take an unseen dataset, do full EDA, present insights

### Final (Week 16 — Capstone)
- End-to-end project with GitHub repo
- 10-minute presentation + Q&A
- Judge criteria: data quality, insights depth, model appropriateness, presentation clarity

---

## GitHub Portfolio Setup (Week 1 Homework)
Students should set this up in Week 1:
1. Create a GitHub account
2. Create repo: `data-science-portfolio`
3. Add a README with name and course overview
4. Each week: push their project notebook to the repo
5. By Week 16: repo has 8+ notebooks = recruiter-ready portfolio

---

## Tools Setup Checklist
- [ ] Python 3.10+ installed
- [ ] Anaconda or pip + venv configured
- [ ] Jupyter Notebook or JupyterLab
- [ ] VS Code with Python extension
- [ ] Google Colab account (backup)
- [ ] Kaggle account (for dataset downloads)
- [ ] GitHub account

---

## Pacing Notes
- **Don't rush Python** (Module 2) — everything else depends on it
- **Module 3 Math** — keep it applied, skip proofs, use Python to verify intuition
- **Modules 10–12** — spend extra time on the conceptual understanding before code
- **Module 16 Capstone** — students need at least 2 weeks ideally; 1 week minimum
- Time Series (Module 15) is labeled optional — skip if short on time

---

## Instructor Checklist Before Each Session
- [ ] Dataset downloaded and tested
- [ ] Code examples run clean on Python 3.10+
- [ ] Jupyter notebook prepared with blank cells for live coding
- [ ] 3 exercises ready with solutions hidden
- [ ] Real-world example prepared to open the lesson
