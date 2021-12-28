'''
4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
'''
numeros = int(input("Por favor ingrese la cantidad de numeros que quiere introducir:"))
lista = list(range(numeros))
nueva_lista = []
suma = 0

for n in lista: 
    suma += float(input("Ingrese un numero a sumar:") )
print("Se introdujo {} numeros , en total se ha sumado la cantidad de {}, y una media de {}".format(numeros, suma, suma/numeros))

