#SQLite in python (insert query)
import sqlite3
conn=sqlite3.connect("sqlite.db")

insert='''
       insert into student(st_name,st_email,st_Address)values("aasim","ghimire@gmail.com","mygadi")
       
'''
conn.execute(insert)
conn.commit()
conn.close()