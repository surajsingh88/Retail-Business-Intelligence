import pandas as pd

payments = pd.read_csv("data/raw/payments.csv")

print(payments.head())
print("Total Payments:", len(payments))

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="retailpro"
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM payments")
count = cursor.fetchone()[0]

print("Existing Payments:", count)
if count == 0:
    query = """
    INSERT INTO payments
    (Payment_ID, Order_ID, Payment_Method, Payment_Status)
    VALUES (%s, %s, %s, %s)
    """

    values = list(payments.itertuples(index=False, name=None))

    cursor.executemany(query, values)
    connection.commit()

    print("Inserted Payments:", cursor.rowcount)
else:
    print("Payments already exist:", count)

cursor.close()
connection.close()