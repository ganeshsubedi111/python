#  create table
import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute(
    '''
    Create table student_course(
    st_id INT AUTO_INCREMENT PRIMARY KEY,
    st_course VARCHAR(50),
    st_phone INT
    
    ) 
    '''
)
conn.close()