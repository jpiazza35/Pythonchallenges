'''
4) Realiza una función llamada intermedio()
 que a partir de dos números, devuelva su punto intermedio:

🖐 Ayuda: El número intermedio de dos números corresponde 
a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24
'''
def intermedio(number1,number2):
    punto_medio = (number1 + number2)//2

    return punto_medio

print(intermedio(-12,24))

