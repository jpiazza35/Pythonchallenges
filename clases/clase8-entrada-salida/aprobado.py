'''
Crear un script llamado aprobado.py que realice lo siguiente:

Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
Si ambos valores son mayores o igual a 7 devolver imprimir “Promocionado”
Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”

'''

import sys


if len(sys.argv) == 3:
    nota1 = int(sys.argv[1])
    nota2 = int(sys.argv[2])
    if(nota1 <0 and nota1>10 and nota2<0 and nota2>10):
        print("usted ingreso un numero erroneo, ingrese valores entre 0 y 10")
    else:
        if(nota1>=7 and nota2>=7):
            print("PROMOCIONADO ya que sus notas fueron {} y {}".format(sys.argv[1], sys.argv[2]))
        elif(nota1>=4 and nota2>=4):
            print("Aprobado pero debe rendir el final ya que se saco {} y {}".format(sys.argv[1], sys.argv[2]))
        elif(nota1>=4 and nota2<4):
            print("Aprobo el primer examen con {} pero el segundo desaprobo con {}".format(sys.argv[1], sys.argv[2]))
        elif(nota1<4 and nota2>4):
            print("Aprobo el segundo examen con {} pero el primero lo desaprobo con {}".format(sys.argv[2],sys.argv[1]))
        else:
            print("estudia por que no aprobaste ningun ejercicio")
else:
    print("ustede no ingreso numeros correctos")