# Realiza un programa que lea una secuencia de números enteros en una misma línea y muestre como resultado la línea en orden inverso.
# El programa incluirá una primera línea X, 1<=X<=100, indicando cuantos números a leer (esa línea no se tendrá en cuenta). Tras ello, en la siguiente línea se leerán X números separados por espacios y se mostrará finalmente en una sola línea el resultado.

# Lee la cantidad de números a procesar
cantidad_numeros = int(input())

# Lee la línea de números y los separa en una lista
numeros = list(map(int, input().split()))

# Invierte la lista de números
numeros_invertidos = numeros[::-1]

# Imprime el resultado en una sola línea
print(" ".join(map(str, numeros_invertidos)))
