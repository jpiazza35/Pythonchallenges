'''
2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
debe repetirse el proceso hasta que lo introduzca correctamente.

'''

numero = int(input("Introduzca un numero impar:"))

while(numero != ""):
    try:
        if(numero == 0):
            numero = int(input("por favor ingrese un numero superior a 0"))
            continue
        elif(numero%2 == 0):
            numero = int(input("vuelva ingresar el valor , ya que el numero no es impar"))
            continue
        else:
            print("excelente , ingreso {} , lo cual es un numero impar!!".format(numero))
            break
    except ValueError:
        print("por favor ingrese")
