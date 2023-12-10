
size = int(input("Introduzca el tamaño de la tabla: "))
start = 0

tabla = [[0]* size for i in range(size)]

for i in range(size):
        for j in range(size):
            tabla[i][j] = int(input(f"Ingrese en el elemento en la fila {i+1}, columna {j+1}: "))

for fila in tabla:
    print(fila)

for i in range(size):
    for j in range(size):
        if i == j and tabla[i][j] != 1 or i != j and tabla[i][j] != 0:
            print("La matriz ingresada NO es una matriz identidad.")
            break