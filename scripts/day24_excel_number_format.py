from openpyxl import load_workbook

# File path
file_path = "reports/Category_Analysis_Report.xlsx"

# Load Excel workbook
wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Number formatting
for row in range(2, ws.max_row + 1):
    ws["B" + str(row)].number_format = '₹#,##0'
    ws["C" + str(row)].number_format = '₹#,##0'
    ws["D" + str(row)].number_format = '#,##0'
    ws["E" + str(row)].number_format = '0.00"%"'

# Save file
wb.save(file_path)

print("Number formatting applied successfully!")