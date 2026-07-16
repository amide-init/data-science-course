# Data Science Course — Claude Context

## Project Purpose
This project contains a complete **Data Science course for college students**, organized into 16 weekly modules. Content is generated module by module, lesson by lesson. The teaching philosophy is **project-first / learning by building**.

## Course Philosophy
- Every module ends with a hands-on project using real datasets (Kaggle, open data)
- Students maintain a GitHub portfolio (one notebook/project per week)
- By the end: 7–10 completed projects demonstrating end-to-end skills
- Avoid theory-heavy lectures; emphasize building real things

## Target Audience
- College students (beginner to intermediate)
- No prior data science experience assumed
- Basic computer literacy assumed

## Content Generation Rules
When generating course lessons, always follow this structure:

### Lesson Folder Format
Each lesson is a **folder** at: `moduleXX_topic/lesson-YY_title/`

Every lesson folder contains:
- `notebook.ipynb` — primary teaching file (always required)
- `script.py` — clean runnable version of the notebook code (include when there is meaningful standalone code)
- `data/` subfolder — any CSV, JSON, or other data files used in the lesson (only if the lesson uses local data not downloaded inline)
- `README.md` — lesson overview: objectives, what files are here, how to run

### Notebook (`notebook.ipynb`) Structure
Every notebook must have these sections as Markdown cells:
1. **Title cell** — lesson title + module number
2. **Learning Objectives** — 3–5 bullet points
3. **Concept Explanation** — clear prose with real-world hook, no jargon without definition
4. **Code cells** — runnable, well-commented; explain WHY not WHAT
5. **Common Mistakes** — markdown cell listing 2–3 pitfalls, then code showing the error and fix
6. **Practice Exercises** — 3–5 exercises as markdown cells with empty code cells below each
7. **Key Takeaways** — final markdown cell with 3-bullet summary

### script.py Format
- Clean, commented version of all runnable code from the notebook
- No exercise scaffolding — just the teaching code
- Sections separated by `# ── Section Name ──` comments
- Include a `if __name__ == "__main__":` guard

### Project Folder Format
Each module's project is also a folder: `moduleXX_topic/project/`
Contains:
- `notebook.ipynb` — full project walkthrough
- `script.py` — runnable solution (optional)
- `data/` — dataset files or a `download_data.py` script if too large to include
- `README.md` — project brief, dataset source, what students build

### Module Folder Format
Each module folder contains:
- `overview.md` — module goal, lesson list with folder links, project description, dataset source, estimated time
- `lesson-01_title/`
- `lesson-02_title/`
- ...
- `project/`

