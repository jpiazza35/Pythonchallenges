'''

Formatea los siguientes valores para mostrar el resultado indicado:

"Hola Mundo" → Alineado a la izquierda en 30 caracteres
"Hola Mundo" → Truncamiento en el sexto carácter (índice 5)
"Hola Mundo" → Alineamiento al centro en 10 caracteres con truncamiento en el tercer carácter (índice 2)
231875 → Formateo a hexadecimal en minúsculas
7887 → Formateo a binario

'''
saludo = "Hola Mundo"

print( "{:<30}".format(saludo))
print("{:.5}".format(saludo))
print("{:^10.3}".format(saludo))
print("{:X}".format(231875))
print("{:b}".format(7887))