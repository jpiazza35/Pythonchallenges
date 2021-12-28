## en base a un pedido de ingreso de frase , hacer un algoritmo  que cuente cuantas palabras ingreso 

palabra = str(input("Por favor ingrese la frase: "))

contador = 0

for palabra in palabra.split():
    contador += 1

print("la cantidad de palabras es de {}".format(contador))