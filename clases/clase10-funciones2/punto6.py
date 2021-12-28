'''
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
 La primera con los números pares, y la segunda con los números impares:
  Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
'''
primer_numero = int(input("ingrese el primer valor de la lista: "))
segundo_numero = int(input("ingrese el segundo valor de la lista: "))
segundo_numero += 10
lista_generada0 = list(range(primer_numero,segundo_numero))

def separar(lista):
    lista_par = []
    lista_impar = []
    for numero in lista:
        if(numero % 2 == 0):
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    return f"la lista {lista} , ahora se formo en 2 listas , una par {lista_par} y esta otra impar {lista_impar}"

print(separar(lista_generada))

