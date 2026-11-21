import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment

# Sales Data Load
df = pd.read_csv("data/processed/sales_from_mysql.csv")

# Products Data Load
products_df = pd.read_csv("data/processed/products_clean.csv")

print("Sales Data:", len(df))
print("Products Data:", len(products_df))

# Sales aur Products Merge
merged_df = df.merge(
    products_df,
    on="Product_ID",
    how="left"
)

# Category Wise Summary
category_summary = merged_df.groupby("Category").agg(
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

print("\nCATEGORY WISE SUMMARY:")
print(category_summary)

# Step 3: Excel Dashboard mein Category Data Add Karna
# Excel Workbook Create
wb = Workbook()

# Worksheet Create
ws = wb.active
ws.title = "Category Dashboard"

# Headers
ws["A1"] = "Category"
ws["B1"] = "Total Revenue"
ws["C1"] = "Total Profit"

# Category Data Excel mein add karo
for row in category_summary.itertuples(index=False, name=None):
    ws.append(row)

print("Category data added to Excel sheet!")
# Bar Chart Create
chart = BarChart()

chart.type = "col"
chart.style = 10
chart.legend.position = "b"

chart.height = 10
chart.width = 20

chart.title = "Category Wise Revenue and Profit"
chart.x_axis.title = "Category"
chart.y_axis.title = "Amount"

# Chart Data Select
data = Reference(
    ws,
    min_col=2,
    max_col=3,
    min_row=1,
    max_row=5
)

# Category Names Select
categories = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=5
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# Chart Excel Sheet mein Add
ws.add_chart(chart, "E2")

# Excel File Save
output_file = "reports/Category_Dashboard.xlsx"

wb.save(output_file)

print("Excel Dashboard Saved Successfully!")
print("File:", output_file)