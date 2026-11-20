import os
ruta = os.path.join(os.path.dirname(__file__), "datos.txt")
archi1=open(ruta,"r")
lineas=archi1.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
archi1.close()