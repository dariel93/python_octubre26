notas_alumnos=[6,4,2,9,5,5,8,0,3.1,7.2]
# Indica cuantos alumnos han aprobado
# Dime la nota mas alta
 
aprobados = 0
for n in notas_alumnos:
    if n > 5:
        aprobados+=1

print(f"El total de aprobados es", aprobados)

mayor = notas_alumnos[0]
for n in notas_alumnos:
    if n > mayor:
        mayor = n

print(f"La nota mas alta es {mayor}")

""""Funciones"""
print(f"La nota mas alta es {max(notas_alumnos)}")
print(f"La nota mas baja es {min(notas_alumnos)}")
print(f"La notas en orden son {sorted(notas_alumnos, reverse=True)}")

        
    