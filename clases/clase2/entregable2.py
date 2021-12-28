'''
5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición:
 en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. 
 ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

matriz = [ 
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

'''


matriz = [ 
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]
 
matriz_nueva = []
for each in  matriz:
    lastvalue= sum(each)
    each.append(lastvalue)
    matriz_nueva.append(each)
    
print("la nueva matriz es {}".format(matriz_nueva))
