
from openpyxl import load_workbook

# Original Excel file
file_path = "reports/Category_Dashboard.xlsx"

# Load workbook
wb = load_workbook(file_path)

# Source sheet
source_ws = wb["Category Dashboard"]

# Create a new sheet
target_ws = wb.create_sheet("Data Copy")

# Copy data from source to target
for row in source_ws.iter_rows():
    for cell in row:
        target_ws[cell.coordinate] = cell.value

# Save as a new workbook
output_path = "reports/Category_Dashboard_Copy.xlsx"
wb.save(output_path)

print("Data copied successfully!")
print("New sheet created: Data Copy")
print("File saved:", output_path)
