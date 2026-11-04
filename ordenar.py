lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista, reverse=True)
print(lista_ordenada)

nombres=["bicicleta", "oro", "casa", "martillo"]
print(sorted(nombres))

# Ordenacion personalizada, por ejemplo por numero de caracteres
print(sorted(nombres, key=lambda e:len(e)))
print(sorted(nombres, key=lambda e:len(e), reverse=True))

# De la lista de numeros , imprime el mayor
print(max(lista))
# Imprime el menor de la lista de nombres
print(min(nombres))
# Imprime el que tiene menos caracteres
print(min(nombres, key=lambda e:len(e)))
