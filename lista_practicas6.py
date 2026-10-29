notas = []
aprobados = 0
sum = 0
total = 0

print("--------Elija una opcion---------")
print("#1. Añadir Nota")
print("#2. Mostrar notas extremas")
print("#3. Total de Aprobados")
print("#4. Nota Media")
print("#5. Mostrar todas")
print("#6. Salir")

while(True):
        
    opcion = int(input("Introduce un Opcion:"))
    
    if (opcion == 1):
        nota = int(input("Introduce una Nota:"))
        notas.append(nota)
        
    elif(opcion == 2):
        print(f"La nota mas alta es {max(notas)}")
        print(f"La nota mas baja es {min(notas)}")
        
    elif(opcion == 3):
        for n in notas:
            if n > 5:
                aprobados+=1
        print(f"El total de aprobados es", aprobados)
        
    elif(opcion == 4):
        
        for nota in notas:
            total +=1
            sum = sum + nota
        print(f"Has incorrido {total} notas, y la media es: {sum/total}")
            
    elif(opcion == 5):
        
        print(notas)
        
    elif(opcion == 6):
        break