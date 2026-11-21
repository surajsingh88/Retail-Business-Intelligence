from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

# File path
file_path = "reports/Category_Dashboard.xlsx"

# Load workbook
wb = load_workbook(file_path)

# Protect workbook structure
wb.security = WorkbookProtection(lockStructure=True)
wb.security.workbookPassword = "workbook123"

# Save workbook
wb.save(file_path)

print("Excel workbook structure protected successfully!")