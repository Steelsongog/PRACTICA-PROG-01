# Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.

archi1 = open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1 = open("datos.txt","r")
contenido = archi1.read()
print(contenido)
archi1.close()