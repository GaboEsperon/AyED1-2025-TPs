"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena de la cadena original utilizando rebanadas (slicing).

    Parámetros:
        cadena (str): cadena original
        posicion (int): índice inicial (0-based)
        cantidad (int): cantidad de caracteres a eliminar

    Retorna:
        str: cadena resultante tras eliminar la subcadena.
    """
    if posicion < 0 or cantidad < 0 or posicion >= len(cadena):
        return cadena  # no se elimina nada si los valores son inválidos
    return cadena[:posicion] + cadena[posicion + cantidad :]


def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena sin utilizar rebanadas.
    Recorre manualmente la cadena y omite los caracteres a eliminar.
    """
    if posicion < 0 or cantidad < 0 or posicion >= len(cadena):
        return cadena

    resultado = ""
    for i, caracter in enumerate(cadena):
        if i < posicion or i >= posicion + cantidad:
            resultado += caracter
    return resultado


def mostrar_opciones(lista: list[str]) -> None:
    """Muestra las opciones del menú numeradas."""
    print("\n--- MENÚ ---")
    for count, item in enumerate(lista, 1):
        print(f"{count} - {item}")
    print()


def menu():
    """
    Menú interactivo para eliminar subcadenas de una cadena con o sin rebanadas.
    Permite ingresar la cadena, posición y cantidad, y muestra el resultado.
    """
    opciones = [
        "Eliminar subcadena (usando rebanadas)",
        "Eliminar subcadena (sin usar rebanadas)",
        "Salir",
    ]

    while True:
        mostrar_opciones(opciones)
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion in ("1", "2"):
            cadena = input("\nIntroduce la cadena: ")
            try:
                posicion = int(input("Introduce la posición de inicio: "))
                cantidad = int(input("Introduce la cantidad de caracteres a eliminar: "))
            except ValueError:
                print("Error: la posición y cantidad deben ser números enteros.\n")
                continue

            if opcion == "1":
                resultado = eliminar_subcadena_rebanadas(cadena, posicion, cantidad)
                print(f"Resultado (con rebanadas): {resultado}")
            else:
                resultado = eliminar_subcadena_sin_rebanadas(cadena, posicion, cantidad)
                print(f"Resultado (sin rebanadas): {resultado}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")


if __name__ == "__main__":
    menu()
