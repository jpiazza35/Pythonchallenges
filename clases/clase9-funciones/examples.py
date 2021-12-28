
numero_elegido = int(input("ingresa un numero:"))
def par_o_impar(number):
    if(number%2 ==0):
        return "es par"
    elif(number%2 !=0):
        return "es Impar"
    else:
        return "el dato ingresado no es correcto"

print(par_o_impar(numero_elegido))
    
def numeros_divisibles(lista, numero):
    for i , elem in enumerate(lista):
        if(i == len(lista)-1):
            if(elem % numero == 0):
                return("Todos los valores son divisibles")
        if(elem % numero == 0):
            continue
        else:
            return f"hay valores que no son divisibles por {numero}"

print(numeros_divisibles([2,4,7,8], 2))
