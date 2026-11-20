import os
ruta = os.path.join(os.path.dirname(__file__), "datos.txt")
archi1=open(ruta,"r+") 
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()