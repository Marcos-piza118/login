from database import Database
from models.user import User
from utils.security import hash_password

class AuthController:
    def register_user(self, username, email, password, full_name):
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor()
                
                # Verificar si el usuario ya existe
                cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
                if cursor.fetchone():
                    print(" El usuario o email ya existe")
                    return False
                
                # Hash de la contraseña
                hashed_password = hash_password(password)
                
                # Insertar nuevo usuario
                cursor.execute(
                    "INSERT INTO users (username, email, password, full_name) VALUES (%s, %s, %s, %s)",
                    (username, email, hashed_password, full_name)
                )
                
                connection.commit()
                return True
                
            except Exception as e:
                print(f"Error en registro: {e}")
                return False
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return False

    def login_user(self, username, password):
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                
                cursor.execute(
                    "SELECT * FROM users WHERE username = %s",
                    (username,)
                )
                
                user_data = cursor.fetchone()
                
                if user_data:
                    user = User(
                        user_data['id'],
                        user_data['username'],
                        user_data['email'],
                        user_data['password'],
                        user_data['role'],
                        user_data['full_name']
                    )
                    
                    if user.verificar_password(password):
                        return user
                
                return None
                
            except Exception as e:
                print(f"Error en login: {e}")
                return None
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return None