import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  # port="3306",
  # password="soheil@1382@#"
  database = 'soheilbutiful'
)
c = mydb.cursor()

sql = "INSERT INTO customers(name,adress) VALUES(%s,%s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
c.executemany(sql, val)

mydb.commit()

print(c.rowcount, "was inserted.")