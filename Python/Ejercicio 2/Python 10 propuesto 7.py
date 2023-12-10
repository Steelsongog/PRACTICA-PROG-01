# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares. 

n = 10
negativos = 0
positivos = 0
multiplos15 = 0
pares = 0

for i in range(n):
    num = int(input("Introduzca 10 valores enteros: "))

    if num < 0:
        negativos =negativos +1
    else :
        positivos =positivos +1

    if num%15 ==0 :
        multiplos15 = multiplos15+1
    if num%2 == 0:
        pares = pares+1

print("La cantidad de positivos es: ",positivos)
print("La cantidad de negativos es: ",negativos)
print("La cantidad de multiplos de 15 es: ",multiplos15)
print("La cantidad de pares es: ",pares)
