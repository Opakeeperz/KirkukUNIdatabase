import sqlite3, os

conn = sqlite3.connect("StudentDatabase.db")
c = conn.cursor()

c.execute("""CREATE TABLE students (
    name TEXT,
    age INTEGER,
    class TEXT,
    grade INTEGER
    )""")

os.remove(__file__)