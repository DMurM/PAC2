from app.databse import get_db_connection

def create_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
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
    cursor.execute("DELETE FROM users WHERE name = %s", (name))
    connection.commit()
    connection.close()
    return

def modif_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET email = %s WHERE name = %s", (email, name))
    connection.commit()
    connection.close()
    return


