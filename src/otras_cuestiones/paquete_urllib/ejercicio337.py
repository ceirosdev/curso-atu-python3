from urllib import request

# Petición para la página
req1 = request.Request(
    "https://opencode.ai/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    },
)
pagina = request.urlopen(req1)
datos = pagina.read()
archivo1 = open("pagina1.html", "wb")
archivo1.write(datos)
archivo1.close()

# Petición para la "imagen"
req2 = request.Request(
    "https://opencode.ai/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    },
)
imagen = request.urlopen(req2)
datos = imagen.read()
archivo2 = open("imagen1.jpg", "wb")
archivo2.write(datos)
archivo2.close()
