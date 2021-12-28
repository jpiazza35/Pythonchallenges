'''
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
'''

#show main menu
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. lista del 0 al 10 inclusive")
print ("2. Lista de numeros completos del -10 al 0 ")
print ("3. lista de numeros PARES del 0 al 20")
print ("4. Lista de numeros IMPARES entre -20 y 0")
print ("5. Lista de numeros multiples de 5 del 0 al 50")
print ("6. EXIT")

print (30 * '-')

option=int(input("Por favor ingrese una opcion para generar una lista [default: 1]: ") or 1)
while(option >= 1 and option <= 5):
    if(option == 1):
        lista =list(range(0,11,1))
        print("Usted eligio la opcion {}, la lista es :\n {}".format(option, lista))
        option=int(input("Por favor ingrese una nueva opcion 6 para salir: ") or 1)
    elif(option == 2):
        lista = list(range(-10,1,1))
        print("Usted eligio la opcion {}, la lista es :\n {}".format(option, lista))
        option=int(input("Por favor ingrese una nueva opcion 6 para salir: ") or 2)
    elif(option == 3):
        lista = list(range(0,21,2))
        print("Usted eligio la opcion {}, la lista es :\n {}".format(option, lista))
        option=int(input("Por favor ingrese una nueva opcion 6 para salir: ") or 3)
    elif(option == 4):
        lista = list(range(-20,1,3))
        print("Usted eligio la opcion {}, la lista es :\n {}".format(option, lista))
        option=int(input("Por favor ingrese una nueva opcion 6 para salir: ") or 4)
    elif(option == 5):
        lista = list(range(0,51,5))
        print("Usted eligio la opcion {}, la lista es :\n {}".format(option, lista))
        option=int(input("Por favor ingrese una nueva opcion o 6 para salir: ") or 5)
    elif(option == 6):
        print("gracias por jugar")
        break

    