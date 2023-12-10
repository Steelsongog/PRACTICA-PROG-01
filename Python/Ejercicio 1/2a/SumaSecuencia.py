
cuenta = str(input("Introduce numeros separados por espacios: "))


cuenta = cuenta.split(" ")
num = 0
total = 0

cuentaNum = len(cuenta)

for i in range(cuentaNum):
    total = total + int(cuenta[i])

print("El total es: ", total)