
texto = str(input("Introduce un texto con plabras Python: "))
contador = 0

while texto.find("Python")>= 0:
    contador = contador +1
    texto = texto[(texto.find("Python")+6):]

print(contador)
    


