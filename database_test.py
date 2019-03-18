import sqlite3
conn = sqlite3.connect("database.db")           //change names of db
cur = conn.cursor()
cur.execute("select * from statement;")         //change table name

results = cur.fetchall()
print(results)
