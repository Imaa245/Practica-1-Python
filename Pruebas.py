inventario = {}

def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def mostrar_inventario():
    for nombre, cantidad in inventario.items():
        print(f"- {nombre}: {cantidad}")

while True:
    print("-" * 20)
    print("Gestión de inventario")
    print("-" * 20)
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("-" * 20)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        agregar_producto(nombre, cantidad)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre)
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")

print("-" * 20)
print("¡Gracias por usar el programa de gestión de inventario!")
print("-" * 20)