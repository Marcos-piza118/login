from database import Database
from utils.security import hash_password

class UserController:
    def get_all_users(self):
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT id, username, email, role, full_name FROM users")
                users = cursor.fetchall()
                return users
            except Exception as e:
                print(f"Error obteniendo usuarios: {e}")
                return []
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return []

    def change_user_role(self, user_id, new_role):
        if new_role not in ['admin', 'user']:
            print("❌ Rol debe ser 'admin' o 'user'")
            return False
            
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "UPDATE users SET role = %s WHERE id = %s",
                    (new_role, user_id)
                )
                connection.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error cambiando rol: {e}")
                return False
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return False

    def delete_user(self, user_id):
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
                connection.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error eliminando usuario: {e}")
                return False
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return False

    def update_user(self, user_id, new_email, new_name, new_password):
        db = Database()
        connection = db.get_connection()
        
        if connection:
            try:
                cursor = connection.cursor()
                
                updates = []
                values = []
                
                if new_email:
                    updates.append("email = %s")
                    values.append(new_email)
                
                if new_name:
                    updates.append("full_name = %s")
                    values.append(new_name)
                
                if new_password:
                    hashed_password = hash_password(new_password)
                    updates.append("password = %s")
                    values.append(hashed_password)
                
                if not updates:
                    print(" No hay cambios que realizar")
                    return False
                
                values.append(user_id)
                query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
                
                cursor.execute(query, values)
                connection.commit()
                
                return cursor.rowcount > 0
                
            except Exception as e:
                print(f"Error actualizando usuario: {e}")
                return False
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return False