"""
Implementa un programa que solicite al usuario que ingrese una lista de números.
Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
Nota: utilice la sentencia break cuando haga falta.
"""

numeros = []
while True:
    numero = int(input('Ingrese un numero (-1 para terminar): '))
    if (numero == -1):
        break
    numeros.append(numero)
print("Lista de números: ")
for numero in numeros:
    if (numero < 0):
        break
    print(numero)