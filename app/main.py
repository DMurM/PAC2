import os
from app import crude

if __name__ == '__main__':
    print("Crea un usuari")
    name = input("Nombre: ")
    password = input("Contrasenya: ")
    crude.create_user(name, password)
    print("Usuari creat")

