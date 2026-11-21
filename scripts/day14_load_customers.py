import pandas as pd
import mysql.connector
from getpass import getpass

# Read CSV
customers = pd.read_csv("data/raw/customers.csv")

# Handle missing values
customers = customers.astype(object).where(
    pd.notna(customers), None
)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password=getpass("MySQL Password: "),
    database="retailpro"
)

cursor = connection.cursor()

# Check existing records
cursor.execute("SELECT COUNT(*) FROM customers")
count = cursor.fetchone()[0]

if count == 0:
    query = """
    INSERT INTO customers
    (Customer_ID, Customer_Name, City, Age)
    VALUES (%s, %s, %s, %s)
    """

    values = list(
        customers.itertuples(index=False, name=None)
    )

    cursor.executemany(query, values)
    connection.commit()

    print("Inserted Records:", cursor.rowcount)

else:
    print("Records already exist:", count)

# Verify records
cursor.execute("SELECT COUNT(*) FROM customers")
print("Total Customers:", cursor.fetchone()[0])

cursor.close()
connection.close()