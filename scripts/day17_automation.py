import pandas as pd
import os

# Project folder path
base_path = os.path.dirname(os.path.dirname(__file__))

# CSV file path
file_path = os.path.join(
    base_path,
    "data",
    "raw",
    "sales.csv"
)

# Read CSV automatically
df = pd.read_csv(file_path)

# Display information
print("Data Loaded Successfully!")

print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))

print("\nFirst 5 Records:")
print(df.head())

# Step 2 – Multiple CSV files automatically read karna

files = ["customers.csv", "products.csv", "orders.csv", "payments.csv", "sales.csv"]


for file in files:

    path = os.path.join(base_path, "data", "raw", file)

    # Read CSV
    data = pd.read_csv(path)

    # Remove duplicates
    clean_data = data.drop_duplicates().copy()

    # Fill missing values
    if "Revenue" in clean_data.columns:
        clean_data["Revenue"] = clean_data["Revenue"].fillna(
            clean_data["Quantity"] * clean_data["Selling_Price"]
        )

        clean_data["Profit"] = (
            clean_data["Revenue"]
            - clean_data["Quantity"] * clean_data["Cost_Price"]
        )

    if "City" in clean_data.columns:
        clean_data["City"] = clean_data["City"].fillna("Unknown")

    # Save cleaned CSV
    output_path = os.path.join(
        base_path,
        "data",
        "processed",
        file.replace(".csv", "_clean.csv")
    )

    clean_data.to_csv(output_path, index=False)

    # Final report
    print("\nFile:", file)
    print("Rows Before:", len(data))
    print("Rows After:", len(clean_data))
    print("Duplicates Removed:", len(data) - len(clean_data))
    print("Missing Values Before:", data.isnull().sum().sum())
    print("Missing Values After:", clean_data.isnull().sum().sum())
    print("Saved:", output_path)



