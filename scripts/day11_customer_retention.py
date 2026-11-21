
import pandas as pd

# Sales data
sales = pd.read_csv("data/processed/sales_clean.csv")

# Orders data
orders = pd.read_csv("data/raw/orders.csv")

# Merge data
retention_data = sales.merge(
    orders,
    on="Order_ID",
    how="left"
)

# Customer-wise purchase count
customer_orders = retention_data.groupby(
    "Customer_ID"
).agg(
    Total_Orders=("Order_ID", "nunique"),
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

print("Customer Retention Data:")
print(customer_orders.head(10))

# Step 2 – Repeat vs One-time Customers

# Customer Retention Category

customer_orders["Customer_Type"] = customer_orders[
    "Total_Orders"
].apply(
    lambda x: "Repeat Customer" if x > 1 else "One-time Customer"
)

print("\nCustomer Type Count:")
print(customer_orders["Customer_Type"].value_counts())

# Step 3 – Repeat Customer Percentage

customer_counts = customer_orders["Customer_Type"].value_counts()

total_customers = customer_counts.sum()

repeat_customers = customer_counts.get("Repeat Customer", 0)

repeat_rate = (repeat_customers / total_customers) * 100

print("\nRepeat Customer Rate:", round(repeat_rate, 2), "%")
