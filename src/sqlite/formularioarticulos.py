import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos:
    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")

    def borrar_articulo(self):
        """Maneja la funcionalidad de borrado de artículos."""
        codigo = self.codigo_borrar.get()
        if not codigo:
            mb.showwarning("Advertencia", "Por favor, introduce el código del artículo a borrar.")
            return

        respuesta = self.articulo1.borrar(codigo)
        if respuesta:
            mb.showinfo("Éxito", f"Artículo con código {codigo} borrado correctamente.")
            self.limpiar_campos()
        else:
            mb.showerror("Error", "No se pudo borrar el artículo o no existe ese código.")

    def modificar_articulo(self):
        """Maneja la funcionalidad de modificación de artículos."""
        codigo = self.codigo_modificar.get()
        nueva_descripcion = self.entrydesc_mod.get()
        precio_str = self.preciomod.get()

        if not codigo or not nueva_descripcion or not precio_str:
            mb.showwarning("Advertencia", "Por favor, rellena todos los campos.")
            return

        try:
            nuevo_precio = float(precio_str)
        except ValueError:
            mb.showerror("Error de entrada", "El precio debe ser un número válido.")
            return

        respuesta = self.articulo1.actualizar(codigo, nueva_descripcion, nuevo_precio)
        if respuesta:
            mb.showinfo("Éxito", f"Artículo con código {codigo} modificado correctamente.")
            self.limpiar_campos()
        else:
            mb.showerror("Error", "No se pudo modificar el artículo o no existe ese código.")

    def limpiar_campos(self):
        # Limpia todos los campos de entrada principales del formulario
        self.codigo.set("")
        self.descripcion.set("")
        self.precio.set("")
        self.codigo_borrar.set("")
        self.entrydesc_mod.delete(0, tk.END)
        self.preciomod.delete(0, tk.END)


    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        # Pestañas existentes
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()

        # NUEVAS pestañas
        self.borrar_articulo()
        self.modificacion_articulo()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def borrar_articulo(self):
        """Crea la pestaña para borrar artículos."""
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar artículo")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Borrado de Artículo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.label_codborrar = ttk.Label(self.labelframe4, text="Código a borrar:")
        self.label_codborrar.grid(column=0, row=0, padx=4, pady=4)
        self.codigo_borrar = tk.StringVar()
        self.entrycodborrar = ttk.Entry(self.labelframe4, textvariable=self.codigo_borrar)
        self.entrycodborrar.grid(column=1, row=0, padx=4, pady=4)

        self.botonborrar=ttk.Button(self.labelframe4, text="Borrar Artículo", command=self.borrar_articulo)
        self.botonborrar.grid(column=1, row=1, padx=4, pady=4)


    def modificacion_articulo(self):
        """Crea la pestaña para modificar artículos."""
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Modificación de Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        # Campos para Código y Datos Nuevos
        self.label_codmod = ttk.Label(self.labelframe5, text="Código a modificar:")
        self.label_codmod.grid(column=0, row=0, padx=4, pady=4)
        self.codigo_modificar = tk.StringVar()
        self.entrycodmod = ttk.Entry(self.labelframe5, textvariable=self.codigo_modificar)
        self.entrycodmod.grid(column=1, row=0, padx=4, pady=4)

        self.labeldesc_mod = ttk.Label(self.labelframe5, text="Nueva Descripción:")
        self.labeldesc_mod.grid(column=0, row=1, padx=4, pady=4)
        # Fix: Changed the potentially conflicting assignment from previous versions to ensure correct behavior
        self.entrydesc_mod = ttk.Entry(self.labelframe5) 
        self.entrydesc_mod.grid(column=1, row=1, padx=4, pady=4)

        self.labelprecio_mod = ttk.Label(self.labelframe5, text="Nuevo Precio:")
        self.labelprecio_mod.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod = tk.StringVar()
        self.entrypreciomod = ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entrypreciomod.grid(column=1, row=2, padx=4, pady=4)

        self.botonmodificar=ttk.Button(self.labelframe5, text="Modificar Artículo", command=self.modificar_articulo)
        self.botonmodificar.grid(column=1, row=3, padx=4, pady=4)

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")


aplicacion1=FormularioArticulos()