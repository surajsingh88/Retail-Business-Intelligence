
import pandas as pd

# Source Excel files
dashboard_file = "reports/Category_Dashboard.xlsx"
analysis_file = "reports/Category_Analysis_Report.xlsx"

# Read dashboard data
dashboard_data = pd.read_excel(
    dashboard_file,
    sheet_name="Category Dashboard",
    header=None
)

# Read category analysis data
analysis_data = pd.read_excel(
    analysis_file,
    sheet_name="Category Analysis"
)

# Create consolidated Excel report
output_file = "reports/Consolidated_Business_Report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    dashboard_data.to_excel(
        writer,
        sheet_name="Dashboard_Data",
        index=False,
        header=False
    )

    analysis_data.to_excel(
        writer,
        sheet_name="Category_Analysis",
        index=False
    )

print("Reports consolidated successfully!")
print("Dashboard rows:", len(dashboard_data))
print("Analysis rows:", len(analysis_data))
print("Output:", output_file)
