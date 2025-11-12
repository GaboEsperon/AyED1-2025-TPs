"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""
def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres.
    Versión con ciclos tradicionales (for + append).
    """
    palabras = frase.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return " ".join(resultado)


def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres.
    Versión usando comprensión de listas.
    """
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    Devuelve una cadena con las palabras de la frase que tienen N o más caracteres.
    Versión usando la función filter() con una lambda.
    """
    return " ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


def main():
    """
    Programa de prueba para verificar el comportamiento de las tres funciones.
    """
    frase = "Un mago nunca llega tarde, ni pronto; llega exactamente cuando se lo propone."
    n = 5

    print(f"Frase original: {frase}")
    print(f"Filtrando palabras con {n} o más caracteres...\n")

    resultado1 = filtrar_palabras_ciclos(frase, n)
    resultado2 = filtrar_palabras_comprension(frase, n)
    resultado3 = filtrar_palabras_filter(frase, n)

    print("Versión con ciclos:       ", resultado1)
    print("Versión con comprensión:  ", resultado2)
    print("Versión con filter():     ", resultado3)


if __name__ == "__main__":
    main()