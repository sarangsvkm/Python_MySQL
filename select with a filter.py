import mysql.connector
db = mysql.connector.connect(
  host="localhost",
    user="root",
    password="admin",
    database="mydatabase"
)
con=db.cursor()
con.execute("SELECT * FROM customers WHERE address ='Apple st 652'")
myresult = con.fetchall()
for x in myresult:
  print(x)