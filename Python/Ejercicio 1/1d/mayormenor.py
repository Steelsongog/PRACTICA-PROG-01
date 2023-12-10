cantidad = int(input("Cuantos numeros vas a introducir: "))

mayor = 0
menor = 100000000

for i in range (0, cantidad) :
    num = int(input("Introduce el numero: "))

    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"El número mayor es el {mayor} y el numero mas pequeño es el {menor}")