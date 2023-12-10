# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor

estudiantesMañanas = 5
estudiantesTardes = 6
estudiantesNoche = 11

edad = 0

edadesM = 0
edadesT = 0
edadesN = 0


for i in range(estudiantesMañanas):
    edad = int(input("Introduzca la edad del alumno de mañanas: "))
    edadesM += edad

for i in range(estudiantesTardes):
    edad = int(input("Introduzca la edad del alumno de tardes: "))
    edadesT += edad

for i in range(estudiantesNoche):
    edad = int(input("Introduzca la edad del alumno de noches: "))
    edadesN += edad

edadesMP = edadesM / estudiantesMañanas
edadesTP = edadesT / estudiantesTardes
edadesNP = edadesN / estudiantesNoche

print("El promedio de edad del turno de mañanas es: ", edadesMP)
print("El promedio de edad del turno de tardes es: ", edadesTP)
print("El promedio de edad del turno de noches es: ", edadesNP)


if edadesMP >edadesTP and edadesMP > edadesNP:
    print("El promedio de edad del turno de mañanas es el mayor de todos.")
elif edadesTP > edadesMP and edadesTP > edadesNP:
    print("El promedio de edad del turno de tardes es el mayor de todos.")
else:
    print("El promedio del turno de noches es el mayor de todos.")