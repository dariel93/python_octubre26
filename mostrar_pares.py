# Realiza un progrma que solicite la introduccion de un numero
# despues, muestra todos los pares entre 1 y ese numero

numero1 = int(input("Introduce un numero X:"))
for c in range(1,numero1+1):
    if c%2 == 0:    
        print(c, "es par")