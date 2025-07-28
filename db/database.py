import sqlite3

def get_db_connection():
    conn = sqlite3.connect('company.db')
    return conn

def init_db():
    from db.models import create_tables
    conn = get_db_connection()
    create_tables(conn)
    conn.close()

