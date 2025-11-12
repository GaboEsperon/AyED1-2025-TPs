"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
"""
import string as st

def ordenar_palabras_por_longitud(cadena: str) -> str:
    """
    Ordena las palabras de una cadena según su longitud, ignorando los signos de puntuación
    para calcular la longitud pero conservándolos en el resultado final.

    Parámetros:
        cadena (str): texto de entrada, con palabras separadas por espacios.

    Retorna:
        str: cadena con las palabras ordenadas por longitud.

    """

    signos = set(st.punctuation + "¿¡")


    palabras = cadena.split()
    palabras_ordenadas = sorted(
        palabras,
        key=lambda palabra: len("".join(ch for ch in palabra if ch not in signos))
    )

    return " ".join(palabras_ordenadas)


def main():
    """
    Programa de prueba con una frase de ejemplo
    """
    frase = "La Fuerza estará contigo, siempre."
    print(f"Frase original:\n{frase}\n")

    resultado = ordenar_palabras_por_longitud(frase)
    print(f"Palabras ordenadas por longitud:\n{resultado}")


if __name__ == "__main__":
    main()
