# solicitar un numero y calcule su factorial
factory = 1
numero = int(input("Introduce un numero:"))
for c in range(1,numero+1):
    factory*= c
print("El factorial del {numero} es: ", factory)