numero = int(input("Ingrese un numero: "))
intentos = 1

while(numero !=5):
    numero = int(input("ingrese otro numero: "))
    intentos += 1 
    if(intentos == 3 and numero!=5):
        print("se te acabaron los intentos") 
        break
else:
    print("Adivinaste")



fin = int(input("Ingrese el final: "))
contador = 0

while(contador < fin):
    contador += 1
    if(contador == 3):
        continue
    print(contador)

x = range(1, 10, 2)
for n in x:  ##recorre del 1 al 9 , ya que el 10 es exclusivo y va de 2 en 2
    print(n)
