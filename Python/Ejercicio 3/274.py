# Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code.

archi1 = open("datos.txt","w", encoding="utf-8") 
archi1.write("Primer línea.\n") 
archi1.write("Segunda línea.\n") 
archi1.write("Tercer línea.\n")  
archi1.close()