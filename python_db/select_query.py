#  SQLite select query in python
import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * from student")
print("st_id","   " ,"st_name","    ","st_email","             ","st_Address")
for n in data:
    print(n[0],"   " ,n[1],"   " ,n[2],"   " ,n[3])