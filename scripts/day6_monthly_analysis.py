import pandas as pd

# Sales data load karo
sales = pd.read_csv("data/processed/sales_clean.csv")

print("Sales Data:")
print(sales.head())

print("\nColumns:")
print(sales.columns)

# Step 2: Orders dataset check karo
# Orders data load karo
orders = pd.read_csv("data/raw/orders.csv")

print("\nOrders Columns:")
print(orders.columns)

print("\nFirst 5 Orders:")
print(orders.head())

# Step 3: Sales + Orders Merge
# Sales aur Orders merge karo
monthly_sales = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Date ko datetime format mein convert karo

monthly_sales["Order_Date"] = pd.to_datetime(
    monthly_sales["Order_Date"]
)

print("\nMerged Monthly Data:")
print(monthly_sales.head())

# Step 4: Monthly Revenue Analysis
# Month extract karo
monthly_sales["Month"] = monthly_sales["Order_Date"].dt.to_period("M")

# Month-wise Revenue
monthly_revenue = monthly_sales.groupby("Month")["Revenue"].sum()

# Sort karo
monthly_revenue = monthly_revenue.sort_index()

print("\nMonthly Revenue:")
print(monthly_revenue)

# Monthly Profit Analysis
# Monthly Profit Analysis

monthly_profit = monthly_sales.groupby("Month")["Profit"].sum()

monthly_profit = monthly_profit.sort_index()

print("\nMonthly Profit:")
print(monthly_profit)

# Step 6: Highest aur Lowest Month automatically find karo
# Highest Revenue Month
best_revenue_month = monthly_revenue.idxmax()
print("\nHighest Revenue Month:", best_revenue_month)

# Lowest Revenue Month
worst_revenue_month = monthly_revenue.idxmin()
print("Lowest Revenue Month:", worst_revenue_month)

# Highest Profit Month
best_profit_month = monthly_profit.idxmax()
print("Highest Profit Month:", best_profit_month)

# Lowest Profit Month
worst_profit_month = monthly_profit.idxmin()
print("Lowest Profit Month:", worst_profit_month)