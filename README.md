# Curso de Programación con Python 🐍

Este repositorio contiene una serie de ejercicios prácticos para el aprendizaje y la práctica de los fundamentos del lenguaje Python.

## 📂 Estructura del Proyecto
El código fuente se encuentra en la carpeta `src/` y está organizado por temas para facilitar el estudio:

- **archivos_de_texto**: Escritura y lectura de archivos de texto por consola y UI (`tkinter`).
- **bucles**: Práctica con estructuras de repetición (`for`, `while`).
- **condicionales**: Ejercicios sobre lógica de control y toma de decisiones (`if`, `elif`, `else`).
- **diccionarios**: Ejercicios sobre almacenar parejas clave y valor (`dict()`).
- **excepciones**: Manejo de errores y situaciones inesperadas mediante bloques `try`, `except`, `finally` y `raise`.
- **funciones**: Ejercicios sobre bloques de código reutilizables con funciones (`def`).
- **listas**: Ejercicios sobre almacenamiento y modificación de listas (`list()`).
- **otras_cuestiones**: Ejercicios adicionales organizados por temáticas específicas:
    - **comprension_listas**: Ejercicios sobre comprensión de listas.
    - **func_orden_superior**: Ejercicios sobre funciones de orden superior.
    - **lambdas**: Ejercicios sobre funciones anónimas (`lambda`).
    - **modulos_paquetes**: Ejercicios sobre módulos y paquetes en Python.
    - **paquete_urllib**: Ejercicios de manejo de peticiones web con `urllib`.
    - **recursividad**: Ejercicios sobre algoritmos recursivos.
- **retos**:
    - **algoritmos**: Ejercicios de lógica y algoritmos.
    - **juegos**: Juegos de consola y su equivalente en UI (`tkinter`).
    - **poo**: Ejercicios sobre Programación Orientada a Objetos (clases, objetos, herencia).
- **sqlite**: Ejercicios sobre base de datos nativa de Python (`SQLite`) por consola y UI (`tkinter`).
- **strings**: Ejercicios sobre manipulación de cadenas de texto.
- **tuplas**: Ejercicios sobre almacenamiento y modificación de tuplas (`tuple()`).
- **variables**: Ejercicios sobre declaración, tipos de datos y manipulación básica.

## 🚀 Cómo ejecutar los ejercicios
Para ejecutar cualquier archivo del proyecto, asegúrate de tener Python instalado y usa el siguiente comando en tu terminal:

```bash
python path/to/your_script.py
```

Si algunos ejercicios están organizados en módulos y al ejecutar los programas no los reconoce, puedes establecer el `PYTHONPATH` en el directorio `src`:

**En PowerShell (Windows):**
```powershell
$env:PYTHONPATH = "$PWD\src"
```

**En Bash (Linux/macOS):**
```bash
export PYTHONPATH="$PWD/src"
```

## 📝 Notas adicionales
- Este proyecto incluye ejercicios de nivel progresivo, incluyendo soluciones en formato interactivo (`.ipynb`) y archivos prácticos para reforzar la lógica de programación.
- Se incluyen ejemplos prácticos de interfaces gráficas utilizando la librería `tkinter`.
