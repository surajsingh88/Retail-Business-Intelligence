import pandas as pd

products = pd.read_csv("data/raw/products.csv")

print(products.head())
print("Total Products:", len(products))

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port = "3307",
    user="root",
    password="root",
    database="retailpro"
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

print("Existing Products:", count)
if count == 0:

    query = """
    INSERT INTO products
    (Product_ID, Product_Name, Category, Cost_Price, Selling_Price)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = list(products.itertuples(index=False, name=None))

    cursor.executemany(query, values)
    connection.commit()

    print("Inserted Products:", cursor.rowcount)

else:
    print("Products already exist:", count)

cursor.close()
connection.close()

