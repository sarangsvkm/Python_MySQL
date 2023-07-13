import mysql.connector

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mydatabase"
)

con =DB.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
con.execute(sql, val)