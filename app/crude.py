from app.databse import database_connect

def create_user(name, password):
    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
    connection.commit()
    connection.close()

def get_users():
    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

