import mysql.connector

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mydatabase"
)

con =DB.cursor()
con.execute("create table customers (name VARCHAR(255),Address VARCHAR(255))")
