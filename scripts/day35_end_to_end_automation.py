
import pandas as pd
import logging
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, Reference

# Project paths
sales_file = Path("data/processed/sales_from_mysql.csv")
products_file = Path("data/processed/products_clean.csv")
output_file = Path("reports/End_to_End_Business_Report.xlsx")

# Create folders
Path("reports").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/day35_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def run_automation():
    try:
        # 1. Check input files
        if not sales_file.exists() or not products_file.exists():
            raise FileNotFoundError("Required CSV file not found")

        # 2. Load datasets
        sales = pd.read_csv(sales_file)
        products = pd.read_csv(products_file)

        # 3. Merge datasets
        df = sales.merge(
            products[["Product_ID", "Category"]],
            on="Product_ID",
            how="left",
            validate="many_to_one"
        )

        if df["Category"].isna().any():
            raise ValueError("Some products have no matching category")

        # 4. Category-wise analysis
        category_report = df.groupby(
            "Category", as_index=False
        ).agg(
            Total_Revenue=("Revenue", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Quantity=("Quantity", "sum")
        )

        # 5. Calculate profit margin
        category_report["Profit_Margin"] = (
            category_report["Total_Profit"]
            / category_report["Total_Revenue"] * 100
        )

        category_report = category_report.sort_values(
            "Total_Revenue", ascending=False
        )

        # 6. Calculate business KPIs
        total_revenue = sales["Revenue"].sum()
        total_profit = sales["Profit"].sum()
        total_quantity = sales["Quantity"].sum()
        total_orders = sales["Order_ID"].nunique()

        profit_margin = (
            total_profit / total_revenue * 100
            if total_revenue else 0
        )

        kpi = pd.DataFrame({
            "Metric": [
                "Total Revenue",
                "Total Profit",
                "Profit Margin",
                "Total Quantity",
                "Total Orders"
            ],
            "Value": [
                total_revenue,
                total_profit,
                profit_margin,
                total_quantity,
                total_orders
            ]
        })

        # 7. Export Excel report
        with pd.ExcelWriter(
            output_file, engine="openpyxl"
        ) as writer:

            kpi.to_excel(
                writer,
                sheet_name="Dashboard",
                startrow=2,
                index=False
            )

            category_report.to_excel(
                writer,
                sheet_name="Category Analysis",
                index=False
            )

        # 8. Apply Excel formatting
        wb = load_workbook(output_file)

        ws_dash = wb["Dashboard"]
        ws_cat = wb["Category Analysis"]

        ws_dash.merge_cells("A1:B1")
        ws_dash["A1"] = "Retail Business - Automated Report"
        ws_dash["A1"].font = Font(
            bold=True, color="FFFFFF", size=16
        )
        ws_dash["A1"].fill = PatternFill(
            start_color="366092",
            end_color="366092",
            fill_type="solid"
        )
        ws_dash["A1"].alignment = Alignment(
            horizontal="center"
        )

        # Format KPI headers
        for cell in ws_dash[3]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(
                start_color="366092",
                end_color="366092",
                fill_type="solid"
            )

        ws_dash.column_dimensions["A"].width = 24
        ws_dash.column_dimensions["B"].width = 20

        # Format KPI numbers
        ws_dash["B4"].number_format = '₹#,##0'
        ws_dash["B5"].number_format = '₹#,##0'
        ws_dash["B6"].number_format = '0.00"%"'
        ws_dash["B7"].number_format = '#,##0'
        ws_dash["B8"].number_format = '#,##0'

        # Format Category Analysis
        for cell in ws_cat[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(
                start_color="366092",
                end_color="366092",
                fill_type="solid"
            )

        for row in range(2, ws_cat.max_row + 1):
            ws_cat[f"B{row}"].number_format = '₹#,##0'
            ws_cat[f"C{row}"].number_format = '₹#,##0'
            ws_cat[f"D{row}"].number_format = '#,##0'
            ws_cat[f"E{row}"].number_format = '0.00"%"'

        ws_cat.freeze_panes = "A2"
        ws_cat.auto_filter.ref = ws_cat.dimensions

        for column in ws_cat.columns:
            letter = column[0].column_letter
            max_length = max(
                len(str(cell.value)) if cell.value is not None else 0
                for cell in column
            )
            ws_cat.column_dimensions[letter].width = max_length + 3

        # 9. Create Revenue and Profit chart
        chart = BarChart()
        chart.type = "col"
        chart.style = 10
        chart.title = "Category-wise Revenue and Profit"
        chart.y_axis.title = "Amount (INR)"
        chart.x_axis.title = "Category"

        data = Reference(
            ws_cat,
            min_col=2,
            max_col=3,
            min_row=1,
            max_row=ws_cat.max_row
        )

        categories = Reference(
            ws_cat,
            min_col=1,
            min_row=2,
            max_row=ws_cat.max_row
        )

        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        chart.height = 8
        chart.width = 16

        ws_dash.add_chart(chart, "D3")

        # 10. Save final workbook
        wb.save(output_file)

        logging.info("End-to-end automation completed successfully")

        print("End-to-End Automation Successful!")
        print("Total Revenue:", total_revenue)
        print("Total Profit:", total_profit)
        print("Profit Margin:", round(profit_margin, 2), "%")
        print("Total Orders:", total_orders)
        print("Output:", output_file)

    except Exception as error:
        logging.exception("Automation failed")
        print("Automation failed:", error)


# Run complete automation
run_automation()
