🎬 Movie Budget vs Revenue Analysis

A data science project analyzing the relationship between film production budgets and worldwide revenue using pandas, seaborn, matplotlib, and scikit-learn.

This project explores how movie budgets impact box office success across decades, including data cleaning, visualization, and predictive modeling.

🚀 Features

✅ Data Cleaning

Removed NaN values, duplicates, and formatted currency fields.

Converted Release_Date into datetime format.

✅ Exploratory Data Analysis (EDA)

Identified international-only releases.

Highlighted unreleased future films.

Calculated the % of films that lost money.

✅ Data Visualization

Bubble chart showing budgets vs worldwide revenue over time.

Regression plots for old films (≤1960s) and modern films (>1960s).

✅ Machine Learning

Linear regression model to predict revenue based on budget.

Computed slope, intercept, R² score, and revenue predictions for a hypothetical budget.

📊 Sample Insights

📌 % of films that failed to break even.

📌 Most expensive films before 1960.

📌 Regression comparison between old vs. modern films.

📌 Predicted revenue for a $350M production.

🛠️ Tech Stack

Python 🐍

pandas – Data cleaning & manipulation

seaborn & matplotlib – Data visualization

scikit-learn – Linear regression modeling

📂 Dataset

The analysis is based on cost_revenue_dirty.csv, which includes:

USD_Production_Budget

USD_Worldwide_Gross

USD_Domestic_Gross

Release_Date

▶️ How to Run

Clone this repo:

git clone https://github.com/DebanilBora/movies-revenue-analysis.git
cd movie-budget-revenue-analysis


Install dependencies:

pip install pandas seaborn matplotlib scikit-learn


Run the script:

python main.py

📌 Example Visualizations

Bubble chart of film budgets over time.

Regression line comparing budget vs revenue for old and new films.

🔖 Tags

#DataScience #MachineLearning #LinearRegression #Movies #Visualization
