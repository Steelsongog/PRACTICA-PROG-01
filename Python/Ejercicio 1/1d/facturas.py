total = 0
factura = "ñ"

while factura !=0:
    factura = int(input("Introduce la factura, 0 para salir: "))
    total = total+factura
print(f"La factura total es {total:.2f}")