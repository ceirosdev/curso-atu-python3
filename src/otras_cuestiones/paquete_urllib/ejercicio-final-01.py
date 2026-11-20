import tkinter as tk
from tkinter import scrolledtext, messagebox
from urllib import request, error

def recuperar_datos():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Atención", "Por favor, ingrese una URL válida.")
        return

    # Limpiar el área de texto antes de mostrar resultados
    txt_resultado.config(state=tk.NORMAL)
    txt_resultado.delete(1.0, tk.END)
    txt_resultado.insert(tk.END, f"Cargando contenido de: {url}...\n\n")
    txt_resultado.update()

    try:
        # Configurar la petición con User-Agent para evitar bloqueos 403
        req = request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        
        with request.urlopen(req) as respuesta:
            datos = respuesta.read().decode("utf-8")
            txt_resultado.insert(tk.END, datos)
            
    except error.HTTPError as err:
        txt_resultado.insert(tk.END, f"Error HTTP: {err.code}\n{err.reason}")
    except error.URLError as err:
        txt_resultado.insert(tk.END, f"Error de red: {err.reason}")
    except Exception as e:
        txt_resultado.insert(tk.END, f"Ocurrió un error inesperado: {e}")
    
    # Volver a poner el widget en modo solo lectura
    txt_resultado.config(state=tk.DISABLED)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Recuperador de Web")
ventana.geometry("800x600")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Ingrese URL del sitio web:", font=("Arial", 12))
label_instruccion.pack(pady=10)

# Frame para el Entry y el Botón (alineados horizontalmente)
frame_url = tk.Frame(ventana)
frame_url.pack(pady=5)

entry_url = tk.Entry(frame_url, width=70)
entry_url.pack(side=tk.LEFT, padx=5)
entry_url.insert(0, "https://opencode.ai/") # URL por defecto

btn_recuperar = tk.Button(frame_url, text="Recuperar", command=recuperar_datos)
btn_recuperar.pack(side=tk.LEFT)

# Área de texto con scroll
txt_resultado = scrolledtext.ScrolledText(ventana, width=90, height=30, state=tk.DISABLED)
txt_resultado.pack(pady=20, padx=10)

# Iniciar la aplicación
ventana.mainloop()