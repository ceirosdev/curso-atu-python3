
import tkinter as tk
from tkinter import ttk, messagebox

from juego_piedra_papel_tijera_para_ui import juego


class InterfazPiedraPapelTijeras:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Piedra, Papel o Tijeras")
        self.ventana.geometry("650x620")
        self.ventana.resizable(False, False)

        # Marcador
        self.juegos_jugados = 0
        self.ganadas_humano = 0
        self.ganadas_pc = 0
        self.empates = 0
        self.max_juegos = 10

        # Opciones del juego
        self.opciones = {
            1: "Piedra",
            2: "Papel",
            3: "Tijera"
        }

        # Símbolos visuales
        self.simbolos = {
            1: "✊",
            2: "✋",
            3: "✌"
        }

        # Variables de la interfaz
        self.texto_jugador = tk.StringVar(value="Esperando elección")
        self.texto_pc = tk.StringVar(value="Esperando elección")
        self.texto_resultado = tk.StringVar(
            value="¡Elige tu jugada para comenzar!"
        )
        self.texto_partidas = tk.StringVar(
            value=f"Partidas: 0 / {self.max_juegos}"
        )
        self.texto_marcador = tk.StringVar(
            value="Jugador: 0    Máquina: 0    Empates: 0"
        )

        self.crear_interfaz()

    def crear_interfaz(self):

        # Contenedor principal
        contenedor = ttk.Frame(self.ventana, padding=20)
        contenedor.pack(fill="both", expand=True)

        # Título
        ttk.Label(
            contenedor,
            text="PIEDRA, PAPEL O TIJERAS",
            font=("Arial", 20, "bold")
        ).pack(pady=(0, 10))

        ttk.Label(
            contenedor,
            text="Jugador contra máquina",
            font=("Arial", 11)
        ).pack(pady=(0, 20))

        # Marcador de partidas
        ttk.Label(
            contenedor,
            textvariable=self.texto_partidas,
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        # Zona de elecciones
        marco_elecciones = ttk.LabelFrame(
            contenedor,
            text="Resultado de la ronda",
            padding=15
        )
        marco_elecciones.pack(fill="x", pady=15)

        marco_elecciones.columnconfigure(0, weight=1)
        marco_elecciones.columnconfigure(1, weight=1)

        # Jugador
        ttk.Label(
            marco_elecciones,
            text="JUGADOR",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, pady=5)

        self.etiqueta_jugador = ttk.Label(
            marco_elecciones,
            text="❔",
            font=("Arial", 45)
        )
        self.etiqueta_jugador.grid(row=1, column=0, pady=5)

        self.etiqueta_nombre_jugador = ttk.Label(
            marco_elecciones,
            textvariable=self.texto_jugador,
            font=("Arial", 12)
        )
        self.etiqueta_nombre_jugador.grid(row=2, column=0, pady=5)

        # Máquina
        ttk.Label(
            marco_elecciones,
            text="MÁQUINA",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=1, pady=5)

        self.etiqueta_pc = ttk.Label(
            marco_elecciones,
            text="❔",
            font=("Arial", 45)
        )
        self.etiqueta_pc.grid(row=1, column=1, pady=5)

        self.etiqueta_nombre_pc = ttk.Label(
            marco_elecciones,
            textvariable=self.texto_pc,
            font=("Arial", 12)
        )
        self.etiqueta_nombre_pc.grid(row=2, column=1, pady=5)

        # Resultado de la ronda
        ttk.Label(
            contenedor,
            textvariable=self.texto_resultado,
            font=("Arial", 14, "bold"),
            wraplength=550,
            justify="center"
        ).pack(pady=15)

        # Botones de elección
        ttk.Label(
            contenedor,
            text="Selecciona tu jugada",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        marco_botones = ttk.Frame(contenedor)
        marco_botones.pack(pady=10)

        ttk.Button(
            marco_botones,
            text="✊ Piedra",
            command=lambda: self.jugar(1)
        ).grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(
            marco_botones,
            text="✋ Papel",
            command=lambda: self.jugar(2)
        ).grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(
            marco_botones,
            text="✌ Tijera",
            command=lambda: self.jugar(3)
        ).grid(row=0, column=2, padx=5, pady=5)

        # Decisión aleatoria
        ttk.Button(
            contenedor,
            text="🎲 Decide por mí",
            command=lambda: self.jugar(0)
        ).pack(pady=8)

        # Marcador
        marco_marcador = ttk.LabelFrame(
            contenedor,
            text="Marcador general",
            padding=12
        )
        marco_marcador.pack(fill="x", pady=15)

        ttk.Label(
            marco_marcador,
            textvariable=self.texto_marcador,
            font=("Arial", 11, "bold")
        ).pack()

        # Reiniciar
        ttk.Button(
            contenedor,
            text="Reiniciar partida",
            command=self.reiniciar
        ).pack(pady=10)

    def jugar(self, decision):

        # Comprobar el límite de partidas
        if self.juegos_jugados >= self.max_juegos:
            messagebox.showinfo(
                "Partida finalizada",
                "Has alcanzado el límite de diez partidas."
            )
            return

        # Ejecutar una partida
        resultado = juego(decision)

        humano = resultado["humano"]
        pc = resultado["pc"]
        ganador = resultado["resultado"]

        # Actualizar las elecciones visuales
        self.etiqueta_jugador.config(
            text=self.simbolos[humano]
        )

        self.etiqueta_pc.config(
            text=self.simbolos[pc]
        )

        self.texto_jugador.set(self.opciones[humano])
        self.texto_pc.set(self.opciones[pc])

        # Actualizar el marcador
        self.juegos_jugados += 1

        if ganador == "humano":

            self.ganadas_humano += 1
            self.texto_resultado.set("¡Has ganado esta ronda!")

        elif ganador == "pc":

            self.ganadas_pc += 1
            self.texto_resultado.set("La máquina ha ganado esta ronda.")

        else:

            self.empates += 1
            self.texto_resultado.set("¡La ronda ha terminado en empate!")

        # Actualizar los contadores
        self.actualizar_marcador()

        # Comprobar si han terminado las partidas
        if self.juegos_jugados == self.max_juegos:

            messagebox.showinfo(
                "Juego finalizado",
                self.obtener_resumen()
            )

    def actualizar_marcador(self):

        self.texto_partidas.set(
            f"Partidas: {self.juegos_jugados} / {self.max_juegos}"
        )

        self.texto_marcador.set(
            f"Jugador: {self.ganadas_humano}    "
            f"Máquina: {self.ganadas_pc}    "
            f"Empates: {self.empates}"
        )

    def obtener_resumen(self):

        return (
            "¡Has terminado las diez partidas!\n\n"
            f"Victorias del jugador: {self.ganadas_humano}\n"
            f"Victorias de la máquina: {self.ganadas_pc}\n"
            f"Empates: {self.empates}"
        )

    def reiniciar(self):

        self.juegos_jugados = 0
        self.ganadas_humano = 0
        self.ganadas_pc = 0
        self.empates = 0

        self.etiqueta_jugador.config(text="❔")
        self.etiqueta_pc.config(text="❔")

        self.texto_jugador.set("Esperando elección")
        self.texto_pc.set("Esperando elección")
        self.texto_resultado.set(
            "¡Elige tu jugada para comenzar!"
        )

        self.actualizar_marcador()


if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazPiedraPapelTijeras(ventana)

    ventana.mainloop()
