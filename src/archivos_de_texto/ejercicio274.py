import os
ruta = os.path.join(os.path.dirname(__file__), "datos.txt")
archi1=open(ruta,"w", encoding="utf-8") 
archi1.write("Primer línea.\n") 
archi1.write("Segunda línea.\n") 
archi1.write("Tercer línea.\n")  
archi1.close()