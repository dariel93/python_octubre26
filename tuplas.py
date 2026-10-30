# Funcion que haga lka tarea indicada arriba, pero devolviendo el rwesuyltado como una tupla

numeros = [4,3,7,8,7,9,2]

def obtener_aprobados():
    return tuple([n+1 for n in numeros if n>=5])

print(obtener_aprobados)

nombre=input("Nombre:")
apellidos=input("Nombre:")
datos=(nombre,apellidos)
print(datos)