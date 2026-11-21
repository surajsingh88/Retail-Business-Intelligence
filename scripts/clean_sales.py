
import pandas as pd

# Load original sales data
sales = pd.read_csv("data/raw/sales.csv")

# Before cleaning
print("Before Cleaning:")
print("Total Rows:", sales.shape[0])
print("Duplicate Rows:", sales.duplicated().sum())

# Remove duplicate rows
sales = sales.drop_duplicates()

# After cleaning
print("\nAfter Cleaning:")
print("Total Rows:", sales.shape[0])
print("Duplicate Rows:", sales.duplicated().sum())

# Save cleaned data
sales.to_csv(
    "data/processed/sales_clean.csv",
    index=False
)

print("\nCleaned data saved successfully!")

# 1. Missing values check karo
print("\nMissing Values:")
print(sales.isnull().sum())

# 2. Missing Revenue calculate karo
sales["Revenue"] = sales["Revenue"].fillna(
    sales["Quantity"] * sales["Selling_Price"]
)
# 3. Verify karo
print("\nMissing Values After Cleaning:")
print(sales.isnull().sum())
sales.to_csv("data/processed/sales_clean.csv", index=False)

# Step 3: Profit Verification
sales["Profit"] = (
    sales["Revenue"] -
    (sales["Quantity"] * sales["Cost_Price"])
)

print("Profit Recalculated Successfully")

print("Missing Profit:", sales["Profit"].isnull().sum())

sales.to_csv(
    "data/processed/sales_clean.csv",
    index=False
)

print("Final Cleaned Dataset Saved!")

