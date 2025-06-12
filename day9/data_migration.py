import sqlite3
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# --- Connect to SQLite (inside instance/) ---
sqlite_conn = sqlite3.connect('instance/SampleDb.db') 
sqlite_cursor = sqlite_conn.cursor()

# --- Connect to PostgreSQL ---
pg_uri = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
pg_conn = psycopg2.connect(pg_uri)
pg_cursor = pg_conn.cursor()

# --- Read data from SQLite ---
sqlite_cursor.execute("SELECT id, name FROM user")
rows = sqlite_cursor.fetchall()

# --- Insert into PostgreSQL ---
for row in rows:
    pg_cursor.execute("INSERT INTO user (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING", row)

pg_conn.commit()

# --- Close connections ---
sqlite_conn.close()
pg_conn.close()

print("✅ Migration Complete!")
