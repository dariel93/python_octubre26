# sustituyte cada elemento de la lista por su cuadrado y luego imprimes la lista entera 
# y la suma de todo su contenido

lista = [4,1,8,2,11]
index = 0
for n in lista:
    lista[index]= n**2
    index+=1
print(lista)
sum = 0
for n in lista:
    sum+=n
print(f"La suma de los datos de la lista {lista} es {sum}")


# Solucion 2

for i, n in enumerate(lista):
    lista[i]= n**2
print(lista)