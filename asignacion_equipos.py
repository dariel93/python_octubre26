# Alevin es 10 años y benjamin es 16
# Hacer un programna q nos solicite la edad y nos muestre a q grupo
# pertenece (el mas cercano a su edad) La edad debe estar entre 9 y 18 años

limite_inf, limite_sup, benjamin, alevin = 9,18,10,16
edad=int(input("Introduce una edad entre 9 y 18:"))
if edad<limite_inf or edad>limite_sup:
    print("La edad no es validas")
else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("Eres Benjamin")
    else:
        print("Eres Alevin")
