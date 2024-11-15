import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='banho_e_cia'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
