import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="retailpro"
)

if connection.is_connected():
    print("MySQL Connected Successfully!")

    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")

    result = cursor.fetchall()

    print("\nDatabase Tables:")

    for table in result:
        print(table[0])

    cursor.close()
    connection.close()