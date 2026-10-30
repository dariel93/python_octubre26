import math

#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas

coordenadas = []
cercanas = []
resp = "s"
while(resp=="s" or resp=="S"):
    try:
        cordenada_x = float(input("Introduce una Coordenada X de la tienda:"))
        cordenada_y = float(input("Introduce una Coordenada Y de la tienda:"))
        coordenadas.append((cordenada_x, cordenada_y))
        resp=input("Desea introducir una nueva coordenada (s/n)? ")
    except ValueError:
        print("No es un valor flotante, vuelva a intentarlo")
        
#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición

ubicacion = (
    float(input("Introduce una Coordenada X: ")),
    float(input("Introduce una Coordenada Y: "))
)

punto_cercano = coordenadas[0]
distancia_minima = math.hypot(
    coordenadas[0][0] - ubicacion[0],
    coordenadas[0][1] - ubicacion[1]
)

for punto in coordenadas:
    distancia = math.hypot(
        punto[0] - ubicacion[0],
        punto[1] - ubicacion[1]
    )

    if distancia < distancia_minima:
        distancia_minima = distancia
        punto_cercano = punto

print(f"La tienda más cercana a {ubicacion} es {punto_cercano}")





