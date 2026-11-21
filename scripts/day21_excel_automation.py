import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.chart import BarChart
import os
# File paths
sales_file = "data/processed/sales_from_mysql.csv"
products_file = "data/processed/products_clean.csv"

output_file = "reports/Automated_Business_Report.xlsx"

# Read data
sales = pd.read_csv(sales_file)
products = pd.read_csv(products_file)

print("Sales Data:", sales.shape)
print("Products Data:", products.shape)

print(sales.head())
print(products.head())

# Merge sales and products
df = sales.merge(products, on="Product_ID", how="left")

print("Merged Data:", df.shape)
print(df.head())

# Category wise analysis

category_report = df.groupby("Category").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

print(category_report)

# Sort categories by revenue

category_report = category_report.sort_values(
    by="Total_Revenue",
    ascending=False
)

print("\nSorted Category Report:")
print(category_report)

# Calculate profit margin

category_report["Profit_Margin"] = (
    category_report["Total_Profit"] /
    category_report["Total_Revenue"] * 100
)

print("\nFinal Category Report:")
print(category_report)

# Export report to Excel

category_report.to_excel(
    "reports/Category_Analysis_Report.xlsx",
    sheet_name="Category Analysis"
)

print("Excel report exported successfully!")