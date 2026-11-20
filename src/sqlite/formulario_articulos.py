import tkinter as tk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import ttk

import articulos


class FormularioArticulos:
    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.articulo1.crear_tabla()

        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.ventana1.resizable(False, False)

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.crear_pestana_borrado()
        self.modificacion_articulo()

        self.ventana1.mainloop()

    def carga_articulos(self):
        pagina = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(pagina, text="Carga de artículos")
        marco = ttk.LabelFrame(pagina, text="Artículo")
        marco.grid(column=0, row=0, padx=8, pady=10)

        ttk.Label(marco, text="Descripción:").grid(
            column=0, row=0, padx=4, pady=4, sticky="e"
        )
        self.descripcioncarga = tk.StringVar()
        ttk.Entry(marco, textvariable=self.descripcioncarga, width=28).grid(
            column=1, row=0, padx=4, pady=4
        )

        ttk.Label(marco, text="Precio:").grid(
            column=0, row=1, padx=4, pady=4, sticky="e"
        )
        self.preciocarga = tk.StringVar()
        ttk.Entry(marco, textvariable=self.preciocarga, width=28).grid(
            column=1, row=1, padx=4, pady=4
        )

        ttk.Button(marco, text="Confirmar", command=self.agregar).grid(
            column=1, row=2, padx=4, pady=8, sticky="e"
        )

    def agregar(self):
        descripcion = self.descripcioncarga.get().strip()
        precio_texto = self.preciocarga.get().strip().replace(",", ".")

        if not descripcion or not precio_texto:
            mb.showwarning("Datos incompletos", "Introduce la descripción y el precio.")
            return

        try:
            precio = float(precio_texto)
            if precio < 0:
                raise ValueError
        except ValueError:
            mb.showerror("Precio no válido", "El precio debe ser un número igual o mayor que cero.")
            return

        try:
            self.articulo1.alta((descripcion, precio))
        except Exception as error:
            mb.showerror("Error", f"No se pudo guardar el artículo.\n{error}")
            return

        mb.showinfo("Información", "El artículo fue guardado correctamente.")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        pagina = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(pagina, text="Consulta por código")
        marco = ttk.LabelFrame(pagina, text="Artículo")
        marco.grid(column=0, row=0, padx=8, pady=10)

        ttk.Label(marco, text="Código:").grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        ttk.Entry(marco, textvariable=self.codigo, width=28).grid(
            column=1, row=0, padx=4, pady=4
        )

        ttk.Label(marco, text="Descripción:").grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        ttk.Entry(marco, textvariable=self.descripcion, state="readonly", width=28).grid(
            column=1, row=1, padx=4, pady=4
        )

        ttk.Label(marco, text="Precio:").grid(column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        ttk.Entry(marco, textvariable=self.precio, state="readonly", width=28).grid(
            column=1, row=2, padx=4, pady=4
        )

        ttk.Button(marco, text="Consultar", command=self.consultar).grid(
            column=1, row=3, padx=4, pady=8, sticky="e"
        )

    def consultar(self):
        codigo = self.codigo.get().strip()
        if not codigo:
            mb.showwarning("Dato incompleto", "Introduce el código del artículo.")
            return

        respuesta = self.articulo1.consulta((codigo,))
        if respuesta:
            self.descripcion.set(respuesta[0]["descripcion"])
            self.precio.set(str(respuesta[0]["precio"]))
        else:
            self.descripcion.set("")
            self.precio.set("")
            mb.showinfo("Información", "No existe un artículo con ese código.")

    def listado_completo(self):
        pagina = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(pagina, text="Listado completo")
        marco = ttk.LabelFrame(pagina, text="Artículos")
        marco.grid(column=0, row=0, padx=8, pady=10)

        ttk.Button(marco, text="Actualizar listado", command=self.listar).grid(
            column=0, row=0, padx=4, pady=4, sticky="w"
        )
        self.scrolledtext1 = st.ScrolledText(marco, width=42, height=12, state="disabled")
        self.scrolledtext1.grid(column=0, row=1, padx=8, pady=8)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()
        self.scrolledtext1.configure(state="normal")
        self.scrolledtext1.delete("1.0", tk.END)

        if not respuesta:
            self.scrolledtext1.insert(tk.END, "No hay artículos registrados.")
        else:
            for fila in respuesta:
                self.scrolledtext1.insert(
                    tk.END,
                    f"Código: {fila['codigo']}\n"
                    f"Descripción: {fila['descripcion']}\n"
                    f"Precio: {fila['precio']:.2f}\n\n",
                )

        self.scrolledtext1.configure(state="disabled")

    def crear_pestana_borrado(self):
        """Construye la pestaña para eliminar artículos."""
        pagina = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(pagina, text="Borrar artículo")
        marco = ttk.LabelFrame(pagina, text="Borrado de artículo")
        marco.grid(column=0, row=0, padx=8, pady=10)

        ttk.Label(marco, text="Código a borrar:").grid(
            column=0, row=0, padx=4, pady=4
        )
        self.codigo_borrar = tk.StringVar()
        ttk.Entry(marco, textvariable=self.codigo_borrar, width=28).grid(
            column=1, row=0, padx=4, pady=4
        )
        ttk.Button(marco, text="Borrar artículo", command=self.borrar_articulo).grid(
            column=1, row=1, padx=4, pady=8, sticky="e"
        )

    def borrar_articulo(self):
        codigo = self.codigo_borrar.get().strip()
        if not codigo:
            mb.showwarning("Dato incompleto", "Introduce el código del artículo que deseas borrar.")
            return

        if not mb.askyesno("Confirmar borrado", f"¿Seguro que deseas borrar el artículo {codigo}?"):
            return

        try:
            eliminado = self.articulo1.borrar(codigo)
        except Exception as error:
            mb.showerror("Error", f"No se pudo borrar el artículo.\n{error}")
            return

        if eliminado:
            mb.showinfo("Éxito", f"El artículo {codigo} fue borrado.")
            self.codigo_borrar.set("")
            self.limpiar_consulta()
        else:
            mb.showerror("No encontrado", "No existe un artículo con ese código.")

    def modificacion_articulo(self):
        """Construye la pestaña para modificar artículos."""
        pagina = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(pagina, text="Modificar artículo")
        marco = ttk.LabelFrame(pagina, text="Modificación de artículo")
        marco.grid(column=0, row=0, padx=8, pady=10)

        ttk.Label(marco, text="Código a modificar:").grid(
            column=0, row=0, padx=4, pady=4
        )
        self.codigo_modificar = tk.StringVar()
        ttk.Entry(marco, textvariable=self.codigo_modificar, width=28).grid(
            column=1, row=0, padx=4, pady=4
        )

        ttk.Label(marco, text="Nueva descripción:").grid(
            column=0, row=1, padx=4, pady=4
        )
        self.entrydesc_mod = ttk.Entry(marco, width=28)
        self.entrydesc_mod.grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(marco, text="Nuevo precio:").grid(
            column=0, row=2, padx=4, pady=4
        )
        self.preciomod = tk.StringVar()
        ttk.Entry(marco, textvariable=self.preciomod, width=28).grid(
            column=1, row=2, padx=4, pady=4
        )

        ttk.Button(marco, text="Modificar artículo", command=self.modificar_articulo).grid(
            column=1, row=3, padx=4, pady=8, sticky="e"
        )

    def modificar_articulo(self):
        codigo = self.codigo_modificar.get().strip()
        descripcion = self.entrydesc_mod.get().strip()
        precio_texto = self.preciomod.get().strip().replace(",", ".")

        if not codigo or not descripcion or not precio_texto:
            mb.showwarning("Datos incompletos", "Rellena los tres campos.")
            return

        try:
            precio = float(precio_texto)
            if precio < 0:
                raise ValueError
        except ValueError:
            mb.showerror("Precio no válido", "El precio debe ser un número igual o mayor que cero.")
            return

        try:
            actualizado = self.articulo1.actualizar(codigo, descripcion, precio)
        except Exception as error:
            mb.showerror("Error", f"No se pudo modificar el artículo.\n{error}")
            return

        if actualizado:
            mb.showinfo("Éxito", f"El artículo {codigo} fue modificado.")
            self.codigo_modificar.set("")
            self.entrydesc_mod.delete(0, tk.END)
            self.preciomod.set("")
            self.limpiar_consulta()
        else:
            mb.showerror("No encontrado", "No existe un artículo con ese código.")

    def limpiar_consulta(self):
        self.codigo.set("")
        self.descripcion.set("")
        self.precio.set("")


if __name__ == "__main__":
    FormularioArticulos()
