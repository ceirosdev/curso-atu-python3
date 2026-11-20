import sqlite3
import os

# Definir la ruta absoluta para que el archivo .db se cree dentro de src/sqlite
db_path = os.path.join(os.path.dirname(__file__), "bd1.db")
conexion = sqlite3.connect(db_path)

conexion.execute(
    "insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50)
)
conexion.execute(
    "insert into articulos(descripcion,precio) values (?,?)", ("peras", 34)
)
conexion.execute(
    "insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25)
)
conexion.commit()
conexion.close()
