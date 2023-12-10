n = -1
contPares = 0
contImpares = 0

while n != 0:
    n = int(input("Introduzca n números enteros (0 para salir): "))

    if n%2 == 0:
        contPares = contPares +1
    elif n%2>0 or n == 1:
        contImpares = contImpares +1

print("Numeros impares: ",contImpares," Numeros pares: ",contPares)