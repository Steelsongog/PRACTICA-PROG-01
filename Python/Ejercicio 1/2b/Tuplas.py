
direccion = input("Nombre de calle (texto), número de puerta (entero) y número de piso (entero): ")

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

direccion = calle, puerta, piso

print(direccion)