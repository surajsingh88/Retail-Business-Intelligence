import pandas as pd
import mysql.connector

# Load orders CSV
orders = pd.read_csv("data/raw/orders.csv")

print(orders.head())
print("Total Orders:", len(orders))

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="retailpro"
)

cursor = connection.cursor()

# Prepare INSERT query
query = """
INSERT INTO orders
(Order_ID, Customer_ID, Order_Date, Status)
VALUES (%s, %s, %s, %s)
"""

values = [
    (
        int(row.Order_ID),
        int(row.Customer_ID),
        row.Order_Date,
        row.Status
    )
    for row in orders.itertuples(index=False)
]

cursor.executemany(query, values)
connection.commit()

print("Inserted Orders:", cursor.rowcount)

cursor.close()
connection.close()