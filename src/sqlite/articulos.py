import sqlite3
from pathlib import Path


class Articulos:
    """Acceso a datos de la tabla articulos."""

    def abrir(self):
        # La base de datos queda junto a este archivo, no según el directorio
        # desde el que se ejecute la aplicación.
        db_path = Path(__file__).resolve().with_name("bd1.db")
        conexion = sqlite3.connect(db_path)
        conexion.row_factory = sqlite3.Row
        return conexion

    def crear_tabla(self):
        """Crea la tabla si todavía no existe."""
        with self.abrir() as conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS articulos (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    descripcion TEXT NOT NULL,
                    precio REAL NOT NULL CHECK (precio >= 0)
                )
                """
            )

    def alta(self, datos):
        """Inserta un artículo. datos debe contener (descripcion, precio)."""
        descripcion, precio = datos
        with self.abrir() as conexion:
            cursor = conexion.execute(
                "INSERT INTO articulos (descripcion, precio) VALUES (?, ?)",
                (descripcion, float(precio)),
            )
            return cursor.lastrowid

    def consulta(self, datos):
        """Devuelve (descripcion, precio) del código indicado, o una lista vacía."""
        codigo = datos[0] if isinstance(datos, (tuple, list)) else datos
        with self.abrir() as conexion:
            cursor = conexion.execute(
                "SELECT descripcion, precio FROM articulos WHERE codigo = ?",
                (codigo,),
            )
            return cursor.fetchall()

    def recuperar_todos(self):
        """Devuelve todos los artículos como tuplas (codigo, descripcion, precio)."""
        with self.abrir() as conexion:
            cursor = conexion.execute(
                "SELECT codigo, descripcion, precio FROM articulos ORDER BY codigo"
            )
            return cursor.fetchall()

    def borrar(self, codigo: str) -> bool:
        """Elimina un artículo por su código."""
        with self.abrir() as conexion:
            cursor = conexion.execute(
                "DELETE FROM articulos WHERE codigo = ?",
                (codigo,),
            )
            return cursor.rowcount > 0

    def actualizar(
        self, codigo: str, nueva_descripcion: str, nuevo_precio: float
    ) -> bool:
        """Actualiza la descripción y el precio de un artículo."""
        with self.abrir() as conexion:
            cursor = conexion.execute(
                """
                UPDATE articulos
                SET descripcion = ?, precio = ?
                WHERE codigo = ?
                """,
                (nueva_descripcion, float(nuevo_precio), codigo),
            )
            return cursor.rowcount > 0
