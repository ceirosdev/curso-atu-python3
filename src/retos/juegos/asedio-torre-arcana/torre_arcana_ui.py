
import tkinter as tk
from tkinter import ttk, messagebox

from torre_arcana import Personaje, Mago, Guerrero


class InterfazTorreArcana:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("La Torre Arcana")
        self.ventana.geometry("850x750")
        self.ventana.minsize(750, 650)

        # Estado inicial
        self.personaje = None
        self.guardian = None
        self.partida_terminada = False

        # Variables visuales
        self.vida_personaje = tk.IntVar(value=0)
        self.vida_guardian = tk.IntVar(value=60)

        self.texto_nombre = tk.StringVar(value="Sin seleccionar")
        self.texto_vida = tk.StringVar(value="Vida: --")
        self.texto_recurso = tk.StringVar(value="")

        self.texto_vida_guardian = tk.StringVar(value="Vida: 60 / 60")

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = ttk.Frame(self.ventana, padding=15)
        contenedor.pack(fill="both", expand=True)

        # Título
        ttk.Label(
            contenedor,
            text="TORRE ARCANA",
            font=("Arial", 23, "bold")
        ).pack(pady=(0, 5))

        ttk.Label(
            contenedor,
            text="Supera la prueba y derrota al guardián de piedra",
            font=("Arial", 11)
        ).pack(pady=(0, 15))

        # Selección de personaje
        self.marco_seleccion = ttk.LabelFrame(
            contenedor,
            text="Selecciona tu personaje",
            padding=12
        )
        self.marco_seleccion.pack(fill="x", pady=8)

        ttk.Button(
            self.marco_seleccion,
            text="🧙 Elegir Mago",
            command=lambda: self.iniciar_partida("mago")
        ).pack(side="left", expand=True, padx=10)

        ttk.Button(
            self.marco_seleccion,
            text="⚔ Elegir Guerrero",
            command=lambda: self.iniciar_partida("guerrero")
        ).pack(side="left", expand=True, padx=10)

        # Panel de personajes
        self.marco_personajes = ttk.Frame(contenedor)
        self.marco_personajes.pack(fill="x", pady=10)

        self.marco_personajes.columnconfigure(0, weight=1)
        self.marco_personajes.columnconfigure(1, weight=1)

        # Panel del jugador
        self.marco_jugador = ttk.LabelFrame(
            self.marco_personajes,
            text="Tu personaje",
            padding=15
        )
        self.marco_jugador.grid(
            row=0, column=0, sticky="nsew", padx=(0, 8)
        )

        ttk.Label(
            self.marco_jugador,
            textvariable=self.texto_nombre,
            font=("Arial", 15, "bold")
        ).pack(pady=5)

        self.etiqueta_icono = ttk.Label(
            self.marco_jugador,
            text="❔",
            font=("Arial", 48)
        )
        self.etiqueta_icono.pack(pady=5)

        ttk.Label(
            self.marco_jugador,
            textvariable=self.texto_vida,
            font=("Arial", 11, "bold")
        ).pack(pady=5)

        self.barra_vida_personaje = ttk.Progressbar(
            self.marco_jugador,
            variable=self.vida_personaje,
            maximum=100,
            length=250
        )
        self.barra_vida_personaje.pack(fill="x", pady=5)

        ttk.Label(
            self.marco_jugador,
            textvariable=self.texto_recurso,
            font=("Arial", 11)
        ).pack(pady=5)

        # Panel del guardián
        self.marco_guardian = ttk.LabelFrame(
            self.marco_personajes,
            text="Enemigo",
            padding=15
        )
        self.marco_guardian.grid(
            row=0, column=1, sticky="nsew", padx=(8, 0)
        )

        ttk.Label(
            self.marco_guardian,
            text="Guardián de piedra",
            font=("Arial", 15, "bold")
        ).pack(pady=5)

        ttk.Label(
            self.marco_guardian,
            text="🗿",
            font=("Arial", 48)
        ).pack(pady=5)

        ttk.Label(
            self.marco_guardian,
            textvariable=self.texto_vida_guardian,
            font=("Arial", 11, "bold")
        ).pack(pady=5)

        self.barra_vida_guardian = ttk.Progressbar(
            self.marco_guardian,
            variable=self.vida_guardian,
            maximum=60,
            length=250
        )
        self.barra_vida_guardian.pack(fill="x", pady=5)

        ttk.Label(
            self.marco_guardian,
            text="Daño básico: 10",
            font=("Arial", 11)
        ).pack(pady=5)

        # Menú de acciones
        self.marco_acciones = ttk.LabelFrame(
            contenedor,
            text="Acciones",
            padding=12
        )
        self.marco_acciones.pack(fill="x", pady=10)

        self.boton_atacar = ttk.Button(
            self.marco_acciones,
            text="Atacar",
            command=self.atacar
        )
        self.boton_atacar.pack(side="left", expand=True, padx=5)

        self.boton_habilidad = ttk.Button(
            self.marco_acciones,
            text="Habilidad especial",
            command=self.usar_habilidad
        )
        self.boton_habilidad.pack(side="left", expand=True, padx=5)

        self.boton_estado = ttk.Button(
            self.marco_acciones,
            text="Consultar estado",
            command=self.consultar_estado
        )
        self.boton_estado.pack(side="left", expand=True, padx=5)

        # Registro de acontecimientos
        marco_registro = ttk.LabelFrame(
            contenedor,
            text="Registro de la partida",
            padding=10
        )
        marco_registro.pack(fill="both", expand=True, pady=10)

        self.registro = tk.Text(
            marco_registro,
            height=10,
            wrap="word",
            font=("Consolas", 10),
            state="disabled"
        )
        self.registro.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            marco_registro,
            orient="vertical",
            command=self.registro.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.registro.config(yscrollcommand=scrollbar.set)

        # Botón de nueva partida
        self.boton_reiniciar = ttk.Button(
            contenedor,
            text="Nueva partida",
            command=self.reiniciar
        )
        self.boton_reiniciar.pack(pady=5)

        # Desactivar acciones hasta elegir personaje
        self.activar_botones(False)

        self.agregar_mensaje(
            "Bienvenido a la Torre Arcana.\n"
            "Selecciona un personaje para comenzar la prueba."
        )

    # Iniciar una nueva partida
    def iniciar_partida(self, tipo):

        if tipo == "mago":
            self.personaje = Mago()
            icono = "🧙"

        else:
            self.personaje = Guerrero()
            icono = "⚔"

        self.guardian = Personaje(
            "Guardián de piedra",
            60,
            10
        )

        self.partida_terminada = False

        self.etiqueta_icono.config(text=icono)
        self.texto_nombre.set(self.personaje.nombre)

        self.actualizar_estado()

        self.activar_botones(True)

        self.agregar_mensaje(
            f"\nHas elegido al {self.personaje.nombre}."
        )

        self.agregar_mensaje(
            "El guardián de piedra aparece ante ti."
        )

        self.agregar_mensaje(
            "¡Comienza la prueba de la Torre Arcana!"
        )

    # Ejecutar un ataque básico
    def atacar(self):

        if not self.puede_jugar():
            return

        danio = self.personaje.danio

        self.agregar_mensaje(
            f"\n{self.personaje.nombre} realiza un ataque básico."
        )

        self.personaje.atacar(self.guardian)

        self.agregar_mensaje(
            f"El guardián recibe {danio} puntos de daño."
        )

        self.finalizar_turno()

    # Ejecutar la habilidad especial
    def usar_habilidad(self):

        if not self.puede_jugar():
            return

        if isinstance(self.personaje, Mago):

            if self.personaje.mana < 15:
                self.agregar_mensaje(
                    "\nNo tienes suficiente maná para lanzar "
                    "una bola de fuego. El turno no se consume."
                )
                return

            nombre_habilidad = "Bola de fuego"
            danio = 20

        else:

            if self.personaje.cargas < 1:
                self.agregar_mensaje(
                    "\nNo tienes cargas disponibles para realizar "
                    "un golpe poderoso. El turno no se consume."
                )
                return

            nombre_habilidad = "Golpe poderoso"
            danio = 24

        self.agregar_mensaje(
            f"\n{self.personaje.nombre} utiliza {nombre_habilidad}."
        )

        ejecutada = self.personaje.habilidad_especial(
            self.guardian
        )

        if ejecutada:

            self.agregar_mensaje(
                f"El guardián recibe {danio} puntos de daño."
            )

            self.finalizar_turno()

        self.actualizar_estado()

    # Gestionar la respuesta del guardián
    def finalizar_turno(self):

        if not self.guardian.esta_vivo():

            self.actualizar_estado()
            self.terminar_partida(True)
            return

        if self.personaje.esta_vivo():

            danio = self.guardian.danio

            self.agregar_mensaje(
                "\nEl guardián responde con un ataque."
            )

            self.guardian.atacar(self.personaje)

            self.agregar_mensaje(
                f"Recibes {danio} puntos de daño."
            )

        self.actualizar_estado()

        if not self.personaje.esta_vivo():

            self.terminar_partida(False)

    # Consultar el estado sin consumir turno
    def consultar_estado(self):

        if not self.personaje:
            return

        self.agregar_mensaje("\n--- ESTADO ACTUAL ---")

        self.agregar_mensaje(
            f"{self.personaje.nombre}: "
            f"{self.personaje.vida} puntos de vida."
        )

        if isinstance(self.personaje, Mago):

            self.agregar_mensaje(
                f"Maná disponible: {self.personaje.mana}"
            )

        elif isinstance(self.personaje, Guerrero):

            self.agregar_mensaje(
                f"Cargas disponibles: {self.personaje.cargas}"
            )

        self.agregar_mensaje(
            f"Guardián: {self.guardian.vida} puntos de vida."
        )

        self.agregar_mensaje(
            "Consultar el estado no consume el turno."
        )

    # Actualizar barras y recursos
    def actualizar_estado(self):

        if not self.personaje or not self.guardian:
            return

        self.vida_personaje.set(self.personaje.vida)
        self.vida_guardian.set(self.guardian.vida)

        self.texto_vida.set(
            f"Vida: {self.personaje.vida} / "
            f"{50 if isinstance(self.personaje, Mago) else 70}"
        )

        self.texto_vida_guardian.set(
            f"Vida: {self.guardian.vida} / 60"
        )

        if isinstance(self.personaje, Mago):

            self.texto_recurso.set(
                f"Maná disponible: {self.personaje.mana} / 30"
            )

            self.boton_habilidad.config(
                text="Bola de fuego (20 daño)"
            )

        elif isinstance(self.personaje, Guerrero):

            self.texto_recurso.set(
                f"Cargas disponibles: {self.personaje.cargas} / 2"
            )

            self.boton_habilidad.config(
                text="Golpe poderoso (24 daño)"
            )

    # Comprobar que la partida permite realizar acciones
    def puede_jugar(self):

        return (
            self.personaje is not None
            and self.guardian is not None
            and not self.partida_terminada
        )

    # Finalizar la partida
    def terminar_partida(self, victoria):

        self.partida_terminada = True

        self.activar_botones(False)

        if victoria:

            mensaje = (
                "¡Enhorabuena!\n"
                "Has derrotado al guardián y superado la prueba."
            )

            self.agregar_mensaje(
                "\n¡VICTORIA! Has superado la Torre Arcana."
            )

        else:

            mensaje = (
                "El guardián te ha derrotado.\n"
                "No has superado la prueba."
            )

            self.agregar_mensaje(
                "\nDERROTA. El guardián ha ganado."
            )

        messagebox.showinfo(
            "Fin de la partida",
            mensaje
        )

    # Activar o desactivar botones
    def activar_botones(self, activo):

        estado = "normal" if activo else "disabled"

        self.boton_atacar.config(state=estado)
        self.boton_habilidad.config(state=estado)
        self.boton_estado.config(state=estado)

    # Añadir mensajes al registro
    def agregar_mensaje(self, mensaje):

        self.registro.config(state="normal")

        self.registro.insert("end", mensaje + "\n")
        self.registro.see("end")

        self.registro.config(state="disabled")

    # Reiniciar la partida
    def reiniciar(self):

        self.personaje = None
        self.guardian = None
        self.partida_terminada = False

        self.vida_personaje.set(0)
        self.vida_guardian.set(60)

        self.texto_nombre.set("Sin seleccionar")
        self.texto_vida.set("Vida: --")
        self.texto_recurso.set("")
        self.texto_vida_guardian.set("Vida: 60 / 60")

        self.etiqueta_icono.config(text="❔")

        self.boton_habilidad.config(
            text="Habilidad especial"
        )

        self.activar_botones(False)

        self.registro.config(state="normal")
        self.registro.delete("1.0", "end")
        self.registro.config(state="disabled")

        self.agregar_mensaje(
            "Nueva partida.\nSelecciona un personaje para comenzar."
        )


if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazTorreArcana(ventana)

    ventana.mainloop()
