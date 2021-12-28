
'''
6) Dadas dos listas, debes generar una tercera con todos los 
elementos que se repitan en ellas, 
pero no debe repetirse ningún elemento en la nueva lista:
Respuesta
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
'''

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista3 = []

for letra in lista_1:
    for letra2 in lista_2:
        if(letra in lista3):
            continue
        elif(letra == letra2):
            lista3.append(letra)
print("en base a la lista 1 : {}\n y la lista 2: {}\n estas son las letras que se repiten {}".format(lista_1,lista_2, lista3))

