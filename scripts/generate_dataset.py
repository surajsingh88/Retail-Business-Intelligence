
import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

# Output folder
output_path = "data/raw"
os.makedirs(output_path, exist_ok=True)

# 1. Customers
customers = pd.DataFrame({
    "Customer_ID": range(1, 101),
    "Customer_Name": [
        f"Customer_{i}" for i in range(1, 101)
    ],
    "City": np.random.choice(
        ["Delhi", "Lucknow", "Mumbai", "Pune", "Jaipur"],
        100
    ),
    "Age": np.random.randint(18, 65, 100)
})

# 2. Products
products = pd.DataFrame({
    "Product_ID": range(101, 131),
    "Product_Name": [
        f"Product_{i}" for i in range(1, 31)
    ],
    "Category": np.random.choice(
        ["Electronics", "Clothing", "Grocery", "Furniture"],
        30
    ),
    "Cost_Price": np.random.randint(100, 3000, 30),
    "Selling_Price": np.random.randint(500, 5000, 30)
})

# 3. Orders
orders = pd.DataFrame({
    "Order_ID": range(1001, 2001),
    "Customer_ID": np.random.randint(1, 101, 1000),
    "Order_Date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-01-01", "2025-12-31"),
            1000
        )
    ),
    "Status": np.random.choice(
        ["Delivered", "Pending", "Cancelled"],
        1000,
        p=[0.75, 0.15, 0.10]
    )
})

# 4. Sales
sales = pd.DataFrame({
    "Sale_ID": range(2001, 3001),
    "Order_ID": orders["Order_ID"],
    "Product_ID": np.random.randint(101, 131, 1000),
    "Quantity": np.random.randint(1, 6, 1000)
})

sales = sales.merge(
    products[["Product_ID", "Selling_Price", "Cost_Price"]],
    on="Product_ID"
)

sales["Revenue"] = sales["Quantity"] * sales["Selling_Price"]
sales["Profit"] = sales["Quantity"] * (
    sales["Selling_Price"] - sales["Cost_Price"]
)

# 5. Payments
payments = pd.DataFrame({
    "Payment_ID": range(3001, 4001),
    "Order_ID": orders["Order_ID"],
    "Payment_Method": np.random.choice(
        ["UPI", "Card", "Cash", "Net Banking"],
        1000
    ),
    "Payment_Status": np.random.choice(
        ["Paid", "Pending", "Failed"],
        1000,
        p=[0.80, 0.12, 0.08]
    )
})

# Introduce data quality issues for practice
sales = pd.concat([sales, sales.iloc[[0]]], ignore_index=True)
sales.loc[5, "Revenue"] = np.nan
customers.loc[10, "City"] = np.nan

# Save CSV files
customers.to_csv(f"{output_path}/customers.csv", index=False)
products.to_csv(f"{output_path}/products.csv", index=False)
orders.to_csv(f"{output_path}/orders.csv", index=False)
sales.to_csv(f"{output_path}/sales.csv", index=False)
payments.to_csv(f"{output_path}/payments.csv", index=False)

print("RetailPro Dataset Generated Successfully!")
print("5 CSV files created in data/raw/")
