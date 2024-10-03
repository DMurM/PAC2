import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

from app import crud

if __name__ == "__main__":
    print("Creando un nuevo usuario...")
    
    print("Introduzca el nombre del usuario:")
    name = input()
    print("Introduzca el email del usuario:")
    email = input() 
    crud.create_user(name, email)

    print("Usuario creado correctamente")
    print("Listando usuarios...")
    users = crud.get_users()
    for user in users:
        print(user)
