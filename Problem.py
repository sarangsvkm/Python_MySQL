import mysql.connector
con=mysql.connector.connect(  host="localhost",user="root",password="admin", database="mydatabase")
c=con.cursor()
# c.execute("create table employee(id int primary key,name varchar(20),age int, salary int)")

c.execute("Insert into employee values(1,'Arun',23,200000)")
c.execute("Insert into employee values(2,'Anu',23,450000)")
c.execute("Insert into employee values(3,'Arun',25,400000)")
c.execute("SELECT * FROM employee")
myresult=c.fetchall()
for x in myresult:
    print(x)
con.commit()