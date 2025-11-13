"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con-
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
def gestionar_eliminaciones(conjunto: set) -> None:
    """
    Permite eliminar números de un conjunto de manera interactiva.
    Muestra el conjunto actualizado tras cada eliminación y finaliza al ingresar -1.

    Parameters:
        conjunto (set): Conjunto inicial de números enteros.
    """
    while True:
        try:
            num = int(input("Ingrese el número que desea eliminar (-1 para salir): "))

            if num == -1:
                print("Proceso finalizado.")
                break

            conjunto.remove(num)
            print(f"Número {num} eliminado. Conjunto actualizado: {conjunto}")

            if not conjunto:
                print("El conjunto ha quedado vacío.")
                break

        except KeyError:
            print(f"El número {num} no existe en el conjunto actual: {conjunto}")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")


def main():
    """
    Programa principal: inicializa el conjunto y gestiona las eliminaciones.
    """
    numeros = set(range(10))
    print(f"Conjunto inicial: {numeros}")
    gestionar_eliminaciones(numeros)


if __name__ == "__main__":
    main()
