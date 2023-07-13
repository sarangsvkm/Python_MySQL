import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Apple st 652'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")