
import pandas as pd

# Sales data
sales = pd.read_csv("data/processed/sales_clean.csv")

# Orders data
orders = pd.read_csv("data/raw/orders.csv")

# Merge datasets
churn_data = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Convert Order Date
churn_data["Order_Date"] = pd.to_datetime(
    churn_data["Order_Date"]
)

# Customer-wise last purchase date
customer_last_purchase = churn_data.groupby(
    "Customer_ID"
)["Order_Date"].max()

print("Last Purchase Date:")
print(customer_last_purchase.head(10))

print("\nTotal Customers:")
print(customer_last_purchase.count())

# Reference date
snapshot_date = churn_data["Order_Date"].max()

# Calculate days since last purchase
days_inactive = snapshot_date - customer_last_purchase

print("\nDays Since Last Purchase:")
print(days_inactive.head(10))

# Identify churned customers
churned_customers = days_inactive[
    days_inactive.dt.days >= 60
]

print("\nChurned Customers:")
print(churned_customers)

print("\nTotal Churned Customers:")
print(len(churned_customers))

# Calculate churn rate
total_customers = customer_last_purchase.count()
churn_rate = (len(churned_customers) / total_customers) * 100

print("\nChurn Rate:")
print(round(churn_rate, 2), "%")