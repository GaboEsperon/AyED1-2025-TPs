"""
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""
import random as rn
from collections import Counter

def generar_lista_aleatoria(n: int) -> list[int]:
    """Genera una lista de longitud n con números aleatorios entre 1 y 100."""
    return [rn.randint(1, 100) for _ in range(n)]


def contiene_repetidos(lista: list[int]) -> bool:
    """Verifica si la lista contiene elementos repetidos de forma eficiente."""
    return len(set(lista)) != len(lista)


def lista_elementos_unicos(lista: list[int]) -> list[int]:
    """Devuelve los elementos que aparecen solo una vez en la lista."""
    contador = Counter(lista)
    return [num for num, count in contador.items() if count == 1]


def mostrar_opciones() -> None:
    """Muestra las opciones disponibles en el menú."""
    print("\nOpciones:")
    print("1 - Generar una lista de números aleatorios")
    print("2 - Verificar si la lista contiene elementos repetidos")
    print("3 - Obtener una lista con elementos únicos")
    print("4 - Salir")


def menu() -> None:
    """Menú principal para interactuar con las funciones de la lista."""
    lista = []

    while True:
        mostrar_opciones()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            while True:
                try:
                    num = int(input("Ingrese la longitud de la lista: "))
                    if num > 0:
                        break
                    print("Ingrese un número positivo mayor que 0.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número entero.")

            lista = generar_lista_aleatoria(num)
            print(f"Lista generada: {lista}")

        elif opcion == "2":
            if not lista:
                print("No hay ninguna lista generada. Primero genere una lista.")
            else:
                if contiene_repetidos(lista):
                    print("La lista contiene elementos repetidos.")
                else:
                    print("Todos los elementos de la lista son únicos.")

        elif opcion == "3":
            if not lista:
                print("No se ha generado ninguna lista. Primero genere una lista.")
            else:
                unica = lista_elementos_unicos(lista)
                print(f"Lista con elementos únicos: {unica}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
