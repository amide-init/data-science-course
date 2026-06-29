# Data Science Course — Full Structure Reference

## Overview
- **Duration:** 12–16 weeks
- **Audience:** College students, beginner level
- **Format:** Weekly modules, each with lessons + a mini project
- **Stack:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SQL

---

## Module 01 — Introduction to Data Science (Week 1)
**Goal:** Students understand what Data Science actually is and where it fits in industry.

### Lessons
1. `lesson-01_what-is-ds/` — What is Data Science?
2. `lesson-02_ai-ml-ds/` — AI vs ML vs Data Science (differences and relationships)
3. `lesson-03_ds-lifecycle/` — The Data Science Lifecycle (end-to-end workflow)
4. `lesson-04_roles-industry/` — Roles in the Industry (Data Analyst, DS, MLE, etc.)
5. `lesson-05_real-world-apps/` — Real-world Applications of Data Science
6. `lesson-06_types-of-data/` — Types of Data (structured, unstructured, numerical, categorical)

### Mini Project
- **Name:** Personal Expenses Analysis
- **Description:** Students track and analyze their own daily expenses in Excel or Python
- **Skills:** Basic data thinking, spreadsheet/Python fundamentals

---

## Module 02 — Python for Data Science (Week 2)
**Goal:** Students get comfortable with Python fundamentals needed for data work.

### Lessons
1. `lesson-01_variables-datatypes/` — Variables and Data Types
2. `lesson-02_operators-conditions/` — Operators and Conditions
3. `lesson-03_loops/` — Loops (for, while)
4. `lesson-04_functions/` — Functions
5. `lesson-05_lists-tuples-sets/` — Lists, Tuples, Sets
6. `lesson-06_dictionaries/` — Dictionaries
7. `lesson-07_exception-handling/` — Exception Handling
8. `lesson-08_file-handling/` — File Handling (CSV, TXT)

### Projects
- Student Management System
- Expense Tracker
- Library Management

---

## Module 03 — Mathematics for Data Science (Week 3)
**Goal:** Students get just enough math to understand ML algorithms (not deep theory).

### Statistics
1. `lesson-01_mean-median-mode/` — Mean, Median, Mode
2. `lesson-02_variance-stddev/` — Variance and Standard Deviation
3. `lesson-03_percentiles-correlation/` — Percentiles and Correlation

### Probability
4. `lesson-04_basic-probability/` — Basic Probability
5. `lesson-05_random-variables/` — Random Variables
6. `lesson-06_normal-distribution/` — Normal Distribution

### Linear Algebra
7. `lesson-07_scalars-vectors/` — Scalars and Vectors
8. `lesson-08_matrices/` — Matrices and Matrix Multiplication
9. `lesson-09_dot-product/` — Dot Product

### Mini Project
- Analyze students' marks statistically (mean, std, distribution)

---

## Module 04 — NumPy (Week 4)
**Goal:** Students use NumPy for efficient numerical computation.

