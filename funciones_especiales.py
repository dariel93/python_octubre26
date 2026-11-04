numeros = [1,8,3,-4,9,-2,-11,16]
positivos = list(filter(lambda n:n>0, numeros))
cuadrados=list(map(lambda n:n**2, positivos))
print(positivos)
print(cuadrados)
# Calcule la suma de los cuadrados de todos los positivos