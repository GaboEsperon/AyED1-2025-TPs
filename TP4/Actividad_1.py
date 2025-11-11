"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""
def es_capicua(cadena: str) -> bool:
    """
    Determina si la cadena de caracteres es capicúa.
    """
    inicio = 0
    fin = len(cadena) - 1

    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1

    return True


def main():
    """
    Programa principal para verificar si una cadena es capicúa.
    """
    while True:
        cadena = input("Ingrese una cadena de caracteres: ")
        if cadena.lower() == "salir":
            print("Saliendo...")
            break
        if es_capicua(cadena):
            print(f"La cadena '{cadena}' es capicúa.")
        else:
            print(f"La cadena '{cadena}' no es capicúa.")


if __name__ == "__main__":
    main()