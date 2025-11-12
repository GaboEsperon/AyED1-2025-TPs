"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comporta-
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena utilizando rebanadas (slicing).

    Parámetros:
        cadena (str): cadena original
        posicion (int): índice inicial (0-based)
        cantidad (int): cantidad de caracteres a extraer

    Retorna:
        str: subcadena extraída, o cadena vacía si los parámetros están fuera de rango
    """
    if posicion < 0 or cantidad < 0 or posicion >= len(cadena):
        return ""
    return cadena[posicion : posicion + cantidad]


def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Extrae una subcadena sin utilizar rebanadas (usa un bucle for).
    """
    subcadena = ""
    if posicion < 0 or cantidad < 0 or posicion >= len(cadena):
        return subcadena

    for i in range(posicion, min(posicion + cantidad, len(cadena))):
        subcadena += cadena[i]
    return subcadena


def mostrar_opciones(lista: list[str]) -> None:
    """Muestra las opciones del menú numeradas."""
    print("\n--- MENÚ ---")
    for count, item in enumerate(lista, 1):
        print(f"{count} - {item}")
    print()


def menu():
    """
    Menú interactivo para extraer subcadenas con o sin rebanadas.
    Permite ingresar la cadena, posición y cantidad, y muestra los resultados.
    """
    opciones = [
        "Extraer subcadena (usando rebanadas)",
        "Extraer subcadena (sin usar rebanadas)",
        "Salir",
    ]

    while True:
        mostrar_opciones(opciones)
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion in ("1", "2"):
            cadena = input("\nIntroduce la cadena: ")
            try:
                posicion = int(input("Introduce la posición de inicio: "))
                cantidad = int(input("Introduce la cantidad de caracteres a extraer: "))
            except ValueError:
                print("Error: la posición y cantidad deben ser números enteros.\n")
                continue

            if opcion == "1":
                resultado = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
                print(f"Resultado (con rebanadas): {resultado}")
            else:
                resultado = extraer_subcadena_sin_rebanadas(cadena, posicion, cantidad)
                print(f"Resultado (sin rebanadas): {resultado}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")


if __name__ == "__main__":
    menu()
