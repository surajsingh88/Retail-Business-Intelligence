import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# File path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load Excel workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Format header
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(
        start_color="366092",
        end_color="366092",
        fill_type="solid"
    )
    cell.alignment = Alignment(horizontal="center")

print("Excel file loaded successfully!")
print("Rows:", ws.max_row)
print("Columns:", ws.max_column)

wb.save(file_path)

print("Formatting applied and file saved successfully!")