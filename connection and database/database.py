# creating database connection in python
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
try:
 mycursor = mydb.cursor()
 mycursor.execute("CREATE DATABASE mydatabase")
 print("successfully created database")
except:
 print("failed to create database")