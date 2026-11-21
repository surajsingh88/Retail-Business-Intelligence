from openpyxl import load_workbook
import os

# File path
file_path = "reports/Category_Dashboard.xlsx"

# Load Excel workbook
wb = load_workbook(file_path)

# Select worksheet
ws = wb["Category Dashboard"]

# Protect worksheet
ws.protection.sheet = True
ws.protection.password = "retail123"

# Save workbook
wb.save(file_path)

print("Excel sheet protected successfully!")