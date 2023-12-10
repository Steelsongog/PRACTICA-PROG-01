num = -1
index = 0
lista = list()

while num != 0:
    num = int(input("Introduzca un numero (0 para terminar): "))
    lista.append(num)

num = int(input("Introduzca de que numero  del que desea conocer la posición: "))

if num in lista:
    pos = lista.index(num)
    print("El número se encuentra en la posicion:", pos)

    while num in lista[pos+1:]:
        print("El número se encuentra en la posicion:", lista.index(num, pos+1))
else:
    print("El numero no se encuentra en la lista.")