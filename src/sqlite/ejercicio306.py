import sqlite3
import os

# Definir la ruta absoluta para que el archivo .db se cree dentro de src/sqlite
db_path = os.path.join(os.path.dirname(__file__), "bd1.db")
conexion = sqlite3.connect(db_path)

codigo = int(input("Ingrese el código de un artículo:"))
cursor = conexion.execute(
    "select descripcion,precio from articulos where codigo=?", (codigo,)
)
fila = cursor.fetchone()
if fila != None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()
