"""
Titanic Project - The Complete Data Science Lifecycle
Clean, runnable version of notebook.ipynb (teaching code only, no exercises).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ── Stage 2: Get the Data ──
def load_data(path="data/titanic.csv"):
    df = pd.read_csv(path)
    print("Shape of dataset:", df.shape)
    return df


# ── Stage 3: Clean the Data ──
def clean_data(df):
    df = df.copy()

    # Fill missing Age with the median (robust to outliers)
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)

    # Fill missing Embarked with the most common port
    most_common_port = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(most_common_port)

    # Cabin is missing too often to fill reliably -> turn into a yes/no flag
    df["Has_Cabin"] = df["Cabin"].notnull().astype(int)
    df = df.drop(columns=["Cabin"])

    return df


# ── Stage 4: Explore the Data ──
def explore_data(df):
    survival_rate = np.mean(df["Survived"]) * 100
    print(f"Overall survival rate: {survival_rate:.1f}%")

    survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100
    print("\nSurvival rate by sex (%):")
    print(survival_by_sex.round(1))

    df["Is_Child"] = np.where(df["Age"] < 12, "Child", "Adult")
    survival_by_age_group = df.groupby("Is_Child")["Survived"].mean() * 100
    print("\nSurvival rate by age group (%):")
    print(survival_by_age_group.round(1))

    survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
    print("\nSurvival rate by passenger class (%):")
    print(survival_by_class.round(1))

    survival_by_class_sex = df.groupby(["Pclass", "Sex"])["Survived"].mean() * 100
    print("\nSurvival rate by class and sex (%):")
    print(survival_by_class_sex.round(1))

    return survival_by_sex, survival_by_class


# ── Stage 5: Communicate (Visualize) ──
def visualize_data(df, survival_by_sex, survival_by_class):
    survived_counts = df["Survived"].value_counts().sort_index()

    plt.figure(figsize=(5, 4))
    plt.bar(["Died", "Survived"], survived_counts.values, color=["#c0392b", "#27ae60"])
    plt.title("Titanic: Overall Survival Count")
    plt.ylabel("Number of Passengers")
    plt.savefig("overall_survival.png")
    plt.close()

    plt.figure(figsize=(5, 4))
    plt.bar(survival_by_sex.index, survival_by_sex.values, color=["#e91e63", "#2980b9"])
    plt.title("Survival Rate by Sex")
    plt.ylabel("Survival Rate (%)")
    plt.ylim(0, 100)
    plt.savefig("survival_by_sex.png")
    plt.close()

    plt.figure(figsize=(5, 4))
    plt.bar(survival_by_class.index.astype(str), survival_by_class.values, color="#8e44ad")
    plt.title("Survival Rate by Passenger Class")
    plt.xlabel("Passenger Class (1 = Upper, 3 = Lower)")
    plt.ylabel("Survival Rate (%)")
    plt.ylim(0, 100)
    plt.savefig("survival_by_class.png")
    plt.close()

    plt.figure(figsize=(7, 4))
    plt.hist(df[df["Survived"] == 1]["Age"], bins=20, alpha=0.6, label="Survived", color="#27ae60")
    plt.hist(df[df["Survived"] == 0]["Age"], bins=20, alpha=0.6, label="Died", color="#c0392b")
    plt.title("Age Distribution: Survived vs Died")
    plt.xlabel("Age")
    plt.ylabel("Number of Passengers")
    plt.legend()
    plt.savefig("age_distribution.png")
    plt.close()

    print("Charts saved as PNG files in the current directory.")


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    survival_by_sex, survival_by_class = explore_data(df)
    visualize_data(df, survival_by_sex, survival_by_class)
