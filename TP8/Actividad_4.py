"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio
"""
def unir_fichas(ficha_uno: tuple[int, int], ficha_dos: tuple[int, int]) -> bool:
    """
    Determina si dos fichas de dominó pueden unirse.

    Parameters:
        ficha_uno (tuple): Primera ficha (dos valores enteros entre 0 y 6).
        ficha_dos (tuple): Segunda ficha (dos valores enteros entre 0 y 6).

    Returns:
        bool: True si las fichas comparten al menos un número, False si no.
    """

    if any(n < 0 or n > 6 for n in ficha_uno + ficha_dos):
        raise ValueError("Los valores de las fichas deben estar entre 0 y 6.")
    
    return not set(ficha_uno).isdisjoint(ficha_dos)


def main():
    """
    Programa principal para probar la función unir_fichas().
    """
    pruebas = [
        ((3, 4), (5, 4)),
        ((2, 6), (6, 1)),
        ((0, 1), (2, 3)),
        ((5, 5), (5, 2)),
        ((3, 4), (1, 2))
    ]

    for f1, f2 in pruebas:
        resultado = unir_fichas(f1, f2)
        print(f"Fichas {f1} y {f2} encajan: {resultado}")


if __name__ == "__main__":
    main()
