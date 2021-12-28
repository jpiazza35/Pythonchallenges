'''
A partir de una lista realizar las siguientes tareas sin modificar la lista original:

1.Borrar los elementos duplicados
2.Ordenar la lista de mayor a menor
3.Eliminar todos los números impares
4.Realizar una suma de todos los números que quedan
5.Añadir como primer elemento de la lista la suma realizada
6. Devolver la lista modificada
7. Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

Nota:
Recorda que para sumar todos los números de una lista podes usar sum

'''

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12,17]
lista2=set(lista)
lista3=list(lista2)
lista3.sort(reverse=True)
print(lista3)
for impar in lista3[:]: ##>>> hago una copia de la lista

    if(impar%2 !=0):
        print(impar)
        lista3.remove(impar)
        continue
    

print("esta es la lista sin impares", lista3)

lista3.append(sum(lista3))

print("la nueva lista es  {} ".format(lista3))
suma_desde_segundo = 0
for f in lista3[1:]:
    suma_desde_segundo = suma_desde_segundo + f
print(suma_desde_segundo)

if(lista3[0] == suma_desde_segundo):
    print("son iguales")
else:
    print("el primer numero de la lista y la suma del segundo al final , no da lo mismo.")