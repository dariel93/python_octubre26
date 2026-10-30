import math

punto1=(3,4)
punto2=(7,6)
def distancia(punto1, punto2):
    return math.hypot(punto1[0]-punto2[0], punto1[1]-punto2[1])
print(distancia) 