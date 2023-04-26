#SQLite in python (insert query)
import sqlite3
conn=sqlite3.connect("sqlite.db")

insert='''
       insert into student_course(st_id,st_course,st_phone)values(2,"HM","98821025")
       
'''
conn.execute(insert)
conn.commit()
conn.close()