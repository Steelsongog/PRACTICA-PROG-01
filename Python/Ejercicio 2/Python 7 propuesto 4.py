
preguntas = int(input("Introduce el numero total de preguntas: "))
aciertos = int(input("Introduce el numero total de preguntas acertadas: "))

Porcentaje = (aciertos/preguntas)*100

if Porcentaje>=90:
    print("Nivel máximo")
elif Porcentaje>=75 and Porcentaje<90:
    print("Nivel medio")
elif Porcentaje>=50 and Porcentaje<75:
    print("Nivel regular")
if Porcentaje>=90:
    print("Fuera de nivel")

