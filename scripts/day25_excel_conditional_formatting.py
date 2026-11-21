from openpyxl import load_workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill

# File path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Green fill for high profit
green_fill = PatternFill(
    start_color="C6EFCE",
    end_color="C6EFCE",
    fill_type="solid"
)

# Red fill for low profit
red_fill = PatternFill(
    start_color="FFC7CE",
    end_color="FFC7CE",
    fill_type="solid"
)

# High profit highlight
ws.conditional_formatting.add(
    "C2:C5",
    CellIsRule(operator="greaterThanOrEqual", formula=["1000000"], fill=green_fill)
)

# Low profit highlight
ws.conditional_formatting.add(
    "C2:C5",
    CellIsRule(operator="lessThan", formula=["500000"], fill=red_fill)
)

# Save workbook
wb.save(file_path)

print("Conditional formatting applied successfully!")