"""from urllib import request

pagina = request.urlopen(
    "https://opencode.ai/docs/skills/"
)
datos = pagina.read()
print(datos)"""

from urllib import request

# Definimos la URL
url = "http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html"

# Creamos un objeto Request con un User-Agent de un navegador común
req = request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    },
)

# Abrimos la petición con el objeto req
with request.urlopen(req) as respuesta:
    datos = respuesta.read()
    print(datos.decode("utf-8"))  # Decodificamos a texto para poder leerlo bien
