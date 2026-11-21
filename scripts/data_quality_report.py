
import pandas as pd

# Load raw and cleaned sales data
raw = pd.read_csv("data/raw/sales.csv")
clean = pd.read_csv("data/processed/sales_clean.csv")

print("===== DATA QUALITY REPORT =====")

print("\nRaw Dataset:")
print("Rows:", len(raw))
print("Duplicates:", raw.duplicated().sum())
print("Missing Values:", raw.isnull().sum().sum())

print("\nCleaned Dataset:")
print("Rows:", len(clean))
print("Duplicates:", clean.duplicated().sum())
print("Missing Values:", clean.isnull().sum().sum())

print("\n===== CLEANING SUMMARY =====")
print("Rows Removed:", len(raw) - len(clean))
print("Data Cleaning Completed!")


report = pd.DataFrame({
    "Metric": ["Total Rows", "Duplicates", "Missing Values"],
    "Raw": [
        len(raw),
        raw.duplicated().sum(),
        raw.isnull().sum().sum()
    ],
    "Cleaned": [
        len(clean),
        clean.duplicated().sum(),
        clean.isnull().sum().sum()
    ]
})

report.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print("Quality Report Saved Successfully!")
