import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('cost_revenue_dirty.csv')

# ------------------ Challenge 1: Explore the Data ------------------
print(data.shape)
print(data.info())
print(data.head())

# Check for NaNs and duplicates
print("Any NaNs:", data.isna().values.any())
print("Any Duplicates:", data.duplicated().values.any())

# ------------------ Challenge 2: Clean Currency Columns ------------------
chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        data[col] = data[col].astype(str).str.replace(char, "")
    data[col] = pd.to_numeric(data[col])

# ------------------ Challenge 3: Convert Release_Date ------------------
data['Release_Date'] = pd.to_datetime(data['Release_Date'])

# ------------------ Filter: International Releases ------------------
international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')

# ------------------ Unreleased Films ------------------
future_releases = data[data['Release_Date'] > pd.to_datetime('2018-05-01')]
print(f"Unreleased films: {len(future_releases)}")

# Cleaned dataset
data_clean = data.drop(future_releases.index)

# ------------------ Bonus: Films that lost money ------------------
money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
loss_percentage = round(len(money_losing) / len(data_clean) * 100, 2)
print(f"{loss_percentage}% of films did not break even.")

# ------------------ Bubble Chart ------------------
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean['Release_Date'].min(), data_clean['Release_Date'].max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')
plt.title("Film Budgets Over Time")
plt.show()

# ------------------ Decade Column ------------------
dt_index = pd.DatetimeIndex(data_clean['Release_Date'])
data_clean['Decade'] = dt_index.year // 10 * 10

# Split into old and new films
old_films = data_clean[data_clean['Decade'] <= 1960]
new_films = data_clean[data_clean['Decade'] > 1960]
print(f"Old films count: {len(old_films)}")
print(f"Most expensive old film:\n{old_films.sort_values(by='USD_Production_Budget', ascending=False).head(1)}")

# ------------------ Regression Plot: Old Films ------------------
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})
plt.title("Old Films: Budget vs Revenue")
plt.show()

# ------------------ Regression Plot: New Films ------------------
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')
plt.title("New Films: Budget vs Revenue")
plt.show()

# ------------------ Linear Regression with Scikit-learn ------------------
regression = LinearRegression()

# Features and target
X_new = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
y_new = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Fit the model
regression.fit(X_new, y_new)

# Intercept and Slope
print(f"Intercept (theta_0): {regression.intercept_[0]:,.2f}")
print(f"Slope (theta_1): {regression.coef_[0][0]:,.2f}")

# R-squared
print(f"R-squared: {regression.score(X_new, y_new):.4f}")

# Predict revenue for $350M budget
budget = 350_000_000
predicted_revenue = regression.predict(pd.DataFrame({'USD_Production_Budget': [budget]}))[0][0]

print(f"Estimated revenue for $350M budget: ${round(predicted_revenue, -6):,.0f}")

# ------------------ Old Films Regression ------------------
X_old = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y_old = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression_old = LinearRegression()
regression_old.fit(X_old, y_old)

print("\n--- Old Films Regression ---")
print(f"Intercept: {regression_old.intercept_[0]:,.2f}")
print(f"Slope: {regression_old.coef_[0][0]:,.2f}")
print(f"R-squared: {regression_old.score(X_old, y_old):.4f}")
