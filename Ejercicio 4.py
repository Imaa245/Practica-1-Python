"""
Cree un programa que dada una lista de números imprima sólo los que son pares.
Nota: utilice la sentencia continue donde haga falta.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in lista:
    if num%2 != 0:
        continue
    print (num)