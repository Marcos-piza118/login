import mysql.connector
from mysql.connector import Error

class Database:
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='estudionet_db',
                user='root',
                password=''
            )
            return connection
        except Error as e:
            print(f"Error conectando a MySQL: {e}")
            return None