import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# MySQL se exported CSV read karna
df = pd.read_csv("data/processed/sales_from_mysql.csv")


# Business metrics calculate karo
# Business Metrics
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

profit_margin = (total_profit / total_revenue) * 100

print("\n--- BUSINESS SUMMARY ---")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Quantity:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")

# Step 3 ka next part: Excel workbook create karna.
# Excel Workbook Create
wb = Workbook()

# Default Sheet ka naam change karo
ws = wb.active
ws.title = "Business Summary"

# Report Title
ws["A1"] = "RETAIL BUSINESS PERFORMANCE REPORT"
ws["A1"].font = Font(bold=True, size=16)

# Headers
ws["A3"] = "Metric"
ws["B3"] = "Value"

# Step 4: Excel sheet mein business metrics add karo.

# Business Metrics ko Excel mein add karo
ws["A4"] = "Total Revenue"
ws["B4"] = total_revenue

ws["A5"] = "Total Profit"
ws["B5"] = total_profit

ws["A6"] = "Total Quantity"
ws["B6"] = total_quantity

ws["A7"] = "Profit Margin"
ws["B7"] = profit_margin / 100
# Number Formatting
ws["B4"].number_format = '₹#,##0.00'
ws["B5"].number_format = '₹#,##0.00'
ws["B6"].number_format = '#,##0'
ws["B7"].number_format = '0.00%'

# Header Formatting
for cell in ws[3]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(
        start_color="366092",
        end_color="366092",
        fill_type="solid"
    )

# Column Width
ws.column_dimensions["A"].width = 25
ws.column_dimensions["B"].width = 20

# Title Alignment
ws["A1"].alignment = Alignment(horizontal="center")
ws.merge_cells("A1:B1")

# Excel Report Save
output_file = "reports/Retail_Business_Report.xlsx"

wb.save(output_file)

print("\nExcel Report Generated Successfully!")
print("File Saved:", output_file)