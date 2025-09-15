from database import Database
from models.user import User
from controllers.auth_controller import AuthController
from controllers.user_controller import UserController

def main():
    print(" ESTUDIONET - Sistema de Autenticación")
    print("=" * 40)
    
    auth = AuthController()
    user_controller = UserController()
    
    while True:
        print("\n MENU PRINCIPAL")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            registrar_usuario(auth)
        elif opcion == "2":
            usuario = login_usuario(auth)
            if usuario:
                if usuario.role == "admin":
                    menu_admin(usuario, user_controller)
                else:
                    menu_usuario(usuario, user_controller)
        elif opcion == "3":
            print(" ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida")

def registrar_usuario(auth):
    print("\n REGISTRO DE NUEVO USUARIO")
    print("-" * 30)
    
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    full_name = input("Nombre completo: ")
    
    if auth.register_user(username, email, password, full_name):
        print(" Usuario registrado exitosamente")
    else:
        print(" Error al registrar usuario")

def login_usuario(auth):
    print("\n INICIO DE SESIÓN")
    print("-" * 20)
    
    username = input("Username: ")
    password = input("Password: ")
    
    usuario = auth.login_user(username, password)
    if usuario:
        print(f" Bienvenido, {usuario.full_name} ({usuario.role})")
        return usuario
    else:
        print(" Credenciales incorrectas")
        return None

def menu_admin(usuario, user_controller):
    while True:
        print(f"\n PANEL ADMINISTRADOR - {usuario.username}")
        print("=" * 40)
        print("1. Listar todos los usuarios")
        print("2. Cambiar rol de usuario")
        print("3. Eliminar usuario")
        print("4. Ver mis datos")
        print("5. Cerrar sesión")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            listar_usuarios(user_controller)
        elif opcion == "2":
            cambiar_rol_usuario(user_controller)
        elif opcion == "3":
            eliminar_usuario(user_controller)
        elif opcion == "4":
            ver_mis_datos(usuario)
        elif opcion == "5":
            print(" Sesión cerrada")
            break
        else:
            print(" Opción no válida")

def menu_usuario(usuario, user_controller):
    while True:
        print(f"\n PANEL USUARIO - {usuario.username}")
        print("=" * 30)
        print("1. Ver mis datos")
        print("2. Editar mis datos")
        print("3. Cerrar sesión")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            ver_mis_datos(usuario)
        elif opcion == "2":
            editar_mis_datos(usuario, user_controller)
        elif opcion == "3":
            print(" Sesión cerrada")
            break
        else:
            print(" Opción no válida")

def listar_usuarios(user_controller):
    print("\n LISTA DE USUARIOS")
    print("-" * 20)
    usuarios = user_controller.get_all_users()
    
    if usuarios:
        for user in usuarios:
            print(f"ID: {user['id']} | User: {user['username']} | Email: {user['email']} | Rol: {user['role']} | Nombre: {user['full_name']}")
    else:
        print("No hay usuarios registrados")

def cambiar_rol_usuario(user_controller):
    print("\n CAMBIAR ROL DE USUARIO")
    user_id = input("ID del usuario: ")
    nuevo_rol = input("Nuevo rol (admin/user): ")
    
    if user_controller.change_user_role(user_id, nuevo_rol):
        print(" Rol cambiado exitosamente")
    else:
        print(" Error al cambiar rol")

def eliminar_usuario(user_controller):
    print("\n ELIMINAR USUARIO")
    user_id = input("ID del usuario a eliminar: ")
    
    if user_controller.delete_user(user_id):
        print(" Usuario eliminado exitosamente")
    else:
        print(" Error al eliminar usuario")

def ver_mis_datos(usuario):
    print("\n MIS DATOS")
    print("-" * 10)
    print(f"ID: {usuario.id}")
    print(f"Username: {usuario.username}")
    print(f"Email: {usuario.email}")
    print(f"Nombre: {usuario.full_name}")
    print(f"Rol: {usuario.role}")

def editar_mis_datos(usuario, user_controller):
    print("\n EDITAR MIS DATOS")
    print("Dejar en blanco para no cambiar")
    
    nuevo_email = input("Nuevo email: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nueva_password = input("Nueva password: ")
    
    if user_controller.update_user(usuario.id, nuevo_email, nuevo_nombre, nueva_password):
        print(" Datos actualizados exitosamente")
    else:
        print(" Error al actualizar datos")

if __name__ == "__main__":
    main()