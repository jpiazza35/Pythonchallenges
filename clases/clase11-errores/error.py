'''
def dividir(a, b):
    if(b == 0):
        return None
    else:
        return a / b

print(dividir(8,3))
'''

def dividir(a, b):
    if(b == 0):
        nuevo_b = int(input('Nuevo B:\n'))
        return dividir(a,nuevo_b)
    else:
        return a / b

print(dividir(8,0))