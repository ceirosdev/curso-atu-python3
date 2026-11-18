
import tkinter as tk
from tkinter import ttk

from dados import JuegoDados


class InterfazDados:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Juego de los Dados")
        self.ventana.geometry("650x590")
        self.ventana.resizable(False, False)

        # Crear una instancia del juego
        self.juego = JuegoDados()

        # Marcador general
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):

        # Título
        ttk.Label(
            self.ventana,
            text="JUEGO DE LOS DADOS",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        # Contenedor de los jugadores
        frame_jugadores = ttk.Frame(self.ventana)
        frame_jugadores.pack(pady=15)

        # Panel del jugador
        self.crear_panel_jugador(
            frame_jugadores,
            "JUGADOR",
            0
        )

        # Panel de la máquina
        self.crear_panel_jugador(
            frame_jugadores,
            "MÁQUINA",
            1
        )

        # Resultado de la partida
        self.lbl_resultado = ttk.Label(
            self.ventana,
            text="Pulsa el botón para lanzar los dados",
            font=("Arial", 13, "bold")
        )
        self.lbl_resultado.pack(pady=20)

        # Botón para lanzar los dados
        self.btn_lanzar = ttk.Button(
            self.ventana,
            text="Lanzar dados",
            command=self.lanzar_dados
        )
        self.btn_lanzar.pack(pady=10)

        # Marcador
        frame_marcador = ttk.LabelFrame(
            self.ventana,
            text="Marcador general",
            padding=15
        )
        frame_marcador.pack(fill="x", padx=30, pady=20)

        self.lbl_victorias = ttk.Label(
            frame_marcador,
            text="Victorias: 0",
            font=("Arial", 11)
        )
        self.lbl_victorias.grid(row=0, column=0, padx=25)

        self.lbl_derrotas = ttk.Label(
            frame_marcador,
            text="Derrotas: 0",
            font=("Arial", 11)
        )
        self.lbl_derrotas.grid(row=0, column=1, padx=25)

        self.lbl_empates = ttk.Label(
            frame_marcador,
            text="Empates: 0",
            font=("Arial", 11)
        )
        self.lbl_empates.grid(row=0, column=2, padx=25)

        # Botón para reiniciar el marcador
        ttk.Button(
            self.ventana,
            text="Reiniciar marcador",
            command=self.reiniciar_marcador
        ).pack(pady=5)

    # Crear el panel visual de cada participante
    def crear_panel_jugador(self, contenedor, nombre, columna):

        frame = ttk.LabelFrame(
            contenedor,
            text=nombre,
            padding=20
        )

        frame.grid(
            row=0,
            column=columna,
            padx=15
        )

        # Etiquetas de los dados
        lbl_dado1 = ttk.Label(
            frame,
            text="⚀",
            font=("Arial", 65)
        )
        lbl_dado1.grid(row=0, column=0, padx=5)

        lbl_dado2 = ttk.Label(
            frame,
            text="⚀",
            font=("Arial", 65)
        )
        lbl_dado2.grid(row=0, column=1, padx=5)

        # Etiqueta de puntuación
        lbl_puntos = ttk.Label(
            frame,
            text="Puntos: 0",
            font=("Arial", 14, "bold")
        )
        lbl_puntos.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=15
        )

        # Guardar las referencias de las etiquetas
        if columna == 0:
            self.dados_jugador = (lbl_dado1, lbl_dado2)
            self.lbl_puntos_jugador = lbl_puntos

        else:
            self.dados_maquina = (lbl_dado1, lbl_dado2)
            self.lbl_puntos_maquina = lbl_puntos

    # Lanzar los dados
    def lanzar_dados(self):

        resultado = self.juego.jugar_ronda()

        # Actualizar dados del jugador
        for etiqueta, valor in zip(
            self.dados_jugador,
            resultado["dados_jugador"]
        ):
            etiqueta.config(text=self.obtener_simbolo(valor))

        # Actualizar dados de la máquina
        for etiqueta, valor in zip(
            self.dados_maquina,
            resultado["dados_maquina"]
        ):
            etiqueta.config(text=self.obtener_simbolo(valor))

        # Actualizar puntuaciones
        self.lbl_puntos_jugador.config(
            text=f"Puntos: {resultado['puntos_jugador']}"
        )

        self.lbl_puntos_maquina.config(
            text=f"Puntos: {resultado['puntos_maquina']}"
        )

        # Determinar el ganador
        estado = resultado["resultado"]

        if estado == "ganador":
            self.victorias += 1
            mensaje = "¡Felicidades! Has ganado."

        elif estado == "perdedor":
            self.derrotas += 1
            mensaje = "La máquina ha ganado."

        else:
            self.empates += 1
            mensaje = "¡La partida ha terminado en empate!"

        self.lbl_resultado.config(text=mensaje)

        # Actualizar el marcador
        self.actualizar_marcador()

    # Obtener el símbolo correspondiente al dado
    def obtener_simbolo(self, valor):

        simbolos = {
            1: "⚀",
            2: "⚁",
            3: "⚂",
            4: "⚃",
            5: "⚄",
            6: "⚅"
        }

        return simbolos[valor]

    # Actualizar el marcador
    def actualizar_marcador(self):

        self.lbl_victorias.config(
            text=f"Victorias: {self.victorias}"
        )

        self.lbl_derrotas.config(
            text=f"Derrotas: {self.derrotas}"
        )

        self.lbl_empates.config(
            text=f"Empates: {self.empates}"
        )

    # Reiniciar el marcador
    def reiniciar_marcador(self):

        self.victorias = 0
        self.derrotas = 0
        self.empates = 0

        self.actualizar_marcador()

        self.lbl_resultado.config(
            text="Marcador reiniciado. ¡A jugar!"
        )


# Ejecutar la aplicación
if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazDados(ventana)

    ventana.mainloop()
