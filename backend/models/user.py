from database import Database
from utils.security import hash_password, verify_password

class User:
    def __init__(self, id, username, email, password, role, full_name):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.full_name = full_name
    
    def verificar_password(self, password):
        return verify_password(password, self.password)