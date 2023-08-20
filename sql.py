import sqlite3
conn=None
try:
    conn=sqlite3.connect("D:/python/database.db")
    print("connection done!")

except sqlite3.DatabaseError:
    print("sorry! cannot connect to the DB")
finally:
    conn.close()
    print("Disconnected with the DB")
