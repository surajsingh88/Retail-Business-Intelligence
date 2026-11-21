
import pandas as pd

# Sales data load karo
sales = pd.read_csv("data/processed/sales_clean.csv")

# Customers data load karo
customers = pd.read_csv("data/processed/customers_clean.csv")

print("Sales Columns:")
print(sales.columns)

print("\nCustomer Columns:")
print(customers.columns)

print("\nFirst 5 Customers:")
print(customers.head())

# Step 2 – Merge datasets

# Step 1: Sales ko Orders ke saath merge karo
orders = pd.read_csv("data/raw/orders.csv")
sales_orders = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Step 2: Sales_Orders ko Customers ke saath merge karo
customer_sales = sales_orders.merge(
    customers,
    on="Customer_ID",
    how="left"
)

print("\nMerged Customer Sales:")
print(customer_sales.head())

print("\nTotal Rows:", len(customer_sales))


# Step 3 – Customer-wise Revenue calculate karo


customer_revenue = customer_sales.groupby(
    "Customer_Name"
)["Revenue"].sum().sort_values(ascending=False)

print("\nTop 10 Customers by Revenue:")
print(customer_revenue.head(10))

# Step 4 – Customer-wise Profit calculate karo

customer_profit = customer_sales.groupby(
    "Customer_Name"
)["Profit"].sum().sort_values(ascending=False)

print("\nTop 10 Customers by Profit:")
print(customer_profit.head(10))


# Step 5 – Customer-wise Profit Margin

customer_summary = customer_sales.groupby(
    "Customer_Name"
).agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

customer_summary["Profit_Margin"] = (
    customer_summary["Total_Profit"] /
    customer_summary["Total_Revenue"] * 100
)

customer_summary = customer_summary.sort_values(
    by="Profit_Margin",
    ascending=False
)

print("\nTop 10 Customers by Profit Margin:")
print(customer_summary.head(10))


# Step 6 – Customer City-wise Analysis


city_revenue = customer_sales.groupby(
    "City"
)["Revenue"].sum().sort_values(ascending=False)

print("\nCity-wise Revenue:")
print(city_revenue)

# : City-wise Profit Analysis

city_profit = customer_sales.groupby(
    "City"
)["Profit"].sum().sort_values(ascending=False)

print("\nCity-wise Profit:")
print(city_profit)

# City-wise Profit Margin

city_summary = customer_sales.groupby("City").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

city_summary["Profit_Margin"] = (
    city_summary["Total_Profit"] /
    city_summary["Total_Revenue"]
) * 100

city_summary = city_summary.sort_values(
    by="Profit_Margin",
    ascending=False
)

print("\nCity-wise Profit Margin:")
print(city_summary)
