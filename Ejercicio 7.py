"""
Escribe un programa que tome una lista de números enteros como entrada del usuario.
Luego, convierte cada número en la lista a string y únelos en una sola cadena,
separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
de 3 de la cadena final.
"""

lista = []
while True:
    num = int(input('Ingrese un numero entero (12345 para terminar): '))
    if (num == 12345):
        break
    lista.append(num)

cadena = ""
for num in lista:
    if ((num % 3) != 0):
        cadena += str(num) + " - "
cadena = cadena[:-3]

print(f"Cadena final: {cadena}")