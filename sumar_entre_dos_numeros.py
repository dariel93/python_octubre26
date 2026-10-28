# Solicita la introduccion de dos numeros y calcula  la suma de 
# todos los numeros comprendidos entre el menor y el mayor

# Solucion 1

numero1 = int(input("Introduce un numero X:"))
numero2 = int(input("Introduce un numero Y:"))
suma = 0
if numero1 < numero2:
    menor=numero1
    mayor=numero2
else:
    menor=numero2
    mayor=numero1
    
for c in range(menor,mayor+1):
    suma += c
        
print("La suma es: ", suma)  

# Solucion 2

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
    
for c in range(numero1,numero2+1):
    suma += c
    
print("La suma es: ", suma) 