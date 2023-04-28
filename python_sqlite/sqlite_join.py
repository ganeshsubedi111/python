# sqlite join in python
'''
inner join- return record that have matching values in both tables
LEFT(outer) Join- return all  record from  the left table and match  record from right tables
RIGHT(outer) Join- return all  record from  the right table and match  record from left tables
full(outer) Join- return all record when there is  match  in either left or right table
'''
import sqlite3
conn=sqlite3.connect("sqlite.db")
print("st_id","st_course","st_phone")
data=conn.execute("SELECT * FROM student_course  as c inner join student as s on c.st_id=s.st_id ")
for a in data:
    print(a)
conn.close()