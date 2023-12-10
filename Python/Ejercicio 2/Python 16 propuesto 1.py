# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista
nombres = []
for i in range(5):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    nombres.append(nombre)

# Mostrar el nombre de persona menor en orden alfabético
nombre_menor = min(nombres)
print("El nombre de persona menor en orden alfabético es:", nombre_menor)
