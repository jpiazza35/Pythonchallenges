ciudades = ["villa maria", "Cordoba", "calchin", "Villa Nueva", "Posee"]

ciudad = str(input("Ingrese la ciudad para ver su ubicacion en la lista:" ))

longitud = len(ciudades)

if(ciudad in ciudades):
    posicion = ciudades.index(ciudad) + 1   
    if(posicion > (longitud+1)/2):
        print("la ciudad de {} esta en la segunda mitad de la lista".format(ciudad))
    elif(posicion < (longitud+1)/2):
        print("la ciudad de {} esta en la primer mitad de la lista".format(ciudad))
    elif(posicion == (longitud+1)/2):
        print("la ciudad esta en la mitad de la lista")
    elif(ciudades.__contains__(ciudad) == False):
        print("la ciudad ingresada no se encuentra en la lista")
else:
    print("La ciudad no se encuentra en la lista")



texto2="gordon pepe&yyy"
texto2.capitalize()
texto2.replace('&','')
print(texto2)

    
