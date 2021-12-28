'''
3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:
 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. 
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

'''
list1 = list(range(0,101))
lista_impares = []
for numero in list1:
    if(numero%2 != 0):
        lista_impares.append(numero)

suma_valores_impares = sum(lista_impares)

print("La suma de valores impares del rango entre 0 a 100 es de {}".format(suma_valores_impares))



