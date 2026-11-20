import os

def leer(directorio):
    lista = os.listdir(directorio)
    for elemento in lista:
        ruta_completa = os.path.join(directorio, elemento)
        
        # Refactorización: Usamos elif para evitar evaluaciones innecesarias
        # y reducir la sensación de anidación.
        if os.path.isfile(ruta_completa):
            print(f"{elemento} [archivo]")
        elif os.path.isdir(ruta_completa):
            print(f"{elemento} [directorio]")
            leer(ruta_completa)

if __name__ == "__main__":
    # Obtener la ruta absoluta del archivo actual
    ruta_script = os.path.abspath(__file__)
    
    # Navegar dos niveles hacia arriba para llegar a la carpeta 'src'
    # Desde: src/otras_cuestiones/recursividad/
    # Subimos a: src/otras_cuestiones/ y luego a: src/
    ruta_src = os.path.abspath(os.path.join(os.path.dirname(ruta_script), "..", ".."))
    
    leer(ruta_src)