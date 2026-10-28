# suma de los 10 primeros numeros naturales del 1 al 10
suma = 0
limite = int(input("Introduce un numero:"))
for c in range(1,limite+1):
    suma+= c
print("La suma de los numeros es: ", suma)