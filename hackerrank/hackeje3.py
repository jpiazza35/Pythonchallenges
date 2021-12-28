##https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.
'''
def mutate_string(string,position,character):
    new_string = ""  ##genero un string vacio
    lista = list(string) ##convierto el string de parametro en lista
    lista[position] = character  ##remplazo el valor en la lista y luego la barro generando un nuevo string
    for elem in lista:
        new_string += elem

    return new_string

print(mutate_string("holamundo", 3,"s"))