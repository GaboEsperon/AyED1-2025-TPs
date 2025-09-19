"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""
import random as rn

def generar_lista(n: int) -> list[int]:
    """Genera una lista de n números aleatorios entre 1 y 200."""
    return [rn.randint(1, 200) for _ in range(n)]


def eliminar_numeros(lista_principal: list[int], lista_eliminar: list[int]) -> list[int]:
    """Elimina de lista_principal todos los elementos que estén en lista_eliminar."""
    return [elem for elem in lista_principal if elem not in lista_eliminar]


def mostrar_menu() -> None:
    """Muestra las opciones disponibles en el programa."""
    print("\n--- Menú ---")
    print("1. Generar listas de números aleatorios")
    print("2. Eliminar números repetidos")
    print("3. Mostrar las listas")
    print("4. Salir")


def main() -> None:
    """Función principal que controla la interacción con el usuario."""
    lista_a: list[int] = []
    lista_b: list[int] = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            while True:
                try:
                    num = int(input("Ingrese la longitud de las listas: "))
                    if num > 0:
                        break
                    print("Ingrese un número mayor que 0.")
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número entero.")

            lista_a = generar_lista(num)
            lista_b = generar_lista(num)
            print("\nListas generadas exitosamente.")

        elif opcion == "2":
            if lista_a and lista_b:
                lista_a = eliminar_numeros(lista_a, lista_b)
                print("\nEliminación completada. Lista A actualizada.")
            else:
                print("\nPrimero genera las listas (opción 1).")

        elif opcion == "3":
            print("\nLista A:", lista_a)
            print("Lista B:", lista_b)

        elif opcion == "4":
            print("\nSaliendo del programa. ¡Adiós!")
            break

        else:
            print("\nOpción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
