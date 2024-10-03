import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

from app import crud

if __name__ == "__main__":
    
    def crear_usuario():
        print("Creando un nuevo usuario...")
        name = input("Introduzca el nombre del usuario: ")
        email = input("Introduce el email del usuario: ") 
        crud.create_user(name, email)
        print("Usuario creado con exito!")

    def mostrar_usuarios():
        print("Mostrando usuarios...")
        users = crud.get_users()
        for user in users:
            print(user)

    def modify_user():
        print("Modificando usuario...")
        name = input("Introduzca el nombre del usuario a modificar: ")
        email = input("Introduzca el email del usuario a modificar: ")
        crud.modif_user(name, email)
        print("Usuario modificado con exito!")

    def eliminar_usuario():

        print("Eliminando usuario...")
        name = input("Introduzca el nombre del usuario a eliminar: ")

        if name == "admin":
            print("No puedes eliminar el admin")
        else:
            user_exists = crud.elim_user(name) 
            if user_exists:
                print("Usuario eliminado con éxito!")
            else:
                print("Usuario no encontrado")


        

def main():
    
    print(" ")
    print("\nBienvenido a PAC2!")
    print("Que quieres hacer?")
    print("1. Crear un usuario")
    print("2. Modificar un usuario")
    print("3. Eliminar un usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Salir")
    print(" ")

    opcion = input("Opcion: ")
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        modify_user()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        mostrar_usuarios()
    elif opcion == "5":
        print("Adios!")
        exit()
    else:
        print("Opcion invalida")
    main()

main()
