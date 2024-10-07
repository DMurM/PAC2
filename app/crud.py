from app.database import get_db_connection

def create_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    connection.commit()
    connection.close()

def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

def elim_user(name):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    connection.commit()
    connection.close()

def modif_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE name = ?", (email, name))
    connection.commit()
    connection.close()
