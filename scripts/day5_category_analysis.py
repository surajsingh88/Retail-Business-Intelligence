import pandas as pd

# Products data load karo
products = pd.read_csv("data/raw/products.csv")

print("Products Columns:")
print(products.columns)

print("\nFirst 10 Products:")
print(products.head(150))

# Step 2: Sales data load aur merge karo
# Sales data load karo
sales = pd.read_csv("data/processed/sales_clean.csv")

# Sales aur Products merge karo
category_sales = sales.merge(
    products,
    on="Product_ID",
    how="left"
)

print("\nMerged Data:")
print(category_sales.head())

# Step 3: Category-wise Revenue calculate karo
category_revenue = category_sales.groupby(
    "Category"
)["Revenue"].sum().sort_values(ascending=False)

print("\nCategory-wise Revenue:")
print(category_revenue)

# Step 4: Category-wise Profit calculate karo
# Step 4 - Category-wise Profit

category_profit = category_sales.groupby(
    "Category"
)["Profit"].sum().sort_values(ascending=False)

print("\nCategory-wise Profit:")
print(category_profit)

category_summary = category_sales.groupby("Category").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

category_summary["Profit_Margin"] = (
    category_summary["Total_Profit"] /
    category_summary["Total_Revenue"]
) * 100

category_summary = category_summary.sort_values(
    by="Profit_Margin",
    ascending=False
)

print("\nCategory-wise Profit Margin:")
print(category_summary)