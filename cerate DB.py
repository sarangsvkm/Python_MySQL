import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
database = "mydatabase"
)

# mycon=mydb.cursor()
#
# mycon.execute("CREATE DATABASE mydatabase2")
# print(mydb)
# mycon.execute("SHOW DATABASES")
#
# for x in mycon:
#   print(x)
#
