"""
Realizar una función recursiva para imprimir una matriz de M x N con el formato 
apropiado.
"""

def imprimir_fila_rec(fila, col=0):
    """
    Imprime recursivamente los elementos de una fila de la matriz.

    Parameters:
        fila (list): Lista que contiene una fila de la matriz.
        col (int): Índice actual dentro de la fila.

    Returns:
        None
    """

    # Caso base: fin de la fila
    if col == len(fila):
        print()
        return

    # Imprime el elemento actual
    print(fila[col], end=" ")

    # Imprime recursivamente el resto de la fila
    imprimir_fila_rec(fila, col + 1)


def imprimir_matriz_rec(mat, fila=0):
    """
    Imprime una matriz M x N en formato apropiado mediante recursividad.

    Parameters:
        mat (list[list[int]]): Matriz a imprimir.
        fila (int): Índice de la fila actual.

    Returns:
        None
    """

    # Caso base: no quedan filas por imprimir
    if fila == len(mat):
        return

    # Imprimir la fila actual usando recursividad
    imprimir_fila_rec(mat[fila])

    # Llamada recursiva para imprimir la siguiente fila
    imprimir_matriz_rec(mat, fila + 1)
