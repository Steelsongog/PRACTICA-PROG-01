sueldo = int(input("Introduzca el sueldo: "))
antiguedad = int(input("Introduzca la antiguedad: "))

if sueldo < 500 and antiguedad>10:
    sueldo = sueldo*1.20
    print("Su nuevo sueldo es ",sueldo," euros")
elif sueldo < 500 and antiguedad < 10:
    sueldo = sueldo*1.05 
    print("Su nuevo sueldo es ",sueldo," euros")
elif sueldo >= 500:
    print("Su nuevo sueldo es ",sueldo," euros")
