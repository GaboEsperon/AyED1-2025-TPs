"""
Desarrollar cada una de las siguientes funciones y escribir un programa que per-
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun-
ción:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen-
tos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random as rnd


def cargar_numeros() -> list[int]:
    """
    Cargar una lista con números al azar de cuatro dígitos.
    La cantidad de elementos será un número al azar de dos dígitos.
    """
    numeros = []
    cantidad = rnd.randint(10, 99)
    for _ in range(cantidad):
        numeros.append(rnd.randint(1000, 9999))
    return numeros


def producto_de_numeros(lista: list[int]) -> int:
    """
    Calcular el producto de todos los elementos de la lista sin usar reduce.
    """
    if not lista:
        return False

    producto = 1
    for num in lista:
        producto *= num
    return producto


def eliminar_apariciones(lista: list[int], num: int) -> None:
    """
    Eliminar todas las apariciones de un valor en la lista.
    """
    while num in lista:
        lista.remove(num)


def capicua(lista: list[int]) -> bool:
    """
    Determinar si el contenido de una lista es capicúa.
    """
    return lista == lista[::-1]


def mostrar_opciones(lista: list[str]) -> None:
    """
    Muestra las opciones del menú.
    """
    for count, items in enumerate(lista, 1):
        print(f"{count} - {items}")


def menu() -> None:
    """
    Menú principal para interactuar con las funciones.
    """
    numeros = []

    while True:
        mostrar_opciones(opciones)
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            numeros = cargar_numeros()
            print("Números cargados:", numeros)
        elif opcion == "2":
            if numeros:
                producto = producto_de_numeros(numeros)
                print(f"El producto de los elementos de la lista es: {producto}")
            else:
                print("No hay números cargados.")
        elif opcion == "3":
            if numeros:
                try:
                    num = int(input("Ingrese el número que quiere eliminar: "))
                    eliminar_apariciones(numeros, num)
                    print(f"Lista después de eliminar {num}: {numeros}")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("No hay números cargados.")
        elif opcion == "4":
            if numeros:
                if capicua(numeros):
                    print("La lista es capicúa.")
                else:
                    print("La lista no es capicúa.")
            else:
                print("No hay números cargados.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


opciones = [
    "Generar una lista al azar.",
    "Calcular producto de los elementos de la lista.",
    "Borrar un valor de la lista.",
    "Ver si la lista es capicúa.",
    "Salir.",
]


menu()