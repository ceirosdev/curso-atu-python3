import sqlite3
import os

# Definir la ruta absoluta para que el archivo .db se cree dentro de src/sqlite
db_path = os.path.join(os.path.dirname(__file__), "bd1.db")
conexion = sqlite3.connect(db_path)

try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()