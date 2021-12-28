'''
Añade al diccionario las claves perro, tigre y mono
 con sus respectivos valores dog, tiger y monkey
Modificá las claves elefante y delfin con los valores elephant y dolphin respectivamente
Por último elimina del dict las claves dolphin y cat
animales = {"elefante": "", "delfin": ""}

'''
animales = {"elefante": "", "delfin": ""}
animales['perro'] = 'dog'
animales['tigre'] = 'tiger'
animales['mono'] = 'monkey'
animales['elefante'] = 'elephant'
animales['delfin'] = 'dolphin'

animales.pop('delfin')


print(animales)


lista_de_diccionarios = [
    {"id": 15, "gender": "male"},
    {"id": 15, "gender": "male"},
    {"id": 15, "gender": "female"},
    {"id": 15, "gender": "trans"}
]

generos = set() ##generamos un conjunto para evitar tanta logica, queremos que nos diga cuantos generos distintos tenemos en toda la lista

for personas in lista_de_diccionarios:
    generos.add(personas["gender"])

print(generos)