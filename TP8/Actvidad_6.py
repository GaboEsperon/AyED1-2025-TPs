"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""
import re

def filtrar_y_ordenar_frase(frase: str) -> str:
    """
    Procesa una frase eliminando palabras repetidas y signos de puntuación.
    Devuelve las palabras únicas ordenadas por longitud (y alfabéticamente en caso de empate).

    Parameters:
        frase (str): Frase ingresada por el usuario, con posibles repeticiones y puntuación.

    Returns:
        str: Palabras únicas ordenadas por longitud y luego alfabéticamente, separadas por espacios.
    """
    # Eliminar signos de puntuación y pasar a minúsculas
    frase_limpia = re.sub(r'[^\w\s]', '', frase.lower())

    # Dividir en palabras y eliminar duplicados
    palabras_unicas = set(frase_limpia.split())

    # Ordenar por longitud y alfabéticamente
    palabras_ordenadas = sorted(palabras_unicas, key=lambda x: (len(x), x))

    return ' '.join(palabras_ordenadas)


def main():
    """
    Programa principal para ingresar una frase y mostrarla procesada.
    """
    frase_usuario = input("Ingrese una frase: ").strip()
    resultado = filtrar_y_ordenar_frase(frase_usuario)
    print("Palabras procesadas:", resultado)


if __name__ == "__main__":
    main()
