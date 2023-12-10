def cargar_lista():
    lista = []
    for i in range(5):
        valor = int(input("Ingrese un entero: "))
        lista.append(valor)
    return lista

def obtener_mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

# Bloque principal
lista_enteros = cargar_lista()

# Desempaquetar la tupla y mostrar el mayor y menor
mayor, menor = obtener_mayor_menor(lista_enteros)
print("Mayor valor en la lista:", mayor)
print("Menor valor en la lista:", menor)
