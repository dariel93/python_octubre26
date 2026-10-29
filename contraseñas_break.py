password = "admin"
intento = 3
acierto = False

while intento > 0:
    contraseña=input("Introduce una Contraseña :")
    if password == contraseña:
        print("Usuario Valido")
        acierto = True
        break
    else :
        print("Vuelva a intentar!")
        intento-=1

if not acierto:
    print("Usuario No Valido")