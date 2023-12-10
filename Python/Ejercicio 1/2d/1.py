# Ejercicio 1:
# Crea un programa llamado FicheroPersonas.py que lea información de personas (nombre y edad) de
# un fichero de texto, y muestre por pantalla los datos de la persona más joven y más vieja del fichero. El
# formato del fichero será como el siguiente, y se deberá almacenar en una lista antes de procesar la información.



# Leer el contenido del archivo y almacenarlo en una lista
archivo = open("personas.txt", 'r')
lineas = archivo.readlines()
archivo.close()

# Procesar la información y almacenarla en una lista de diccionarios
personas = []
for linea in lineas:
    nombre, edad = linea.strip().split(';')
    personas.append({'nombre': nombre, 'edad': int(edad)})

# Encontrar la persona más joven y la más vieja
persona_mas_joven = max(personas, key=lambda x: x['edad'])
persona_mas_vieja = min(personas, key=lambda x: x['edad'])

# Mostrar los resultados por pantalla
if personas:
    print(f"\nPersona más joven: {persona_mas_joven['nombre']} - Edad: {persona_mas_joven['edad']} años")
    print(f"Persona más vieja: {persona_mas_vieja['nombre']} - Edad: {persona_mas_vieja['edad']} años")
