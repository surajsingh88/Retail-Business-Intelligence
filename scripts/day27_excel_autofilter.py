from openpyxl import load_workbook

# Excel file path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Apply AutoFilter
ws.auto_filter.ref = ws.dimensions

# Save workbook
wb.save(file_path)

print("AutoFilter applied successfully!")