# Se tiene la siguiente lista:

# lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

# Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
# Volver a imprimir la lista. 


# Definir la lista
lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

# Imprimir la lista original
print("Lista original:")
for fila in lista:
    print(fila)

# Fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista"
for i in range(len(lista[0])):
    if lista[0][i] > 50:
        lista[0][i] = 0

# Imprimir la lista después de la modificación
print("\nLista después de fijar a cero elementos mayores a 50 en el primer elemento:")
for fila in lista:
    print(fila)
