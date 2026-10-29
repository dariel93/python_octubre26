
resp = "s"
while(resp=="s" or resp=="S"):
    numero = int(input("Introduce un numero:"))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    resp=input("Desea introducir otro numero(s/n)? ")