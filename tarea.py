# Solicitamos al usuario que introduzca un lenguaje y le mostramos 
#todos los cursos relacionados con ese lenguaje
cursos = "Java Basico, Python principiante, C, Java Avanzado, Java Enterprise, cobol"
lista_cursos=cursos.split(",")
lenguaje = input("Que lenguaje te interesa?: ")
for curso in lista_cursos:
   if lenguaje.lower() in curso.lower().split(" "):
        print(curso)