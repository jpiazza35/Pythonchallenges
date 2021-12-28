lista1 = [1,12,123]
lista2 = ["bye", "ciao", "Agur", "Adieu"]


lista1.append(1234)
lista1.append("Hola")

lista2.append("Adios")
lista2.append(1234)

lista3 = lista1[0:2]
lista4 = lista2[1:3]
lista5 = lista4 + lista3

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print("lista5",lista5)