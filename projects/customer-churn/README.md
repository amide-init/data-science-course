# Customer Churn Prediction — The Complete Machine Learning Lifecycle

## What this project is
A hands-on project that walks students through the full **11-step Machine Learning lifecycle**
(Problem Definition → Data Collection → Data Understanding → Data Cleaning & Preprocessing →
Feature Engineering → Model Selection → Model Training → Model Evaluation → Model Improvement →
Deployment → Monitoring & Maintenance) on a real churn dataset, combining **NumPy**, **Pandas**,
**Matplotlib**, and **scikit-learn** in one place.

## Dataset
- `data/train-data.csv` — ~440,000 customers used to train the model
- `data/test-data.csv` — ~64,000 customers, a genuinely separate holdout file used only in the
  Monitoring & Maintenance stage

Columns: `CustomerID, Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay,
Subscription Type, Contract Length, Total Spend, Last Interaction, Churn` (the target, 0 = stayed,
1 = churned).

## Files
- `notebook.ipynb` — the full teaching walkthrough. Explains each lifecycle stage, then cleans,
  encodes, engineers features, trains and tunes models, and ends with practice exercises.
- `script.py` — clean runnable version of the teaching code (no exercises). Running it prints
  metrics, saves a trained model (`churn_model.joblib`), and saves a confusion-matrix chart as a
  PNG file.
- `data/` — the training and holdout datasets used throughout.

## How to run
```bash
# From the projects/customer-churn/ folder
jupyter notebook notebook.ipynb
```
or run the script version directly:
```bash
python script.py
```

## What students learn
1. **Problem Definition & Data Collection** — framing a churn question and loading real data
2. **Data Understanding (EDA)** — checking class balance and spotting strong churn signals
   (contract length, support calls) with Pandas and Matplotlib
3. **Data Cleaning & Preprocessing** — dropping broken rows and an ID column, one-hot encoding
   text columns with `pd.get_dummies`
4. **Feature Engineering** — creating a new `Spend_Per_Tenure` feature
5. **Model Selection & Training** — comparing a Logistic Regression baseline against a Random
   Forest with scikit-learn
6. **Model Evaluation** — accuracy, precision, recall, F1, and confusion matrices
7. **Model Improvement** — tuning Random Forest with `GridSearchCV`
8. **Deployment** — saving a model with `joblib` and writing a `predict_churn()` helper
9. **Monitoring & Maintenance** — checking the deployed model against `test-data.csv` and seeing
   firsthand why validation accuracy alone is never the end of the story (a real, honest example
   of data drift, not a scripted one)
