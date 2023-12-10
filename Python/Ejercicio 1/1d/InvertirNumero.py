
num = int(input("Introduce un número: "))
numInv = 0

while (num>0):
    num2 = int(num%10) 
    num = int(num/10)
    numInv = numInv + num2
    numInv = int(numInv*10)


print(f"El numero invertido es {numInv/10}")