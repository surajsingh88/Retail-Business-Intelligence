
from openpyxl import load_workbook

# Excel file path
file_path = "reports/Category_Dashboard.xlsx"

# Load workbook
wb = load_workbook(file_path)

# Print all sheet names
print("Sheet names:", wb.sheetnames)

# Access a specific sheet
ws = wb["Category Dashboard"]

# Print sheet name
print("Current sheet:", ws.title)

# Print data from the sheet
for row in ws.iter_rows(min_row=1, max_row=5, values_only=True):
    print(row)
