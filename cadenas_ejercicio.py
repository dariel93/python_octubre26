temperaturas="12.4, 23.6, 17.8, 3.5, 29.0, 11.6"
# Cual es la temperatura mas baja

baja = float(temperaturas.split(",")[0])

for temp in temperaturas.split(","):
    temp = float(temp)
    if temp < baja:
        baja = temp

print(f"La temperatura mas baja es {baja}")

# Corta

print("La temperatura mas baja es: ", min([float(t) for t in temperaturas.split(",")]))