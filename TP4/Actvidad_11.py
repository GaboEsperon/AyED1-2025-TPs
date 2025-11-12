def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Cuenta cuántas veces se encuentra una subcadena dentro de otra cadena,
    sin diferenciar mayúsculas y sin requerir que los caracteres sean consecutivos,
    pero sí en el mismo orden.

    Parámetros:
        cadena (str): texto donde se busca.
        subcadena (str): patrón a buscar.

    Retorna:
        int: cantidad de veces que la subcadena aparece como subsecuencia.

    """
    if not subcadena:
        return 0

    cadena = cadena.lower()
    subcadena = subcadena.lower()

    count = 0
    start = 0

    while start < len(cadena):
        temp = subcadena
        for i in range(start, len(cadena)):
            if cadena[i] == temp[0]:
                temp = temp[1:]
                if not temp:
                    count += 1
                    start = i + 1
                    break
        else:
            break
    return count


def main():
    """
    Programa de prueba con una frase particular.
    """
    cadena = (
        "En un agujero en el suelo vivía un hobbit. "
        "No un agujero sucio y húmedo, ni tampoco un agujero seco, "
        "sino un agujero-hobbit, y eso significa comodidad."
    )
    subcadena = "hobbit"

    cantidad = contar_subcadena(cadena, subcadena)
    print("Frase analizada:")
    print(cadena)
    print(f"\nSubcadena buscada: '{subcadena}'")
    print(f"Cantidad encontrada: {cantidad}")


if __name__ == "__main__":
    main()
