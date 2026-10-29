lista = [4,1,8,2,11]

# Solucion 1        
for n in lista:
    if n % 2 == 0:
        print(n)

# Solucion 2        
lista_pares = [n for n in lista if n % 2 == 0]
print(lista_pares)