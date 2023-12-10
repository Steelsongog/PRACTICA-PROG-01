# Realiza un programa que lea una secuencia de números enteros, uno por línea.

# El programa deberá mostrar como resultado el número más alto, seguido del número más bajo, separados por un espacio.

# El programa incluirá una primera línea X, 1<=X<=100, indicando cuantos números a leer (esa línea no se tendrá en cuenta). Tras ello se leerán X números en las próximas X líneas.

# Lee la cantidad de números a procesar
cantidad_numeros = int(input())

# Inicializa variables para el número más alto y más bajo
numero_mas_alto = float('-inf')
numero_mas_bajo = float('inf')

# Lee los números y encuentra el más alto y el más bajo
for _ in range(cantidad_numeros):
    numero = int(input())
    numero_mas_alto = max(numero_mas_alto, numero)
    numero_mas_bajo = min(numero_mas_bajo, numero)

# Imprime el resultado
print(numero_mas_alto, numero_mas_bajo)
