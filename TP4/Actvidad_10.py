"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función.
"""
import re

def reemplazar_palabra(
    cadena: str, palabra_a_reemplazar: str, nueva_palabra: str, ignorar_mayusculas: bool = True
) -> tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa en la cadena por otra.

    Parámetros:
        cadena (str): texto original.
        palabra_a_reemplazar (str): palabra que se desea sustituir.
        nueva_palabra (str): palabra por la cual se reemplazará.
        ignorar_mayusculas (bool): si True, ignora diferencias de mayúsculas/minúsculas.

    Retorna:
        tuple[str, int]: cadena modificada y cantidad de reemplazos realizados.

    """
    flags = re.IGNORECASE if ignorar_mayusculas else 0
    patron = r"\b" + re.escape(palabra_a_reemplazar) + r"\b"

    nueva_cadena, cantidad = re.subn(patron, nueva_palabra, cadena, flags=flags)
    return nueva_cadena, cantidad


def main():
    """
    Programa de prueba: reemplaza palabras en una frase particular.
    """
    cadena_original = "El dragón duerme. El dragón sueña con fuego y destrucción."
    palabra_a_reemplazar = "dragón"
    nueva_palabra = "fénix"

    cadena_resultante, cantidad_reemplazos = reemplazar_palabra(
        cadena_original, palabra_a_reemplazar, nueva_palabra
    )

    print("Frase original:")
    print(cadena_original)
    print("\nFrase modificada:")
    print(cadena_resultante)
    print(f"\nCantidad de reemplazos realizados: {cantidad_reemplazos}")


if __name__ == "__main__":
    main()
