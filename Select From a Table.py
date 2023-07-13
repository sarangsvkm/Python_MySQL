import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydatabase"
)
con=db.cursor()
con.execute("SELECT * FROM customers")
myresult=con.fetchall()
for x in myresult:
    print(x)