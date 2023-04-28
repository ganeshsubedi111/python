#SQLite search query in python
import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * from student")
print("st_id","   " ,"st_name","    ","st_email","             ","st_Address")
for n in data:
    print(n[0],"   " ,n[1],"   " ,n[2],"   " ,n[3])
print("\n")
print("-------after search query--------")

data=conn.execute("SELECT * FROM student where st_name='jagat'")
print("st_id","   " ,"st_name","    ","st_email","             ","st_Address")
for n in data:
    print(n[0],"   " ,n[1],"   " ,n[2],"   " ,n[3])

# print we can also search by user input
print("\n")
print("please enter below the student name that you want to show\n")
st_name=input("enter a student name:")
data=conn.execute("SELECT * FROM student where st_name='"+st_name+"'")
print("st_id","   " ,"st_name","    ","st_email","             ","st_Address")
for n in data:
    print(n[0],"   " ,n[1],"   " ,n[2],"   " ,n[3])
