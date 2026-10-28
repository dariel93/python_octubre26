# Solicita la introducion de una contraseña, si es correcta
# le dice que es un usario valido. si no es correcta, se le vuelve a Pendir
# Asi, hasta tres intentos. Si despues del tercer intento la contraseña es incorrecta
# le dice q no es un usuario valido

password = "admin"
intento = 3
acertado = False
    
while intento > 0 and acertado==False:
    contraseña=str(input("Introduce una Contraseña :"))
    if password == contraseña:
        print("La Contraseña es correcta")
        acertado=True
        
    else :
        print("Vuelva a intentar")
        intento-=1
if acertado == True:
    print("Usuario Valido")
else:
    print("Usuario No Valido")
    