from getpass import getpass
import mysql.connector
import pandas as pd

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password=getpass("MySQL Password: "),
    database="retailpro"
)
# Read SQL data
query = "SELECT * FROM sales"

df = pd.read_sql(query, connection)

print("Data Fetched Successfully!")
print("Total Rows:", len(df))
print(df.head())

# Next task: Automatic CSV Export
output_path = "data/processed/sales_from_mysql.csv"

df.to_csv(output_path, index=False)

# Automatic Revenue & Profit Report
# Business Summary Report

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

profit_margin = (total_profit / total_revenue) * 100

print("\n----- BUSINESS SUMMARY -----")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Quantity:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")

print("CSV Exported Successfully!")
print("File Saved:", output_path)

connection.close()
from getpass import getpass

try:
    connection = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password=getpass("MySQL Password: "),
        database="retailpro"
    )

    if connection.is_connected():
        print("MySQL Connected Successfully!")

except mysql.connector.Error as error:
    print("Database Connection Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection Closed")
