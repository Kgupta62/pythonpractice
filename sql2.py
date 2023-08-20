import sqlite3
conn=None
try:
    conn=sqlite3.connect("D:/python/database.db")
    print("connection done!")
    cur=conn.cursor()
    cur.execute("select * from database")
    for rec in cur:
        name,no,price=rec
        print(name,no,price,sep=",")
except sqlite3.DatabaseError:
    print("sorry! cannot connect to the DB")
finally:
    conn.close()
    print("Disconnected with the DB")
