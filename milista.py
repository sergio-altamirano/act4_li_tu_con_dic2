# Ejemplo de uso de listas
misnovias=["made", "vanesa", "keyla"]
misnumeros=[69, 13, 4]
# Mostramos mis novias
print(misnovias)

# Mostramos mis numeros
print(misnumeros)
print("---Accediendo a los datos de la lista---")
print(misnovias[0])

if "made" in misnovias:
  print("Made es mi novia")
else:
  print("esa persona no es mi novia")

print("Numero de novias")
nnovias=len(misnovias)
print(f"Numero de novias: {nnovias}")

posicion=0
print("Ciclo for en listas")
for medianaranja in misnovias:
  print(posicion," ",medianaranja)
  posicion=posicion+1