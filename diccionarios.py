"""ciudades = {}
ciudades["Madrid"] = 3200000
ciudades["Getafe"] = 1000000
ciudades["Alcoron"] = 1200000
ciudades["Avila"] = 1300000

del(ciudades["Avila"])
for k,v in ciudades.items():
    print(f"La ciudad {k} tiene {v} habitantes")"""

lista_reproduccion=[
    {"titulo":"cancion inventada", "duracion": 3.20, "valoracion":4},
    {"titulo":"Bohemia Rapsody", "duracion": 5.40, "valoracion":10},
    {"titulo":"Green summer", "duracion": 4.10, "valoracion":7}
]

#Se solicita la introducción de los datos de una nueva canción.
#si la canción no existe, se agrega a la lista. Si ya existe no se hace nada
#Después, el programa muestra todos los titulos almacenados
#y la valoración media de toda la lista de reproducción

titulo = input("Introduce el titulo de la cancion: ")
duracion = float(input("Introduce la duracion: "))
valoracion = int(input("Introduce la valoracion: "))

cancion = {"titulo":titulo, "duracion": duracion, "valoracion":valoracion}

if cancion["titulo"] not in [cancion["titulo"] for cancion in lista_reproduccion]:
    lista_reproduccion.append(cancion)
    suma=0
    for c in lista_reproduccion:
        suma+=c["valoracion"]
        print(c["titulo"])
    print(f"Valoracion media {suma/len(lista_reproduccion)}")
else:
    print(f"La cancion '{cancion["titulo"]}' ya se encuentra")


# Solucion 2

def comprobar_cancion(titulo):
    return titulo in [can["titulo"] for can in lista_reproduccion]

if not comprobar_cancion(titulo):
    lista_reproduccion.append(cancion)
else:
    print("La canción no fue añadida")
suma=0
for c in lista_reproduccion:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"Valoración media {suma/len(lista_reproduccion)}") 
    
        


    





