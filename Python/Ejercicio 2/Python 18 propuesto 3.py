# Cargar una lista con 5 elementos enteros
lista_enteros = []
for i in range(5):
    elemento = int(input("Ingrese un elemento entero para la lista: "))
    lista_enteros.append(elemento)

# Ordenar de menor a mayor y mostrar por pantalla
lista_enteros.sort()
print("Lista ordenada de menor a mayor:", lista_enteros)

# Ordenar de mayor a menor y mostrar por pantalla
lista_enteros.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista_enteros)
