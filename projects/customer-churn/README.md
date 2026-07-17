# Customer Churn Prediction — The Complete Data Science Lifecycle

## What this project is
A hands-on project that walks students through the full **7-step Data Science lifecycle**
(Define → Collect → Clean → Explore → Model → Evaluate → Deploy) — the same lifecycle taught in
Module 1 — on a real churn dataset, combining **NumPy**, **Pandas**, **Matplotlib**, and
**scikit-learn** in one place. Cleaning is done *before* exploring, since a chart or groupby
result built on broken rows can be quietly misleading — encoding, feature engineering, model
selection, and training all happen together under Step 5 (Model), once the data is understood.

## Dataset
- `data/train-data.csv` — ~440,000 customers used to train the model
- `data/test-data.csv` — ~64,000 customers, a genuinely separate holdout file used only in the
  Deploy stage, to check the model after it "ships"

Columns: `CustomerID, Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay,
Subscription Type, Contract Length, Total Spend, Last Interaction, Churn` (the target, 0 = stayed,
1 = churned).

## Files
- `notebook.ipynb` — the full teaching walkthrough. Explains each lifecycle stage, then cleans,
  encodes, engineers features, trains models, and ends with practice exercises.
- `notebook_lite.ipynb` — a lean, code-first version of the same pipeline for live-coding in
  class: short one-line section headers, no essays, no exercises — just the runnable steps.
- `script.py` — clean runnable version of the teaching code (no exercises). Running it prints
  metrics, saves a trained model (`churn_model.joblib`), and saves the subscription-mix,
  churn-by-gender, and confusion-matrix charts as PNG files.
- `data/` — the training and holdout datasets used throughout.

## How to run
```bash
# From the projects/customer-churn/ folder
jupyter notebook notebook.ipynb        # full walkthrough
jupyter notebook notebook_lite.ipynb   # lean, code-first version
```
or run the script version directly:
```bash
python script.py
```

## What students learn
1. **Define** — framing a vague ask ("predict churn") as a sharp, answerable question
2. **Collect** — loading real customer data, and keeping a genuinely separate holdout file for later
3. **Clean** — dropping broken rows and an ID column *before* exploring, so the analysis
   that follows is trustworthy
4. **Explore (EDA)** — checking class balance and spotting strong churn signals
   (contract length, gender, support calls, correlation with churn) with Pandas and Matplotlib,
   including a pie chart of the customer mix by subscription type and a churn-by-gender bar chart
5. **Model** — getting the data model-ready (one-hot encoding with `pd.get_dummies` and a new
   `Spend_Per_Tenure` feature), choosing between a Logistic Regression baseline and a Random
   Forest, and training both
6. **Evaluate** — accuracy, precision, recall, F1, and confusion matrices
7. **Deploy** — saving a model with `joblib`, writing a `predict_churn()` helper, and then
   monitoring it against `test-data.csv` to see firsthand why validation accuracy alone is never
   the end of the story (a real, honest example of data drift, not a scripted one)
