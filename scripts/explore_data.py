
import pandas as pd

# Load sales dataset
sales = pd.read_csv("data/raw/sales.csv")

# Load customers dataset
customers = pd.read_csv("data/raw/customers.csv")


print("========== SALES DATA ==========")

# First 5 rows
print(sales.head())

# Data types
print("\nData Types:")
print(sales.dtypes)

# Statistical summary
print("\nStatistical Summary:")
print(sales.describe())


print("\n========== CUSTOMERS DATA ==========")

# First 5 rows
print(customers.head())

# Data types
print("\nData Types:")
print(customers.dtypes)

# Statistical summary
print("\nStatistical Summary:")
print(customers.describe())


print("Total Revenue:", sales["Revenue"].sum())

print("Average Revenue:", sales["Revenue"].mean())

print("Maximum Revenue:", sales["Revenue"].max())

print("Minimum Revenue:", sales["Revenue"].min())

print("Total Profit:", sales["Profit"].sum())

print("Average Profit:", sales["Profit"].mean())

print("Maximum Profit:", sales["Profit"].max())

print("Minimum Profit:", sales["Profit"].min())

profit_margin = (
    sales["Profit"].sum() /
    sales["Revenue"].sum()
) * 100

print("Profit Margin:", profit_margin)

profit_margin = (
    sales["Profit"].sum() /
    sales["Revenue"].sum()
) * 100

print("Profit Margin:", profit_margin, "%")