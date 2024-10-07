import sqlite3
from config import DATABASE_PATH

def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
