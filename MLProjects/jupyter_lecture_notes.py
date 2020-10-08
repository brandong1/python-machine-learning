# Read the imported csv file
import matplotlib.pyplot as plt  # setting alias to plt
from pandas import DataFrame
import pandas
data = pandas.read_csv('cost_revenue_clean.csv')

# Show summary statistics on data from csv
data.describe()

# Scientific Notation Examples
# 3.29e7 = 3.29 x 10 ^ 7 = 32,900,000.0

# From Linear Regression.ipynb
data = pandas.read_csv('cost_revenue_clean.csv')

data.describe()

# Importing Data from csv columns
X = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])

# Making chart visually bigger
plt.figure(figsize=(10, 6))

# alpha adds transparency
plt.scatter(X, y, alpha=0.3)

# Title of the entire chart
plt.title('Film Cost vs Global Revenue')

# X and Y axis labels
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross $')

# Remove whitespace that is outside the limits I set
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()
