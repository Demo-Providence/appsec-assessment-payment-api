import sqlite3
conn = sqlite3.connect("payments.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS payments")
cursor.execute("""
CREATE TABLE users (
 id INTEGER PRIMARY KEY,
 username TEXT,
 password TEXT,
 role TEXT
)
""")
cursor.execute("""
CREATE TABLE payments (
 id INTEGER PRIMARY KEY,
 username TEXT,
 amount INTEGER,
 status TEXT
)
""")
'processed')")
cursor.execute("INSERT INTO payments VALUES (2, 'bob', 7500, 'pending')")
cursor.execute("INSERT INTO payments VALUES (3, 'admin', 99999, 
'approved')")
conn.commit()
conn.close()
print("Database initialized successfully"