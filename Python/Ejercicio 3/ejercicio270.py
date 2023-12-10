# Es una forma más compacta de recorrer cada una de las líneas del archivo de texto.

archi1 = open("datos.txt","r")
for linea in archi1:
    print(linea, end = '')
archi1.close()