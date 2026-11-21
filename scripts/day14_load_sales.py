import pandas as pd

# Load cleaned sales data
sales = pd.read_csv("data/processed/sales_clean.csv")

print(sales.head())
print("Total Sales:", len(sales))
print("Columns:", sales.columns.tolist())

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="retailpro"
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")
count = cursor.fetchone()[0]

print("Existing Sales:", count)
if count == 0:

    sales = pd.read_csv("data/processed/sales_clean.csv")

    query = """
    INSERT INTO sales
    (Sale_ID, Order_ID, Product_ID, Quantity,
     Selling_Price, Cost_Price, Revenue, Profit)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = list(sales.itertuples(index=False, name=None))

    cursor.executemany(query, values)
    connection.commit()

    print("Inserted Sales:", cursor.rowcount)

else:
    print("Sales already exist:", count)

cursor.close()
connection.close()