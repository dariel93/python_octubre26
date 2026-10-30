cursos = ["Java", "Python", "Typescript", "C", "Dart"]
# Pregunta al usuario que lenguaje de programcion quiere aprender,
# y el programa le indicara si existe un curso para ese lenguaje o no

# Solucion Larga

lenguaje = input("Que lenguaje de programacion desea aprender:")
encontrado = False
for curso in cursos:
    if curso==lenguaje:
        print("Tengo ese curso!")
        encontrado=True
        break
if not encontrado:
    print("Lo siento, no tengo ese curso")

# Solucion corta

lenguaje = input("Que lenguaje de programacion desea aprender:")
if lenguaje in cursos:
    print("Tengo ese curso!")
else:
    print("Lo siento, no tengo ese curso")
    
# Solucion de minusculas o mayusculas

lenguaje = input("Que lenguaje de programacion desea aprender:")
if lenguaje.lower() in [c.lower() for c in cursos]:
    print("Tengo ese curso!")
else:
    print("Lo siento, no tengo ese curso")