## Standalone Projects Folder (`projects/`)
Separate from the `moduleXX_topic/project/` folders (which are tied to a specific
module's lesson sequence), the top-level `projects/` folder holds standalone,
cross-cutting practice projects — e.g. full data-science-lifecycle walkthroughs that
aren't scoped to one module's syllabus.

Each project gets its own subfolder: `projects/<project-name>/`, following the same
file convention as module projects:
- `notebook.ipynb` — full project walkthrough
- `script.py` — clean runnable version (optional)
- `data/` — dataset file(s) used (e.g. `data/titanic.csv`)
- `README.md` — project brief: what it teaches, dataset source, files, how to run

Existing project folders:
- `projects/titatnic/` — Titanic dataset, full DS lifecycle (Ask → Get → Clean →
  Explore → Communicate) combining NumPy, Pandas, and Matplotlib
- `projects/customer-churn/` — customer churn project (in progress)

When asked to generate a new standalone project, create it as a new
`projects/<project-name>/` folder following this same structure rather than nesting
it under a module.

## Directory Structure
```
data-science/
├── CLAUDE.md                        ← this file
├── COURSE_STRUCTURE.md              ← full roadmap reference
├── TEACHING_GUIDE.md                ← pedagogy notes for instructors
├── projects/                        ← standalone cross-module projects
│   ├── titatnic/
│   │   ├── notebook.ipynb
│   │   ├── script.py
│   │   ├── data/titanic.csv
│   │   └── README.md
│   └── customer-churn/
├── module01_intro/
│   ├── overview.md
│   ├── lesson-01_what-is-ds/
│   │   ├── notebook.ipynb
│   │   └── README.md
│   ├── lesson-02_ai-ml-ds/
│   │   ├── notebook.ipynb
│   │   └── README.md
│   ├── lesson-03_ds-lifecycle/
│   ├── lesson-04_roles-industry/
│   ├── lesson-05_real-world-apps/
│   ├── lesson-06_types-of-data/
│   └── project/
│       ├── notebook.ipynb
│       ├── data/
│       └── README.md
├── module02_python/
│   ├── overview.md
│   ├── lesson-01_variables-datatypes/
│   │   ├── notebook.ipynb
│   │   ├── script.py
│   │   └── README.md
│   └── project/
├── module03_mathematics/
├── module04_numpy/
├── module05_pandas/
├── module06_data_cleaning/
├── module07_visualization/
├── module08_eda/
├── module09_sql/
├── module10_ml_basics/
├── module11_regression/
├── module12_classification/
├── module13_clustering/
├── module14_recommendation/
├── module15_time_series/
├── module16_capstone/
└── bonus_industry_skills/
```

## Module Summary Table

| Module | Week | Topic | Project |
|--------|------|-------|---------|
| 01 | 1 | Introduction to Data Science | Personal Expenses Analysis |
| 02 | 2 | Python for Data Science | Student Management System |
| 03 | 3 | Mathematics (Stats + Linear Algebra) | Marks Analysis |
| 04 | 4 | NumPy | Image Matrix Operations |
| 05 | 5 | Pandas | Netflix/IPL Dataset Analysis |
| 06 | 6 | Data Cleaning | Employee Dataset Cleaning |
| 07 | 7 | Data Visualization | COVID Dashboard |
| 08 | 8 | Exploratory Data Analysis (EDA) | Titanic Analysis |
| 09 | 9 | SQL for Data Science | E-commerce Analytics |
| 10 | 10 | ML Fundamentals | Dataset Preparation |
| 11 | 11 | Regression | House Price Prediction |
| 12 | 12 | Classification | Loan Approval Prediction |
| 13 | 13 | Clustering | Customer Segmentation |
| 14 | 14 | Recommendation Systems | Movie Recommender |
| 15 | 15 | Time Series (Optional) | Sales Trend Analysis |
| 16 | 16 | Capstone Project | End-to-End DS Project |

## Generation Workflow
When asked to generate content:
1. Identify the module and lesson from COURSE_STRUCTURE.md
2. Create the lesson folder: `moduleXX_topic/lesson-YY_title/`
3. Generate `notebook.ipynb` with all required sections (title, objectives, concept, code, mistakes, exercises, takeaways)
4. Generate `script.py` if the lesson has runnable code (most lessons do)
5. Generate `README.md` for the lesson folder
6. If a data file is needed and is small (<1MB), include it in `data/`; otherwise add a download snippet in the notebook
7. If this is the first lesson of a module, also create `overview.md` for the module
8. Keep all code beginner-friendly: no one-liners that sacrifice clarity for brevity

## Datasets Used Per Module
- Module 05: IPL dataset, Netflix dataset (Kaggle)
- Module 06: Employee dataset (Kaggle)
- Module 07: COVID-19 dataset (Our World in Data / Kaggle)
- Module 08: Titanic dataset (Kaggle)
- Module 09: E-commerce/Northwind database
- Module 11: House price dataset (Boston/California Housing)
- Module 12: Loan approval dataset (Kaggle)
- Module 13: Mall customers / E-commerce customer dataset
- Module 14: MovieLens dataset
- Module 15: Stock price / Sales time series data

## Tone and Style
- Friendly, encouraging, conversational
- "You" address to the student directly
- Explain the WHY before the HOW
- Connect every concept to a real-world use case
- No unnecessary jargon; define terms when first introduced
