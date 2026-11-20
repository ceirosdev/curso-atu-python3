from urllib import request
from urllib import error

# URL de prueba
url = "https://opencode.ai/"

try:
    # Crear la petición con User-Agent para evitar bloqueos 403
    req = request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    
    # Ejecutar la petición
    with request.urlopen(req) as respuesta:
        datos = respuesta.read().decode("utf-8")
        print(datos)

except error.HTTPError as err:
    print(f"Código de respuesta HTTP devuelto por el servidor {err.code}")
    print(f"No existe el recurso {err.filename}")
except error.URLError as err:
    print(f"Error de red: {err.reason}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
