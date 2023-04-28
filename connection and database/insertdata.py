import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, address,phone) VALUES (%s, %s,%d)"
val = ("Ganesh", "Parbat ",21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")