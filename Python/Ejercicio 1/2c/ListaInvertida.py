nombre = input("Introduzca una serie de nombres separados por comas: ")

listaNombre = nombre.split(", ")
datos = list()
for elemento in listaNombre: 
    datos.append(elemento)

datos.reverse()

print(datos)    