# Clientes.py
import mysql.connector
from Conexion import CConexion

class CClientes:
    @staticmethod
    def mostrarClientes():
        conexion = CConexion.ConexionBaseDatos()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")  # Cambiado a 'usuarios'
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as error:
                print(f"Error al mostrar usuarios: {error}")
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()
        return []

    @staticmethod
    def ingresarClientes(cc, nombres, apellidos, sexo):
        conexion = CConexion.ConexionBaseDatos()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "INSERT INTO usuarios (cc, nombres, apellidos, sexo) VALUES (%s, %s, %s, %s)"  # Cambiado a 'usuarios'
                valores = (cc, nombres, apellidos, sexo)
                cursor.execute(sql, valores)
                conexion.commit()
                print("Usuario ingresado correctamente")
            except mysql.connector.Error as error:
                print(f"Error al ingresar usuario: {error}")
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()

    @staticmethod
    def actualizarClientes(cc, nombres, apellidos, sexo):
        conexion = CConexion.ConexionBaseDatos()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "UPDATE usuarios SET nombres = %s, apellidos = %s, sexo = %s WHERE cc = %s"  # Cambiado a 'usuarios'
                valores = (nombres, apellidos, sexo, cc)
                cursor.execute(sql, valores)
                conexion.commit()
                print("Usuario actualizado correctamente")
            except mysql.connector.Error as error:
                print(f"Error al actualizar usuario: {error}")
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()

    @staticmethod
    def eliminarClientes(cc):
        conexion = CConexion.ConexionBaseDatos()
        if conexion:
            try:
                cursor = conexion.cursor()
                sql = "DELETE FROM usuarios WHERE cc = %s"  # Cambiado a 'usuarios'
                valores = (cc,)
                cursor.execute(sql, valores)
                conexion.commit()
                print("Usuario eliminado correctamente")
            except mysql.connector.Error as error:
                print(f"Error al eliminar usuario: {error}")
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()