### Lessons
1. `lesson-01_ndarray/` — The ndarray (N-dimensional array)
2. `lesson-02_creating-arrays/` — Creating Arrays (zeros, ones, arange, linspace, random)
3. `lesson-03_indexing-slicing/` — Indexing and Slicing
4. `lesson-04_broadcasting/` — Broadcasting
5. `lesson-05_vectorization/` — Vectorization (why it's faster than loops)
6. `lesson-06_matrix-operations/` — Matrix Operations
7. `lesson-07_random-module/` — Random Module

### Project
- Represent an image as a NumPy array, do basic operations (grayscale, crop, flip)

---

## Module 05 — Pandas (Week 5)
**Goal:** Students can load, inspect, filter, and summarize tabular data.

### Lessons
1. `lesson-01_series/` — Series
2. `lesson-02_dataframe/` — DataFrame
3. `lesson-03_read-csv-excel/` — Reading CSV and Excel files
4. `lesson-04_selecting-filtering/` — Selecting Rows and Columns, Filtering
5. `lesson-05_sorting/` — Sorting Data
6. `lesson-06_missing-values/` — Handling Missing Values
7. `lesson-07_groupby/` — GroupBy
8. `lesson-08_merge-join/` — Merge and Join
9. `lesson-09_apply/` — Apply (custom functions)
10. `lesson-10_pivot-tables/` — Pivot Tables

### Project
- Analyze IPL, Netflix, or Spotify datasets

---

## Module 06 — Data Cleaning (Week 6)
**Goal:** Students can take a messy real-world dataset and make it analysis-ready.

### Lessons
1. `lesson-01_missing-values/` — Handling Missing Values (strategies: drop, fill, impute)
2. `lesson-02_duplicates/` — Finding and Removing Duplicates
3. `lesson-03_outliers/` — Detecting and Handling Outliers (IQR, Z-score)
4. `lesson-04_encoding/` — Encoding Categorical Variables (Label, One-Hot)
5. `lesson-05_feature-scaling/` — Feature Scaling (Normalization, Standardization)
6. `lesson-06_data-transformation/` — Data Transformation (skewness, log transform)

### Project
- Clean a messy employee dataset (real Kaggle data)

---

## Module 07 — Data Visualization (Week 7)
**Goal:** Students can create clear, informative charts to communicate findings.

### Matplotlib
1. `lesson-01_matplotlib-basics/` — Matplotlib Basics (figure, axes, anatomy of a plot)
2. `lesson-02_line-bar-scatter/` — Line Plot, Bar Chart, Scatter Plot
3. `lesson-03_histogram-pie/` — Histogram and Pie Chart
4. `lesson-04_box-plot/` — Box Plot

### Seaborn
5. `lesson-05_seaborn-basics/` — Seaborn Overview
6. `lesson-06_heatmap-pairplot/` — Heatmap and Pairplot
7. `lesson-07_count-dist-plot/` — Countplot and Distribution Plot

### Project
- COVID Dashboard (multi-chart visualization of COVID-19 data)

---

## Module 08 — Exploratory Data Analysis (Week 8)
**Goal:** Students can independently investigate a dataset and extract business insights.

### Lessons
1. `lesson-01_eda-intro/` — What is EDA and Why It Matters
2. `lesson-02_univariate/` — Univariate Analysis
3. `lesson-03_bivariate/` — Bivariate Analysis
4. `lesson-04_correlation/` — Correlation Analysis
5. `lesson-05_feature-relationships/` — Feature Relationships
6. `lesson-06_business-insights/` — Deriving Business Insights from Data

### Project
- Titanic Survival Analysis (full EDA notebook)

---

## Module 09 — SQL for Data Science (Week 9)
**Goal:** Students can query databases to extract and analyze data.

### Lessons
1. `lesson-01_select-where/` — SELECT and WHERE
2. `lesson-02_groupby-orderby/` — GROUP BY, ORDER BY, HAVING
3. `lesson-03_joins/` — JOINS (INNER, LEFT, RIGHT, FULL)
4. `lesson-04_subqueries/` — Subqueries
5. `lesson-05_window-functions/` — Window Functions (ROW_NUMBER, RANK, LAG, LEAD)

### Project
- Analyze an e-commerce database (orders, products, customers)

---

## Module 10 — Machine Learning Basics (Week 10)
**Goal:** Students understand what ML is conceptually before touching algorithms.

### Lessons
1. `lesson-01_what-is-ml/` — What is Machine Learning?
2. `lesson-02_supervised-unsupervised/` — Supervised vs Unsupervised Learning
3. `lesson-03_features-labels/` — Features and Labels
4. `lesson-04_train-test-split/` — Train/Test Split and Cross-Validation
5. `lesson-05_overfitting-underfitting/` — Overfitting and Underfitting
6. `lesson-06_sklearn-intro/` — Introduction to Scikit-learn

### Project
- Dataset preparation and train/test split exercise

---

## Module 11 — Regression (Week 11)
**Goal:** Students can build and evaluate regression models.

### Algorithms
1. `lesson-01_linear-regression/` — Linear Regression (intuition + implementation)
2. `lesson-02_multiple-regression/` — Multiple Linear Regression
3. `lesson-03_polynomial-regression/` — Polynomial Regression (brief intro)

### Evaluation
4. `lesson-04_regression-metrics/` — MAE, MSE, RMSE, R²

### Project
- House Price Prediction (California Housing dataset)

---

## Module 12 — Classification (Week 12)
**Goal:** Students can build and evaluate classification models.

### Algorithms
1. `lesson-01_logistic-regression/` — Logistic Regression
2. `lesson-02_decision-tree/` — Decision Tree
3. `lesson-03_random-forest/` — Random Forest
4. `lesson-04_knn/` — K-Nearest Neighbors (KNN)

### Evaluation
5. `lesson-05_classification-metrics/` — Accuracy, Precision, Recall, F1, Confusion Matrix

### Project
- Loan Approval Prediction

---

## Module 13 — Clustering (Week 13)
**Goal:** Students understand and apply unsupervised learning for grouping.

### Lessons
1. `lesson-01_kmeans/` — K-Means Clustering
2. `lesson-02_elbow-method/` — Choosing K: The Elbow Method
3. `lesson-03_hierarchical/` — Hierarchical Clustering (Dendrograms)

### Project
- Customer Segmentation (Mall Customers dataset)

---

## Module 14 — Recommendation Systems (Week 14)
**Goal:** Students understand how recommendation engines work and can build a basic one.

### Lessons
1. `lesson-01_intro-recsys/` — Introduction to Recommendation Systems
2. `lesson-02_content-based/` — Content-Based Filtering
3. `lesson-03_collaborative/` — Collaborative Filtering
4. `lesson-04_matrix-factorization/` — Matrix Factorization (brief intro)

### Project
- Movie Recommendation System (MovieLens dataset)

---

## Module 15 — Time Series (Optional, Week 15)
**Goal:** Students understand time-based data and can do basic trend analysis.

### Lessons
1. `lesson-01_time-series-intro/` — What is Time Series Data?
2. `lesson-02_components/` — Trend, Seasonality, Noise
3. `lesson-03_moving-average/` — Moving Averages and Smoothing
4. `lesson-04_forecasting-basics/` — Forecasting Basics (ARIMA intro, only conceptual)

### Project
- Stock Price / Sales Trend Analysis

---

## Module 16 — Capstone Project (Week 16)
**Goal:** Students complete one substantial end-to-end project independently.

### Workflow
```
Collect Data → Clean Data → Analyze → Visualize → Train Model → Evaluate → Deploy
```

### Suggested Projects
1. House Price Prediction
2. Student Performance Analysis
3. Employee Salary Prediction
4. Fake News Detection
5. Customer Churn Prediction
6. Loan Approval Prediction
7. Sales Forecasting
8. Movie Recommendation
9. IPL Data Analysis
10. Credit Card Fraud Detection

---

## Bonus Module — Industry Readiness Skills
- Git & GitHub basics
- Jupyter Notebook / Google Colab
- Virtual environments (venv, conda)
- VS Code setup for data science
- Kaggle (competitions, datasets, notebooks)
- API basics
- Working with CSV/JSON/APIs
- Basic web scraping (BeautifulSoup)

---

## Final Portfolio (Each Student Completes)
1. Student Performance Analysis
2. IPL Data Analysis Dashboard
3. Customer Segmentation
4. House Price Prediction
5. Loan Approval Prediction
6. Movie Recommendation System
7. Sales Dashboard
8. End-to-End Capstone Project
