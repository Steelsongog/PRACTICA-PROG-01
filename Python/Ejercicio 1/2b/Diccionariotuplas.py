
dni = input("Introduzca su DNI : ")
direccion = input("Introduzca el nombre de calle (texto), número de puerta (entero) y número de piso (entero): ")

lista = direccion.split(" ")

contador = 0
calle = ""
puerta = 0
piso = 0


for item in lista:

    if contador == 0:
        calle = item
    if contador == 1:
        puerta = item
    if contador == 2:
        piso = item
    contador = contador +1

user = {}

user[dni] = (dni, calle, puerta, piso)

dni = input("Dime el dni a buscar: ")

if dni in user:
    print("Los datos para el dni buscado son: ", direccion)        
else:
    print("El DNI introducido no se encuentra en la base de datos.")