numeros = [4,3,7,8,7,9,2]

# Dada esa lista de notas , crea otra lista 
# que contenga solo los aprobados. Ademas , le
# añadiras un punto extra a cada uno
# Finalmente se imprimer la lista
# [8,9,8,10]


"""def aprobados():
    aprobados = []
    for n in numeros:
        if n > 5:
            aprobados.append(n+1)
    return aprobados
            
print(aprobados())"""

aprobados = [n+1 for n in numeros if n>=5]