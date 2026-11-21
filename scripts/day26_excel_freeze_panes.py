from openpyxl import load_workbook

# Excel file path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Freeze header row
ws.freeze_panes = "A2"

# Save workbook
wb.save(file_path)

print("Freeze panes applied successfully!")