# Al iniciar el programa se debe iniciar el siuiente menu
#1.Añadir Nota
#2.mostrar notas extremas
#3.total de aprobados
#4.nota media
#5.mostrar todas
#6.Salir 

# El usuario elige una opcion (1 a 6) y el programa le muestra o le pide
# los datos necesarios para llevar a cabo la accion. Despues vuelve a salir el menu
# y asi hasta que elija la opcion de salir

notas = []

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
        aprobados = 0
        for n in notas:
            if n >= 5:
                aprobados+=1
        print(f"El total de aprobados es", aprobados)
        
    elif(opcion == 4):
        suma = 0
        for nota in notas:
            suma += nota
            
        if(len(notas)==0):
            print("No hay notas")
        else:
            print(f"nota media {suma/len(notas)}")
            
    elif(opcion == 5):
        
        print(notas)
        
    elif(opcion == 6):
        break
        