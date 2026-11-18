
import tkinter as tk
from tkinter import ttk, messagebox

from retos.poo.cajero import Cajero
from retos.poo.clientes_con_fondos import clientes_con_fondos


class AplicacionCajero:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cajero automático")
        self.ventana.geometry("550x590")
        self.ventana.resizable(False, False)

        # Crear el cajero y cargar los clientes
        self.cajero = Cajero()
        self.cajero.clientes = clientes_con_fondos()

        self.crear_interfaz()
        self.actualizar_clientes()

    def crear_interfaz(self):

        # Título
        titulo = ttk.Label(
            self.ventana,
            text="CAJERO AUTOMÁTICO",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        # Contenedor de los campos
        frame_datos = ttk.LabelFrame(
            self.ventana,
            text="Datos de la operación",
            padding=15
        )
        frame_datos.pack(fill="x", padx=20, pady=10)

        # Nombre del cliente
        ttk.Label(
            frame_datos,
            text="Nombre del cliente:"
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.entrada_nombre = ttk.Entry(frame_datos, width=30)
        self.entrada_nombre.grid(row=0, column=1, pady=5)

        # Importe
        ttk.Label(
            frame_datos,
            text="Importe (€):"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entrada_monto = ttk.Entry(frame_datos, width=30)
        self.entrada_monto.grid(row=1, column=1, pady=5)

        # Botones de operaciones
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.pack(pady=15)

        ttk.Button(
            frame_botones,
            text="Depositar",
            command=self.depositar
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            frame_botones,
            text="Extraer",
            command=self.extraer
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            frame_botones,
            text="Consultar saldo",
            command=self.consultar_saldo
        ).grid(row=0, column=2, padx=5)

        # Lista de clientes
        frame_clientes = ttk.LabelFrame(
            self.ventana,
            text="Clientes y saldos",
            padding=10
        )
        frame_clientes.pack(fill="both", expand=True, padx=20, pady=10)

        self.lista_clientes = ttk.Treeview(
            frame_clientes,
            columns=("nombre", "saldo"),
            show="headings",
            height=8
        )

        self.lista_clientes.heading("nombre", text="Cliente")
        self.lista_clientes.heading("saldo", text="Saldo (€)")

        self.lista_clientes.column("nombre", width=250)
        self.lista_clientes.column("saldo", width=200, anchor="center")

        self.lista_clientes.pack(fill="both", expand=True)

        # Botón para limpiar los campos
        ttk.Button(
            self.ventana,
            text="Limpiar campos",
            command=self.limpiar_campos
        ).pack(pady=5)

    def buscar_cliente(self, nombre):

        encontrado, indice = self.cajero.cliente_e_indice(nombre)

        if not encontrado:
            messagebox.showerror(
                "Cliente no encontrado",
                "No existe un cliente con ese nombre."
            )
            return None

        return self.cajero.clientes[indice]

    def obtener_monto(self):

        try:
            monto = float(self.entrada_monto.get())

            if monto <= 0:
                messagebox.showerror(
                    "Importe incorrecto",
                    "El importe debe ser mayor que cero."
                )
                return None

            return monto

        except ValueError:
            messagebox.showerror(
                "Importe incorrecto",
                "Introduce un importe numérico válido."
            )
            return None

    def depositar(self):

        nombre = self.entrada_nombre.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Campo obligatorio",
                "Introduce el nombre del cliente."
            )
            return

        cliente = self.buscar_cliente(nombre)

        if cliente is None:
            return

        monto = self.obtener_monto()

        if monto is None:
            return

        self.cajero.depositar(monto, nombre)

        self.actualizar_clientes()

        messagebox.showinfo(
            "Depósito realizado",
            f"Se han depositado {monto:.2f} € a {nombre}."
        )

    def extraer(self):

        nombre = self.entrada_nombre.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Campo obligatorio",
                "Introduce el nombre del cliente."
            )
            return

        cliente = self.buscar_cliente(nombre)

        if cliente is None:
            return

        monto = self.obtener_monto()

        if monto is None:
            return

        if monto > cliente.monto:
            messagebox.showerror(
                "Saldo insuficiente",
                "El cliente no dispone de saldo suficiente."
            )
            return

        self.cajero.extraer(monto, nombre)

        self.actualizar_clientes()

        messagebox.showinfo(
            "Extracción realizada",
            f"Se han extraído {monto:.2f} € de la cuenta de {nombre}."
        )

    def consultar_saldo(self):

        nombre = self.entrada_nombre.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Campo obligatorio",
                "Introduce el nombre del cliente."
            )
            return

        cliente = self.buscar_cliente(nombre)

        if cliente is None:
            return

        messagebox.showinfo(
            "Consulta de saldo",
            f"Cliente: {cliente.nombre}\n"
            f"Saldo disponible: {cliente.monto:.2f} €"
        )

    def actualizar_clientes(self):

        # Eliminar los datos anteriores de la tabla
        for elemento in self.lista_clientes.get_children():
            self.lista_clientes.delete(elemento)

        # Cargar los datos actualizados
        for cliente in self.cajero.clientes:
            self.lista_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.nombre,
                    f"{cliente.monto:.2f} €"
                )
            )

    def limpiar_campos(self):

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_monto.delete(0, tk.END)


# Ejecutar la aplicación
if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = AplicacionCajero(ventana)

    ventana.mainloop()
