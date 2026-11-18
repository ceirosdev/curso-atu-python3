
import tkinter as tk
from tkinter import ttk, messagebox

from ahorcado_para_ui import Ahorcado


class InterfazAhorcado:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Juego del Ahorcado")
        self.ventana.geometry("650x720")
        self.ventana.resizable(False, False)

        # Crear una instancia del juego
        self.juego = Ahorcado(8)

        # Alfabeto español
        self.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        # Crear la interfaz
        self.crear_interfaz()

        # Actualizar los elementos
        self.actualizar_interfaz()

    def crear_interfaz(self):

        # Título
        ttk.Label(
            self.ventana,
            text="JUEGO DEL AHORCADO",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        # Contenedor principal
        frame_principal = ttk.Frame(self.ventana)
        frame_principal.pack(fill="both", expand=True, padx=20)

        # Canvas para dibujar el ahorcado
        self.canvas = tk.Canvas(
            frame_principal,
            width=250,
            height=230,
            bg="white",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.canvas.pack(pady=10)

        # Palabra por adivinar
        self.lbl_palabra = ttk.Label(
            frame_principal,
            text="",
            font=("Arial", 25, "bold")
        )
        self.lbl_palabra.pack(pady=15)

        # Intentos restantes
        self.lbl_intentos = ttk.Label(
            frame_principal,
            text="Intentos restantes: 8",
            font=("Arial", 12)
        )
        self.lbl_intentos.pack(pady=5)

        # Mensajes del juego
        self.lbl_mensaje = ttk.Label(
            frame_principal,
            text="¡Adivina la palabra!",
            font=("Arial", 12)
        )
        self.lbl_mensaje.pack(pady=10)

        # Teclado de letras
        frame_teclado = ttk.LabelFrame(
            frame_principal,
            text="Selecciona una letra",
            padding=10
        )
        frame_teclado.pack(pady=10)

        self.botones_letras = {}

        columnas = 9

        for indice, letra in enumerate(self.alfabeto):

            fila = indice // columnas
            columna = indice % columnas

            boton = ttk.Button(
                frame_teclado,
                text=letra,
                width=4,
                command=lambda l=letra: self.procesar_letra(l)
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=3,
                pady=3
            )

            self.botones_letras[letra] = boton

        # Botón de nueva partida
        ttk.Button(
            frame_principal,
            text="Nueva partida",
            command=self.nueva_partida
        ).pack(pady=15)

    # Procesar la letra seleccionada
    def procesar_letra(self, letra):

        resultado = self.juego.adivinar_letra(letra)

        estado = resultado["estado"]

        # Actualizar los elementos de la interfaz
        self.actualizar_interfaz()

        if estado in ("acierto", "error"):
            self.lbl_mensaje.config(
                text=resultado["mensaje"]
            )

        elif estado == "repetida":
            self.lbl_mensaje.config(
                text=resultado["mensaje"]
            )

        elif estado == "ganada":

            self.lbl_mensaje.config(
                text=resultado["mensaje"]
            )

            messagebox.showinfo(
                "¡Victoria!",
                f"¡Felicidades! Has adivinado la palabra:\n"
                f"{self.juego.palabra}"
            )

            self.deshabilitar_letras()

        elif estado == "perdida":

            self.lbl_mensaje.config(
                text=resultado["mensaje"]
            )

            # Mostrar la palabra correcta
            self.lbl_palabra.config(
                text=" ".join(self.juego.palabra.upper())
            )

            messagebox.showinfo(
                "Fin del juego",
                f"Te has quedado sin intentos.\n"
                f"La palabra era: {self.juego.palabra.upper()}"
            )

            self.deshabilitar_letras()

    # Actualizar los elementos visuales
    def actualizar_interfaz(self):

        # Actualizar la palabra
        self.lbl_palabra.config(
            text=" ".join(self.juego.obtener_progreso().upper())
        )

        # Actualizar los intentos
        self.lbl_intentos.config(
            text=f"Intentos restantes: "
                 f"{self.juego.intentos_restantes}"
        )

        # Dibujar el ahorcado
        self.dibujar_ahorcado()

        # Deshabilitar las letras utilizadas
        for letra in self.juego.obtener_letras_introducidas():

            self.botones_letras[letra.upper()].config(
                state="disabled"
            )

    # Dibujar progresivamente el ahorcado
    def dibujar_ahorcado(self):

        self.canvas.delete("all")

        errores = (
            self.juego.intentos_maximos
            - self.juego.intentos_restantes
        )

        # 1. Base
        if errores >= 1:
            self.canvas.create_line(
                20, 210, 150, 210,
                width=3
            )

        # 2. Poste vertical
        if errores >= 2:
            self.canvas.create_line(
                60, 210, 60, 20,
                width=3
            )

        # 3. Poste horizontal
        if errores >= 3:
            self.canvas.create_line(
                60, 20, 160, 20,
                width=3
            )

        # 4. Cuerda
        if errores >= 4:
            self.canvas.create_line(
                160, 20, 160, 50,
                width=3
            )

        # 5. Cabeza
        if errores >= 5:
            self.canvas.create_oval(
                140, 50, 180, 90,
                width=2
            )

        # 6. Cuerpo
        if errores >= 6:
            self.canvas.create_line(
                160, 90, 160, 150,
                width=2
            )

        # 7. Brazos
        if errores >= 7:
            self.canvas.create_line(
                160, 105, 130, 130,
                width=2
            )

            self.canvas.create_line(
                160, 105, 190, 130,
                width=2
            )

        # 8. Piernas
        if errores >= 8:
            self.canvas.create_line(
                160, 150, 130, 185,
                width=2
            )

            self.canvas.create_line(
                160, 150, 190, 185,
                width=2
            )

    # Deshabilitar todas las letras
    def deshabilitar_letras(self):

        for boton in self.botones_letras.values():
            boton.config(state="disabled")

    # Iniciar una nueva partida
    def nueva_partida(self):

        self.juego.reiniciar_partida()

        # Habilitar nuevamente todas las letras
        for boton in self.botones_letras.values():
            boton.config(state="normal")

        self.lbl_mensaje.config(
            text="¡Adivina la palabra!"
        )

        self.actualizar_interfaz()


# Ejecutar la aplicación
if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazAhorcado(ventana)

    ventana.mainloop()
