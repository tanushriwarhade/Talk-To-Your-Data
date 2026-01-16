import sqlite3
from pathlib import Path

db_path = Path("data/chinook.db")

print("DB exists:", db_path.exists())

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables found:")
for t in tables:
    print(t[0])

conn.close()
