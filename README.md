📂 Project Overview

The script performs the following steps:

Data Exploration

Loads the dataset (cost_revenue_dirty.csv).

Inspects shape, info, and missing values.

Detects and removes duplicates.

Data Cleaning

Cleans currency columns (USD_Production_Budget, USD_Worldwide_Gross, USD_Domestic_Gross).

Converts Release_Date to datetime.

Removes unreleased and international-only films.

Insights & Filtering

Identifies films that lost money.

Splits films into old (≤1960s) and new (>1960s) for comparison.

Visualizations

Bubble Chart: Budgets over time with revenue scaling.

Regression Plots: Budget vs revenue for old and new films.

Linear Regression (Scikit-learn)

Fits regression models for old and new films.

Evaluates slope, intercept, and R² score.

Predicts expected revenue for a given budget (e.g., $350M).