'''
 Python program to
# demonstrate sets
  
# Same as {"a", "b", "c"}
myset = set(["a", "b", "c"])
print(myset)
  
# Adding element to the set
myset.add("d")
print(myset)
'''

grupo = set(["Miguel", "Blanca", "Mario", "Andrés"])

grupo.update(["Ana", "Ramón", "Marta", "Eric", "David"])
grupo.remove("Mario")
grupo.remove("Miguel")
print(grupo)


lista_paises = ["Argentina", "Brazil","Brazil"]
paises = set(lista_paises)

print("convirtio la lista a conjunto y remueve los repetidos",paises)

nombre = "pepe"
conjunto = set(nombre)
print("remueve los repetidos de nombre", conjunto)