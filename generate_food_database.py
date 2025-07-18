import sqlite3

conn = sqlite3.connect('database/users.db')
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT,
    phone TEXT,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("New users.db with email and phone created.")
