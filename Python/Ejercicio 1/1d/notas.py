n1 = int(input("Introduce la primera nota: "))
n2 = int(input("Introduce la segunda nota: "))
n3 = int(input("Introduce la tercera nota: "))


if n1<4 and n2<4 and n3<4:
    notaFinal = 0
elif n1<4 or n2<4 or n3<4:
    notaFinal = 2
elif n1>4 and n2>4 and n3>4:
    n1 = n1*0.30
    n2 = n2*0.20
    n3 = n3*0.50
    notaFinal = n1+n2+n3
    
print(f"La nota final es : {notaFinal}")