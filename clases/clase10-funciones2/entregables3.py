import math
from typing import Match
'''
 Realiza una función llamada area_rectangulo()
que devuelva el área del rectángulo a partir de una base 
y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura

'''
def area_rectangulo(base, altura):
    rectangulo = base * altura
    return rectangulo

area_de_rectangulo = area_rectangulo(base=15,altura=10)
print(f'El area del rectangulo es {area_de_rectangulo}')

'''
2) Realiza una función llamada area_circulo()
que devuelva el área de un círculo a partir de un radio.
Calcula el área de un círculo de 5 de radio

🖐Ayuda: El área de un círculo se obtiene al elevar el radio
 a dos y multiplicando el resultado por el número pi. 
 Puedes utilizar el valor 3.14159 como pi 
 o importarlo del módulo math.

'''
import math
def area_circulo(radio):
    PI = math.pi
    radio *= 2 
    resultado = radio * PI
    print(f'El radio es de {resultado}')

area_circulo(5)

