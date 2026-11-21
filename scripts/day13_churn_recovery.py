import pandas as pd

# Load sales data
sales = pd.read_csv("data/processed/sales_clean.csv")

# Load orders data
orders = pd.read_csv("data/raw/orders.csv")

# Merge datasets
recovery_data = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

print(recovery_data.head())

print("\nTotal Rows:")
print(len(recovery_data))

# Step 2: Churned customers ka data nikalo
# Convert Order Date
recovery_data["Order_Date"] = pd.to_datetime(
    recovery_data["Order_Date"]
)

# Find last purchase date
last_purchase = recovery_data.groupby(
    "Customer_ID"
)["Order_Date"].max()

# Calculate inactive days
snapshot_date = recovery_data["Order_Date"].max()

days_inactive = (snapshot_date - last_purchase).dt.days

# Identify churned customers
churned_ids = days_inactive[days_inactive >= 60].index

print("\nChurned Customer IDs:")
print(churned_ids)

print("\nTotal Churned Customers:")
print(len(churned_ids))

# Step 3: Churned customers ka Revenue aur Profit
# Filter churned customer data
churned_data = recovery_data[
    recovery_data["Customer_ID"].isin(churned_ids)
]

# Customer-wise revenue and profit
churned_summary = churned_data.groupby("Customer_ID").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order_ID", "nunique")
).reset_index()

print("\nChurned Customer Business Summary:")
print(churned_summary)

print("\nTotal Revenue from Churned Customers:")
print(churned_summary["Total_Revenue"].sum())

print("\nTotal Profit from Churned Customers:")
print(churned_summary["Total_Profit"].sum())

# Step 4: High-value churned customers
# Sort customers by profit
high_value_churn = churned_summary.sort_values(
    by="Total_Profit",
    ascending=False
)

print("\nTop 5 High Value Churned Customers:")
print(high_value_churn.head(5))

# Step 5: Recovery priority
# Assign recovery priority
high_value_churn["Recovery_Priority"] = high_value_churn[
    "Total_Profit"
].apply(
    lambda x: "High" if x >= 60000 else "Medium"
)

print("\nCustomer Recovery Priority:")
print(
    high_value_churn[
        ["Customer_ID", "Total_Profit", "Recovery_Priority"]
    ].head(5)
)