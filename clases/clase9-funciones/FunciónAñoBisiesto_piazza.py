'''
>> Consigna: Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número debe indicar que se ingrese un número.

Sugerencia: En el formulario debe estar el print de pantalla de la consola con el ejercicio resuelto, como así también el código tipeado.

Información a tener en cuenta al realizar el entregable:

Se recuerda que los años bisiestos son múltiplos de 4, 
pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

'''

aneo = int(input('ingrese el año para saber si es Bisiesto: '))


def año_bisiesto(numero):
    if(numero % 400 == 0):
        print('El numero {} es bisiesto'.format(numero))
        numero = int(input('ingrese un nuevo año para saber si es Bisiesto: '))
    elif(numero % 4 == 0):
        if(numero % 100 == 0):
            print(f'el año {numero} no es bisiesto')
            numero = int(input('ingrese un nuevo año para saber si es Bisiesto: '))
        else:
            print('el año {} es bisiesto'.format(numero))
            numero = int(input('ingrese un nuevo año para saber si es Bisiesto: '))
            
    else:
        print(f'el año {numero} no es bisiesto')



año_bisiesto(aneo)