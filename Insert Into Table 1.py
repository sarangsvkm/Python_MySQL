import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydatabase"
)
con=db.cursor()

sql="INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
    ('SRG','SRF@@')
]
con.executemany(sql,val)
db.commit()