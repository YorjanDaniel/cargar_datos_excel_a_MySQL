# Conexion.py
import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(
                user="root",          # Usuario de MySQL
                password="yorjan2425", # Contraseña de MySQL
                host="127.0.0.1",     # Host de la base de datos
                database="clientes",  # Nombre de la base de datos (asegúrate de que sea el correcto)
                port="3306"           # Puerto de MySQL
            )
            print("Conexión exitosa")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarse a la base de datos: {error}")
            return None