import sqlite3
import os

# Definir la ruta absoluta para que el archivo .db se cree dentro de src/sqlite
# db_path = os.path.join(os.path.dirname(__file__), "bd1.db")
db_path = "bd1.db"
conexion = sqlite3.connect(db_path)

precio = float(input("Ingrese un precio:"))
cursor = conexion.execute(
    "select descripcion from articulos where precio<?", (precio,)  #
)
filas = cursor.fetchall()
if len(filas) > 0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()
