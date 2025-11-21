"""
Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N.
"""

def minimo_fila_rec(fila, col=0, actual=None):
    """
    Determina recursivamente el mínimo valor dentro de una fila.

    Parameters:
        fila (list[int]): Lista que representa una fila de la matriz.
        col (int): Índice actual dentro de la fila.
        actual (int): Valor mínimo encontrado hasta el momento.

    Returns:
        int: Mínimo valor de la fila.
    """

    # Inicializar el valor mínimo en la primera llamada
    if actual is None:
        actual = fila[0]

    # Caso base: fin de la fila
    if col == len(fila):
        return actual

    # Actualizar el mínimo si corresponde
    if fila[col] < actual:
        actual = fila[col]

    return minimo_fila_rec(fila, col + 1, actual)


def minimo_matriz_rec(mat, fila=0, minimo_global=None):
    """
    Encuentra el mínimo elemento dentro de una matriz M x N usando recursividad.

    Parameters:
        mat (list[list[int]]): Matriz de números enteros.
        fila (int): Índice de la fila actual.
        minimo_global (int): Mínimo encontrado hasta el momento.

    Returns:
        int: El valor mínimo de toda la matriz.
    """

    # Caso base: no quedan filas
    if fila == len(mat):
        return minimo_global

    # Mínimo de la fila actual
    minimo_fila = minimo_fila_rec(mat[fila])

    # Actualizar el mínimo global
    if minimo_global is None or minimo_fila < minimo_global:
        minimo_global = minimo_fila

    # Recursión sobre el resto de la matriz
    return minimo_matriz_rec(mat, fila + 1, minimo_global)
