# Solictar la introducciuon de numeros, uno a uno
#y los guardamos en una lista. Despues de pedir un numero
#pregunta si quiere introducir otro, si deice si (S), pide uno nuevo 
# y asi sucesivamente hasta que diga que no (n)
#al final , muestra la lista completa

lista=[]
resp = "s"
while(resp=="s" or resp=="S"):
    try:
        numero = int(input("Introduce un numero:"))
        lista.append(numero)
        resp=input("Desea introducir otro numero(s/n)? ")
    except ValueError:
        print("No es un valor numerico, vuelva a intentarlo")
        
print(f"La lista es: {lista}")