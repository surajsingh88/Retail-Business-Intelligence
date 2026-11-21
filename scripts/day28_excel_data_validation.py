from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation

# File path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Create dropdown list
category_dropdown = DataValidation(
    type="list",
    formula1='"Grocery,Furniture,Clothing,Electronics"',
    allow_blank=True
)

# Add dropdown to worksheet
ws.add_data_validation(category_dropdown)

# Apply dropdown to cells A2:A5
category_dropdown.add("A2:A5")

# Save workbook
wb.save(file_path)

print("Category dropdown created successfully!")