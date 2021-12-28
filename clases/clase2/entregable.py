#A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. 
#Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:
#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
'''
Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4
'''
nota_1 = float(input("ingrese la nota1: ") or "10")
nota_1_por = float(input("ingrese el valor Porcentual de la nota 1: ") or "15") / 100
nota_2 = float(input("ingrese la nota 2: ") or "7")
nota_2_por = float(input("ingrese el valor Porcentual de la nota 2: ") or "35") / 100
nota_3 = float(input("Ingrese la nota 3: ") or "4" )
nota_3_por = float(input("ingrese el valor Porcentual de la nota 3: ") or "50") / 100




nota_media = nota_1 * nota_1_por + nota_2 * nota_2_por + nota_3 * nota_3_por

print("""Dado de que la nota_1 fue {} y tiene un valor porcentual del {}
      y que la nota2 fue de {} y tiene un valor porcentual del {} 
      y la nota 3 fue de {}, y tiene un valor porcentual del {}, la media es {}""".format(nota_1,nota_1_por,nota_2,nota_2_por,nota_3, nota_3_por,nota_media))

