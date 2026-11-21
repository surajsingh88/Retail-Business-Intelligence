import pandas as pd

# Sales data load karo
sales = pd.read_csv("data/processed/sales_clean.csv")

# Orders data load karo
orders = pd.read_csv("data/raw/orders.csv")

# Customers data load karo
customers = pd.read_csv("data/processed/customers_clean.csv")

# Sales aur Orders merge karo
sales_orders = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Customer data merge karo
customer_sales = sales_orders.merge(
    customers,
    on="Customer_ID",
    how="left"
)

print("Customer Sales Data:")
print(customer_sales.head())

print("\nTotal Customers:")
print(customer_sales["Customer_ID"].nunique())

# Step 2 – Customer Summary Analysis
# Customer-wise Summary

customer_summary = customer_sales.groupby(
    ["Customer_ID", "Customer_Name"]
).agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum"),
    Purchase_Count=("Order_ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

print("\nCustomer Summary:")
print(customer_summary.head(10))

print("\nTop 10 Customers by Revenue:")
print(
    customer_summary.sort_values(
        by="Total_Revenue",
        ascending=False
    ).head(10)
)

# Customer Segmentation

customer_summary["Segment"] = pd.qcut(
    customer_summary["Total_Revenue"],
    q=3,
    labels=["Low Value", "Regular", "High Value"]
)

print("\nCustomer Segmentation:")
print(customer_summary.head(10))

print("\nSegment-wise Customer Count:")
print(customer_summary["Segment"].value_counts())

# Step 4 – Segment-wise Business Analysis
segment_summary = customer_summary.groupby(
    "Segment",
    observed=True
).agg(
    Total_Revenue=("Total_Revenue", "sum"),
    Total_Profit=("Total_Profit", "sum"),
    Avg_Revenue=("Total_Revenue", "mean"),
    Avg_Profit=("Total_Profit", "mean"),
    Total_Customers=("Customer_ID", "count")
)

print("\nSegment-wise Business Analysis:")
print(segment_summary)
