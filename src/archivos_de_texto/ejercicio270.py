import os
ruta = os.path.join(os.path.dirname(__file__), "datos.txt")
archi1=open(ruta,"r")
for linea in archi1:
    print(linea, end='')
archi1.close()