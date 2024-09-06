arcoiris=("Azul", "verde", "rojo", "Amarillo")
print(arcoiris)

print("-- longitud del arcoiris --")
print(len(arcoiris))

animales= ("pantera", 20, "estructura", 1.7)
print(animales)
print("elementos de la tupla")
print(animales[2])

rateros= ("juan", "ana", "pedro")
y= list(rateros)
y[1]= "polainas"
x= tuple(Y)
print(x)
print("agregando elementos")
Nanimal=("boby", "chetos")
y= list(Nanimal)
y.append("tontolin")
otratupla= tuple(y)

print(otratupla)
print("uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)