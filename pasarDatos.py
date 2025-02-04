import pandas as pd
from sqlalchemy import create_engine

try:
    # Leer el archivo de Excel
    df = pd.read_excel("datos.xlsx")
    print("Archivo de Excel leído correctamente.")

    # Crear una conexión a la base de datos (por ejemplo, MySQL)
    engine = create_engine("mysql+pymysql://usuario:contraseña@localhost/nombre_base_de_datos")
    print("Conexión a la base de datos establecida correctamente.")

    # Cargar los datos en la base de datos
    df.to_sql("nombre_tabla", con=engine, if_exists="replace", index=False)
    print("Datos cargados correctamente en la base de datos.")

except FileNotFoundError:
    print("Error: El archivo de Excel no se encontró. Verifica la ruta del archivo.")

except pd.errors.EmptyDataError:
    print("Error: El archivo de Excel está vacío o no contiene datos válidos.")

except Exception as e:
    print(f"Error inesperado: {e}")

else:
    print("Proceso completado sin errores.")

finally:
    print("Finalizando el proceso de importación.")