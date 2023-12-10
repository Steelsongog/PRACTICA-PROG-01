# Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1.
# Dejar como comentario dentro del código fuente el enunciado del problema. 

valores = 0
total = 0
while valores != -1:
    valores = int(input("Introduce valores entero (-1 para salir del programa): "))
    total += valores

print("La suma de los valores es: ",total)