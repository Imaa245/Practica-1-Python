"""
Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y
muestre cuántos años le faltan para alcanzar los 100 años.
"""

edad = int(input("Ingrese su edad: "))
if edad >= 0  and edad <= 100:
    print (f"Te faltan {100 - edad} años para llegar a los 100")