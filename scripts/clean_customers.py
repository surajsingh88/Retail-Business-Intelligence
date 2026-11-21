# 4: Customers Data Cleaning

import pandas as pd

# Load customers data
customers = pd.read_csv("data/raw/customers.csv")

# Before cleaning
print("Before Cleaning:")
print("Missing Values:")
print(customers.isnull().sum())

# Check missing City rows
print("\nMissing City Records:")
print(customers[customers["City"].isnull()])

# Fill missing City
customers["City"] = customers["City"].fillna("Unknown")

# After cleaning
print("\nAfter Cleaning:")
print(customers.isnull().sum())

# Save cleaned data
customers.to_csv(
    "data/processed/customers_clean.csv",
    index=False
)

print("\nCustomers Data Saved Successfully!")
