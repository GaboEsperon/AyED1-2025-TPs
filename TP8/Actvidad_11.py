"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

def contar_vocales(palabra: str) -> dict[str, int]:
    """
    Cuenta cuántas vocales contiene una palabra y la cantidad de cada una.

    Parameters:
        palabra (str): La palabra en la que se contarán las vocales.

    Returns:
        dict[str, int]: Diccionario con la cantidad de cada vocal encontrada.
    """
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in palabra.lower():
        if letra in conteo:
            conteo[letra] += 1

    return conteo


def procesar_frase_vocales(frase: str) -> None:
    """
    Procesa una frase, contando las vocales en cada palabra e imprimiendo el resultado.

    Parameters:
        frase (str): La frase a analizar.
    """
    palabras = frase.split()

    for palabra in palabras:
        resultado = contar_vocales(palabra)
        print(f"Palabra: {palabra} - Vocales: {resultado}")


def main():
    """
    Lee una frase y llama a la función contar_vocales para cada palabra.
    """
    frase = input("Ingrese una frase: ")
    procesar_frase_vocales(frase)


if __name__ == "__main__":
    main()