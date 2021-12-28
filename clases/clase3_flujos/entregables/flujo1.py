'''
1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''


import sys

#show main menu
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Result of sum of both numbers")
print ("2. Result of the subtraction of both numbers ")
print ("3. multiplication among both values")
print ("4. Exit")
print (30 * '-')

numero = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el primer numero:"))
option = int(input("please choose one of the options menu[1-4]:"))



if(option > 4 or option < 1):
    print("the value that you entered is not correct, please write from 1 to 4")
elif(option == 1):
    suma = numero + numero2
    print("la suma entre {} y {} da como resultado: {}".format(numero,numero2,suma))
elif(option == 2):
    resta = numero - numero2
    print("la resta entre {} y {} da como resultado: {}".format(numero,numero2,resta))
elif(option == 3):
    multi = numero * numero2
    print("la multiplicacion entre {} y {} da como resultado: {}".format(numero,numero2,multi))
elif(option == 4):
    print("saliendo del programa")
    sys.exit()
else:
    print("You did not introduce a valid option , please retry")