# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores. 

# Crear una lista de 5 enteros y cargarlos por teclado
lista_enteros = []
for i in range(5):
    valor = int(input("Ingrese un entero: "))
    lista_enteros.append(valor)

# Generar una nueva lista con los valores menores a 10
nueva_lista = [valor for valor in lista_enteros if valor < 10]

# Imprimir la lista original y la nueva lista
print("Lista original:", lista_enteros)
print("Nueva lista sin elementos mayores o iguales a 10:", nueva_lista)
