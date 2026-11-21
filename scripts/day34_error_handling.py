
import pandas as pd
import logging
from pathlib import Path

# Project paths
base_path = Path(".")
dashboard_file = base_path / "reports/Category_Dashboard.xlsx"
analysis_file = base_path / "reports/Category_Analysis_Report.xlsx"
output_file = base_path / "reports/Consolidated_Business_Report.xlsx"

# Create logs folder
log_folder = base_path / "logs"
log_folder.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_folder / "day34_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_report():
    try:
        # Check input files
        if not dashboard_file.exists():
            raise FileNotFoundError(dashboard_file)

        if not analysis_file.exists():
            raise FileNotFoundError(analysis_file)

        # Read Excel sheets
        dashboard = pd.read_excel(
            dashboard_file,
            sheet_name="Category Dashboard",
            header=None
        )

        analysis = pd.read_excel(
            analysis_file,
            sheet_name="Category Analysis"
        )

        # Create consolidated report
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            dashboard.to_excel(
                writer,
                sheet_name="Dashboard_Data",
                index=False,
                header=False
            )

            analysis.to_excel(
                writer,
                sheet_name="Category_Analysis",
                index=False
            )

        logging.info("Report generated successfully")

        print("Report generated successfully!")
        print("Dashboard rows:", len(dashboard))
        print("Analysis rows:", len(analysis))
        print("Output:", output_file)

    except Exception as error:
        logging.exception("Report generation failed")
        print("Error:", error)

# Run automation
generate_report()
