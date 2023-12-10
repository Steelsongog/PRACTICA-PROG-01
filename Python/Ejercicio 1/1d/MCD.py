
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

res = 100
mayor = 0
mcd = 0
menor = 0

while res > menor :

    if n1 > n2:
        res = n1%n2
        mayor = res
        menor = n2
        n1 = res
    else:
        res = n2%n1
        mayor = res
        menor = n1
        n2 = res

    mcd = res

print(f"El MCD es {mcd}")


