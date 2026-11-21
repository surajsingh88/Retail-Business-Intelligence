import pandas as pd
# Step 1 – Dataset load karo
sales = pd.read_csv("data/processed/sales_clean.csv")
products = pd.read_csv("data/raw/products.csv")

print("Sales Data Loaded")
print("Products Data Loaded")

print(sales.head())
print(products.head())

# Step 2 – Dono datasets ko combine karo

product_sales = sales.merge(
    products,
    on="Product_ID",
    how="left"
)

print(product_sales.head())

# Step 3 – Product-wise Revenue calculate karo
product_revenue = product_sales.groupby(
    "Product_Name"
)["Revenue"].sum().sort_values(ascending=False)

print("\nProduct-wise Revenue:")
print(product_revenue)

# Step 4 - Product-wise Profit calculate karo

product_profit = product_sales.groupby(
    "Product_Name"
)["Profit"].sum().sort_values(ascending=False)

print("\nProduct-wise Profit:")
print(product_profit)

# Step 5 - Product-wise Profit Margin

product_summary = product_sales.groupby("Product_Name").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

product_summary["Profit_Margin"] = (
    product_summary["Total_Profit"] /
    product_summary["Total_Revenue"]
) * 100

product_summary = product_summary.sort_values(
    by="Profit_Margin",
    ascending=False
)

print("\nProduct-wise Profit Margin:")
print(product_summary)

print("\nTop 5 Products by Revenue:")
print(product_revenue.head(5))