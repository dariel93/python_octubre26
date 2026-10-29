# Solicta una nota, despues otra, y asi sucesivamente hasta introducir un cero
#en ese momento, no pediras mas notas y mostrara la nota media de las introducidas hasta el momento

sum = 0
total = 0
nota = int(input("Introduce un nota:"))
while(nota>0):
    total +=1
    sum = sum + nota
    nota = int(input("Introduce un nota:"))
try:
    print(f"Has incorrido {total} notas, y la media es: {sum/total}")
except ZeroDivisionError:
    print("No hay notas")