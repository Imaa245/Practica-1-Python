"""
Cree un programa que dada una lista de números imprima sólo los que son pares.
Nota: utilice la sentencia continue donde haga falta.

Modifique el ejercicio de arriba para que dada la lista de número genere dos nuevas listas, una
con los número pares y otras con los que son impares. Imprima las listas al terminar de
procesarlas.
"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for num in lista:
    if num%2 != 0:
        impares.append(num)
        continue
    print (num)
    pares.append(num)
print ("Numeros pares: ")
for num in pares:
    print (num)
print ("Numeros impares: ")
for num in impares:
    print (num)

