
from pathlib import Path
from openpyxl import load_workbook
import math

# Project files
report_file = Path("reports/End_to_End_Business_Report.xlsx")
log_file = Path("logs/day35_automation.log")

# Check files
if not report_file.exists():
    raise FileNotFoundError("Final Excel report not found!")

if not log_file.exists():
    print("Warning: Automation log not found!")

# Load report
wb = load_workbook(report_file, data_only=True)

# Check sheets
required_sheets = ["Dashboard", "Category Analysis"]

for sheet in required_sheets:
    if sheet not in wb.sheetnames:
        raise ValueError(f"Missing sheet: {sheet}")

dashboard = wb["Dashboard"]
category = wb["Category Analysis"]

# Verify KPIs
expected_kpis = {
    "Revenue": (dashboard["B4"].value, 9310426),
    "Profit": (dashboard["B5"].value, 3999674),
    "Margin": (dashboard["B6"].value, 42.96),
    "Orders": (dashboard["B8"].value, 1000)
}

for name, (actual, expected) in expected_kpis.items():
    if actual is None or not math.isclose(
        float(actual), expected, rel_tol=0, abs_tol=0.01
    ):
        raise ValueError(f"{name} verification failed: {actual}")

    print(f"{name}: PASS")

# Verify categories
categories = {
    category.cell(row, 1).value
    for row in range(2, category.max_row + 1)
}

expected_categories = {
    "Clothing", "Electronics", "Furniture", "Grocery"
}

if categories != expected_categories:
    raise ValueError("Category verification failed!")

print("Categories: PASS")

# Verify chart
chart_count = len(wb["Dashboard"]._charts)

if chart_count == 0:
    raise ValueError("Dashboard chart not found!")

print("Dashboard Chart: PASS")

print("\nFINAL PROJECT VERIFICATION SUCCESSFUL!")
print("Report:", report_file)
print("Log:", log_file)
