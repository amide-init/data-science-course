"""
Customer Churn Prediction - The Complete Machine Learning Lifecycle
Clean, runnable version of notebook.ipynb (teaching code only, no exercises).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay,
)

CATEGORICAL_COLUMNS = ["Gender", "Subscription Type", "Contract Length"]


# ── Step 2: Data Collection ──
def load_data(path="data/train-data.csv"):
    df = pd.read_csv(path)
    print("Shape of dataset:", df.shape)
    return df


# ── Step 3: Data Understanding (EDA) ──
def explore_data(df):
    churn_rate = df["Churn"].value_counts(normalize=True) * 100
    print("\nChurn distribution (%):")
    print(churn_rate.round(1))

    churn_by_contract = df.groupby("Contract Length")["Churn"].mean() * 100
    print("\nChurn rate by contract length (%):")
    print(churn_by_contract.round(1))

    # Pie chart: customer mix by subscription type - a genuine part-to-whole split
    # of the customer base into three roughly even categories.
    subscription_counts = df["Subscription Type"].value_counts()
    plt.figure(figsize=(5, 5))
    plt.pie(
        subscription_counts.values,
        labels=subscription_counts.index,
        autopct="%1.0f%%",
        colors=["#2a78d6", "#008300", "#e87ba4"],
        startangle=90,
    )
    plt.title("Customer Mix by Subscription Type")
    plt.savefig("subscription_mix.png")
    plt.close()

    return churn_by_contract


# ── Step 4-5: Data Cleaning, Preprocessing & Feature Engineering ──
def clean_and_engineer(df):
    df = df.dropna().drop(columns=["CustomerID"])
    df["Spend_Per_Tenure"] = df["Total Spend"] / (df["Tenure"] + 1)
    df_encoded = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS, drop_first=True)
    return df_encoded


# ── Step 7: Model Training ──
def train_models(df_encoded):
    X = df_encoded.drop(columns=["Churn"])
    y = df_encoded["Churn"].astype(int)

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train_scaled, y_train)

    random_forest = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    random_forest.fit(X_train, y_train)

    return {
        "log_reg": log_reg,
        "random_forest": random_forest,
        "X_train": X_train,
        "X_val": X_val,
        "X_val_scaled": X_val_scaled,
        "y_train": y_train,
        "y_val": y_val,
    }


# ── Step 8: Model Evaluation ──
def evaluate_models(models):
    log_reg_pred = models["log_reg"].predict(models["X_val_scaled"])
    rf_pred = models["random_forest"].predict(models["X_val"])
    y_val = models["y_val"]

    results = pd.DataFrame(
        {
            "Logistic Regression": [
                accuracy_score(y_val, log_reg_pred),
                precision_score(y_val, log_reg_pred),
                recall_score(y_val, log_reg_pred),
                f1_score(y_val, log_reg_pred),
            ],
            "Random Forest": [
                accuracy_score(y_val, rf_pred),
                precision_score(y_val, rf_pred),
                recall_score(y_val, rf_pred),
                f1_score(y_val, rf_pred),
            ],
        },
        index=["Accuracy", "Precision", "Recall", "F1 Score"],
    )
    print("\nValidation metrics:")
    print(results.round(4))

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    ConfusionMatrixDisplay.from_predictions(
        y_val, log_reg_pred, display_labels=["Stayed", "Churned"], ax=axes[0], colorbar=False
    )
    axes[0].set_title("Logistic Regression")
    ConfusionMatrixDisplay.from_predictions(
        y_val, rf_pred, display_labels=["Stayed", "Churned"], ax=axes[1], colorbar=False
    )
    axes[1].set_title("Random Forest")
    plt.tight_layout()
    plt.savefig("confusion_matrices.png")
    plt.close()

    return rf_pred


# ── Step 9: Deployment ──
def save_model(model, feature_columns, path="churn_model.joblib"):
    joblib.dump(model, path)
    print(f"\nModel saved to {path}. It expects {len(feature_columns)} input columns.")


def predict_churn(customer, model, columns):
    row = pd.DataFrame([customer])
    row["Spend_Per_Tenure"] = row["Total Spend"] / (row["Tenure"] + 1)
    row = pd.get_dummies(row, columns=CATEGORICAL_COLUMNS)
    row = row.reindex(columns=columns, fill_value=0)
    prediction = model.predict(row)[0]
    probability = model.predict_proba(row)[0][1]
    return f"{'Churn' if prediction == 1 else 'Stay'} (probability of churn: {probability:.1%})"


# ── Step 10: Monitoring & Maintenance ──
def check_on_holdout(model, feature_columns, val_accuracy, path="data/test-data.csv"):
    test_df = pd.read_csv(path).dropna().drop(columns=["CustomerID"])
    test_df["Spend_Per_Tenure"] = test_df["Total Spend"] / (test_df["Tenure"] + 1)
    test_df_encoded = pd.get_dummies(test_df, columns=CATEGORICAL_COLUMNS)

    X_test = test_df_encoded.drop(columns=["Churn"]).reindex(columns=feature_columns, fill_value=0)
    y_test = test_df_encoded["Churn"].astype(int)

    test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_pred)

    print(f"\nValidation accuracy (same source file as training): {val_accuracy:.2%}")
    print(f"Holdout accuracy   (test-data.csv, a genuinely separate file): {test_accuracy:.2%}")
    return test_accuracy


if __name__ == "__main__":
    df = load_data()
    explore_data(df)

    df_encoded = clean_and_engineer(df)
    models = train_models(df_encoded)
    rf_pred = evaluate_models(models)

    random_forest = models["random_forest"]
    feature_columns = models["X_train"].columns.tolist()

    save_model(random_forest, feature_columns)

    sample_customer = {
        "Age": 42, "Gender": "Male", "Tenure": 3, "Usage Frequency": 2,
        "Support Calls": 9, "Payment Delay": 20, "Subscription Type": "Basic",
        "Contract Length": "Monthly", "Total Spend": 150, "Last Interaction": 28,
    }
    print("\nSample prediction:", predict_churn(sample_customer, random_forest, feature_columns))

    val_accuracy = accuracy_score(models["y_val"], rf_pred)
    check_on_holdout(random_forest, feature_columns, val_accuracy)

    print("\nCharts saved as subscription_mix.png and confusion_matrices.png")
