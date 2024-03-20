"""
Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
"""

grados_celsius = int (input ("Ingrese una temperatura en grados Celsius para convertir: "))
grados_f = (grados_celsius * 9/5) + 32
print (f"Temperatura {grados_celsius}° a Fahrenheit: {grados_f}°F")