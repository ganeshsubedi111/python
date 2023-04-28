# creating table 
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
try:
 mycursor = mydb.cursor()
 mycursor.execute("CREATE TABLE users (uid INT primary key auto_increment ,name VARCHAR(255), address VARCHAR(255),phone INT)")
 print("successfully created table")
except:
 print("failed to create table")
