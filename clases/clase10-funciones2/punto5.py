'''
5) Realizá una función llamada recortar() 
que reciba tres parámetros.
El primero es el número a recortar,
el segundo es el límite inferior y el
tercero el límite superior.
La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10

'''

def recortar(limite_inferior,limite_sup, numero):
    limite_sup = limite_sup + 1
    lista_x = list(range(limite_inferior, limite_sup))
    print(lista_x)
    if(numero < min(lista_x)):
        return min(lista_x)
    elif(numero > max(lista_x)):
        return max(lista_x)
    else:
        return numero

print(recortar(2,10,10))
