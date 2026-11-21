from openpyxl import load_workbook

file_path = "reports/Category_Analysis_Report.xlsx"

wb = load_workbook(file_path)
ws = wb["Category Analysis"]

# Auto adjust column width
for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter

    for cell in column:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))

    ws.column_dimensions[column_letter].width = max_length + 3

wb.save(file_path)

print("Column width adjusted successfully!")