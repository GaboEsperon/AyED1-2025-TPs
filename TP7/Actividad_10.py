"""
Consigna:
Escribir una función que sume todos los elementos de una matriz de M x N y devuelva
el resultado. No usar la función sum().
"""

def sumar_fila_rec(fila, col=0):
    """
    Suma recursivamente los elementos de una fila.

    Parameters:
        fila (list[int]): Lista que representa una fila de la matriz.
        col (int): Índice actual dentro de la fila.

    Returns:
        int: Suma de los elementos de la fila.
    """

    # Caso base: fin de la fila
    if col == len(fila):
        return 0

    # Suma el elemento actual y continúa recursivamente
    return fila[col] + sumar_fila_rec(fila, col + 1)


def sumar_matriz_rec(mat, fila=0):
    """
    Suma todos los elementos de una matriz M x N utilizando recursividad.

    Parameters:
        mat (list[list[int]]): Matriz cuyos elementos se desean sumar.
        fila (int): Índice de la fila actual.

    Returns:
        int: Suma total de los elementos de la matriz.
    """

    # Caso base: no quedan filas por procesar
    if fila == len(mat):
        return 0

    # Suma la fila actual y continúa recursivamente
    return sumar_fila_rec(mat[fila]) + sumar_matriz_rec(mat, fila + 1)
