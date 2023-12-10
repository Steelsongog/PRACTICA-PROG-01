entero = int(input("Introduce un número entero: "))

print("Los números impares hasta ese número son: ", end ="")
for i in range (0, entero):
    if (i%2>0):
        if(i+1 == entero or i+2 == entero):
            print(f"{i} ",end ="")
        else:
            print(f"{i}, ",end ="")

