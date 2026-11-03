"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros 
  cuyo precio sea igual o inferior al introducido

Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
""" 


def menu():
    print("1.- Nuevo libro")
    print("2.- Mostrar todos")
    print("3.- Buscar por titulo")
    print("4.- Libros por precio maximo")
    print("5.- Salir")


libreria=[]

def buscar_titulo(titulo):   
    encontrado=False    
    for i in libros:
        if titulo.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print(f"Título: {i['titulo']} Autor: {i['autor']} Precio: {i['precio']}")
            encontrado= True
            break
    if not encontrado:
        print("Libro no encontrado")
    return encontrado

opcion_elegida=0
while opcion_elegida!=5 :
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            titulo = input("Introduce el titulo del libro: ")
            precio = float(input("Introduce el Precio: "))
            autor = input("Introduce el autor del libro: ")
            libro = {"titulo":titulo, "precio": precio, "autor":autor}
            if not buscar_titulo(titulo):
                libreria.append(libro)
            else:
                print("El libro ya se encuentra")
        case 2:
            for libro in libreria:
                print(libro["titulo"])
        case 3:
            titulo = input("Introduce el titulo buscado: ")
            encontrado = False

            for libro in libreria:
                if libro["titulo"].lower() == titulo.lower():
                    print("Titulo:", libro["titulo"])
                    print("Autor:", libro["autor"])
                    print("Precio:", libro["precio"])
                    encontrado = True
                    break

            if not encontrado:
                print("No se ha encontrado ningún libro con ese título.")
        case 4:
            precio = float(input("Introduce el Precio Maximo: "))
            for libro in libreria:
                if libro["precio"] <= precio:
                    print(libro["titulo"])
        case 5:
            print("Fin del programa!")
        case _:
            print("Opción no válida")




"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""
libros=[]
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Nuevo libro")
    print("2 - Mostrar todos")
    print("3 - Buscar por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
def titulos():
    print("Títulos de los libros:")
    for lib in libros:
        print(f"Título: {lib["titulo"]} precio:{lib["precio"]}")
def buscar_titulo(titulo):   
    encontrado=False    
    for i in libros:
        if titulo.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print(f"Título: {i['titulo']} Autor: {i['autor']} Precio: {i['precio']}")
            encontrado= True
            break
    if not encontrado:
        print("Libro no encontrado")
    return encontrado
def nuevo_libro():
	titulo = input("Título: ")
	autor = input("Autor: ")
	try:
		precio = float(input("Precio: "))
	except ValueError:
		print("Precio no válido. No se agregó el libro.")
		return
	if not buscar_titulo(titulo):
		libros.append({"titulo": titulo, "autor": autor, "precio": precio})
		print("Libro agregado.")
	else:
		print("Libro repetido, no se agregó")
def libros_por_precio_maximo(max_precio):  
    titulos = [n["titulo"] for n in libros if n["precio"]<=max_precio]    
    if len(titulos)>0:
        print(f"Libros con precio <= {max_precio}:")
        for j in titulos:
            print(j)  
    else:
        print("No hay libros con ese precio o inferior.")
opcion="0"    
while opcion!="5":
	mostrar_menu()
	opcion=input("Elige una opción: ")
	if opcion == "1":
		nuevo_libro()
	elif opcion == "2":
		titulos()
	elif opcion == "3":
		buscar=input("Introduce el titulo del libro que quieres buscar: ")
		buscar_titulo(buscar)
	elif opcion == "4":
		try:
			max_precio = float(input("Precio máximo: "))
			libros_por_precio_maximo(max_precio)
		except ValueError:
			print("Precio no válido.")
	elif opcion == "5":
		print("Saliendo del programa...")
	else:
		print("Opción no válida. Intenta de nuevo.") 

